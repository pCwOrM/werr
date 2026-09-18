"""
wevv: Core System-One Fractal Decision Engine
Evaluates typed questions (noul, choice, score) directly from deterministic
Mandelbrot geometry with zero matrix weights (0 Byte VRAM/RAM tensors).
"""
import os
import sys
import time
import math
import hashlib
from typing import Dict, List, Any, Optional, Union
import numpy as np

from wevv.fractal import compute_mandelbrot_patch, extract_quadrant_weights, extract_quadtree_features, sigmoid
from wevv.datatypes import (
    NoulQuestion, ChoiceQuestion, ScoreQuestion,
    NoulAnswer, ChoiceAnswer, ScoreAnswer,
    WevvResponse
)


class WevvEngine:
    """
    Zero-Memory System-One Decision Engine.
    Processes arbitrary program state into typed, probabilistic decisions in < 1ms.
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

    def _state_to_vector(self, state: Dict[str, Any]) -> np.ndarray:
        """
        Deterministically converts arbitrary dictionary state (floats, ints, bools, strings)
        into a continuous latent vector [-1.0, 1.0].
        """
        values = []
        for k, v in sorted(state.items()):
            if isinstance(v, (int, float)):
                # Sigmoidal squashing for unbounded numericals
                norm_val = 2.0 / (1.0 + math.exp(-float(v) / 10.0 if abs(v) < 700 else (-1.0 if v < 0 else 1.0))) - 1.0
                values.append(norm_val)
            elif isinstance(v, bool):
                values.append(1.0 if v else -1.0)
            elif isinstance(v, str):
                # Hash string into a deterministic continuous angle
                h = int(hashlib.md5(v.encode('utf-8')).hexdigest()[:8], 16)
                angle = (h % 10000) / 10000.0 * 2.0 * math.pi
                values.append(math.sin(angle))
                values.append(math.cos(angle))
            else:
                values.append(0.0)

        if not values:
            return np.zeros(4, dtype=np.float64)

        # Pad to at least 4 dimensions
        while len(values) < 4:
            values.append(0.0)
        return np.array(values, dtype=np.float64)

    def decide(
        self,
        state: Dict[str, Any],
        questions: Dict[str, Union[NoulQuestion, ChoiceQuestion, ScoreQuestion]]
    ) -> WevvResponse:
        """
        Evaluates a bundle of typed questions against a single program state.
        All questions are answered in a single parallel pass.
        """
        start_time = time.perf_counter()

        # 1. State-to-Wave Modulation
        vec = self._state_to_vector(state)
        # Coordinate perturbation
        scale = 1.0 / self.zoom
        delta_x = float(np.tanh(np.mean(vec[0::2]))) * scale * 0.45
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
                # Multi-dimensional state dot product with fractal quadtree weights
                n_dim = min(len(vec), len(tile_weights))
                dot_product = float(np.dot(vec[:n_dim], tile_weights[:n_dim])) + q_obj.weight_bias
                prob = float(sigmoid(dot_product))
                is_true = prob >= q_obj.threshold
                conf = float(min(1.0, abs(prob - 0.5) * 2.0))

                answers[q_name] = NoulAnswer(
                    type="noul",
                    noul=round(prob, 4),
                    decision=is_true,
                    confidence=round(conf, 4)
                )

            elif isinstance(q_obj, ChoiceQuestion):
                # Categorical decision across defined criteria
                options = list(q_obj.criteria.keys())
                num_opts = len(options)

                scores = []
                for i in range(num_opts):
                    q_res = float(quad_ratios[i % 4])
                    feat_idx = (i * 2) % len(vec)
                    # State resonance with this quadrant
                    st_res = float(vec[feat_idx]) * (q_res - 0.5) * 4.0
                    score_i = q_res * 2.5 + st_res + (1.0 - avg_escape) * 0.5
                    scores.append(score_i)

                # Softmax normalization
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
                # Continuous ordinal scaling
                num_steps = len(q_obj.criteria)
                n_dim = min(len(vec), len(tile_weights))
                state_activation = float(sigmoid(np.dot(vec[:n_dim], tile_weights[:n_dim])))
                combined_val = (black_ratio * 0.4 + state_activation * 0.6)
                raw_score = combined_val * (num_steps - 1)
                bounded_score = max(0.0, min(float(num_steps - 1), raw_score))

                # Compute soft probabilities across discrete steps
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

        return WevvResponse(
            model="wevv-0.1.0-fractal",
            answers=answers,
            latency_ms=round(elapsed_ms, 2),
            memory_tensor_bytes=0,
            coordinate_bytes=24
        )
