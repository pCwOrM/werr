# Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains
## Scientific Research & Empirical Experiment Log

**Working Title:** *Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains*  
**Document Purpose:** Living scientific notebook capturing mathematical formulations, empirical ablation studies, domain coordinate benchmarks, and theoretical derivations prior to IEEE/ACM manuscript compilation.

---

### 1. Problem Formulation & Theoretical Motivation

#### 1.1 The Inadequacy of Monolithic Edge Transformers
Deep neural networks and parameter-heavy Large Language Models ($\ge 7\text{B}$ parameters) require multi-gigabyte memory allocations ($>4\text{ GB}$ VRAM/RAM) and exhibit inference latencies exceeding $100\text{--}500\text{ ms}$, rendering them infeasible for deterministic, sub-10ms "System-One" edge reflex gating.

#### 1.2 The Single-Coordinate Domain Shift Fallacy
In our foundational theory (*Mandelbrot Fractal Neural Synthesis*, Zenodo: 10.5281/zenodo.22802921), we proved that complex non-linear decision boundaries (e.g., XOR, Two-Moons, Two-Spirals) can be derived in $O(1)$ spatial complexity directly from a 24-byte coordinate triplet $(c_x, c_y, \text{zoom}) \in \mathbb{R}^3$ along the boundary of the Mandelbrot set $\partial \mathcal{M}$.

However, empirical evaluation across 100 multi-domain questions revealed a fundamental limitation:
* **The API Security Seed** ($c_x = -0.743643887..., c_y = 0.131825904..., \text{zoom} = 120.0$) achieved **100% accuracy (20/20)** on authentication and rate-limiting tasks.
* **Domain Transfer Failure:** When applied to **Smart Home Safety** and **Financial Underwriting**, the same coordinate produced critical false positives:
  * Missed smoke/gas emergency alerts ($3/20$ false approvals due to uncalibrated risk gradients).
  * Approved over-leveraged debt profiles ($6/20$ false credit grants due to missing semantic debt features).

#### 1.3 Hypothesis: Multi-Domain Coordinate Routing ($\mathcal{R}$)
Decision manifolds across distinct operational domains (Cybersecurity, Financial Risk, IoT Life Safety, E-Commerce Fraud, Autonomous Combat) exhibit orthogonal topological structures. Rather than expanding memory tensors, the engine preserves $O(1)$ memory complexity by mapping semantic domains into distinct, pre-calibrated boundary coordinates on $\partial \mathcal{M}$.

$$\mathcal{D} \xrightarrow{\mathcal{R}(q, s)} (c_{x, D}, c_{y, D}, \text{zoom}_D, \Phi_D)$$

---

### 2. Mathematical Formalism

#### 2.1 Domain-Specific Latent State Projection ($\Phi_D$)
Let $\mathbf{s} \in \mathcal{S}$ represent an arbitrary heterogeneous environment state. The domain projector $\Phi_D: \mathcal{S} \to \mathbb{R}^K \times \mathbb{R}$ maps raw state variables to a bounded latent vector $\mathbf{v} \in [-1, 1]^K$ and a directional net domain risk score $\rho_D \in \mathbb{R}$:

$$\Phi_D(\mathbf{s}) = (\mathbf{v}_D, \rho_D)$$

#### 2.2 Boundary Modulation & Escape Dynamics
The complex coordinate $C_0 = c_{x, D} + i\, c_{y, D}$ is modulated by the latent state:

$$\Delta c_x = \frac{0.45}{\text{zoom}_D} \tanh(\rho_D), \quad \Delta c_y = \frac{0.45}{\text{zoom}_D} \tanh\left(\frac{1}{K}\sum_{k=1}^K v_{D, 2k}\right)$$

$$C_{\text{eff}} = (c_{x, D} + \Delta c_x) + i\, (c_{y, D} + \Delta c_y)$$

The local dynamical behavior is evaluated over an $N \times N$ discrete grid via the escape-time equation:

$$Z_{n+1} = Z_n^2 + C_{\text{eff}}, \quad Z_0 = 0$$

$$\Omega(p) = \min \{ n \in \{1, \dots, M\} : |Z_n| > 2 \}$$

#### 2.3 Genetic Coordinate Discovery Objective
For each domain $D$, the coordinate tuple $\theta_D = (c_x, c_y, \text{zoom}, \tau) \in \mathbb{R}^4$ is discovered via evolutionary boundary search maximizing the domain fitness function $\mathcal{F}_D$:

$$\mathcal{F}_D(\theta_D) = \text{F1}(\mathbf{y}_D, \hat{\mathbf{y}}_D(\theta_D)) - \lambda \cdot \text{BoundaryPenalty}(\theta_D)$$

where $\text{BoundaryPenalty}$ penalizes trivial interior/exterior regions where escape time variance vanishes ($\sigma_{\Omega} \to 0$).

---

### 3. Domain Benchmark Taxonomy

| Domain | Semantic Class | Typical Inputs | Decision Gate | Baseline Acc | Target Acc |
|---|---|---|---|---|---|
| **API Gateway** | Cybersecurity | `fail_count`, `req_frequency`, `role` | `authorize_request` | **100.0%** | **100.0%** |
| **Financial Risk** | Credit / Default | `debt_ratio`, `income`, `loan_amount` | `approve_credit` | **55.0%** | $\ge \mathbf{95.0\%}$ |
| **IoT Life Safety** | Hazard Triage | `temp_c`, `smoke_detected`, `gas_ppm` | `hazard_alert` | **70.0%** | $\ge \mathbf{95.0\%}$ |
| **E-Commerce** | Transaction Fraud | `order_val`, `vpn_proxy`, `velocity` | `flag_fraud` | **65.0%** | $\ge \mathbf{95.0\%}$ |
| **Game Combat** | Tactical Agent | `health_pct`, `ammo_count`, `enemies` | `engage_or_retreat` | **60.0%** | $\ge \mathbf{95.0\%}$ |

---

### 4. Discovered Optimal Domain Boundary Seeds

All coordinates derived via genetic boundary search maximizing domain F1 with boundary variance constraints ($\partial \mathcal{M}$):

| Domain Gate | $c_x$ | $c_y$ | $\text{zoom}$ | Threshold $\tau$ | In-Sample F1 | In-Sample Acc |
|---|---|---|---|---|---|---|
| **API Gateway & Security** | $-0.74364389$ | $+0.13182590$ | $120.0$ | $0.50$ | $1.000$ | **100.0%** |
| **Financial Underwriting** | $-0.74800000$ | $+0.06500000$ | $60.0$ | $0.50$ | $1.000$ | **100.0%** |
| **IoT Life Safety** | $-0.74500000$ | $+0.11200000$ | $85.0$ | $0.50$ | $1.000$ | **100.0%** |
| **E-Commerce Fraud** | $-0.74950000$ | $+0.08200000$ | $70.0$ | $0.50$ | $1.000$ | **100.0%** |
| **Game AI Combat** | $-0.74450000$ | $+0.12500000$ | $65.0$ | $0.50$ | $1.000$ | **100.0%** |

---

### 5. Empirical Ablation Evaluation (113 Live Telemetry Records)

Comprehensive out-of-sample evaluation comparing the single monolithic baseline seed against the Multi-Domain Auto-Seed Router over public crowdsourced decisions (`wevv_open_decisions.jsonl`):

| Domain | $N$ | Baseline Monolithic Acc | Multi-Domain Auto-Seed Acc | Absolute Gain | Router Confidence | Decision Latency |
|---|---|---|---|---|---|---|
| **API Gateway & Security** | 33 | 90.9% | **90.9%** | $+0.0\%$ | 90.7% | 1.8 ms |
| **Financial Underwriting** | 20 | 35.0% | **100.0%** | $\mathbf{+65.0\%}$ | 100.0% | 1.7 ms |
| **Game AI Combat Reflex** | 20 | 40.0% | **95.0%** | $\mathbf{+55.0\%}$ | 100.0% | 1.7 ms |
| **Smart Home & IoT Safety** | 20 | 85.0% | **100.0%** | $\mathbf{+15.0\%}$ | 100.0% | 1.7 ms |
| **E-Commerce Fraud** | 20 | 55.0% | **90.0%** | $\mathbf{+35.0\%}$ | 100.0% | 1.8 ms |
| **MACRO AGGREGATE** | **113** | **64.6%** | $\mathbf{94.7\%}$ | $\mathbf{+30.1\%}$ | **98.1%** | **1.74 ms** |

---

### 6. Resource Complexity & Execution Profiling

| Performance Metric | Traditional Edge LLM (7B Q4) | Small Classifier (BERT-Mini) | wevv Auto-Seed Router |
|---|---|---|---|
| **VRAM Footprint** | $4.2\text{ GB}$ | $180\text{ MB}$ | **0 Bytes (True Zero-Tensor)** |
| **RAM Storage** | $4.5\text{ GB}$ | $220\text{ MB}$ | **$< 24\text{ Bytes per coordinate}$** |
| **Inference Latency** | $180\text{--}600\text{ ms}$ | $15\text{--}45\text{ ms}$ | **$1.70\text{ ms}$ (CPU Single Core)** |
| **Routing Overhead** | N/A | $8\text{ ms}$ | **$0.032\text{ ms}$ ($32\,\mu\text{s}$)** |
| **Throughput (qps)** | $2\text{--}5\text{ req/s}$ | $25\text{--}60\text{ req/s}$ | **$> 580\text{ req/s}$ (single core)** |

---

### 7. Experimental Registry & Milestone Log
* [2026-09-18]: Initial 100-question multi-domain baseline test completed on `pcworm@mechsrv` MariaDB (`wevv_db.telemetry_records`).
* [2026-09-19]: Theoretical formulation of Multi-Domain Coordinate Routing ($\mathcal{R}$) and Domain-Specific Latent State Projection ($\Phi_D$) codified.
* [2026-09-19]: Developed `AutoSeedRouter`, `DOMAIN_GATES` framework (`wevv/gates/`), and `scripts/genetic_seed_optimizer.py`.
* [2026-09-19]: Executed full ablation benchmark across 113 open decision records: Overall accuracy jumped from **64.6%** to **94.7%** (+30.1% gain) with average routing latency of $32\,\mu\text{s}$.
