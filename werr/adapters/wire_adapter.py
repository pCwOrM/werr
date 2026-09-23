"""
werr.adapters.wire_adapter
==========================
Clean, transparent protocol adapter bridging external JSON benchmark tasks
directly into Werr's machine-native System-One engine (werr.engine.WerrEngine).

Design Invariants:
1. 100% Air-Gapped: Zero network imports, zero socket calls, zero telemetry.
2. 0 Bytes VRAM: Strictly invokes WerrEngine's deterministic coordinate derivation.
3. Zero Task Heuristics: Zero hand-written task strings, zero dataset gaming.
"""
import time
import re
from typing import Dict, Any, Optional

from werr.engine import WerrEngine, _normalize_text
from werr.datatypes import NoulQuestion, ChoiceQuestion, ScoreQuestion


def extract_state_text(state: Any) -> str:
    """Recursively formats arbitrary state payload into readable text."""
    if isinstance(state, str):
        return state
    if isinstance(state, dict):
        parts = []
        for k, v in state.items():
            if isinstance(v, (str, int, float, bool)):
                parts.append(f"{k}: {v}")
            elif isinstance(v, dict):
                sub = ", ".join(f"{sk}: {sv}" for sk, sv in v.items())
                parts.append(f"{k}: {{{sub}}}")
            elif isinstance(v, list):
                parts.append(f"{k}: {', '.join(str(x) for x in v)}")
            else:
                parts.append(f"{k}: {str(v)}")
        return "\n".join(parts)
    if isinstance(state, list):
        return " ".join(str(x) for x in state)
    return str(state)


class JevWireAdapter:
    """
    Transparent wire-adapter for Jev-compatible evaluation harnesses.
    Translates raw JSON tasks to typed Werr questions and delegates
    inference to WerrEngine.
    """
    def __init__(self, engine: Optional[WerrEngine] = None):
        self.engine = engine or WerrEngine()

    def decide(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes a single benchmark task through WerrEngine.
        """
        t0 = time.perf_counter()
        task_id = task.get("id", "task_0")
        q = task.get("question", {})
        q_type = q.get("type", "choice")
        instructions = q.get("instructions", "")
        criteria = q.get("criteria", {})
        labels = task.get("labels", [])
        raw_state = task.get("state", {})
        expected = task.get("expected")

        # Normalize state
        state_dict = raw_state if isinstance(raw_state, dict) else {"content": str(raw_state)}
        state_text = extract_state_text(raw_state)

        # Build native typed question
        if q_type == "choice":
            cand_labels = labels if labels else (
                list(criteria.keys()) if isinstance(criteria, dict) else []
            )
            crit_dict = criteria if isinstance(criteria, dict) else {lbl: "" for lbl in cand_labels}
            werr_q = ChoiceQuestion(instructions=instructions, criteria=crit_dict)
            resp = self.engine.decide(state=state_dict, questions={"main": werr_q})
            ans = resp.answers["main"]
            predicted = ans.choice
            probs = ans.probabilities

        elif q_type == "noul":
            werr_q = NoulQuestion(instructions=instructions)
            resp = self.engine.decide(state=state_dict, questions={"main": werr_q})
            ans = resp.answers["main"]
            predicted = "yes" if ans.decision else "no"
            probs = {"yes": ans.noul, "no": round(1.0 - ans.noul, 4)}

        elif q_type == "score":
            crit_dict = {str(i): c for i, c in enumerate(criteria)} if isinstance(criteria, list) else (
                criteria if isinstance(criteria, dict) else {"0": "low", "1": "medium", "2": "high"}
            )
            werr_q = ScoreQuestion(instructions=instructions, criteria=crit_dict)
            resp = self.engine.decide(state=state_dict, questions={"main": werr_q})
            ans = resp.answers["main"]
            predicted = str(int(round(ans.score)))
            probs = {str(k): v for k, v in ans.probabilities.items()}

        else:
            predicted = labels[0] if labels else "unknown"
            probs = {predicted: 1.0}

        lat_ms = (time.perf_counter() - t0) * 1000.0
        pred_str = str(predicted).strip().lower()
        exp_str = str(expected).strip().lower() if expected is not None else ""
        correct = (pred_str == exp_str) if expected is not None else None

        return {
            "id": task_id,
            "type": q_type,
            "predicted": predicted,
            "expected": expected,
            "correct": correct,
            "probs": probs,
            "latency_ms": round(lat_ms, 3)
        }
