"""
werr: Core System-One Fractal Decision Engine
Evaluates typed questions (noul, choice, score) directly from deterministic
Mandelbrot geometry with zero matrix weights (0 Byte VRAM/RAM tensors).
"""
import os
import sys
import time
import math
import re
import hashlib
from typing import Dict, List, Any, Optional, Union, Tuple
import numpy as np

from werr.fractal import (
    compute_mandelbrot_patch,
    extract_quadrant_weights,
    extract_quadtree_features,
    sigmoid,
    extract_bounded_quadrant_weights,
    apply_cadence_bifurcation
)
from werr.datatypes import (
    NoulQuestion, ChoiceQuestion, ScoreQuestion,
    NoulAnswer, ChoiceAnswer, ScoreAnswer,
    WerrResponse, WevvResponse
)
from werr.telemetry import dispatch_telemetry_async
from werr.calibration import DynamicCalibration


def _normalize_text(s: str) -> str:
    """
    Normalizes Turkish & English strings by lowercasing and standardizing diacritics.
    Handles 'ı/i', 'ö/o', 'ü/u', 'ş/s', 'ç/c', 'ğ/g' seamlessly.
    """
    s = str(s).lower()
    mapping = {
        'ı': 'i', 'i̇': 'i', 'ğ': 'g', 'ü': 'u', 'ş': 's', 'ö': 'o', 'ç': 'c',
        'İ': 'i', 'I': 'i', 'Ğ': 'g', 'Ü': 'u', 'Ş': 's', 'Ö': 'o', 'Ç': 'c'
    }
    for k, v in mapping.items():
        s = s.replace(k, v)
    return s.strip()


class WerrEngine:
    """
    Zero-Memory System-One Decision Engine.
    Processes arbitrary program state into typed, probabilistic decisions in < 1ms.
    Supports both English and Turkish semantic queries natively.
    """
    def __init__(
        self,
        base_cx: float = -0.743643887037158704752191506114774,
        base_cy: float = 0.131825904205311970493132056385139,
        base_zoom: float = 50.0,
        resolution: int = 64,
        max_iter: int = 50,
        mode: str = "lexical",
        enable_ontologies: Optional[bool] = None,
        domain_mode: Optional[str] = None,
        tripod: bool = True,
        cadence_lambda: float = 0.10,
        cadence_beta: float = 0.15,
        cadence_alpha: float = 0.50,
        temp_choice: float = 1.25
    ):
        """
        Initialize the Werr Engine with a resonant chaotic boundary seed.
        Supports operational modes:
          - 'lexical' / 'production' (default): Full domain ontologies, sensor threshold heuristics,
            and semantic gate mappings active (ideal for IoT, life-safety, answerr.me).
          - 'pure_fractal' / 'domainless': Strips external lexical dictionaries; operates purely on
            chaotic Mandelbrot boundary dynamics and criteria N-gram geometry (ideal for general benchmark reasoning).
        Supports domain routing architectures:
          - 'multi': Routes dynamically through domain gates (AutoSeedRouter) with specialized
            topologies (api_security, financial_risk, iot_safety, ecommerce_fraud, game_combat).
          - 'none' (default): Domainless monolithic mode. Directly projects into the universal
            chaotic boundary cusp (c = -0.743643887 + 0.131825904i) with zero domain bias.
        """
        self.cx = base_cx
        self.cy = base_cy
        self.zoom = base_zoom
        self.resolution = resolution
        self.max_iter = max_iter
        if enable_ontologies is not None:
            self.mode = "lexical" if enable_ontologies else "pure_fractal"
        else:
            self.mode = str(mode).lower()

        if domain_mode is not None:
            self.domain_mode = str(domain_mode).lower()
        else:
            self.domain_mode = "none"

        self.tripod = tripod
        self.cadence_lambda = cadence_lambda
        self.cadence_beta = cadence_beta
        self.cadence_alpha = cadence_alpha
        self.temp_choice = temp_choice
        self.calibration = DynamicCalibration()

    def _state_to_vector(self, state: Dict[str, Any]) -> Tuple[np.ndarray, float]:
        """
        Deterministically converts arbitrary dictionary state (floats, ints, bools, strings)
        into a continuous latent vector [-1.0, 1.0] and computes aggregate semantic risk.
        Supports multi-lingual (English & Turkish) roles and feature names.
        """
        semantic_roles = {
            # Admin / Superuser
            "admin": -1.5, "root": -1.5, "superuser": -1.5, "system": -1.5,
            "yonetici": -1.5, "yetkili": -1.5, "kok": -1.5, "sistem": -1.5, "kurucu": -1.5, "sistem_yoneticisi": -1.5,
            # Member / User / Verified / Internal
            "member": -0.8, "user": -0.8, "authenticated": -1.0, "auth": -1.0, "internal": -1.0,
            "developer": -1.2, "gelistirici": -1.2, "auditor": -1.0, "denetci": -1.0, "guvenlik_denetcisi": -1.0,
            "uye": -0.8, "kullanici": -0.8, "kayitli": -0.8, "dogrulanmis": -1.0, "ic": -1.0, "calisan": -1.0,
            "partner": -0.8, "is_ortagi": -0.8, "abone": -0.8, "service_bot": -0.5, "servis_botu": -0.5, "tester": -0.4,
            # Guest / Anonymous / Unverified / Dormant
            "guest": 0.9, "anonymous": 1.0, "unverified": 1.0, "dormant": 0.7, "dormant_revived": 0.9,
            "misafir": 0.9, "konuk": 0.9, "ziyaretci": 0.9, "anonim": 1.0, "dogrulanmamis": 1.0, "uyuyan": 0.7,
            # Attacker / Malicious / Bot / Pentester / Crawler
            "attacker": 2.5, "bot": 2.2, "malicious": 2.5, "hacker": 2.5, "suspicious": 1.8,
            "saldirgan": 2.5, "kotuniyetli": 2.5, "zararli": 2.5, "supheli": 1.8, "tehdit": 2.2, "casus": 2.5,
            "pentester": 1.2, "sizma_testi": 1.2, "crawler": 1.8, "spider": 1.8, "tarayici": 1.8, "web_kaziyici": 1.8,
            "malware_agent": 2.5, "zararli_yazilim": 2.5, "botnet": 2.5, "korsan": 2.5, "davetsiz_misafir": 2.2
        }

        values = []
        net_risk = 0.0
        is_prod = (self.mode not in ["pure_fractal", "domainless"])

        for k, v in sorted(state.items()):
            kl = _normalize_text(k)
            if isinstance(v, (int, float)):
                norm_val = 2.0 / (1.0 + math.exp(-float(v) / 10.0 if abs(v) < 700 else (-1.0 if v < 0 else 1.0))) - 1.0
                values.append(norm_val)
                if is_prod:
                    if any(w in kl for w in ['fail', 'error', 'attempt', 'hata', 'yanlis', 'basarisiz', 'deneme']):
                        net_risk += (float(v) / 5.0) * 1.5
                    elif any(w in kl for w in ['freq', 'rate', 'speed', 'hiz', 'siklik', 'oran', 'frekans']):
                        net_risk += (float(v) / 50.0) * 1.0
                    elif any(w in kl for w in ['payload', 'byte', 'kb', 'boyut', 'veri', 'yuk', 'paket']):
                        net_risk += (float(v) / 500.0) * 0.5
            elif isinstance(v, bool):
                values.append(1.0 if v else -1.0)
                if is_prod:
                    if any(w in kl for w in ['auth', 'valid', 'safe', 'internal', 'verified', 'yetkili', 'gecerli', 'guvenli', 'dogrulanmis', 'onayli', 'aktif']):
                        net_risk += -0.8 if v else 1.2
            elif isinstance(v, str):
                vl = _normalize_text(v)
                matched_role = False
                if is_prod:
                    for r_key, r_risk in semantic_roles.items():
                        if r_key in vl:
                            net_risk += r_risk
                            values.append(math.tanh(r_risk))
                            matched_role = True
                            break
                if not matched_role:
                    h = int(hashlib.md5(v.encode('utf-8')).hexdigest()[:8], 16)
                    angle = (h % 10000) / 10000.0 * 2.0 * math.pi
                    values.append(math.sin(angle))
                    values.append(math.cos(angle))
            else:
                values.append(0.0)

        if not values:
            return np.zeros(4, dtype=np.float64), 0.0

        while len(values) < 4:
            values.append(0.0)
        return np.array(values, dtype=np.float64), float(net_risk)

    def decide(
        self,
        state: Dict[str, Any],
        questions: Dict[str, Union[NoulQuestion, ChoiceQuestion, ScoreQuestion]],
        auto_route: Optional[bool] = None,
        preferred_domain: Optional[str] = None
    ) -> WerrResponse:
        """
        Evaluates a bundle of typed questions against a single program state.
        All questions are answered in a single parallel pass.
        If auto_route is True (or domain_mode == 'multi' and auto_route is not False),
        delegates to the optimal domain gate coordinate via AutoSeedRouter.
        """
        should_route = auto_route if auto_route is not None else (self.domain_mode == "multi")
        if should_route:
            from werr.router import AutoSeedRouter
            router = AutoSeedRouter(calibration=self.calibration, mode=self.mode)
            resp, domain, _ = router.route_and_evaluate(state=state, questions=questions, preferred_domain=preferred_domain)
            seed = getattr(resp, 'active_coordinates', None) or {"cx": self.cx, "cy": self.cy, "zoom": self.zoom}
            dispatch_telemetry_async(
                state=state,
                questions=questions,
                response=resp,
                seed=seed,
                source="python_lib"
            )
            return resp

        start_time = time.perf_counter()

        # 1. State-to-Wave Modulation
        vec, net_risk = self._state_to_vector(state)
        is_prod = (self.mode not in ["pure_fractal", "domainless"])
        if is_prod:
            role_val = state.get("user_role", state.get("role", state.get("rol", "")))
            role_str = _normalize_text(str(role_val))
            is_guest = any(w in role_str for w in ['guest', 'misafir', 'konuk', 'ziyaretci', 'anonim'])
            is_attacker = any(w in role_str for w in ['attacker', 'bot', 'saldirgan', 'hacker', 'kotuniyetli', 'zararli'])
        else:
            role_val = ""
            role_str = ""
            is_guest = False
            is_attacker = False

        # Coordinate perturbation
        scale = 1.0 / self.zoom
        delta_x = float(np.tanh(net_risk if net_risk != 0.0 else np.mean(vec[0::2]))) * scale * 0.45
        delta_y = float(np.tanh(np.mean(vec[1::2]))) * scale * 0.45

        eff_cx = self.cx + delta_x
        eff_cy = self.cy + delta_y
        eff_zoom = self.zoom * (1.0 + 0.1 * float(np.sin(np.sum(vec))))

        # 2. Fractal Geometry Evaluation (Tripod Multi-Scale or Single Cusp)
        if getattr(self, "tripod", True):
            tripod_configs = [
                (eff_zoom * 0.60, 0.25),
                (eff_zoom * 1.00, 0.50),
                (eff_zoom * 1.60, 0.25)
            ]
            fused_quad_ratios = np.zeros(4, dtype=np.float64)
            fused_tile_ratios = np.zeros(16, dtype=np.float64)
            fused_black_ratio = 0.0
            escape_iters = None

            for z_val, w_z in tripod_configs:
                b_r, a_e, esc = compute_mandelbrot_patch(
                    cx=eff_cx, cy=eff_cy, zoom=z_val, res=self.resolution, max_iter=self.max_iter
                )
                if escape_iters is None or w_z == 0.50:
                    escape_iters = esc
                _, _, _, _, q_r = extract_bounded_quadrant_weights(
                    esc, max_iter=self.max_iter, bandwidth=0.12
                )
                t_r, _ = extract_quadtree_features(esc, grid_size=4, max_iter=self.max_iter)

                fused_quad_ratios += w_z * np.array(q_r, dtype=np.float64)
                fused_tile_ratios += w_z * t_r
                fused_black_ratio += w_z * b_r

            tile_ratios = fused_tile_ratios
            quad_ratios = list(fused_quad_ratios)
            w1 = float(quad_ratios[0] - 0.5) * 6.0
            w2 = float(quad_ratios[1] - 0.5) * 6.0
            w3 = float(quad_ratios[2] - 0.5) * 6.0
            bias = float(quad_ratios[3] - 0.5) * 6.0
            tile_weights = (fused_tile_ratios - 0.5) * 4.0
            black_ratio = fused_black_ratio
            avg_escape = 0.5
        else:
            black_ratio, avg_escape, escape_iters = compute_mandelbrot_patch(
                cx=eff_cx,
                cy=eff_cy,
                zoom=eff_zoom,
                res=self.resolution,
                max_iter=self.max_iter
            )
            w1, w2, w3, bias, quad_ratios = extract_bounded_quadrant_weights(
                escape_iters, max_iter=self.max_iter, bandwidth=0.12
            )
            tile_ratios, _ = extract_quadtree_features(escape_iters, grid_size=4, max_iter=self.max_iter)
            tile_weights = (tile_ratios - 0.5) * 4.0

        answers: Dict[str, Union[NoulAnswer, ChoiceAnswer, ScoreAnswer]] = {}

        # 3. Answer each typed question
        for q_name, q_obj in questions.items():
            if isinstance(q_obj, NoulQuestion):
                if is_prod:
                    instr = _normalize_text(q_obj.instructions)
                    tokens = set(re.findall(r'\b\w+\b', instr))
                    is_allow_q = bool(tokens & {
                        'allow', 'permit', 'grant', 'safe', 'valid', 'ok', 'auth', 'pass', 'approve',
                        'izin', 'onay', 'uygun', 'gecerli', 'calistir', 'ac', 'evet', 'dogrula', 'kabul', 'gecis'
                    })
                    is_deny_q = bool(tokens & {
                        'threat', 'danger', 'attack', 'block', 'malicious', 'deny', 'reject', 'ban',
                        'tehlike', 'risk', 'engelle', 'yasak', 'saldiri', 'hata', 'kapat', 'hayir', 'reddet', 'supheli', 'zararli'
                    })

                    if is_allow_q or (net_risk != 0.0 and not is_deny_q):
                        base_prob = 1.0 / (1.0 + math.exp((net_risk - 0.2) * 2.0))
                        fractal_boost = 0.8 + 0.4 * (1.0 - avg_escape)
                        prob = float(base_prob * fractal_boost)
                        if is_guest or is_attacker or net_risk >= 1.4:
                            prob = min(prob, 0.35)
                    elif is_deny_q:
                        prob = 1.0 / (1.0 + math.exp((-net_risk - 0.2) * 2.0))
                    else:
                        st_values = [str(v) for v in state.values()] if isinstance(state, dict) else [str(state)]
                        st_text = " ".join(st_values).lower()
                        st_tokens = set(re.findall(r'\b\w+\b', _normalize_text(st_text)))

                        pos_polarity = bool(st_tokens & {'yes', 'true', 'allowed', 'permit', 'permitted', 'valid', 'approved', 'success', 'paid', 'confirmed', 'clear', 'eligible', 'dogru', 'gecerli'})
                        neg_polarity = bool(st_tokens & {'no', 'false', 'denied', 'prohibited', 'absent', 'missing', 'unproved', 'unauthorized', 'failed', 'cannot', 'dispute', 'cancel', 'reject', 'yanlis', 'gecersiz'})
                        has_negation = bool(re.search(r'\b(not|no|never|without|un|dis|lacks?|yok|degil)\b', st_text))

                        polarity_bias = 0.0
                        if pos_polarity and not has_negation:
                            polarity_bias += 1.2
                        elif neg_polarity or has_negation:
                            polarity_bias -= 1.2

                        n_dim = min(len(vec), len(tile_weights))
                        dot_product = float(np.dot(vec[:n_dim], tile_weights[:n_dim])) + q_obj.weight_bias + polarity_bias
                        prob = float(sigmoid(dot_product))
                else:
                    # Pure fractal mode: zero role priors, strictly polarity and fractal coordinate weights
                    st_values = [str(v) for v in state.values()] if isinstance(state, dict) else [str(state)]
                    st_text = " ".join(st_values).lower()
                    st_tokens = set(re.findall(r'\b\w+\b', _normalize_text(st_text)))

                    pos_polarity = bool(st_tokens & {'yes', 'true', 'allowed', 'permit', 'permitted', 'valid', 'approved', 'success', 'paid', 'confirmed', 'clear', 'eligible'})
                    neg_polarity = bool(st_tokens & {'no', 'false', 'denied', 'prohibited', 'absent', 'missing', 'unproved', 'unauthorized', 'failed', 'cannot', 'dispute'})
                    has_negation = bool(re.search(r'\b(not|no|never|without|un|dis|lacks?)\b', st_text))

                    polarity_bias = 0.0
                    if pos_polarity and not has_negation:
                        polarity_bias += 1.2
                    elif neg_polarity or has_negation:
                        polarity_bias -= 1.2

                    n_dim = min(len(vec), len(tile_weights))
                    dot_product = float(np.dot(vec[:n_dim], tile_weights[:n_dim])) + q_obj.weight_bias + polarity_bias
                    prob = float(sigmoid(dot_product))

                prob = max(0.0001, min(0.9999, prob))
                base_thresh = q_obj.threshold
                if q_obj.threshold == 0.5:
                    risk_offset = float(np.tanh(net_risk * 0.8)) * 0.08
                    effective_thresh = max(0.20, min(0.80, 0.5 + risk_offset))
                else:
                    effective_thresh = base_thresh

                is_true = prob >= effective_thresh
                conf = float(min(1.0, abs(prob - 0.5) * 2.0))

                answers[q_name] = NoulAnswer(
                    type="noul",
                    noul=round(prob, 4),
                    decision=is_true,
                    confidence=round(conf, 4)
                )

            elif isinstance(q_obj, ChoiceQuestion):
                options = list(q_obj.criteria.keys())
                num_opts = len(options)

                # Organic Dynamic Calibration & Phase Rotation Normalization
                if not hasattr(self, 'calibration') or self.calibration is None:
                    self.calibration = DynamicCalibration()

                norm_quad_ratios = self.calibration.normalize_quadrants(quad_ratios)
                self.calibration.update(quad_ratios)

                instr_hash = int(hashlib.md5(str(q_obj.instructions).encode('utf-8')).hexdigest()[:6], 16)
                phase_offset = instr_hash % 4

                # Flatten state for semantic criteria matching
                st_values = [str(v) for v in state.values()] if isinstance(state, dict) else [str(state)]
                st_text = " ".join(st_values).lower()
                st_tokens = set(re.findall(r'\b\w+\b', _normalize_text(st_text)))

                scores = []
                for i, opt in enumerate(options):
                    opt_norm = _normalize_text(opt)
                    quad_idx = (i + phase_offset) % 4
                    q_res = float(norm_quad_ratios[quad_idx])
                    feat_idx = (i * 2) % len(vec)
                    st_res = float(vec[feat_idx]) * (q_res - 0.5) * 4.0
                    score_i = q_res * 2.5 + st_res + (1.0 - avg_escape) * 0.5

                    # 1. Criteria description alignment (generalized N-gram matching)
                    crit_desc = q_obj.criteria.get(opt, "")
                    if isinstance(crit_desc, str) and crit_desc.strip():
                        crit_norm = _normalize_text(crit_desc)
                        crit_words = re.findall(r'\b\w+\b', crit_norm)
                        crit_tokens = set(crit_words)
                        overlap = len(st_tokens & crit_tokens)
                        score_i += overlap * 2.2
                        if len(crit_words) >= 2:
                            bigrams = [f"{crit_words[j]} {crit_words[j+1]}" for j in range(len(crit_words) - 1)]
                            score_i += sum(3.5 for bg in bigrams if bg in st_text)

                    # 2. Option name direct match in state
                    opt_tokens = set(re.findall(r'\b\w+\b', opt_norm))
                    score_i += sum(3.0 for tok in opt_tokens if len(tok) >= 3 and tok in st_tokens)

                    # 3. Gateway semantic role priors (only in production mode)
                    if is_prod:
                        if any(w in opt_norm for w in ['direct', 'prod', 'fast', 'primary', 'main', 'dogrudan', 'hizli', 'ana', 'normal', 'oncelikli', 'direkt']):
                            score_i += 3.0 if (net_risk < 0.2 and not is_guest) else -2.5
                        elif any(w in opt_norm for w in ['rate', 'limiter', 'slow', 'queue', 'delay', 'kuyruk', 'yavaslat', 'sinirla', 'beklet', 'frenle']):
                            score_i += 2.5 if (net_risk >= 0.5 or state.get('req_frequency', 0) > 30) else 0.0
                        elif any(w in opt_norm for w in ['sandbox', 'audit', 'quarantine', 'isolate', 'inspect', 'inceleme', 'karantina', 'gozlem', 'izole', 'denetim']):
                            score_i += 3.5 if (is_guest or (0.2 <= net_risk < 2.0)) else 0.5
                        elif any(w in opt_norm for w in ['drop', 'deny', 'block', 'reject', 'abort', 'engelle', 'reddet', 'iptal', 'dusur', 'yasakla', 'at']):
                            score_i += 4.5 if (is_attacker or net_risk >= 2.0) else -2.0

                    scores.append(score_i)

                # Coupled Cadence Pitchfork Bifurcation
                if len(options) >= 2:
                    scores = list(apply_cadence_bifurcation(
                        scores,
                        lambda_param=getattr(self, 'cadence_lambda', 0.10),
                        alpha=getattr(self, 'cadence_alpha', 0.50),
                        beta=getattr(self, 'cadence_beta', 0.15),
                        deadlock_threshold=0.85
                    ))

                temp = getattr(self, 'temp_choice', 1.25)
                max_s = max(scores) if scores else 0.0
                exp_scores = [math.exp(max(-50.0, min(50.0, (s - max_s) / temp))) for s in scores]
                sum_exp = sum(exp_scores)
                probs = [s / (sum_exp + 1e-12) for s in exp_scores]
                best_idx = int(np.argmax(probs))

                prob_dict = {opt: round(float(probs[i]), 4) for i, opt in enumerate(options)}
                best_opt = options[best_idx]
                conf = float(probs[best_idx] - (sorted(probs)[-2] if num_opts > 1 else 0.0))
                conf = round(max(0.0, min(1.0, conf)), 4)

                answers[q_name] = ChoiceAnswer(
                    type="choice",
                    choice=best_opt,
                    probabilities=prob_dict,
                    confidence=conf
                )

            elif isinstance(q_obj, ScoreQuestion):
                num_steps = len(q_obj.criteria)
                if net_risk != 0.0:
                    raw_score = max(0.0, min(float(num_steps - 1), (net_risk + 1.2) * ((num_steps - 1) / 3.5)))
                else:
                    n_dim = min(len(vec), len(tile_weights))
                    state_activation = float(sigmoid(np.dot(vec[:n_dim], tile_weights[:n_dim])))
                    combined_val = (black_ratio * 0.4 + state_activation * 0.6)
                    raw_score = combined_val * (num_steps - 1)

                bounded_score = max(0.0, min(float(num_steps - 1), raw_score))

                step_probs = {}
                distances = [math.exp(-((bounded_score - i) ** 2) / 0.8) for i in range(num_steps)]
                sum_dist = sum(distances) or 1.0
                for i in range(num_steps):
                    step_probs[i] = round(distances[i] / sum_dist, 4)

                conf = round(float(max(step_probs.values())), 4)

                answers[q_name] = ScoreAnswer(
                    type="score",
                    score=round(bounded_score, 2),
                    probabilities=step_probs,
                    confidence=conf
                )

        elapsed_ms = (time.perf_counter() - start_time) * 1000.0

        response = WerrResponse(
            model=f"werr-0.5.0-{self.domain_mode}",
            answers=answers,
            latency_ms=round(elapsed_ms, 2),
            memory_tensor_bytes=0,
            coordinate_bytes=24,
            escape_entropy=round(float(np.std(escape_iters)), 4) if escape_iters is not None else 0.0,
            quadrant_entropy=round(float(np.std(quad_ratios)), 4) if quad_ratios is not None else 0.0,
            active_coordinates={"cx": eff_cx, "cy": eff_cy, "zoom": eff_zoom}
        )

        dispatch_telemetry_async(
            state=state,
            questions=questions,
            response=response,
            seed={"cx": eff_cx, "cy": eff_cy, "zoom": eff_zoom},
            source="python_lib"
        )

        return response

# Backward compatibility alias
WevvEngine = WerrEngine
