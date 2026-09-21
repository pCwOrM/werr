"""
Unit tests for core procedural Mandelbrot weight generation and quadrant extraction.
Mandelbrot Fractal Neural Synthesis.
"""
import unittest
import sys
import os
import numpy as np

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.mandelbrot_core import compute_mandelbrot_patch, extract_quadrant_weights


class TestMandelbrotCore(unittest.TestCase):

    def test_patch_generation_bounds(self):
        """Verify patch generation output dimensions and normalized ratio bounds."""
        res = 64
        max_iter = 50
        black_ratio, avg_escape, escape_iters = compute_mandelbrot_patch(
            cx=-0.75, cy=0.1, zoom=2.0, res=res, max_iter=max_iter
        )

        self.assertEqual(escape_iters.shape, (res, res))
        self.assertTrue(0.0 <= black_ratio <= 1.0)
        self.assertTrue(0.0 <= avg_escape <= 1.0)
        self.assertTrue(np.all(escape_iters >= 0))
        self.assertTrue(np.all(escape_iters <= max_iter))

    def test_quadrant_weights_extraction(self):
        """Verify 4-quadrant area extraction maps to valid floating point scalars."""
        _, _, escape_iters = compute_mandelbrot_patch(
            cx=-0.056, cy=0.806, zoom=1.5, res=128, max_iter=100
        )
        w1, w2, w3, bias, ratios = extract_quadrant_weights(escape_iters, max_iter=100)

        for val in [w1, w2, w3, bias]:
            self.assertIsInstance(val, float)
            self.assertTrue(-3.0 <= val <= 3.0)
        self.assertEqual(len(ratios), 4)
        for r in ratios:
            self.assertTrue(0.0 <= r <= 1.0)

    def test_coordinate_reproducibility(self):
        """Verify exact byte-level determinism across repeated patch generations."""
        cx, cy, zoom = -0.75, 0.0, 1.0
        r1, _, iters1 = compute_mandelbrot_patch(cx, cy, zoom, res=32, max_iter=30)
        r2, _, iters2 = compute_mandelbrot_patch(cx, cy, zoom, res=32, max_iter=30)

        self.assertEqual(r1, r2)
        np.testing.assert_array_equal(iters1, iters2)


if __name__ == '__main__':
    unittest.main()
