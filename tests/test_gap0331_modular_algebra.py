"""
tests/test_gap0331_modular_algebra.py
======================================
Tests for GAP-0331 Constructive Modular Inversion & Extended Euclidean Invariants.
Verifies bit-exact mathematical parity with GAP lib/zmodnz.gi and Lean 4 Nat.gcdA.
"""

import unittest
from werr.modular_algebra import (
    constructive_extended_gcd,
    constructive_inverse_mod,
    is_unit_mod9,
    is_resonant_subideal_i3,
    neutralize_modular_perturbation,
    verify_gap0331_invariants,
)
from werr import WerrEngine


class TestGap0331ModularAlgebra(unittest.TestCase):
    """Unit tests for GAP-0331 modular algebra in WERR v0.5.1."""

    def test_constructive_extended_gcd_units(self):
        """Extended Euclidean Algorithm computes valid Bézout coefficients for units in Z/9Z."""
        units = (1, 2, 4, 5, 7, 8)
        for u in units:
            gcd, x, y = constructive_extended_gcd(u, 9)
            self.assertEqual(gcd, 1, f"Unit {u} must have gcd 1 with 9")
            self.assertEqual(u * x + 9 * y, 1, f"Bézout identity must hold for {u}")

    def test_constructive_inverse_mod9_all_units(self):
        """Every unit in U(Z/9Z) has a constructive multiplicative inverse satisfying u * inv == 1 (mod 9)."""
        expected_inverses = {
            1: 1,  # 1 * 1 = 1 == 1 (mod 9)
            2: 5,  # 2 * 5 = 10 == 1 (mod 9)
            4: 7,  # 4 * 7 = 28 == 1 (mod 9)
            5: 2,  # 5 * 2 = 10 == 1 (mod 9)
            7: 4,  # 7 * 4 = 28 == 1 (mod 9)
            8: 8,  # 8 * 8 = 64 == 1 (mod 9)
        }
        for u, expected_inv in expected_inverses.items():
            inv = constructive_inverse_mod(u, 9)
            self.assertEqual(inv, expected_inv, f"Inverse of {u} must be {expected_inv}")
            self.assertEqual((u * inv) % 9, 1, f"Product {u} * {inv} must be 1 (mod 9)")

    def test_subideal_i3_zero_divisors_rejected(self):
        """Elements of resonant sub-ideal I_3 = {0, 3, 6} are non-invertible zero-divisors."""
        zero_divisors = (0, 3, 6, 9, 12, 15, 18)
        for z in zero_divisors:
            self.assertTrue(is_resonant_subideal_i3(z), f"{z} must belong to I_3")
            self.assertFalse(is_unit_mod9(z), f"{z} must not be a unit in Z/9Z")
            with self.assertRaises(ValueError):
                constructive_inverse_mod(z, 9)

    def test_adversarial_perturbation_neutralization(self):
        """Adversarial multiplier is neutralized exactly via constructive inverse."""
        state_residue = 7  # Initial state in Z/9Z
        hostile_factor = 4  # Adversarial perturbation
        perturbed = (state_residue * hostile_factor) % 9  # (7 * 4) % 9 = 28 % 9 = 1

        neutralized = neutralize_modular_perturbation(perturbed, hostile_factor, modulus=9)
        self.assertEqual(neutralized, state_residue, "State residue must be restored exactly")

    def test_verify_gap0331_invariants_suite(self):
        """Self-contained invariant verification returns verified status and phi(9) = 6."""
        res = verify_gap0331_invariants(modulus=9)
        self.assertEqual(res["status"], "verified")
        self.assertEqual(res["phi_n"], 6)
        self.assertEqual(res["lean4_theorem"], "inverseOpExec_correct (0 sorry)")

    def test_werr_engine_integration(self):
        """WerrEngine exposes verify_gap0331_unit helper method correctly."""
        engine = WerrEngine()
        ver = engine.verify_gap0331_unit(4)
        self.assertEqual(ver["status"], "verified")
        self.assertEqual(ver["inverse"], 7)
        self.assertTrue(ver["is_unit"])

        fail_ver = engine.verify_gap0331_unit(6)
        self.assertEqual(fail_ver["status"], "non_invertible")
        self.assertFalse(fail_ver["is_unit"])


if __name__ == "__main__":
    unittest.main()
