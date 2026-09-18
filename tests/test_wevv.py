"""
Unit tests for the wevv System-One Fractal Decision Engine.
"""
import unittest
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from wevv import (
    WevvEngine,
    NoulQuestion,
    ChoiceQuestion,
    ScoreQuestion,
    NoulAnswer,
    ChoiceAnswer,
    ScoreAnswer,
    create_security_guard,
    create_smart_router,
    create_risk_evaluator
)


class TestWevvEngine(unittest.TestCase):

    def setUp(self):
        self.engine = WevvEngine(resolution=32, max_iter=30)
        self.sample_state = {
            "user_id": 4291,
            "role": "admin",
            "is_internal": True,
            "latency": 45.2,
            "error_count": 0
        }

    def test_zero_memory_contract(self):
        """Verify the engine strictly adheres to the 0-byte matrix tensor contract."""
        response = self.engine.decide(
            state=self.sample_state,
            questions={"check": NoulQuestion(instructions="Is valid?")}
        )
        self.assertEqual(response.memory_tensor_bytes, 0)
        self.assertEqual(response.coordinate_bytes, 24)

    def test_noul_primitive(self):
        """Test binary/boolean decision evaluation."""
        q = NoulQuestion(instructions="Authorize action?", threshold=0.5)
        resp = self.engine.decide(state=self.sample_state, questions={"auth": q})

        ans = resp.answers["auth"]
        self.assertIsInstance(ans, NoulAnswer)
        self.assertEqual(ans.type, "noul")
        self.assertTrue(0.0 <= ans.noul <= 1.0)
        self.assertIsInstance(ans.decision, bool)
        self.assertTrue(0.0 <= ans.confidence <= 1.0)
        # Helper methods
        self.assertEqual(resp.noul("auth"), ans.noul)
        self.assertEqual(resp.boolean("auth"), ans.decision)

    def test_choice_primitive_quadrant(self):
        """Test categorical choice with <= 4 options (4-Quadrant mode)."""
        criteria = {
            "fast": "Fast lane",
            "normal": "Normal lane",
            "slow": "Slow lane"
        }
        q = ChoiceQuestion(instructions="Route request", criteria=criteria)
        resp = self.engine.decide(state=self.sample_state, questions={"route": q})

        ans = resp.answers["route"]
        self.assertIsInstance(ans, ChoiceAnswer)
        self.assertEqual(ans.type, "choice")
        self.assertIn(ans.choice, criteria.keys())
        self.assertAlmostEqual(sum(ans.probabilities.values()), 1.0, places=2)
        self.assertTrue(0.0 <= ans.confidence <= 1.0)
        self.assertEqual(resp.choice("route"), ans.choice)

    def test_choice_primitive_quadtree(self):
        """Test categorical choice with > 4 options (Quadtree 2^p mode)."""
        criteria = {f"opt_{i}": f"Option description {i}" for i in range(8)}
        q = ChoiceQuestion(instructions="Select from 8 options", criteria=criteria)
        resp = self.engine.decide(state=self.sample_state, questions={"choice8": q})

        ans = resp.answers["choice8"]
        self.assertIn(ans.choice, criteria.keys())
        self.assertAlmostEqual(sum(ans.probabilities.values()), 1.0, places=2)

    def test_score_primitive(self):
        """Test scalar ordinal score evaluation."""
        criteria = ["Very Low", "Low", "Medium", "High", "Critical"]
        q = ScoreQuestion(instructions="Rate priority", criteria=criteria)
        resp = self.engine.decide(state=self.sample_state, questions={"priority": q})

        ans = resp.answers["priority"]
        self.assertIsInstance(ans, ScoreAnswer)
        self.assertEqual(ans.type, "score")
        self.assertTrue(0.0 <= ans.score <= len(criteria) - 1)
        self.assertAlmostEqual(sum(ans.probabilities.values()), 1.0, places=2)
        self.assertEqual(resp.score("priority"), ans.score)

    def test_bundled_parallel_execution(self):
        """Test multiple questions evaluated in a single forward pass."""
        questions = {
            "allow": NoulQuestion(instructions="Allow access?"),
            "lane": ChoiceQuestion(instructions="Select lane", criteria={"a": "Lane A", "b": "Lane B"}),
            "rank": ScoreQuestion(instructions="Rank request", criteria=["Low", "Med", "High"])
        }
        resp = self.engine.decide(state=self.sample_state, questions=questions)

        self.assertEqual(len(resp.answers), 3)
        self.assertIn("allow", resp.answers)
        self.assertIn("lane", resp.answers)
        self.assertIn("rank", resp.answers)
        self.assertTrue(resp.latency_ms > 0.0)

    def test_presets(self):
        """Verify pre-calibrated gate presets."""
        guard = create_security_guard(resolution=32)
        router = create_smart_router(resolution=32)
        evaluator = create_risk_evaluator(resolution=32)

        for p_name, eng in [("guard", guard), ("router", router), ("eval", evaluator)]:
            resp = eng.decide(self.sample_state, {"n": NoulQuestion("Test")})
            self.assertIsInstance(resp.answers["n"], NoulAnswer, f"Preset {p_name} failed")


if __name__ == "__main__":
    unittest.main()
