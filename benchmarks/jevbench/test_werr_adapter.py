"""Unit test for WerrLocalAdapter adhering to JevBench specification."""
import unittest
from jevbench.adapters import WerrLocalAdapter
from jevbench.tasks import Task


def make_task(qtype, criteria, labels):
    return Task(
        id="test_task_1",
        family="decision_boundary",
        state={"user": "operator", "signal_level": 42.5, "status": "nominal"},
        labels=labels,
        expected=labels[0],
        split="public",
        question={"type": qtype, "instructions": "Evaluate operational criteria.", "criteria": criteria}
    )


class TestWerrLocalAdapter(unittest.TestCase):
    def setUp(self):
        self.adapter = WerrLocalAdapter()

    def test_adapter_choice_decision(self):
        t = make_task("choice", {"approve": "Approve request", "reject": "Reject request", "hold": "Hold request"}, ["approve", "reject", "hold"])
        res = self.adapter.run(t)
        self.assertTrue(res.ok)
        self.assertIn("approve", res.probs)
        self.assertIn("reject", res.probs)
        self.assertIn("hold", res.probs)
        self.assertAlmostEqual(sum(res.probs.values()), 1.0, places=3)
        self.assertEqual(res.raw["runtime"]["memory_weights"], "0 Bytes")

    def test_adapter_noul_decision(self):
        t = make_task("noul", {"true": "Safe to proceed", "false": "Do not proceed"}, ["no", "yes"])
        res = self.adapter.run(t)
        self.assertTrue(res.ok)
        self.assertIn("yes", res.probs)
        self.assertIn("no", res.probs)
        self.assertAlmostEqual(sum(res.probs.values()), 1.0, places=3)

    def test_adapter_score_decision(self):
        t = make_task("score", ["low risk", "medium risk", "high risk"], ["0", "1", "2"])
        res = self.adapter.run(t)
        self.assertTrue(res.ok)
        self.assertIn("0", res.probs)
        self.assertIn("1", res.probs)
        self.assertIn("2", res.probs)
        self.assertAlmostEqual(sum(res.probs.values()), 1.0, places=3)


if __name__ == "__main__":
    unittest.main()
