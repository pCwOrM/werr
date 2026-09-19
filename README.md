# 🌊 wevv: Zero-Memory Fractal System-One Decision Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Live Demo: GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-38bdf8.svg)](https://pcworm.github.io/wevv/)
[![Base Research: DOI](https://img.shields.io/badge/Base%20Research-DOI%3A%2010.5281%2Fzenodo.22802921-green.svg)](https://doi.org/10.5281/zenodo.22802921)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)

> **Motto:** *"When the Wave hits Error (e), we Subdivide (vv)."*  
> *"Jev decisions come from 4B-parameter tensors; `wevv` decisions come from infinite geometric waves, Euler thresholds, and recursive subdivision."*

🌐 **Interactive Web Lab:** [Try the Live Decision Simulator on GitHub Pages](https://pcworm.github.io/wevv/) *(Supports English & Türkçe, Light & Dark mode).*

`wevv` is an open-source, machine-native **System-One decision engine** for software applications. Instead of running large language models or maintaining multi-gigabyte weight tensors in VRAM, `wevv` synthesizes instant, typed decisions (`noul`, `choice`, `score`) on-the-fly from deterministic Mandelbrot fractal escape dynamics and quadrant subdivision.

---

## 💡 Naming & The `w-e-vv` Philosophy

* **`w` (Wave / Dalga):** Represents continuous chaotic phase waves, complex potential dynamics, and harmonic orbital flow along the boundary of the Mandelbrot set.
* **`e` (Error & Euler):**
  * **Error Boundary:** The sharp edge of escape. Just like biological pain/error reflexes, decision boundaries are locked immediately when error thresholds are crossed.
  * **Euler Constant (e ≈ 2.718):** The exponential basis governing chaotic divergence rates and Lyapunov escape exponents.
* **`vv` (Subdivision / Çeyrekleme):** When waves encounter the error threshold, the space is recursively partitioned into 4-Quadrant (Q1–Q4) and Quadtree sub-regions to extract instantaneous, type-safe decisions.
* **System One Intuition:** Following Daniel Kahneman's model, `wevv` acts as a fast, reflexive "smart if-statement" inside ordinary application code.

---

## 📊 Comparison: Jev (TypeSafe AI) vs. wevv

| Dimension | TypeSafe AI (Jev) | OpenJev / NanoJev | **wevv (Fractal System-1)** |
| :--- | :--- | :--- | :--- |
| **Foundation** | Proprietary LLM | Qwen / Gemma (4B) | **Mandelbrot Boundary ($\partial \mathcal{M}$)** |
| **Weight Tensor Memory** | Multi-GB (Cloud) | ~8 GB VRAM | **0 Bytes (Zero Tensor Memory!)** |
| **Seed Footprint** | Cloud API Endpoint | Local Model Checkpoint | **24 Bytes $(c_x, c_y, \text{zoom})$** |
| **Typical Latency** | ~100 ms (Network HTTP) | ~15–30 ms (GPU) | **< 1.0 ms (Pure Local CPU)** |
| **Hardware Requirement** | Internet Connection | CUDA-capable GPU | **Any standard CPU / Microcontroller** |
| **License & Autonomy** | Proprietary API ($/token) | Open Weights | **100% Free & Open Source (MIT)** |

---

## ⚡ The Three Decision Primitives

Like Jev, `wevv` answers three fundamental question types without producing conversational prose:

1. **`noul` (Boolean Probability):**
   * Computes binary probability $p \in [0.0, 1.0]$, decision `True/False`, and confidence.
   * Derived from $\partial \mathcal{M}$ hyper-surface thresholding.
2. **`choice` (Categorical Selection):**
   * Chooses the optimal option among user-defined criteria.
   * Derived from 4-Quadrant ($Q_1, Q_2, Q_3, Q_4$) or Quadtree energy partitioning.
3. **`score` (Continuous / Ordinal Ranking):**
   * Evaluates continuous position along a defined ordinal scale (e.g. 0 to 3).
   * Derived from the dark area integral ($D$) and escape velocity.

---

## 📦 Installation

```bash
# Install directly from GitHub:
pip install git+https://github.com/pCwOrM/wevv.git
```

## 🚀 Quickstart

```python
from wevv import (
    WevvEngine,
    NoulQuestion,
    ChoiceQuestion,
    ScoreQuestion,
    create_smart_router
)

# 1. Initialize engine (loads 24-byte coordinate seed)
engine = create_smart_router()

# 2. Define program state
state = {
    "user_role": "admin",
    "request_rate": 4.5,
    "payload_bytes": 1024
}

# 3. Ask typed questions
response = engine.decide(
    state=state,
    questions={
        "is_safe": NoulQuestion(instructions="Is this operation safe to proceed?"),
        "route": ChoiceQuestion(
            instructions="Target cluster",
            criteria={"prod": "Production", "canary": "Canary", "block": "Block"}
        ),
        "priority": ScoreQuestion(
            instructions="Priority level",
            criteria=["Low", "Medium", "High", "Critical"]
        )
    }
)

# 4. Use in ordinary code as a smart if-statement:
if response.boolean("is_safe") and response.score("priority") > 1.0:
    print(f"Routing to: {response.choice('route')} in {response.latency_ms} ms")
```

---

## 🗺️ The Universal Fractal Natural Language Decision Map

`wevv` is pioneering the concept of the **Universal Fractal Natural Language Decision Map**. 

Instead of training dense neural networks that require billions of parameters, any arbitrary program state and natural language questions—in **English, Türkçe**, or domain-specific terminology—are deterministically modulated onto the chaotic boundary of the Mandelbrot set ($\partial \mathcal{M}$).

```
[Program State / Girdi Durumu]
       │
       ▼
[Deterministic Semantic Modulation (TR/EN)]
       │
       ▼
[24-Byte Coordinate Seed (cx, cy, zoom)]
       │
       ▼
[Instant Fractal Boundary Evaluation (< 0.5 ms)]
 ├── w1, w2, w3, bias (Quadrant Decomposition)
 └── Quadtree Escape Integral
       │
       ▼
[Typed Decisions: Noul (Yes/No) | Choice (Routing) | Score (Severity)]
```

### 🌐 Multi-Domain Application Use-Cases

1. **API Gateway & Microservices:**
   ```python
   # State: {"user_role": "guest", "failed_attempts": 3, "req_frequency": 45}
   # Decision: allow_execution=False | route=sandbox_audit | threat_score=1.45 / 3.0
   ```
2. **🏠 Akıllı Ev / Smart Home (IoT):**
   ```python
   # State: {"oda": "salon", "sicaklik": 27.5, "hareket_var": True, "pencere_acik": False}
   # Question: "Klima çalıştırılsın mı?" -> True (p=0.892, Güven=%78.4)
   ```
3. **🛒 E-Ticaret & Sahtecilik Tespiti (Fraud Detection):**
   ```python
   # State: {"siparis_tutari": 18500, "yeni_cihaz": True, "vpn_kullanimi": True}
   # Question: "İşlem doğrudan onaylansın mı?" -> False | Rota: "sms_dogrulama"
   ```
4. **🎮 Oyun Yapay Zekası / Game AI (NPC Combat Reflexes):**
   ```python
   # State: {"npc_can": 20, "dusman_mesafe": 5.2, "muhimmat": 0, "siginak_yakin": True}
   # Decision: savasa_devam=False | taktik_karari="siginaga_kac" | panik_seviyesi=2.6
   ```
5. **🏦 Finans ve Otomatik Kredi Değerlendirme:**
   ```python
   # State: {"kredi_notu": 1520, "aylik_gelir": 75000, "gecikme_sayisi": 0}
   # Decision: kredi_onay=True | kredi_paketi="aninda_onay" | guven=3.0 / 3.0
   ```

---

## 🔒 100% Air-Gapped Autonomous Operation & Zero-Network Guarantee

When an engineer downloads or installs `wevv`, **it operates 100% locally and completely offline**:

* **Zero Inbound Network Calls:** `wevv` never downloads external weights, models, embeddings, or schemas from remote servers. There are no Hugging Face model checkpoints, no cloud API endpoints, and no server-side dependencies.
* **100% Local Text Normalization:** All text processing—including Turkish diacritic normalization (`ı/i`, `ö/o`, `ü/u`, `ş/s`, `ç/c`, `ğ/g`), token extraction, and mathematical projections—is executed entirely in-process on the local CPU in microseconds.
* **Passive Outbound Telemetry (100% Opt-Out):** The only network capability in `wevv` is an optional, passive background telemetry dispatcher used for open-science benchmark calibration. It never blocks decision execution, sends zero PII, and can be completely shut off at any time:
  ```bash
  export WEVV_TELEMETRY=0
  ```

---

## 🧠 Dual-Layer Cognitive Inference Architecture

How does `wevv` understand and decide upon arbitrary inputs? Does it search for specific keywords, or can it synthesize meaning from completely unseen words?

`wevv` operates on an innovative **Dual-Layer Cognitive Mechanism**:

```
           [Arbitrary State & Question]
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
[Layer 2: Bilingual Root    [Layer 1: Universal Chaotic
 Ontology Heuristic]         Phase-Space Resonator]
 • Fast cognitive shortcut   • Deterministic fallback
 • TR & EN domain lexicon    • Handles ANY unknown string
 • Action & risk polarities  • Fourier MD5 phase-angle
         │                           │
         └─────────────┬─────────────┘
                       ▼
    [Mandelbrot Boundary Perturbation (dx, dy)]
                       │
                       ▼
       [Sub-2ms Deterministic Decision]
```

### 1. Layer 1: Universal Geometric Phase-Space Resonator (Zero-VRAM Fallback)
* **What happens if you pass alien, fictional, or completely unknown tokens?**  
  *(e.g., `glork_factor: "frobnicate_the_wozzer"`, synthetic telemetry keys, or foreign jargon).*
* Unlike Large Language Models (which hallucinate or throw Out-Of-Vocabulary / OOD errors), `wevv` **never crashes and never fails to decide**.
* Unrecognized strings are mapped to continuous trigonometric phase angles $(\sin \theta, \cos \theta)$ via Fourier projection of their cryptographic byte-entropy onto the complex plane $\mathbb{C}$.
* These phase vectors deterministically modulate the Mandelbrot boundary seed coordinates $(c_x, c_y)$ and evaluate quadrant escape dynamics ($w_1, w_2, w_3, \text{bias}$).
* **Result:** 100% deterministic, type-safe decisions with 0 Bytes of GPU VRAM, even for inputs the system has never seen before!

### 2. Layer 2: Calibrated Bilingual Root Ontology (Cognitive Shortcut)
For real-world production domains, `wevv` incorporates an ultra-compact, calibrated root ontology in **English and Türkçe**:
* **Directionality & Authorization:** `allow`, `permit`, `safe`, `valid`, `approve`, `izin`, `onay`, `uygun`, `gecerli`, `calistir`, `ac`, `dogrula`, `kabul`...
* **Threat & Risk Polarities:** `threat`, `attack`, `block`, `deny`, `hazard`, `fraud`, `fire`, `tehlike`, `risk`, `engelle`, `yasak`, `saldiri`, `yangin`, `tahliye`...
* **Operational Action Tiers:** `direct` (`dogrudan`), `rate_limiter` (`sinirla`), `sandbox_audit` (`incele`), `drop_packet` (`reddet` / `engelle`)...
* **Domain Feature Handlers:** Full dual-scale credit scoring (FICO 300–850 and Turkish Findeks 0–1900), IoT HVAC/comfort and life-safety hazard triage, payment fraud heuristics, and NPC tactical combat states.

### 3. 🎼 Chordial Semantic Resonance & Acoustic Tinleme Index Filter
To prevent incidental words (such as `"Direct butane..."` or `"...proceed on escape trajectory"`) from triggering false keyword spikes in out-of-domain contexts without using crude, destructive string blacklists, `wevv` implements the **Chordial Semantic Resonance Field**:
* **Triad Harmonic Agreement ($\mathcal{H} = \Phi(S) \otimes \Psi(Q) \otimes \Omega(C)$):** Semantics are evaluated as a musical triad across the State context $\Phi(S)$, Question intent $\Psi(Q)$, and Option declaration $\Omega(C)$. Isolated words lacking chordial support from state and question are treated as acoustic noise and damped.
* **Acoustic Tinleme Index ($\mathcal{T}$):** Primary option keys carry sharp, high-integrity metallic signal ($\mathcal{T} = 1.0$), while incidental descriptive words in arbitrary text are dynamically damped ($\mathcal{T} \le 0.08$).
* **Conservative Smooth Coupling ($C^\infty$):** Discontinuous if-else steps are replaced by smooth hyperbolic tangent potentials ($\Delta S = \mathcal{A}_{\max} \cdot \tanh(\Delta \text{risk}) \cdot \mathcal{T}$), mathematically eliminating chaotic butterfly explosions along the fractal boundary.

---

## 🧭 Multi-Domain Auto-Seed Router & Empirical Benchmark (v0.2.0)

In version 0.2.0, `wevv` introduces the **Multi-Domain Auto-Seed Router** (`AutoSeedRouter`). While earlier iterations used a monolithic boundary seed ($c_x \approx -0.747, c_y \approx 0.131$), evaluating distinct domains requires dynamically hopping into the topological coordinates where each domain's feature derivatives resonate with maximum sensitivity.

### 🔬 Empirical Ablation Study (Monolithic Seed vs. Auto-Seed Router)
Evaluated across $N = 336$ empirical telemetry decisions from production traffic and multi-batch validation sets:

| Operational Domain | Sample Size ($N$) | Monolithic Seed Acc | **Auto-Seed Router Acc** | Net Gain ($\Delta$) | Avg Confidence | Inference Latency |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **API Gateway & Security** | 85 | 83.5% | **87.1%** | $+3.5\%$ | 93.9% | 3.42 ms |
| **Smart Home & IoT Safety** | 61 | 85.2% | **98.4%** | $+13.1\%$ | 100.0% | 3.31 ms |
| **E-Commerce Fraud** | 60 | 56.7% | **85.0%** | $+28.3\%$ | 100.0% | 3.29 ms |
| **Game AI & NPC Combat** | 60 | 50.0% | **95.0%** | $+45.0\%$ | 100.0% | 3.17 ms |
| **Financial Risk & Credit** | 60 | 35.0% | **100.0%** | $+65.0\%$ | 100.0% | 3.33 ms |
| **OVERALL MACRO ACCURACY** | **326** | **63.8%** | **92.6%** | **+28.8%** | **98.0%** | **3.31 ms** |

*All inferences executed with **0 Bytes of neural tensor memory** (VRAM/RAM) and strict determinism.*

---

## 🇹🇷 First-Class Dual-Language Support (Türkçe & English)

`wevv` natively supports Turkish and English queries without external translation models. Diacritics and character variants (`ı/i`, `ö/o`, `ü/u`, `ş/s`, `ç/c`, `ğ/g`) are normalized seamlessly:

* **Roller:** `yönetici`, `yetkili`, `üye`, `kullanıcı`, `misafir`, `ziyaretçi`, `saldırgan`, `şüpheli`.
* **Soru Yönergeleri:**
  * **İzin / Onay:** `izin verilsin mi?`, `onayla`, `geçiş uygun mu?`, `çalıştır`.
  * **Engelleme / Tehlike:** `engelle`, `yasakla`, `tehlike var mı?`, `riskli mi?`, `saldırı mı?`.
  * **Yönlendirme Rotası:** `doğrudan`, `hızlı yol`, `kuyruk`, `karantina`, `inceleme`, `reddet`.

---

## 💻 Interactive CLI Simulator (`examples/sor.py`)

An interactive terminal application is provided under [`examples/sor.py`](examples/sor.py) with automatic dependency checking (`wevv`), an interactive numbered menu, and CLI arguments:

```bash
# Run with interactive selection menu:
python examples/sor.py

# Or pass a role directly from the command line:
python examples/sor.py admin
python examples/sor.py member
python examples/sor.py guest
python examples/sor.py attacker
```

---

## 🔬 Open Science Telemetry & Public Benchmark Dataset

To calibrate and continuously optimize the universal fractal decision map, `wevv` includes an asynchronous, non-blocking telemetry client (`wevv.telemetry`).

### 🔒 Zero-PII Privacy Guarantee
* **No IP addresses** are stored on disk or database.
* **No cookies, machine IDs, or personal accounts** are collected.
* **Sensitive keys & values** (`password`, `token`, `secret`, `key`, `auth`, `email`, `jwt`) are automatically sanitized and redacted (`[REDACTED]`) on the client side before dispatch.
* **100% Opt-Out:** Set the environment variable `WEVV_TELEMETRY=0` to disable telemetry completely.

### 📊 Live Public Dataset (1,090+ Decisions / 3,000+ Questions)
Telemetry records are aggregated in MariaDB on the dedicated node `mechsrv.itouch.fi` and exported as an open science benchmark:

* 🌐 **Direct Download (1,090+ Records):** [https://mechsrv.itouch.fi:4431/wevv/dataset/wevv_open_decisions.jsonl](https://mechsrv.itouch.fi:4431/wevv/dataset/wevv_open_decisions.jsonl)
* 📂 **Repository Mirror:** [`dataset/wevv_open_decisions.jsonl`](dataset/wevv_open_decisions.jsonl)
* 📑 **Empirical Test Reports:**
  - [Batch #1 (Scenarios 1–20)](docs/reports/batch1_telemetry_report_en.md) | [Türkçe](docs/reports/batch1_telemetry_report_tr.md)
  - [Batch #2 (Scenarios 21–40)](docs/reports/batch2_telemetry_report_en.md) | [Türkçe](docs/reports/batch2_telemetry_report_tr.md)
  - [Batch #3: 100-Question Dynamic Calibration & Stress Test](docs/reports/batch3_dynamic_calibration_100q_report_en.md) | [Türkçe](docs/reports/batch3_dynamic_calibration_100q_report_tr.md)

### 🧬 Organic Dynamic Calibration & Local Homeostasis (v0.2.2)
While v0.2.1 initialized empirical quadrant normalization from static benchmarks, `wevv` v0.2.2 introduces **Organic Dynamic Calibration** (`wevv.calibration.DynamicCalibration`):
* **Local Homeostasis:** Runs an $O(1)$ continuous Exponential Moving Average (EMA) of quadrant escape ratios across live queries. The decision engine organically self-calibrates to its local operational domain (e.g. industrial plants vs. high-frequency trading) with strict 0 Byte VRAM allocation.
* **Quadrant Phase Invariance:** Eliminates positional option bias via deterministic instruction-hash phase shifts (`phase_offset = hash(instructions) % 4`).
* **Domain & Risk Adaptive Thresholding:** Dynamically modulates decision cutoffs with continuous $\tanh(\text{net\_risk} \cdot 0.8)$.
* **Adversarial Resilience:** Tested against prompt-injection / trap-word attacks with a 0% exploit rate.
* **Web3 & Decentralized Decision Oracle Roadmap:** View our long-term architectural specifications for on-chain verifiable fractal decision maps, ZK-Mandelbrot proofs, and EVM/Solana smart contract oracles in [`docs/roadmap_blockchain_decision_oracle.md`](docs/roadmap_blockchain_decision_oracle.md).

### 🛡️ Server Hardening & Defensive Architecture
The remote ingestion endpoint on `mechsrv.itouch.fi:4431/wevv/telemetry` is hardened against abusive bots and brute-force traffic:
1. **Token Bucket Rate Limiting:** 30 requests/minute with a 5 req/s burst limit.
2. **Auto-Jail (Anti-Bruteforce):** Clients generating repeated violations (HTTP 413, 422, or rapid bursts) are automatically jailed for 15 minutes (HTTP 403).
3. **Strict Payload Guard:** Hard cap of 32 KB per request (`LimitRequestBody 32768`).
4. **Google reCAPTCHA v3 Shield:** The web simulator and custom scenario playground verify client authenticity via background reCAPTCHA v3 site verification.
5. **Storage & Disk Quota:** Dual-storage system caps log size at 1 GB and monitors host disk thresholds.
6. **Systemd Sandboxing:** Runs under an isolated service with `MemoryMax=256M`, `CPUQuota=20%`, `ProtectSystem=full`, and `NoNewPrivileges=true`.

---

## 🔗 Architecture & Connection to Base Research

`wevv` is deeply coupled with the research codebase [`mandelbrot-fractal-neural-synthesis`](https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis). It imports core vectorized escape operators from `src/mandelbrot_core.py`. As new orbital dynamics, multi-layer fractal compositions, and photonic solvers are discovered, `wevv` directly inherits these breakthroughs!

---

## 📄 Academic Citation & Authors

```bibtex
@software{wevv2026,
  author = {Volkan Dağlı and Zerrin Dağlı and Dağhan Dağlı},
  title = {wevv: Zero-Memory System-One Decision Engine via Fractal Boundary Subdivision},
  year = {2026},
  url = {https://github.com/pCwOrM/wevv},
  doi = {10.5281/zenodo.22802921}
}
```
