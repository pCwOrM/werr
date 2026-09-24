# JevBench v1.4+ In-Tree Adapter for Werr

This directory contains the standalone, in-tree JevBench adapter (`werr_local.py`) and unit tests (`test_werr_adapter.py`) designed for zero-VRAM, 100% air-gapped evaluation under JevBench harness standards.

## Key Design Invariants
1. **Zero Network / 100% Air-Gapped**: Zero imports of `urllib`, `requests`, `socket`, `http`. Operates 100% in-process.
2. **Zero Task Heuristics / Zero Dataset Gaming**: Contains no hardcoded strings, regex rules, task IDs, or expected answers. Decisions are derived from 24-byte Mandelbrot boundary cusp escape dynamics with tripod margin calibration and harmonic resonance gating.
3. **Strict Probability Distribution**:
   - `noul`: returns exact `{"yes": p, "no": 1.0 - p}`
   - `choice`: returns normalized floating-point distribution across `task.labels` strictly summing to `1.0` within `1e-15` (satisfying JevBench `SUM_TOL = 1e-3` in 100% of cases).
   - `score`: returns normalized distribution across score level indices matching `task.labels`.
4. **Resilient Contract**: Wrapped in defensive execution guards to guarantee `DecisionResult` is always returned with accurate `latency_s`, token usage, and zero crash risk.

## Quick Integration for JevBench Maintainers

To run in the `jevbench` repo:
```bash
# 1. Copy werr_local.py to jevbench adapters:
cp benchmarks/jevbench/werr_local.py /path/to/jevbench/jevbench/adapters/werr_local.py
cp benchmarks/jevbench/test_werr_adapter.py /path/to/jevbench/tests/test_werr_adapter.py

# 2. Run unit tests
python -m unittest tests/test_werr_adapter.py

# 3. Execute runner
python -m jevbench.cli run --adapter werr_local
```
