"""Unit test for WerrLocalAdapter adhering to JevBench specification."""
import json
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
        self.assertTrue(self.adapter.load())

    def test_criteria_static_method(self):
        """Verify criteria normalization across canonical task types."""
        t_choice = make_task("choice", {"a": "Option A", "b": "Option B"}, ["a", "b"])
        self.assertEqual(WerrLocalAdapter.criteria(t_choice), {"a": "Option A", "b": "Option B"})

        t_noul = make_task("noul", {"true": "Permitted", "false": "Denied"}, ["no", "yes"])
        self.assertEqual(WerrLocalAdapter.criteria(t_noul), {"yes": "Permitted", "no": "Denied"})

        t_score = make_task("score", ["low", "med", "high"], ["0", "1", "2"])
        self.assertEqual(WerrLocalAdapter.criteria(t_score), {"0": "low", "1": "med", "2": "high"})

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
        self.assertEqual(res.status, 200)
        self.assertEqual(res.probs_source, "native")
        self.assertIn("approve", res.probs)
        self.assertIn("reject", res.probs)
        self.assertIn("hold", res.probs)
        clean = validate_probs(res.probs, t.labels, sum_tol=1e-3)
        self.assertEqual(set(clean.keys()), set(t.labels))
        self.assertAlmostEqual(sum(res.probs.values()), 1.0, places=6)
        self.assertEqual(res.raw["runtime"]["memory_weights"], "0 Bytes")
        self.assertEqual(res.usage["vram_bytes"], 0)
        # Runner JSON serialization invariant (allow_nan=False)
        raw_encoded = json.dumps({"request": res.request_body, "response": res.raw, "probs": res.probs}, allow_nan=False)
        self.assertTrue(len(raw_encoded) > 0)

    def test_adapter_noul_decision(self):
        t = make_task("noul", {"true": "Safe to proceed", "false": "Do not proceed"}, ["no", "yes"])
        res = self.adapter.run(t)
        self.assertTrue(res.ok)
        self.assertEqual(res.status, 200)
        self.assertEqual(res.probs_source, "native")
        self.assertIn("yes", res.probs)
        self.assertIn("no", res.probs)
        clean = validate_probs(res.probs, t.labels, sum_tol=1e-3)
        self.assertEqual(set(clean.keys()), set(t.labels))
        self.assertAlmostEqual(sum(res.probs.values()), 1.0, places=6)

    def test_adapter_score_decision(self):
        t = make_task("score", ["low risk", "medium risk", "high risk"], ["0", "1", "2"])
        res = self.adapter.run(t)
        self.assertTrue(res.ok)
        self.assertEqual(res.status, 200)
        self.assertEqual(res.probs_source, "native")
        self.assertIn("0", res.probs)
        self.assertIn("1", res.probs)
        self.assertIn("2", res.probs)
        clean = validate_probs(res.probs, t.labels, sum_tol=1e-3)
        self.assertEqual(set(clean.keys()), set(t.labels))
        self.assertAlmostEqual(sum(res.probs.values()), 1.0, places=6)


if __name__ == "__main__":
    unittest.main()
