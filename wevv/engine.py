"""
wevv: Core System-One Fractal Decision Engine
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

from wevv.fractal import compute_mandelbrot_patch, extract_quadrant_weights, extract_quadtree_features, sigmoid
from wevv.datatypes import (
    NoulQuestion, ChoiceQuestion, ScoreQuestion,
    NoulAnswer, ChoiceAnswer, ScoreAnswer,
    WevvResponse
)
from wevv.telemetry import dispatch_telemetry_async


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


class WevvEngine:
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
        max_iter: int = 50
    ):
        """
        Initialize the Wevv Engine with a resonant chaotic boundary seed.
        """
        self.cx = base_cx
        self.cy = base_cy
        self.zoom = base_zoom
        self.resolution = resolution
        self.max_iter = max_iter

    def _state_to_vector(self, state: Dict[str, Any]) -> Tuple[np.ndarray, float]:
        """
        Deterministically converts arbitrary dictionary state (floats, ints, bools, strings)
        into a continuous latent vector [-1.0, 1.0] and computes aggregate semantic risk.
        Supports multi-lingual (English & Turkish) roles and feature names.
        """
        semantic_roles = {
            # Admin / Superuser
            "admin": -1.5, "root": -1.5, "superuser": -1.5, "system": -1.5,
            "yonetici": -1.5, "yetkili": -1.5, "kok": -1.5, "sistem": -1.5, "kurucu": -1.5,
            # Member / User / Verified
            "member": -0.8, "user": -0.8, "authenticated": -1.0, "auth": -1.0, "internal": -1.0,
            "uye": -0.8, "kullanici": -0.8, "kayitli": -0.8, "dogrulanmis": -1.0, "ic": -1.0, "calisan": -1.0,
            # Guest / Anonymous / Unverified
            "guest": 0.9, "anonymous": 1.0, "unverified": 1.0,
            "misafir": 0.9, "konuk": 0.9, "ziyaretci": 0.9, "anonim": 1.0, "dogrulanmamis": 1.0,
            # Attacker / Malicious / Bot
            "attacker": 2.5, "bot": 2.2, "malicious": 2.5, "hacker": 2.5, "suspicious": 1.8,
            "saldirgan": 2.5, "kotuniyetli": 2.5, "zararli": 2.5, "supheli": 1.8, "tehdit": 2.2, "casus": 2.5
        }

        values = []
        net_risk = 0.0

        for k, v in sorted(state.items()):
            kl = _normalize_text(k)
            if isinstance(v, (int, float)):
                norm_val = 2.0 / (1.0 + math.exp(-float(v) / 10.0 if abs(v) < 700 else (-1.0 if v < 0 else 1.0))) - 1.0
                values.append(norm_val)
                if any(w in kl for w in ['fail', 'error', 'attempt', 'hata', 'yanlis', 'basarisiz', 'deneme']):
                    net_risk += (float(v) / 5.0) * 1.5
                elif any(w in kl for w in ['freq', 'rate', 'speed', 'hiz', 'siklik', 'oran', 'frekans']):
                    net_risk += (float(v) / 50.0) * 1.0
                elif any(w in kl for w in ['payload', 'byte', 'kb', 'boyut', 'veri', 'yuk', 'paket']):
                    net_risk += (float(v) / 500.0) * 0.5
            elif isinstance(v, bool):
                values.append(1.0 if v else -1.0)
                if any(w in kl for w in ['auth', 'valid', 'safe', 'internal', 'verified', 'yetkili', 'gecerli', 'guvenli', 'dogrulanmis', 'onayli', 'aktif']):
                    net_risk += -0.8 if v else 1.2
            elif isinstance(v, str):
                vl = _normalize_text(v)
                matched_role = False
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
        auto_route: bool = False,
        preferred_domain: Optional[str] = None
    ) -> WevvResponse:
        """
        Evaluates a bundle of typed questions against a single program state.
        All questions are answered in a single parallel pass.
        If auto_route=True, delegates to the optimal domain gate coordinate via AutoSeedRouter.
        """
        if auto_route:
            from wevv.router import AutoSeedRouter
            router = AutoSeedRouter()
            resp, domain, _ = router.route_and_evaluate(state=state, questions=questions, preferred_domain=preferred_domain)
            return resp

        start_time = time.perf_counter()

        # 1. State-to-Wave Modulation
        vec, net_risk = self._state_to_vector(state)
        role_val = state.get("user_role", state.get("role", state.get("rol", "")))
        role_str = _normalize_text(str(role_val))
        is_guest = any(w in role_str for w in ['guest', 'misafir', 'konuk', 'ziyaretci', 'anonim'])
        is_attacker = any(w in role_str for w in ['attacker', 'bot', 'saldirgan', 'hacker', 'kotuniyetli', 'zararli'])

        # Coordinate perturbation
        scale = 1.0 / self.zoom
        delta_x = float(np.tanh(net_risk if net_risk != 0.0 else np.mean(vec[0::2]))) * scale * 0.45
        delta_y = float(np.tanh(np.mean(vec[1::2]))) * scale * 0.45

        eff_cx = self.cx + delta_x
        eff_cy = self.cy + delta_y
        eff_zoom = self.zoom * (1.0 + 0.1 * float(np.sin(np.sum(vec))))

        # 2. Fractal Geometry Evaluation (Single Forward Pass)
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

        answers: Dict[str, Union[NoulAnswer, ChoiceAnswer, ScoreAnswer]] = {}

        # 3. Answer each typed question
        for q_name, q_obj in questions.items():
            if isinstance(q_obj, NoulQuestion):
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
                    n_dim = min(len(vec), len(tile_weights))
                    dot_product = float(np.dot(vec[:n_dim], tile_weights[:n_dim])) + q_obj.weight_bias
                    prob = float(sigmoid(dot_product))

                prob = max(0.0001, min(0.9999, prob))
                is_true = prob >= q_obj.threshold
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

                scores = []
                for i, opt in enumerate(options):
                    opt_norm = _normalize_text(opt)
                    q_res = float(quad_ratios[i % 4])
                    feat_idx = (i * 2) % len(vec)
                    st_res = float(vec[feat_idx]) * (q_res - 0.5) * 4.0
                    score_i = q_res * 2.5 + st_res + (1.0 - avg_escape) * 0.5

                    if any(w in opt_norm for w in ['direct', 'prod', 'fast', 'primary', 'main', 'dogrudan', 'hizli', 'ana', 'normal', 'oncelikli', 'direkt']):
                        score_i += 3.0 if (net_risk < 0.2 and not is_guest) else -2.5
                    elif any(w in opt_norm for w in ['rate', 'limiter', 'slow', 'queue', 'delay', 'kuyruk', 'yavaslat', 'sinirla', 'beklet', 'frenle']):
                        score_i += 2.5 if (net_risk >= 0.5 or state.get('req_frequency', 0) > 30) else 0.0
                    elif any(w in opt_norm for w in ['sandbox', 'audit', 'quarantine', 'isolate', 'inspect', 'inceleme', 'karantina', 'gozlem', 'izole', 'denetim']):
                        score_i += 3.5 if (is_guest or (0.2 <= net_risk < 2.0)) else 0.5
                    elif any(w in opt_norm for w in ['drop', 'deny', 'block', 'reject', 'abort', 'engelle', 'reddet', 'iptal', 'dusur', 'yasakla', 'at']):
                        score_i += 4.5 if (is_attacker or net_risk >= 2.0) else -2.0

                    scores.append(score_i)

                exp_scores = np.exp(np.array(scores) - np.max(scores))
                probs = exp_scores / np.sum(exp_scores)

                prob_dict = {opt: round(float(p), 4) for opt, p in zip(options, probs)}
                best_opt = max(prob_dict.items(), key=lambda x: x[1])[0]
                conf = round(float(max(probs) - (np.sum(probs) - max(probs)) / max(1, num_opts - 1)), 4)
                conf = max(0.0, min(1.0, conf))

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

        response = WevvResponse(
            model="wevv-0.1.0-fractal",
            answers=answers,
            latency_ms=round(elapsed_ms, 2),
            memory_tensor_bytes=0,
            coordinate_bytes=24
        )

        dispatch_telemetry_async(
            state=state,
            questions=questions,
            response=response,
            seed={"cx": eff_cx, "cy": eff_cy, "zoom": eff_zoom},
            source="python_lib"
        )

        return response
