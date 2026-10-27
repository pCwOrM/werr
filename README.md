<div align="center">

# WERR
### Zero-Memory Fractal Reflex Decision Engine · Waves & Errors

[![License: BSL 1.1](https://img.shields.io/badge/License-BSL_1.1-0ea5e9.svg)](LICENSE)
[![Formal Verification: Lean 4](https://img.shields.io/badge/Lean_4-0_sorry_(Verified)-10b981.svg)](https://github.com/pCwOrM/gap-lean4-port)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-6366f1.svg)](https://pypi.org/project/werrio/)
[![Zenodo DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22774934-f59e0b.svg)](https://doi.org/10.5281/zenodo.22774934)
[![ArXiv Preprint](https://img.shields.io/badge/arXiv-2609.25498-b91c1c.svg)](https://arxiv.org/abs/2609.25498)

<p align="center">
  <b>A deterministic, procedural System-1 reflex engine that derives typed decisions directly from Mandelbrot boundary escape dynamics—requiring zero neural weights, zero VRAM, and sub-microsecond compute latency.</b>
</p>

[Quickstart](#-quickstart-in-30-seconds) •
[Architecture](#-mathematical--formal-architecture) •
[Decision Primitives](#-the-three-typed-primitives) •
[Benchmarks](#-empirical-evaluation--benchmarks) •
[Formal Proofs](#-formal-verification-lean-4) •
[Ecosystem](#-the-werr-ecosystem) •
[Research Chronology](RESEARCH_CHRONOLOGY.md) •
[Türkçe Dokümantasyon](README_TR.md)

</div>

---

## 🏛️ The Paradigm

Contemporary artificial intelligence architectures rely predominantly on massive, dense parameter tensors. While effective for generative deliberation (System-2), deploying multi-gigabyte models for ultra-high-frequency reflex arbitration, edge gating, or on-chain logic incurs unsustainable computational latency, memory footprints, and non-deterministic hallucination risks.

**WERR (Waves & Errors)** introduces an orthogonal paradigm: **Procedural Reflex Inference**. Instead of storing billions of learned weights in memory, WERR treats decision boundaries as geometric invariants across the complex plane. Given an arbitrary natural language prompt, program state, or telemetry frame:

1. **Deterministic Projection:** The context is projected onto bounded coordinates in the complex plane $\mathbb{C}$.
2. **Iterative Orbital Dynamics:** The coordinate is evaluated through procedural polynomial escape trajectories ($z_{n+1} = z_n^2 + c$).
3. **Harmonic Reflex Extraction:** Three immutable typed decision primitives are derived in $\le 0.3\,\mu\text{s}$ on commodity CPUs or 32-byte storage slots on the Ethereum Virtual Machine (EVM).

```
Input Telemetry / Context
           │
           ▼
┌──────────────────────────────────────┐
│  Procedural Coordinate Projection    │  ◄── 24-byte coordinate seed
└──────────────────────────────────────┘
           │  c = x + iy ∈ ℂ
           ▼
┌──────────────────────────────────────┐
│   Orbital Complex Dynamics Engine    │  ◄── z_{n+1} = z_n^2 + c
└──────────────────────────────────────┘
           │  Escape radius & Lyapunov Lyapunov exponent
           ▼
┌─────────────────────────────────────────────────────────────┐
│                   Three Typed Primitives                    │
│   • noul   (Boolean binary gate: ALLOW / DENY)              │
│   • choice (Categorical quadrant: 0, 1, 2, 3)               │
│   • score  (Continuous severity metric: [0.0, 1.0])         │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚡ Quickstart in 30 Seconds

WERR is published as a zero-dependency Python package and an open-source Rust/C core.

### Installation

```bash
pip install werrio
```

*Or install the latest release directly from GitHub:*

```bash
pip install git+https://github.com/pCwOrM/werr.git
```

### Basic Usage

```python
import werr

# Initialize the engine (loads immutable coordinate seeds in memory)
engine = werr.WerrEngine()

# 1. Binary Reflex Gate (noul): returns True or False
is_safe = engine.noul(
    question="Is this transaction payload safe to sign?",
    context="Transfer 0.05 ETH to verified contract 0x7a25... on Base L2"
)

# 2. Discrete Route Selector (choice): returns categorical integer index [0, 1, 2, 3]
route = engine.choice(
    question="Select the optimal execution lane:",
    options=["FastLane Atlas", "Private Sequencer", "Public Mempool", "Off-chain Solver"]
)

# 3. Continuous Severity Metric (score): returns float in range [0.0, 1.0]
risk_score = engine.score(
    question="Evaluate liquidation cascade vulnerability under 15% collateral drop",
    context="MetaMorpho Steakhouse USDC Vault · Borrow: $4.73B · Health Factor: 1.04"
)

print(f"Safety Gate: {is_safe} | Selected Route: {route} | Risk: {risk_score:.4f}")
```

---

## 📐 The Three Typed Primitives

WERR avoids ambiguous natural-language string outputs in automated runtime pipelines. Every evaluation resolves to one of three strictly typed invariants:

| Primitive | Mathematical Nature | Output Type | Primary Industry Use-Case |
| :--- | :--- | :---: | :--- |
| **`noul`** | Topological boundary separation | `bool` | High-throughput safety firewalls, agent action permits, guardrails. |
| **`choice`** | Orthogonal quadrant partition | `int` $\in \{0, 1, 2, 3\}$ | Multi-lane transaction routing, policy triage, heuristic branch selection. |
| **`score`** | Normalized Lyapunov escape velocity | `float` $\in [0.0, 1.0]$ | Dynamic DeFi fee computation, collateral shock scoring, anomaly ranking. |

---

## 🔬 Mathematical & Formal Architecture

WERR operates across an orthogonal 8-state ($2^3$) parameter matrix (v0.5.1), balancing domain routing, lexical ontology, and harmonic tuning:

* **Zero-VRAM State Machine:** Operates without neural network weights. Execution memory footprint is $\le 128\,\text{KB}$ across runtime stacks.
* **Bounded Convergence:** Escape bounds are rigorously proved; the engine cannot hang, loop indefinitely, or consume unbounded stack frames.
* **Deterministic Replicability:** The identical seed and input context yield bit-exact outputs across x86-64 bare metal, ARM64 Apple Silicon, RISC-V edge microcontrollers, and EVM smart contracts.

---

## 🏆 Empirical Evaluation & Benchmarks

The procedural reflex paradigm has been validated across standardized benchmarks and real-time execution environments:

| Benchmark / Environment | Task & Domain | Baseline / Competitor | WERR Result | Performance Multiplier |
| :--- | :--- | :--- | :---: | :---: |
| **WindTunnel WebMCP** | 49 Complex Web Automation Scenarios | LLM-based autonomous agents | **49 / 49 Solved (100%)** | 0 tokens consumed, $\le 1\,\text{ms}$ step latency |
| **Snake AI Real-Time** | Continuous 60 FPS trajectory reflex | Laya-MLX (Dense PyTorch neural net) | **Surpasses MLX at 600 steps** | $40\times$ faster decision loop, zero GPU load |
| **Jevenator 2 Vision** | Real-time object tracking & triage | Maisa djev neural classifier | **Competitive parity** | $99.98\%$ reduction in memory footprint |
| **Base Morpho SVR** | Multi-call liquidation telemetry | Standard mempool searchers | **94.38% value recapture** | $\le 0.3\,\text{ms}$ solver margin compression |

> 📊 **Historical Benchmark Archive:** Complete ablation studies, JevBench grand matrix versions (v1.1 to v1.4.1), and 40-core Xeon gauntlet logs are recorded in [RESEARCH_CHRONOLOGY.md](RESEARCH_CHRONOLOGY.md).

---

## 🛡️ Formal Verification (Lean 4)

The core topological invariants, boundary escape inequalities, and discrete partition theorems of WERR are formally verified in the **Lean 4** interactive theorem prover with **0 `sorry`** statements.

* **Repository:** [`pCwOrM/gap-lean4-port`](https://github.com/pCwOrM/gap-lean4-port)
* **Preprint / Monograph:** Zenodo DOI: [`10.5281/zenodo.22974544`](https://doi.org/10.5281/zenodo.22974544)
* **Scope:** Machine-checked formal verification of Schreier-Sims sifting, cyclic quotient stability, and boundary containment under bounded perturbation.

---

## 🌐 The WERR Ecosystem

WERR serves as the foundational mathematical engine across a tri-fold architectural stack:

```
                          ┌─────────────────────────────┐
                          │            WERR             │
                          │   Core Mathematical Engine  │
                          │  Zero-Memory System-1 Reflex │
                          └──────────────┬──────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
  ┌─────────────────────────────┐                 ┌─────────────────────────────┐
  │          Werracle           │                 │           answerr           │
  │   On-Chain Decision Oracle  │                 │  Dual-Cognition Workspace   │
  │  DeFi Risk Radar & DaaS     │                 │ Natural Language Gating API │
  │   https://radar.werracle.com│                 │     https://answerr.me      │
  └─────────────────────────────┘                 └─────────────────────────────┘
```

* **`werr`:** Core algorithm, coordinate seeds, and native Python/Rust runtime libraries.
* **[`werracle`](https://github.com/pCwOrM/werracle):** Smart contract implementations, Q16.16 fixed-point Solidity escape math, Uniswap v4 hook templates, and [Werracle Risk Radar](https://radar.werracle.com).
* **[`answerr`](https://github.com/pCwOrM/answerr):** Dual-cognition workspace bridging System-2 deliberate natural language policy compilation with WERR System-1 deterministic execution.

---

## 📄 Academic Citation & Archival References

If you cite or replicate this research in scientific publications, please use the following citation metadata:

```bibtex
@software{dagli2026werr,
  author       = {Dağlı, Volkan and Dağlı, Zerrin and Dağlı, Dağhan},
  title        = {{werr: Zero-Memory Fractal System-One Decision Engine (Waves & Errors)}},
  month        = oct,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v0.5.1},
  doi          = {10.5281/zenodo.22774934},
  url          = {https://github.com/pCwOrM/werr}
}
```

* **Archival Preprint:** arXiv:2609.25498 `[cs.AI / math.DS]` ([https://arxiv.org/abs/2609.25498](https://arxiv.org/abs/2609.25498))
* **Full Research Chronology:** [`RESEARCH_CHRONOLOGY.md`](RESEARCH_CHRONOLOGY.md)

---

## ⚖️ License & Intellectual Property

* **Open-Science, Educational & Evaluation Use:** The Licensed Work is free to run, inspect, benchmark, test, fork, and replicate for all non-commercial academic research and personal evaluations under the **Business Source License 1.1 (BSL 1.1)**.
* **Commercial Operations & Production Licensing:** Any commercial production use, hosted SaaS deployment, or proprietary redistribution requires a commercial license from the Licensor:
  * **Licensor:** `ITOUCH BİLİŞİM SİSTEMLERİ MÜHENDİSLİK DANIŞMANLIK SANAYİ VE TİCARET LİMİTED ŞİRKETİ` (`ITouch Systems` · Cukurova University Science Park, Adana, Türkiye).
  * **Scientific Co-Authors & Inventors:** Volkan Dağlı (*Anadolu University*), Dr. Zerrin Dağlı (*Mersin University — Academic Advisor, Co-Author & Co-Inventor*), Dağhan Dağlı (*Toros University — Co-Author & Co-Inventor*).
  * **Chain of Title & Assignment:** The scientific co-authors have irrevocably assigned administrative and IP management authority to Volkan Dağlı, who has transferred exclusive global commercial licensing and operational rights to ITouch Systems.
  * **Trademarks:** `WERR™`, `Werracle™`, `answerr™`, and `WerrSoma™` are trademarks owned exclusively by ITouch Systems.
  * **Patent Applications:** TÜRKPATENT **TR 2026/016285** & **TR 2026/016633**.
  * **Inquiries:** `contact@werracle.com` · `ask@answerr.me`

---

<div align="center">
  <sub>Developed by ITouch Systems · Cukurova University Science Park, Adana, Turkey</sub><br>
  <sub>Copyright &copy; 2026 ITouch Bilişim Sistemleri Ltd. Şti. All rights reserved.</sub>
</div>
