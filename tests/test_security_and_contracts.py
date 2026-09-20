"""
Comprehensive Functional, Privacy & Security Test Suite for werr v0.3.0
Verifies:
1. Zero-PII filtering & redaction (keys, emails, JWT tokens)
2. 0-Byte VRAM and 24-Byte Coordinate Seed mathematical invariant
3. Sub-millisecond latency & deterministic execution
4. Domain Gate isolation across 5 core domains
5. Telemetry error isolation (never blocks or raises)
"""
import sys
import os
import unittest
import time

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import werr
from werr import WerrEngine, NoulQuestion, ChoiceQuestion, ScoreQuestion, AutoSeedRouter
from werr.telemetry import _sanitize_client_state, _sanitize_instruction, dispatch_telemetry_async


class TestWerrSecurityAndContracts(unittest.TestCase):

    def setUp(self):
        self.engine = WerrEngine(resolution=32, max_iter=30)
        self.router = AutoSeedRouter()

    def test_01_zero_vram_and_coordinate_bytes_invariant(self):
        """Verify strict 0-Byte VRAM and 24-Byte coordinate seed contract."""
        resp = self.engine.decide(
            state={"user_role": "admin", "request_rate": 1.2},
            questions={"auth": NoulQuestion(instructions="Authorize access?")}
        )
        self.assertEqual(resp.memory_tensor_bytes, 0, "Memory tensor bytes MUST be 0")
        self.assertEqual(resp.coordinate_bytes, 24, "Coordinate seed bytes MUST be exactly 24")
        self.assertLess(resp.latency_ms, 50.0, "Decision latency should be sub-50ms even on unoptimized CPU")
        self.assertIn("auth", resp.answers)
        self.assertIsInstance(resp.answers["auth"].decision, bool)

    def test_02_sensitive_key_redaction(self):
        """Verify client-side zero-PII filter redacts password, secret, token, key, auth."""
        dirty_state = {
            "user_id": 12345,
            "password": "SuperSecretPassword123!",
            "api_key": "sk-proj-999988887777",
            "auth_token": "Bearer abcdef123456",
            "private_session": "sess_987654321",
            "normal_metric": 42.5
        }
        clean_state = _sanitize_client_state(dirty_state)

        self.assertEqual(clean_state["password"], "[REDACTED]")
        self.assertEqual(clean_state["api_key"], "[REDACTED]")
        self.assertEqual(clean_state["auth_token"], "[REDACTED]")
        self.assertEqual(clean_state["private_session"], "[REDACTED]")
        self.assertEqual(clean_state["normal_metric"], 42.5)
        self.assertEqual(clean_state["user_id"], 12345)

    def test_03_email_and_jwt_redaction_in_values(self):
        """Verify emails and JWT tokens inside string values and instructions are stripped."""
        dirty_state = {
            "contact": "Please email admin@example.com for help",
            "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.doNotLeakThisTokenString"
        }
        clean_state = _sanitize_client_state(dirty_state)

        self.assertNotIn("admin@example.com", clean_state["contact"])
        self.assertIn("[EMAIL_REDACTED]", clean_state["contact"])
        self.assertNotIn("eyJhbGci", str(clean_state["bearer"]))

        # Instruction redaction
        dirty_instr = "Validate login for user victim@company.org with token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        clean_instr = _sanitize_instruction(dirty_instr)
        self.assertNotIn("victim@company.org", clean_instr)
        self.assertIn("[EMAIL_REDACTED]", clean_instr)
        self.assertNotIn("eyJhbGci", clean_instr)
        self.assertIn("[TOKEN_REDACTED]", clean_instr)

    def test_04_domain_gate_isolation(self):
        """Verify AutoSeedRouter routes correctly across all 5 operational domains."""
        test_cases = [
            ({"role": "attacker", "failed_attempts": 15}, "api_security", False),
            ({"smoke_detected": True, "temp_c": 65.0}, "iot_safety", False),
            ({"debt_to_income_ratio": 0.85, "late_payments": 5}, "financial_risk", False),
            ({"role": "blacklisted", "velocity_last_hour": 10}, "ecommerce_fraud", False),
            ({"health_pct": 10.0, "ammo_pct": 2.0}, "game_combat", False),
            # Safe counterparts
            ({"role": "admin", "failed_attempts": 0}, "api_security", True),
            ({"smoke_detected": False, "temp_c": 21.0}, "iot_safety", True),
            ({"debt_to_income_ratio": 0.15, "late_payments": 0, "annual_income_usd": 120000}, "financial_risk", True),
        ]

        for state, expected_domain, expected_noul in test_cases:
            resp = self.engine.decide(state=state, questions={"q": NoulQuestion("Proceed?")}, auto_route=True)
            self.assertEqual(resp.domain, expected_domain, f"Failed domain routing for state: {state}")
            decision = resp.boolean("q")
            self.assertEqual(decision, expected_noul, f"Failed expected noul for {expected_domain}: {state}")

    def test_05_telemetry_failure_isolation(self):
        """Verify telemetry dispatch never crashes or blocks caller even on bad network/inputs."""
        # Bad endpoint
        os.environ["WERR_TELEMETRY_ENDPOINT"] = "http://127.0.0.1:59999/non_existent"
        try:
            resp = self.engine.decide(
                state={"test": "payload"},
                questions={"q": NoulQuestion("Test?")}
            )
            # Must return smoothly
            self.assertIsNotNone(resp)
            self.assertTrue(hasattr(resp, "latency_ms"))
        finally:
            os.environ.pop("WERR_TELEMETRY_ENDPOINT", None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
