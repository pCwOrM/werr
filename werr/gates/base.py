"""
wevv: Domain Gate Base Interface
Defines the contract for domain-specific latent projections and fractal coordinates.
"""
from abc import ABC, abstractmethod
import math
import re
import hashlib
from typing import Dict, List, Any, Tuple, Optional, Union
import numpy as np

from werr.fractal import compute_mandelbrot_patch, extract_quadrant_weights, extract_quadtree_features, sigmoid
from werr.datatypes import (
    NoulQuestion, ChoiceQuestion, ScoreQuestion,
    NoulAnswer, ChoiceAnswer, ScoreAnswer, WevvResponse
)
from werr.calibration import DynamicCalibration


def normalize_text(s: str) -> str:
    """Standardizes English & Turkish text for robust keyword matching."""
    s = str(s).lower()
    mapping = {
        'ı': 'i', 'i̇': 'i', 'ğ': 'g', 'ü': 'u', 'ş': 's', 'ö': 'o', 'ç': 'c',
        'İ': 'i', 'I': 'i', 'Ğ': 'g', 'Ü': 'u', 'Ş': 's', 'Ö': 'o', 'Ç': 'c'
    }
    for k, v in mapping.items():
        s = s.replace(k, v)
    return s.strip()


def safe_float(v: Any, default: float = 0.0) -> float:
    """Safely converts arbitrary input to float, handling strings, None, and [REDACTED] markers."""
    try:
        if isinstance(v, (int, float)):
            return float(v)
        if isinstance(v, str):
            v_clean = v.strip()
            if not v_clean or v_clean.startswith("[REDACTED"):
                return default
            return float(v_clean)
        return default
    except (ValueError, TypeError):
        return default


class DomainGate(ABC):
    """
    Abstract base class for domain-specific System-One decision gates.
    Each gate encapsulates:
    1. A calibrated 24-byte boundary coordinate triplet (cx, cy, zoom) on dM.
    2. A domain-specific latent state projector Phi_D(s) -> (v, rho).
    3. Natural language keywords for autonomous intent routing.
    """
    name: str = "base"
    cx: float = -0.7436438870371587
    cy: float = 0.1318259042053119
    zoom: float = 50.0
    resolution: int = 64
    max_iter: int = 50
    default_threshold: float = 0.5
    keywords: List[str] = []

    def __init__(
        self,
        cx: Optional[float] = None,
        cy: Optional[float] = None,
        zoom: Optional[float] = None,
        resolution: int = 64,
        max_iter: int = 50,
        threshold: Optional[float] = None
    ):
        if cx is not None:
            self.cx = cx
        if cy is not None:
            self.cy = cy
        if zoom is not None:
            self.zoom = zoom
        self.resolution = resolution
        self.max_iter = max_iter
        if threshold is not None:
            self.default_threshold = threshold
        self.calibration = DynamicCalibration()

    @abstractmethod
    def project_state(self, state: Dict[str, Any]) -> Tuple[np.ndarray, float]:
        """
        Projects domain-specific raw environment state into:
        1. Continuous latent feature vector v in [-1.0, 1.0]^K
        2. Scalar directional domain risk metric rho in R
        """
        pass

    def evaluate_state_and_questions(
        self,
        state: Dict[str, Any],
        questions: Dict[str, Union[NoulQuestion, ChoiceQuestion, ScoreQuestion]]
    ) -> WevvResponse:
        """
        Executes a single forward evaluation pass over the gate's fractal coordinate manifold.
        Zero matrix tensors allocated (0 Bytes VRAM).
        """
        import time
        start_time = time.perf_counter()

        # 1. Domain Latent State Projection
        vec, net_risk = self.project_state(state)

        # 2. Boundary Coordinate Modulation
        scale = 1.0 / self.zoom
        delta_x = float(np.tanh(net_risk if net_risk != 0.0 else np.mean(vec[0::2]))) * scale * 0.45
        delta_y = float(np.tanh(np.mean(vec[1::2]))) * scale * 0.45

        eff_cx = self.cx + delta_x
        eff_cy = self.cy + delta_y
        eff_zoom = self.zoom * (1.0 + 0.1 * float(np.sin(np.sum(vec))))

        # 3. Escape-Time Boundary Dynamics
        black_ratio, avg_escape, escape_iters = compute_mandelbrot_patch(
            cx=eff_cx,
            cy=eff_cy,
            zoom=eff_zoom,
            res=self.resolution,
            max_iter=self.max_iter
        )

        w1, w2, w3, bias, quad_ratios = extract_quadrant_weights(escape_iters, self.max_iter)
        tile_ratios, _ = extract_quadtree_features(escape_iters, grid_size=4, max_iter=self.max_iter)
        tile_weights = (tile_ratios - 0.5) * 4.0

        answers = {}

        # 4. Typed Question Answering
        for q_name, q_obj in questions.items():
            if isinstance(q_obj, NoulQuestion):
                ans = self._evaluate_noul(q_obj, vec, net_risk, avg_escape, tile_weights)
                answers[q_name] = ans
            elif isinstance(q_obj, ChoiceQuestion):
                ans = self._evaluate_choice(q_obj, vec, net_risk, avg_escape, quad_ratios, tile_ratios)
                answers[q_name] = ans
            elif isinstance(q_obj, ScoreQuestion):
                ans = self._evaluate_score(q_obj, vec, net_risk, avg_escape, quad_ratios)
                answers[q_name] = ans

        elapsed_ms = (time.perf_counter() - start_time) * 1000.0

        return WevvResponse(
            domain=self.name,
            answers=answers,
            latency_ms=round(elapsed_ms, 3),
            memory_tensor_bytes=0,
            coordinate_bytes=24,
            escape_entropy=round(float(np.std(escape_iters)), 4),
            quadrant_entropy=round(float(np.std(quad_ratios)), 4),
            active_coordinates={"cx": eff_cx, "cy": eff_cy, "zoom": eff_zoom}
        )

    def _evaluate_noul(
        self,
        q_obj: NoulQuestion,
        vec: np.ndarray,
        net_risk: float,
        avg_escape: float,
        tile_weights: np.ndarray
    ) -> NoulAnswer:
        instr = normalize_text(q_obj.instructions)
        tokens = set(re.findall(r'[a-zA-Z0-9]+', instr)) | {instr}

        allow_keywords = {
            'allow', 'permit', 'grant', 'safe', 'valid', 'ok', 'auth', 'pass', 'approve',
            'clear', 'cleared', 'clean', 'sustain', 'proceed', 'enable', 'accept', 'authorize',
            'confirm', 'eligible', 'trust', 'trusted', 'normal', 'continue', 'activate', 'release',
            'izin', 'izin_ver', 'onay', 'onayla', 'onaylandi', 'uygun', 'gecerli', 'calistir',
            'ac', 'evet', 'dogrula', 'dogrulandi', 'kabul', 'gecis', 'surdur', 'aktif', 'guvenli',
            'yetkili', 'temiz', 'devam', 'verilsin', 'edilsin', 'tahsis_et', 'engage'
        }
        deny_keywords = {
            'threat', 'danger', 'attack', 'block', 'malicious', 'deny', 'reject', 'ban', 'hazard',
            'fraud', 'fire', 'suspicious', 'retreat', 'evacuate', 'alarm', 'violation', 'abusive',
            'unauthorized', 'critical', 'stop', 'halt', 'drop', 'freeze', 'quarantine',
            'tehlike', 'risk', 'engelle', 'engellensin', 'yasak', 'yasakla', 'saldiri', 'hata',
            'kapat', 'hayir', 'reddet', 'reddedilsin', 'supheli', 'zararli', 'yangin', 'tahliye',
            'alarm', 'kac', 'durdur', 'iptal', 'sahte', 'dolandirici', 'ihlali', 'dondur', 'kes'
        }

        is_allow_q = bool(tokens & allow_keywords)
        is_deny_q = bool(tokens & deny_keywords)

        # Disambiguate when prompt title mentions risk/threat/fraud but interrogative asks for clearance
        if is_allow_q and is_deny_q:
            if bool(tokens & {'clear', 'cleared', 'permit', 'allow', 'approve', 'safe', 'valid', 'pass', 'sustain', 'izin', 'onay', 'kabul', 'tahsis_et'}):
                is_deny_q = False

        if is_allow_q or (net_risk != 0.0 and not is_deny_q):
            base_prob = 1.0 / (1.0 + math.exp((net_risk - 0.2) * 2.0))
            fractal_boost = 0.8 + 0.4 * (1.0 - avg_escape)
            prob = float(base_prob * fractal_boost)
            if net_risk >= 1.4:
                prob = min(prob, 0.30)
            elif net_risk <= -1.0:
                prob = max(prob, 0.75)
        elif is_deny_q:
            base_prob = 1.0 / (1.0 + math.exp((-net_risk - 0.2) * 2.0))
            fractal_boost = 0.8 + 0.4 * avg_escape
            prob = float(base_prob * fractal_boost)
            if net_risk >= 1.4:
                prob = max(prob, 0.75)
        else:
            n_dim = min(len(vec), len(tile_weights))
            dot_product = float(np.dot(vec[:n_dim], tile_weights[:n_dim])) + q_obj.weight_bias
            prob = float(sigmoid(dot_product))

        prob = max(0.0001, min(0.9999, prob))
        base_thresh = q_obj.threshold if q_obj.threshold != 0.5 else self.default_threshold
        # Adaptive Noul Thresholding: modulate slightly with net_risk if default 0.5 is used
        if q_obj.threshold == 0.5:
            risk_offset = float(np.tanh(net_risk * 0.8)) * 0.08
            threshold = max(0.20, min(0.80, base_thresh + risk_offset))
        else:
            threshold = base_thresh

        is_true = prob >= threshold
        conf = float(min(1.0, abs(prob - 0.5) * 2.0))

        return NoulAnswer(
            type="noul",
            noul=round(prob, 4),
            decision=is_true,
            confidence=round(conf, 4)
        )

    def _evaluate_choice(
        self,
        q_obj: ChoiceQuestion,
        vec: np.ndarray,
        net_risk: float,
        avg_escape: float,
        quad_ratios: np.ndarray,
        tile_ratios: np.ndarray
    ) -> ChoiceAnswer:
        options = list(q_obj.criteria.keys())
        num_opts = len(options)
        scores = []

        direct_kw = {
            'direct', 'direct_api', 'prod', 'fast', 'allow', 'approve', 'auto_approve', 'engage',
            'normal', 'safe', 'instant', 'proceed', 'forward', 'uretim',
            'dogrudan', 'direkt', 'onayla', 'otomatik_onay', 'saldir', 'gecis',
            'calistir', 'izin_ver'
        }
        caution_kw = {
            'rate', 'limiter', 'rate_limiter', 'slow', 'caution', 'warning', 'review', 'manual',
            'underwrite', 'manual_underwrite', 'counter_offer', 'sandbox', 'sandbox_audit',
            'audit', 'verify', 'isolate', 'sms', 'challenge', 'step_up', 'quarantine', 'kuyruk',
            'sinirla', 'hiz_sinirlayici', 'incele', 'inceleme', 'uyar', 'uyari', 'karantina',
            'manuel', 'denetle', 'beklet', 'dogrulama', 'karsi_teklif', 'gozden_gecir',
            'guvenlik_incelemesi', 'ikincil', 'eko', 'eko_mod', 'kefil', 'kefil_iste'
        }
        block_kw = {
            'reject', 'deny', 'block', 'drop', 'drop_packet', 'blacklist', 'alarm', 'retreat',
            'evacuate', 'adverse', 'reject_adverse', 'terminate', 'freeze',
            'engelle', 'reddet', 'kac', 'tahliye', 'dusur', 'kara_liste', 'durdur',
            'baglantiyi_kes', 'hesabi_dondur', 'ret', 'acil_tahliye', 'panik', 'bloke',
            'kes', 'siginaga_kac', 'paketi_dusur', 'islemi_reddet', 'basvuru_reddi'
        }

        instr_tokens = set(re.findall(r'[a-zA-Z0-9]+', normalize_text(str(q_obj.instructions))))
        gate_keywords = {normalize_text(kw) for kw in getattr(self, 'keywords', [])}

        # -----------------------------------------------------------------
        # Organic Dynamic Calibration & Phase Rotation Normalization
        # Adapts continuous empirical baselines via Exponential Moving Average (EMA)
        # Eliminates positional choice bias (Q1/Q3 vs Q0/Q2) organically.
        # -----------------------------------------------------------------
        if not hasattr(self, 'calibration') or self.calibration is None:
            self.calibration = DynamicCalibration()

        norm_quad_ratios = self.calibration.normalize_quadrants(quad_ratios)
        self.calibration.update(quad_ratios)

        instr_hash = int(hashlib.md5(str(q_obj.instructions).encode('utf-8')).hexdigest()[:6], 16)
        phase_offset = instr_hash % 4

        for i, opt in enumerate(options):
            opt_norm = normalize_text(opt)
            desc_norm = normalize_text(str(q_obj.criteria.get(opt, "")))
            opt_key_tokens = set(re.findall(r'[a-zA-Z0-9]+', opt_norm)) | {opt_norm}
            opt_desc_tokens = set(re.findall(r'[a-zA-Z0-9]+', desc_norm))
            
            quad_idx = (i + phase_offset) % 4
            q_res = float(norm_quad_ratios[quad_idx])
            feat_idx = (i * 2) % len(vec)
            st_res = float(vec[feat_idx]) * (q_res - 0.5) * 4.0
            score_i = q_res * 2.5 + st_res + (1.0 - avg_escape) * 0.5

            # -----------------------------------------------------------------
            # Chordial Semantic Resonance & Phase-Coherence Modulation
            # Prevents butterfly spikes from isolated descriptive words while
            # preserving harmonic affinity (Tinleme Index) and sub-gate resonance.
            # -----------------------------------------------------------------
            matched_cat = None
            in_key = False

            if bool(opt_key_tokens & block_kw):
                matched_cat = 'block'
                in_key = True
            elif bool(opt_desc_tokens & block_kw):
                matched_cat = 'block'
                in_key = False
            elif bool(opt_key_tokens & caution_kw):
                matched_cat = 'caution'
                in_key = True
            elif bool(opt_desc_tokens & caution_kw):
                matched_cat = 'caution'
                in_key = False
            elif bool(opt_key_tokens & direct_kw):
                matched_cat = 'direct'
                in_key = True
            elif bool(opt_desc_tokens & direct_kw):
                matched_cat = 'direct'
                in_key = False

            if matched_cat is not None:
                # Acoustic Tinleme Index (T):
                # Primary key matches carry full metallic sharpness (T = 1.0)
                if in_key:
                    tinleme = 1.0
                else:
                    # Incidental descriptive words require harmonic agreement with question/gate
                    has_chord = bool(instr_tokens & (block_kw | caution_kw | direct_kw | gate_keywords))
                    tinleme = 0.40 if has_chord else 0.045

                # Smooth, conservative hyperbolic alignment curve (no discontinuous cliffs)
                if matched_cat == 'block':
                    align = math.tanh(net_risk - 0.70)
                    amplitude = 4.5
                elif matched_cat == 'caution':
                    diff = net_risk - 0.70
                    align = math.exp(-2.0 * diff * diff) * 1.5 - 0.5
                    amplitude = 3.5
                elif matched_cat == 'direct':
                    align = math.tanh(0.35 - net_risk)
                    amplitude = 4.2

                score_i += amplitude * align * tinleme

            scores.append(score_i)

        # Softmax
        exp_scores = [math.exp(max(-50.0, min(50.0, s))) for s in scores]
        sum_exp = sum(exp_scores)
        probs = [s / sum_exp for s in exp_scores]
        best_idx = int(np.argmax(probs))

        prob_dict = {opt: round(probs[i], 4) for i, opt in enumerate(options)}
        conf = float(probs[best_idx] - (sorted(probs)[-2] if num_opts > 1 else 0.0))

        return ChoiceAnswer(
            type="choice",
            choice=options[best_idx],
            probabilities=prob_dict,
            confidence=round(max(0.0, min(1.0, conf)), 4)
        )

    def _evaluate_score(
        self,
        q_obj: ScoreQuestion,
        vec: np.ndarray,
        net_risk: float,
        avg_escape: float,
        quad_ratios: np.ndarray
    ) -> ScoreAnswer:
        levels = q_obj.criteria
        num_levels = len(levels)
        raw_val = float(sigmoid(net_risk * 1.2)) * (num_levels - 1)
        raw_val = max(0.0, min(float(num_levels - 1), raw_val))

        center_idx = int(round(raw_val))
        center_idx = max(0, min(num_levels - 1, center_idx))

        level_probs = {}
        for i, lvl in enumerate(levels):
            dist = abs(i - raw_val)
            p = math.exp(-0.5 * (dist ** 2))
            level_probs[lvl] = p
        total_p = sum(level_probs.values())
        level_probs = {k: round(v / total_p, 4) for k, v in level_probs.items()}

        conf = float(level_probs[levels[center_idx]])

        return ScoreAnswer(
            type="score",
            score=round(raw_val, 2),
            level=levels[center_idx],
            probabilities=level_probs,
            confidence=round(conf, 4)
        )
