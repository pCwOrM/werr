# WERR-Gemma: Dual-Process SWE Agent Replication Package

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Kaggle Paper Track](https://img.shields.io/badge/Kaggle_Writeup-10.34740%2Fkaggle%2Fw%2F125932-20beff.svg)](https://doi.org/10.34740/kaggle/w/125932)
[![Verification Kernel: MIT v1.0.5](https://img.shields.io/badge/hermes--verifiable--math-MIT_v1.0.5-green.svg)](https://github.com/pCwOrM/hermes-verifiable-math)

Official **Apache License 2.0** companion code, declarative ADK submission bundle, and standalone reproducibility package for the Kaggle Paper Track writeup:

> **Dual-Process SWE Agent: Gemma 4 with Zero-Tensor Reflex & Formal Verification**  
> Volkan Dağlı, Dr. Zerrin Dağlı, Dağhan Dağlı (*WERR Research Lab*) — [Writeup DOI: `10.34740/kaggle/w/125932`](https://doi.org/10.34740/kaggle/w/125932)

---

## Licensing & Competition Compliance Notice

While the broader [`pCwOrM/werr`](https://github.com/pCwOrM/werr) repository (covering Web3/DeFi Werracle oracles, `answerr.me` SaaS services, and enterprise products) remains governed by **BSL 1.1**, this entire **`gemma4_swe_agent/`** directory and all Competition deliverables listed under Additional Use Grant Section 4 of the root [`LICENSE`](../LICENSE) are explicitly dual-licensed without commercial restriction under the OSI-approved **[Apache License, Version 2.0](LICENSE)** to ensure full compliance with the Kaggle Competition Rules.

The symbolic and formal verification coprocessor [`hermes-verifiable-math`](https://github.com/pCwOrM/hermes-verifiable-math) (`v1.0.5`, backwards-compatible with all `v1.0.4` isolation and AST bounds cited in the paper) is independently licensed under **MIT**.

---

## Architectural Profiles: Declarative Competition Harness vs. Full-Stack Local Profile

To ensure transparent reproducibility across both Kaggle evaluation environments and standalone local workstations, this package cleanly separates the two deployment profiles discussed in the paper:

1. **Profile A — Declarative Competition Profile (`adk_declarative_submission/`):**
   Matches the strict declarative YAML-only `adk-submission` / `swegemma` harness constraint of the featured Kaggle competition (`agent.yaml`, `eval_config.yaml`, `configs/sampling.yaml`, `prompts/system.md` targeting `gemma-4-31b-it-qat-w4a16-ct`), where custom Python `agent_fn` and runtime hooks are disallowed.
2. **Profile B — Full-Stack Dual-Process Local Profile (`dual_process_agent.py`):**
   Implements the complete local System-1 + System-2 + Verification pipeline on developer workstations:
   - **Zero-VRAM System-1 Triage (`DualProcessSweRouter`):** Deterministic 24-byte SHA-256 coordinate seed `Θ = (cx, cy, zoom)`, 3-tier harmonic tripod `Z = {0.60, 1.00, 1.60}·zoom` over `z_{n+1} = z_n^2 + c`, and `Z/9Z` closed ideal (`{0, 3, 6}`) routing in sub-5ms CPU time (0 Bytes GPU VRAM).
   - **Semantic Token Damping Filter (`T_desc = 0.045`):** Blocks indirect prompt injections and destructive shell-escape sequences before invoking System-2.
   - **Sandboxed Verification Bridge (`verify_bounded_expression`):** Enforces 5.0s OS subprocess timeout, AST resource bounds (`exponent <= 5000`, `digits <= 100`, power-tower rejection), and automatic decimal-to-rational upgrading (`0.1 + 0.2 == 0.3`).

---

## Quick Verification & Tests

Run the self-contained Apache-2.0 verification test suite directly (no GPU or proprietary dependencies required):

```bash
python -m pytest gemma4_swe_agent/tests -v
```
