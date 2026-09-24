"""Unit test for WerrLocalAdapter adhering to JevBench specification."""
import unittest
from jevbench.adapters import WerrLocalAdapter
from jevbench.tasks import Task
from jevbench.scoring import validate_probs


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

    def test_local_adapter_contract_and_tariffs(self):
        """Verify JevBench in-process unmetered contract invariants."""
        self.assertIsNone(self.adapter.price_input_per_m)
        self.assertIsNone(self.adapter.price_output_per_m)
        t = make_task("choice", {"a": "Alpha", "b": "Beta"}, ["a", "b"])
        self.assertEqual(self.adapter.reserve_estimate(t), 0.0)
        self.assertEqual(self.adapter.cost_basis, "local_cpu_no_provider_tariff")

    def test_build_request_does_not_leak_gold(self):
        """Invariant: build_request must never include expected/gold answers."""
        t = make_task("choice", {"a": "Alpha", "b": "Beta"}, ["a", "b"])
        req = self.adapter.build_request(t)
        self.assertNotIn("expected", req)
        self.assertNotIn("gold", req)
        self.assertNotIn("ground_truth", req)
        self.assertNotIn("answer_key", req)

    def test_adapter_choice_decision(self):
        t = make_task("choice", {"approve": "Approve request", "reject": "Reject request", "hold": "Hold request"}, ["approve", "reject", "hold"])
        res = self.adapter.run(t)
        self.assertTrue(res.ok)
        self.assertIn("approve", res.probs)
        self.assertIn("reject", res.probs)
        self.assertIn("hold", res.probs)
        clean = validate_probs(res.probs, t.labels, sum_tol=1e-3)
        self.assertEqual(set(clean.keys()), set(t.labels))
        self.assertAlmostEqual(sum(res.probs.values()), 1.0, places=4)
        self.assertEqual(res.raw["runtime"]["memory_weights"], "0 Bytes")

    def test_adapter_noul_decision(self):
        t = make_task("noul", {"true": "Safe to proceed", "false": "Do not proceed"}, ["no", "yes"])
        res = self.adapter.run(t)
        self.assertTrue(res.ok)
        self.assertIn("yes", res.probs)
        self.assertIn("no", res.probs)
        clean = validate_probs(res.probs, t.labels, sum_tol=1e-3)
        self.assertEqual(set(clean.keys()), set(t.labels))
        self.assertAlmostEqual(sum(res.probs.values()), 1.0, places=4)

    def test_adapter_score_decision(self):
        t = make_task("score", ["low risk", "medium risk", "high risk"], ["0", "1", "2"])
        res = self.adapter.run(t)
        self.assertTrue(res.ok)
        self.assertIn("0", res.probs)
        self.assertIn("1", res.probs)
        self.assertIn("2", res.probs)
        clean = validate_probs(res.probs, t.labels, sum_tol=1e-3)
        self.assertEqual(set(clean.keys()), set(t.labels))
        self.assertAlmostEqual(sum(res.probs.values()), 1.0, places=4)


if __name__ == "__main__":
    unittest.main()
