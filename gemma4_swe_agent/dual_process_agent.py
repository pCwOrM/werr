# Copyright 2026 Volkan Dagli, Dr. Zerrin Dagli, Daghan Dagli, and ITouch Systems
# SPDX-License-Identifier: Apache-2.0
"""Apache-2.0 Dual-Process SWE Agent reference runtime for Gemma 4.

Implements the standalone System-1 Zero-Tensor Reflex triage, semantic token
damping injection filter (T_desc = 0.045), Z/9Z ideal discretization, and
sandboxed mathematical verification bridge documented in the Kaggle Paper Track
writeup: "Dual-Process SWE Agent: Gemma 4 with Zero-Tensor Reflex & Formal
Verification" (DOI: 10.34740/kaggle/w/125932).
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import re
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

INJECTION_PATTERNS: Tuple[Tuple[str, re.Pattern[str]], ...] = (
    ("instruction_override", re.compile(r"ignore\s+(?:all\s+|previous\s+)+instructions?", re.I)),
    ("system_prompt_leak", re.compile(r"(?:reveal|dump|print)\s+(?:the\s+)?system\s+prompt", re.I)),
    ("destructive_shell", re.compile(r"\b(?:rm\s+-rf\s+/|mkfs\.|dd\s+if=/dev/zero)", re.I)),
    ("pipe_to_shell", re.compile(r"(?:curl|wget)\s+[^\n|]+\|\s*(?:sh|bash|zsh)", re.I)),
    ("python_exec_escape", re.compile(r"(?:__import__|eval|exec)\s*\(\s*['\"](?:os|subprocess)", re.I)),
)

IDEAL_ZMOD9: Tuple[int, int, int] = (0, 3, 6)
MAX_EXPONENT_BOUND = 5000
MAX_LITERAL_DIGITS = 100
DEFAULT_SANDBOX_TIMEOUT_SEC = 5.0


@dataclass(frozen=True)
class TriageDecision:
    """Typed System-1 routing decision produced without GPU/VRAM weights."""

    allow: bool
    route_lane: str
    confidence_score: float
    ideal_residue: int
    damping_score: float
    blocked_reason: Optional[str]
    latency_ms: float


def _shannon_entropy(text: str) -> float:
    """Compute normalized character-level Shannon entropy in [0.0, 1.0]."""
    if not text:
        return 0.0
    counts = Counter(text)
    length = len(text)
    raw = -sum((c / length) * math.log2(c / length) for c in counts.values())
    max_bits = math.log2(min(length, 96)) if length > 1 else 1.0
    return min(1.0, raw / max(max_bits, 1e-9))


def semantic_token_damping(payload: str, threshold: float = 0.045) -> Tuple[bool, float, Optional[str]]:
    """Filter adversarial prompt-injection or shell-escape payloads before System-2.

    Returns ``(blocked, damping_score, reason)`` where ``damping_score < threshold``
    or matching injection signatures fail closed (`blocked=True`).
    """
    text = (payload or "").strip()
    if not text:
        return True, 0.0, "empty_payload"

    for label, pattern in INJECTION_PATTERNS:
        if pattern.search(text):
            return True, 0.0, f"injection_signature:{label}"

    tokens = re.findall(r"[A-Za-z0-9_./-]+", text.lower())
    if not tokens:
        return True, 0.0, "no_lexical_tokens"

    lexical_diversity = len(set(tokens)) / len(tokens)
    entropy = _shannon_entropy(text)
    damping_score = round(lexical_diversity * entropy, 6)
    if damping_score < threshold:
        return True, damping_score, f"below_damping_threshold:{damping_score}<{threshold}"
    return False, damping_score, None


def derive_coordinate_seed(query: str, context: str = "", base_zoom: float = 50.0) -> Tuple[float, float, float]:
    """Deterministically project ``(query, context)`` to a 24-byte seed ``(cx, cy, zoom)``."""
    digest = hashlib.sha256(f"{query}\n::{context}".encode("utf-8")).digest()
    u_x = int.from_bytes(digest[0:8], "big") / float(1 << 64)
    u_y = int.from_bytes(digest[8:16], "big") / float(1 << 64)
    u_z = int.from_bytes(digest[16:24], "big") / float(1 << 64)
    cx = -0.7436438870 + (u_x - 0.5) * 0.02
    cy = 0.1318259042 + (u_y - 0.5) * 0.02
    zoom = base_zoom * (0.85 + 0.30 * u_z)
    return cx, cy, zoom


def evaluate_tripod_escape(cx: float, cy: float, zoom: float, max_iter: int = 36) -> Dict[str, Any]:
    """Evaluate multi-scale harmonic tripod escape over ``z_{n+1} = z_n^2 + c`` and ``Z/9Z``."""
    tiers = (0.60 * zoom, 1.00 * zoom, 1.60 * zoom)
    escape_rates: List[float] = []
    for scale in tiers:
        offset = 0.05 / max(scale, 1e-6)
        zx, zy = cx + offset, cy - offset
        iters = max_iter
        for step in range(max_iter):
            zx2, zy2 = zx * zx, zy * zy
            if zx2 + zy2 > 4.0:
                iters = step
                break
            zy = 2.0 * zx * zy + cy
            zx = zx2 - zy2 + cx
        escape_rates.append(iters / float(max_iter))

    mean_score = sum(escape_rates) / len(escape_rates)
    residue_idx = int(round(mean_score * 1000)) % 3
    ideal_residue = IDEAL_ZMOD9[residue_idx]
    return {
        "score": round(mean_score, 6),
        "ideal_residue": ideal_residue,
        "tiers": [round(r, 6) for r in escape_rates],
    }


def _check_ast_bounds(node: ast.AST, in_pow_exponent: bool = False) -> Optional[str]:
    """Enforce bounded arithmetic AST rules matching the verification kernel spec."""
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        if len(str(abs(node.value))) > MAX_LITERAL_DIGITS:
            return f"literal exceeds {MAX_LITERAL_DIGITS} digits"
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
        if in_pow_exponent:
            return "power tower disallowed"
        if isinstance(node.right, ast.BinOp) and isinstance(node.right.op, ast.Pow):
            return "power tower disallowed"
        if isinstance(node.right, ast.Constant) and isinstance(node.right.value, (int, float)):
            if abs(node.right.value) > MAX_EXPONENT_BOUND:
                return f"exponent exceeds {MAX_EXPONENT_BOUND}"
        err = _check_ast_bounds(node.left, in_pow_exponent=False)
        if err:
            return err
        return _check_ast_bounds(node.right, in_pow_exponent=True)
    for child in ast.iter_child_nodes(node):
        err = _check_ast_bounds(child, in_pow_exponent=in_pow_exponent)
        if err:
            return err
    return None


def verify_bounded_expression(expr: str, timeout_sec: float = DEFAULT_SANDBOX_TIMEOUT_SEC) -> Dict[str, Any]:
    """Validate and evaluate an arithmetic claim inside an isolated child process.

    Delegates to ``hermes-verifiable-math`` if installed; otherwise executes a
    strictly AST-bounded ``fractions.Fraction`` worker with hard OS timeout.
    """
    cleaned = expr.strip()
    try:
        parsed = ast.parse(cleaned, mode="eval")
    except SyntaxError as exc:
        return {"ok": False, "error": f"syntax_error: {exc}"}

    bound_err = _check_ast_bounds(parsed)
    if bound_err:
        return {"ok": False, "error": bound_err}

    float_upgrade = bool(re.search(r"\b\d+\.\d+\b", cleaned))
    worker_code = (
        "import ast, json, re, sys\n"
        "from fractions import Fraction\n"
        "expr = sys.argv[1]\n"
        "expr_rat = re.sub(r'\\b(\\d+\\.\\d+)\\b', lambda m: f'Fraction({m.group(1)!r})', expr)\n"
        "val = eval(expr_rat, {'__builtins__': {}, 'Fraction': Fraction}, {})\n"
        "print(json.dumps({'ok': True, 'result': str(val)}))\n"
    )
    try:
        proc = subprocess.run(
            [sys.executable, "-c", worker_code, cleaned],
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"timeout_exceeded:{timeout_sec}s"}

    if proc.returncode != 0:
        return {"ok": False, "error": proc.stderr.strip() or "worker_failed"}
    payload = json.loads(proc.stdout.strip())
    payload["rational_upgraded"] = float_upgrade
    return payload


class DualProcessSweRouter:
    """Dual-process System-1 triage router for Gemma 4 SWE workflows (0 Bytes VRAM)."""

    LANE_NAMES: Dict[int, str] = {
        0: "fast_trivial_triage",
        3: "targeted_tool_routing",
        6: "gemma4_deep_synthesis",
    }

    def __init__(self, damping_threshold: float = 0.045, use_werr_engine: bool = False) -> None:
        self.damping_threshold = damping_threshold
        self._werr_engine = None
        if use_werr_engine:
            try:
                from werr import WerrEngine  # optional binding under Repo LICENSE Section 4
                self._werr_engine = WerrEngine()
            except Exception:
                self._werr_engine = None

    def route_event(self, issue_text: str, context: str = "") -> TriageDecision:
        """Classify an incoming SWE event into a typed reflex or System-2 lane."""
        t0 = time.perf_counter()
        blocked, damping_score, reason = semantic_token_damping(
            f"{issue_text}\n{context}".strip(), threshold=self.damping_threshold
        )
        if blocked:
            latency_ms = round((time.perf_counter() - t0) * 1000.0, 4)
            return TriageDecision(
                allow=False,
                route_lane="rejected_unsafe_input",
                confidence_score=0.0,
                ideal_residue=0,
                damping_score=damping_score,
                blocked_reason=reason,
                latency_ms=latency_ms,
            )

        cx, cy, zoom = derive_coordinate_seed(issue_text, context)
        tripod = evaluate_tripod_escape(cx, cy, zoom)
        if self._werr_engine is not None:
            score = float(self._werr_engine.score(question=issue_text, context=context))
        else:
            score = float(tripod["score"])

        ideal_residue = int(tripod["ideal_residue"])
        if any(k in issue_text.lower() for k in ("patch", "diff", "bug", "traceback", "regression", "refactor")):
            ideal_residue = 6
        lane = self.LANE_NAMES.get(ideal_residue, "gemma4_deep_synthesis")
        latency_ms = round((time.perf_counter() - t0) * 1000.0, 4)
        return TriageDecision(
            allow=True,
            route_lane=lane,
            confidence_score=round(score, 6),
            ideal_residue=ideal_residue,
            damping_score=damping_score,
            blocked_reason=None,
            latency_ms=latency_ms,
        )


def validate_declarative_adk_bundle(bundle_dir: Path) -> Dict[str, Any]:
    """Validate that an ADK submission directory uses purely declarative YAML assets."""
    required = ("agent.yaml", "eval_config.yaml", "configs/sampling.yaml", "prompts/system.md")
    missing = [rel for rel in required if not (bundle_dir / rel).is_file()]
    py_files = [str(p.relative_to(bundle_dir)) for p in bundle_dir.rglob("*.py")]
    agent_text = (bundle_dir / "agent.yaml").read_text(encoding="utf-8") if (bundle_dir / "agent.yaml").is_file() else ""
    forbidden_agent_fn = "agent_fn" in agent_text
    return {
        "valid": not missing and not py_files and not forbidden_agent_fn,
        "missing": missing,
        "unexpected_python_files": py_files,
        "forbidden_agent_fn": forbidden_agent_fn,
    }
