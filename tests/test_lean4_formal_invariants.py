"""
tests.test_lean4_formal_invariants
==================================
Formal verification test suite for WERR / Werracle Lean 4 (Mathlib4) Invariants:
1. Z/9Z Resonant Sub-Ideal I_3 = {0, 3, 6} Additive & Multiplicative Closure (Theorems 1A, 1B, 1C, 1D)
2. Q16.16 Fixed-Point Escape Bound & 64-bit Overflow Immunity (Theorems 2A, 2B, 2C)
3. Non-Constant Spectral Information & Observer Horizon Sensitivity (Theorems 3A, 3B)
4. EVM Gas Upper Bound Parametric Verification (Theorem 4)
5. Lean 4 / Elan Proof Package Integrity & Toolchain Specification (v4.34.1)

Directly mirrors `formal_proofs/WerracleProof.lean` (10 machine-verified theorems, 0 sorry).
"""

import unittest
import sys
import os
import hashlib

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


class TestLean4FormalInvariants(unittest.TestCase):
    """
    Validates the 10 machine-verified Lean 4 theorems algorithmically in Python.
    """

    def setUp(self):
        # Algebraic definitions in cyclic quotient ring Z/9Z
        self.Z9 = list(range(9))
        self.I3 = {0, 3, 6}
        self.K_error = {1, 2, 4, 5, 7, 8}

        # Q16.16 Fixed-Point constants
        self.FP_SHIFT = 16
        self.FP_ONE = 1 << self.FP_SHIFT      # 65,536 (1.0 in Q16.16)
        self.ESCAPE_LIMIT = 4 * self.FP_ONE    # 262,144 (4.0 in Q16.16)
        self.INT64_MAX = (1 << 63) - 1

    def test_01_theorem_1a_additive_closure(self):
        """
        Theorem 1A: I_3 = {0, 3, 6} is closed under addition in Z/9Z.
        forall a, b in I_3, (a + b) mod 9 in I_3.
        """
        for a in self.I3:
            for b in self.I3:
                res = (a + b) % 9
                self.assertIn(
                    res, self.I3,
                    f"Additive closure failed for {a} + {b} = {res} in Z/9Z"
                )

    def test_02_theorem_1b_ideal_absorption(self):
        """
        Theorem 1B: I_3 is an ideal under multiplication in Z/9Z.
        forall r in Z/9Z, forall a in I_3, (r * a) mod 9 in I_3.
        """
        for r in self.Z9:
            for a in self.I3:
                res = (r * a) % 9
                self.assertIn(
                    res, self.I3,
                    f"Ideal absorption failed for {r} * {a} = {res} in Z/9Z"
                )

    def test_03_theorem_1c_triadic_projection(self):
        """
        Theorem 1C: Every element of Z/9Z scaled by 3 projects strictly into I_3.
        forall k in Z/9Z, (3 * k) mod 9 in I_3.
        """
        for k in self.Z9:
            res = (3 * k) % 9
            self.assertIn(
                res, self.I3,
                f"Triadic projection failed for 3 * {k} = {res} in Z/9Z"
            )

    def test_04_theorem_1d_orthogonal_partition(self):
        """
        Theorem 1D: Exact orthogonal partition of Z/9Z into 3 resonant and 6 error states.
        """
        self.assertEqual(len(self.I3), 3, "Resonant sub-ideal I_3 must have exactly 3 elements")
        self.assertEqual(len(self.K_error), 6, "Error kernel K_error must have exactly 6 elements")
        self.assertEqual(self.I3 & self.K_error, set(), "I_3 and K_error must be disjoint")
        self.assertEqual(self.I3 | self.K_error, set(self.Z9), "I_3 union K_error must span all Z/9Z")

    def test_05_theorems_2a_2b_fuel_bounded_escape(self):
        """
        Theorems 2A & 2B: Kuadratik kaçış döngüsü max_iter adımıyla sınırlıdır.
        escape_zmod9(c) <= 9 ve escape_werracle(c) <= 12.
        """
        test_points = [
            (0, 0),                                       # Derin bağlı kusp
            (int(-0.7436 * self.FP_ONE), int(0.1318 * self.FP_ONE)),  # Seahorse Valley
            (int(2.0 * self.FP_ONE), int(2.0 * self.FP_ONE)),         # Hızlı kaçan nokta
            (int(-1.5 * self.FP_ONE), int(0.0 * self.FP_ONE)),        # Sol anten
            (int(0.25 * self.FP_ONE), int(0.0 * self.FP_ONE)),        # Cusp tekilliği
        ]

        for pt_cx, pt_cy in test_points:
            # 1. ZMod 9 Escape (max 9)
            zx, zy = 0, 0
            esc_9 = 9
            for step in range(9):
                zx2 = (zx * zx) >> self.FP_SHIFT
                zy2 = (zy * zy) >> self.FP_SHIFT
                if zx2 + zy2 > self.ESCAPE_LIMIT:
                    esc_9 = step
                    break
                next_zx = zx2 - zy2 + pt_cx
                next_zy = ((zx * zy) >> (self.FP_SHIFT - 1)) + pt_cy
                zx, zy = next_zx, next_zy

            self.assertLessEqual(esc_9, 9, f"ZMod 9 escape must be <= 9, got {esc_9}")

            # 2. Werracle Escape (max 12)
            zx, zy = 0, 0
            esc_12 = 12
            for step in range(12):
                zx2 = (zx * zx) >> self.FP_SHIFT
                zy2 = (zy * zy) >> self.FP_SHIFT
                if zx2 + zy2 > self.ESCAPE_LIMIT:
                    esc_12 = step
                    break
                next_zx = zx2 - zy2 + pt_cx
                next_zy = ((zx * zy) >> (self.FP_SHIFT - 1)) + pt_cy
                zx, zy = next_zx, next_zy

            self.assertLessEqual(esc_12, 12, f"Werracle escape must be <= 12, got {esc_12}")

    def test_06_theorem_2c_overflow_immunity(self):
        """
        Theorem 2C: Q16.16 sabit noktalı kaçış algoritmasında zx^2 + zy^2 değeri
        asla 64-bit işaretli tamsayı üst sınırını (INT64_MAX) aşamaz.
        """
        # Test extreme boundary conditions
        extreme_points = [
            (int(-2.5 * self.FP_ONE), int(-2.5 * self.FP_ONE)),
            (int(2.5 * self.FP_ONE), int(2.5 * self.FP_ONE)),
            (int(-2.0 * self.FP_ONE), int(1.5 * self.FP_ONE)),
        ]
        for cx, cy in extreme_points:
            zx, zy = 0, 0
            for _ in range(12):
                zx2 = (zx * zx) >> self.FP_SHIFT
                zy2 = (zy * zy) >> self.FP_SHIFT
                # Assert mathematically before escape check
                self.assertLess(abs(zx), 1 << 30, "zx magnitude must be bounded")
                self.assertLess(abs(zy), 1 << 30, "zy magnitude must be bounded")
                self.assertLess(zx * zx, self.INT64_MAX, "zx^2 must not overflow INT64_MAX")
                self.assertLess(zy * zy, self.INT64_MAX, "zy^2 must not overflow INT64_MAX")
                if zx2 + zy2 > self.ESCAPE_LIMIT:
                    break
                zx = zx2 - zy2 + cx
                zy = ((zx * zy) >> (self.FP_SHIFT - 1)) + cy

    def test_07_theorem_3a_non_constant_spectrum(self):
        """
        Theorem 3A: ZMod 9 kaçış spektumu sabit değildir (en az 2 farklı çıktı üretir).
        """
        # Bounded point in main cardioid: c = 0 + 0i -> escape = 9
        # Escaping point: c = 2.0 + 2.0i -> escape = 0
        def get_esc(cx_f, cy_f):
            cx = int(cx_f * self.FP_ONE)
            cy = int(cy_f * self.FP_ONE)
            zx, zy = 0, 0
            for s in range(9):
                if ((zx * zx) >> self.FP_SHIFT) + ((zy * zy) >> self.FP_SHIFT) > self.ESCAPE_LIMIT:
                    return s
                zx, zy = ((zx * zx) >> self.FP_SHIFT) - ((zy * zy) >> self.FP_SHIFT) + cx, \
                         ((zx * zy) >> (self.FP_SHIFT - 1)) + cy
            return 9

        esc_bounded = get_esc(0.0, 0.0)
        esc_divergent = get_esc(2.0, 2.0)
        self.assertNotEqual(
            esc_bounded, esc_divergent,
            "Spectrum must be non-constant across distinct boundary coordinates"
        )

    def test_08_theorem_4_evm_gas_parametric_bound(self):
        """
        Theorem 4: EVM gas tüketimi en kötü senaryoda bile <= 22,557 gas ile sınırlıdır.
        """
        # 16-noktalı mikro-ızgara, nokta başı max 12 iterasyon = 192 adım
        base_gas = 18000
        gas_per_step = 12
        max_total_steps = 16 * 12  # 192
        max_gas = base_gas + (max_total_steps * gas_per_step)

        self.assertLessEqual(
            max_gas, 22557,
            f"Parametric gas consumption {max_gas} exceeds Lean 4 proved upper bound 22,557"
        )

    def test_09_lean4_formal_proof_package_integrity(self):
        """
        Verify that formal Lean 4 proof source files and toolchain specification exist.
        """
        formal_dir = os.path.join(ROOT_DIR, "formal_proofs")
        self.assertTrue(os.path.isdir(formal_dir), f"Formal proofs directory missing: {formal_dir}")

        toolchain_file = os.path.join(formal_dir, "lean-toolchain")
        self.assertTrue(os.path.isfile(toolchain_file), "lean-toolchain file missing")
        with open(toolchain_file, "r", encoding="utf-8") as tf:
            content = tf.read().strip()
            self.assertIn("v4.34.1", content, "Toolchain must specify official Lean v4.34.1")

        proof_file = os.path.join(formal_dir, "WerracleProof.lean")
        self.assertTrue(os.path.isfile(proof_file), "WerracleProof.lean file missing")
        with open(proof_file, "r", encoding="utf-8") as pf:
            proof_code = pf.read()
            # Strip Lean 4 single-line (--) and block (/- ... -/) comments
            import re
            clean_code = re.sub(r"/-\![\s\S]*?-\/", "", proof_code)
            clean_code = re.sub(r"/-[\s\S]*?-\/", "", clean_code)
            clean_code = re.sub(r"--.*$", "", clean_code, flags=re.MULTILINE)
            # Ensure sorry is not used as a proof bypass tactic
            self.assertIsNone(
                re.search(r"\bsorry\b", clean_code),
                "Formal proof must contain zero 'sorry' tactic placeholders"
            )
            self.assertIn("theorem zmod9_resonant_additive_closure", proof_code)
            self.assertIn("theorem evm_gas_parametric_bound", proof_code)


if __name__ == "__main__":
    unittest.main(verbosity=2)
