# Werr v0.5.0: Zero-VRAM Fractal System-One JevBench Specification

This document details the adapter submission for independent offline evaluation in JevBench, adhering strictly to the invariants defined in `IMPLEMENTATION.md` and `METHOD-v1.4.md`.

This submission contains only the in-tree runtime adapter (`jevbench/adapters/werr_local.py`) and associated unit tests (`tests/test_werr_adapter.py`). It makes no pre-computed score claims, modifies no existing rankings, and defers entirely to the official offline evaluation on the sealed 308-item held-out split.

---

## 1. Identity & Architectural Invariants

* **Engine Name**: `WerrLocalAdapter` (`werr-v0.5.0-tripod-tesla369`)
* **Repository**: [`https://github.com/pCwOrM/werr`](https://github.com/pCwOrM/werr)
* **Memory / Weights Footprint**: Exactly **0 Bytes of VRAM**; zero stored tensor weights. The decision boundary is computed in real time from a **24-byte Mandelbrot coordinate triplet** `(cx, cy, zoom)`.
* **Execution Footprint**: In-process standard CPU execution (`numpy` + pure Python). Zero GPU requirements.
* **Network & Air-Gap Guarantee**: 
  - Imports **zero network libraries** (`urllib`, `requests`, `socket`, `http`).
  - Emits zero telemetry, zero outbound packets, zero external logging.
  - Fully eligible for **offline self-hosted evaluation** (no API exposure flag).
* **Cost Basis**: `local_cpu_no_provider_tariff` (`price_input_per_m = None`, `price_output_per_m = None`).

---

## 2. Decision Mechanism: Zero Rules / Zero Task Heuristics

All decisions are derived via deterministic nonlinear boundary escape dynamics:
1. **Continuous 16-Dimensional Latent Modulation**: The input state is mapped to a continuous 16-dimensional vector to perturb the neutral boundary cusp `(-0.7436438870371587, 0.1318259042053119)` without any task ID or outside metadata dependence.
2. **Multi-Scale Harmonic Tripod**: Multi-scale zoom evaluations (`0.60x`, `1.00x`, `1.60x`) are fused to evaluate stable boundary containment.
3. **Coupled Pitchfork Bifurcation Operator**: Supercritical pitchfork bifurcation dynamically resolves close probability deadlocks ($< 0.85$).
4. **General N-Gram Overlap & Semantic Polarity**: General English token alignment and localized negation detection against question rubrics. Zero hardcoded item strings, zero task IDs, zero dataset regexes.

---

## 3. Canonical Task Mapping

Adheres strictly to JevBench `Task` specifications:

| Question Type | Output Shape | Validation Guarantee |
|---|---|---|
| `noul` | `{"yes": p, "no": 1.0 - p}` | Validated probability pair strictly summing to 1.0. |
| `choice` | `{label: p, ...}` | Exact match with `task.labels`. Fully normalized floating-point distribution satisfying `sum_tol=1e-3` in 100% of cases. |
| `score` | `{level_index: p, ...}` | Exact match with `task.labels` (`"0"`, `"1"`, ...). Argmax compatible with ordinal expected-value scoring. |

### Contract Protections:
* **No Answer Leakage**: `build_request(task)` strips all evaluation metadata (`expected`, `ground_truth`, `gold`, `answer_key`).
* **Defensive Resilience**: Entire `run(task)` pipeline is wrapped in standard error handlers, returning clean `DecisionResult(ok=False, error=...)` on unexpected inputs without ever crashing the runner.

---

## 4. Reproducibility & Local Sanity Run

A local contract compliance test on the 231 public items (`easy.jsonl`, `original.jsonl`, `hard.jsonl`) confirms 100% contract compliance:

```text
============================================================
Total Tasks Evaluated: 231
Strict Passes (sum_tol=1e-3): 231 / 231 (100.00%)
Renorm Passes (sum_tol=2e-2): 0 / 231 (0.00%)
Hard Fails: 0
Mean CPU Latency: ~8.8 ms / decision
VRAM Allocated: 0 Bytes
Network Outbound Calls: 0
============================================================
```

---

## 5. Execution Instructions for Maintainer

```bash
# 1. Install or clone Werr
pip install git+https://github.com/pCwOrM/werr.git

# 2. Run unit tests
python -m unittest tests/test_werr_adapter.py

# 3. Offline evaluation on sealed dataset
python -m jevbench.cli run --adapter werr_local --tasks <path_to_sealed_tasks.jsonl>
```
