"""
werr Fractal Kernel: Vectorized Mandelbrot generator and quadrant/quadtree feature extractors.
Self-contained, pure NumPy implementation for Zero-Memory System-One Decision Engine.
"""
import math
import numpy as np


def compute_mandelbrot_patch(cx: float, cy: float, zoom: float, res: int = 64, max_iter: int = 50):
    """
    Vectorized Mandelbrot patch generator.
    Returns:
      - black_ratio: Non-escaping dark area ratio in [0, 1]
      - avg_escape: Normalized average escape time in [0, 1]
      - escape_iters: 2D integer array of shape (res, res)
    """
    scale = 1.0 / zoom
    x = np.linspace(cx - scale, cx + scale, res)
    y = np.linspace(cy - scale, cy + scale, res)
    C = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    Z = np.zeros_like(C)
    escape_iters = np.full(C.shape, max_iter, dtype=int)
    mask = np.ones(C.shape, dtype=bool)

    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + C[mask]
        escaped = np.abs(Z) > 2.0
        newly_escaped = escaped & mask
        escape_iters[newly_escaped] = i
        mask = mask & (~escaped)

    black_pixels = np.sum(escape_iters == max_iter)
    black_ratio = black_pixels / (res * res)
    avg_escape = np.mean(escape_iters) / max_iter
    return black_ratio, avg_escape, escape_iters


def extract_quadrant_weights(escape_iters: np.ndarray, max_iter: int = 50):
    """
    Partitions patch into 4 quadrants (VV subdivision):
      - Q1 (Top-Left)     -> w1
      - Q2 (Top-Right)    -> w2
      - Q3 (Bottom-Left)  -> w3
      - Q4 (Bottom-Right) -> bias
    """
    h, w = escape_iters.shape
    mid_h, mid_w = h // 2, w // 2

    q1 = escape_iters[:mid_h, :mid_w]
    q2 = escape_iters[:mid_h, mid_w:]
    q3 = escape_iters[mid_h:, :mid_w]
    q4 = escape_iters[mid_h:, mid_w:]

    quads = [q1, q2, q3, q4]
    weights = []
    ratios = []

    for q in quads:
        ratio = np.sum(q == max_iter) / q.size
        ratios.append(ratio)
        w_val = (ratio - 0.5) * 6.0
        weights.append(w_val)

    return weights[0], weights[1], weights[2], weights[3], ratios


def extract_quadtree_features(escape_iters: np.ndarray, grid_size: int = 4, max_iter: int = 50):
    """
    Hierarchical 2^p x 2^p Quadtree Partitioning.
    Subdivides a patch into grid_size x grid_size sub-tiles.
    Returns:
      - ratios: 1D array of dark area ratios in [0, 1]
      - avg_escapes: 1D array of normalized average escape times in [0, 1]
    """
    h, w = escape_iters.shape
    tile_h = h // grid_size
    tile_w = w // grid_size
    ratios = []
    avg_escapes = []
    for r in range(grid_size):
        for c in range(grid_size):
            tile = escape_iters[r*tile_h:(r+1)*tile_h, c*tile_w:(c+1)*tile_w]
            dark_ratio = np.sum(tile == max_iter) / tile.size
            avg_esc = np.mean(tile) / max_iter
            ratios.append(dark_ratio)
            avg_escapes.append(avg_esc)
    return np.array(ratios), np.array(avg_escapes)


def sigmoid(x):
    """Numerically stable sigmoid function."""
    return 1.0 / (1.0 + np.exp(-np.clip(x, -50.0, 50.0)))


# =========================================================================
# Bounded Domain Density Estimation (arXiv:1810.11107)
# =========================================================================

def _vec_erf(x: np.ndarray) -> np.ndarray:
    """
    Vectorized error function approximation (Abramowitz & Stegun 7.1.26).
    Maximum absolute error: < 1.5e-7. Pure NumPy, zero external dependencies.
    """
    x = np.asarray(x, dtype=np.float64)
    sign = np.sign(x)
    x_abs = np.abs(x)
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911
    t = 1.0 / (1.0 + p * x_abs)
    poly = ((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t
    y = 1.0 - poly * np.exp(-x_abs * x_abs)
    return sign * y


def normal_cdf(z: np.ndarray) -> np.ndarray:
    """Standard normal cumulative distribution function Phi(z)."""
    return 0.5 * (1.0 + _vec_erf(z / np.sqrt(2.0)))


def compute_boundary_correction_weights(u: np.ndarray, bandwidth: float = 0.12) -> np.ndarray:
    """
    Computes boundary weight inverse W(u, h) = 1 / omega(u, h) on [0, 1] (arXiv:1810.11107).
    """
    u_clamped = np.clip(u, 0.0, 1.0)
    h = max(1e-4, bandwidth)
    phi_left = normal_cdf(u_clamped / h)
    phi_right = normal_cdf((1.0 - u_clamped) / h)
    omega = np.clip(phi_left + phi_right - 1.0, 0.45, 1.0)
    return 1.0 / omega


def extract_bounded_quadrant_weights(
    escape_iters: np.ndarray,
    max_iter: int = 50,
    bandwidth: float = 0.12
):
    """
    Boundary-corrected quadrant weight extraction (arXiv:1810.11107).
    Partitions escape matrix into 4 quadrants, compensating for boundary truncation on [0, 1].
    """
    h, w = escape_iters.shape
    mid_h, mid_w = h // 2, w // 2

    q1 = escape_iters[:mid_h, :mid_w]
    q2 = escape_iters[:mid_h, mid_w:]
    q3 = escape_iters[mid_h:, :mid_w]
    q4 = escape_iters[mid_h:, mid_w:]

    quads = [q1, q2, q3, q4]
    weights = []
    ratios = []

    for q in quads:
        u = q.astype(np.float64) / float(max_iter)
        weights_corr = compute_boundary_correction_weights(u, bandwidth=bandwidth)
        cusp_mask = (u >= 0.90).astype(np.float64)
        boundary_corrected_ratio = np.sum(weights_corr * cusp_mask) / np.sum(weights_corr)
        avg_energy = np.sum(weights_corr * u) / np.sum(weights_corr)
        composite_ratio = 0.65 * boundary_corrected_ratio + 0.35 * avg_energy
        ratios.append(float(composite_ratio))
        w_val = float((composite_ratio - 0.5) * 6.0)
        weights.append(w_val)

    return weights[0], weights[1], weights[2], weights[3], ratios


# =========================================================================
# Cadence Supercritical Pitchfork Bifurcation Operator
# =========================================================================

def apply_cadence_bifurcation(
    scores,
    lambda_param: float = 0.20,
    alpha: float = 0.50,
    beta: float = 0.25,
    fractal_fields = None,
    deadlock_threshold: float = 0.85
) -> np.ndarray:
    """
    Applies coupled pitchfork bifurcation to break destructive nodal deadlocks
    between competing decision candidates.
    """
    s = np.array(scores, dtype=np.float64)
    K = len(s)
    if K <= 1:
        return s

    sorted_s = np.sort(s)
    top_gap = sorted_s[-1] - sorted_s[-2]

    if top_gap < deadlock_threshold:
        diff_matrix = s[:, np.newaxis] - s[np.newaxis, :]
        bif_force = np.sum(np.sign(diff_matrix) * (np.abs(diff_matrix) ** alpha), axis=1)

        if fractal_fields is not None and len(fractal_fields) == K:
            h_arr = np.array(fractal_fields, dtype=np.float64)
            h_diff_matrix = h_arr[:, np.newaxis] - h_arr[np.newaxis, :]
            bif_force += beta * np.sum(h_diff_matrix, axis=1)

        effective_lambda = lambda_param * (1.0 + (deadlock_threshold - top_gap) / deadlock_threshold)
        return s + effective_lambda * bif_force
    else:
        if fractal_fields is not None and len(fractal_fields) == K:
            return s + np.array(fractal_fields, dtype=np.float64) * 0.35
        return s
