"""
wevv Fractal Kernel: Vectorized Mandelbrot generator and quadrant/quadtree feature extractors.
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
