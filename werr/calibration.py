"""
wevv: Organic Dynamic Calibration & Local Homeostasis
Maintains continuous exponential moving averages (EMA) of quadrant escape ratios
and risk distributions, allowing the decision engine to organically adapt to local
operational domains without allocating neural tensors (0 Bytes VRAM).
"""
import os
import json
from typing import Optional, Dict, Any, List
import numpy as np


# Initial empirical baseline derived from the 969-decision benchmark dataset
DEFAULT_BASE_QUAD_MEAN = [0.38, 0.91, 0.35, 0.91]


class DynamicCalibration:
    """
    Organic calibration controller that dynamically tracks running quadrant ratios
    and adapts baseline normalization in O(1) time with zero tensor memory overhead.
    """
    def __init__(
        self,
        base_quad_mean: Optional[List[float]] = None,
        alpha: float = 0.03,
        auto_persist: bool = False,
        persist_path: Optional[str] = None
    ):
        self.quad_mean = np.array(base_quad_mean or DEFAULT_BASE_QUAD_MEAN, dtype=np.float64)
        self.alpha = float(alpha)
        self.sample_count = 0
        self.auto_persist = auto_persist
        self.persist_path = persist_path or os.path.expanduser("~/.werr/calibration_state.json")
        if self.auto_persist:
            self.load()

    @property
    def norm_scale(self) -> float:
        """Dynamic scaling factor maintaining constant total topological energy."""
        return float(np.mean(self.quad_mean))

    @property
    def current_quad_mean(self) -> np.ndarray:
        return self.quad_mean

    def update(self, observed_quad_ratios: np.ndarray) -> None:
        """
        Updates running empirical quadrant baseline via Exponential Moving Average (EMA).
        O(1) execution time, zero tensor allocation.
        """
        obs = np.asarray(observed_quad_ratios, dtype=np.float64)
        if obs.shape == (4,):
            self.quad_mean = (1.0 - self.alpha) * self.quad_mean + self.alpha * obs
            self.sample_count += 1
            if self.auto_persist and self.sample_count % 25 == 0:
                self.save()

    def normalize_quadrants(self, quad_ratios: np.ndarray) -> np.ndarray:
        """
        Applies dynamic baseline normalization to input quadrant ratios:
        Q_norm = (Q_obs / Q_mean) * mean(Q_mean)
        Eliminates positional choice bias while preserving fine-grained fractal perturbations.
        """
        return (quad_ratios / (self.quad_mean + 1e-6)) * self.norm_scale

    def to_dict(self) -> Dict[str, Any]:
        return {
            "quad_mean": [round(float(x), 4) for x in self.quad_mean],
            "sample_count": self.sample_count,
            "alpha": self.alpha,
            "norm_scale": round(self.norm_scale, 4)
        }

    def save(self) -> None:
        try:
            os.makedirs(os.path.dirname(self.persist_path), exist_ok=True)
            with open(self.persist_path, "w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, indent=2)
        except Exception:
            pass

    def load(self) -> None:
        try:
            if os.path.exists(self.persist_path):
                with open(self.persist_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if "quad_mean" in data and len(data["quad_mean"]) == 4:
                        self.quad_mean = np.array(data["quad_mean"], dtype=np.float64)
                        self.sample_count = int(data.get("sample_count", 0))
        except Exception:
            pass
