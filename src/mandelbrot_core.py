"""
Mandelbrot Core Module: High-performance vectorized patch generator and 4-quadrant weight extractor.
Mandelbrot Fractal Neural Synthesis Research Group.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Dynamic paths
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SRC_DIR)
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

def compute_mandelbrot_patch(cx, cy, zoom, res=128, max_iter=100):
    """
    Vectorized Mandelbrot patch generator.
    Returns:
    - black_ratio: Area ratio of non-escaping dark region [0, 1]
    - avg_escape: Normalized escape time [0, 1]
    - escape_iters: 2D integer array (res, res)
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

def extract_quadrant_weights(escape_iters, max_iter=100):
    """
    Partitions a 128x128 Mandelbrot patch into 4 quadrants:
    - Q1 (Top-Left)     -> w1 (Weight 1)
    - Q2 (Top-Right)    -> w2 (Weight 2)
    - Q3 (Bottom-Left)  -> w3 (Auxiliary / Weight 3)
    - Q4 (Bottom-Right) -> bias (Activation Threshold)
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

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.clip(x, -50.0, 50.0)))
