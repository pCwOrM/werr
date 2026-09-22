# Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries

[![Live Web Portal](https://img.shields.io/badge/Live%20Portal-GitHub%20Pages-10b981.svg?logo=github)](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/)
[![Interactive Labs](https://img.shields.io/badge/Interactive%20Labs-100%25%20Client--Side-818cf8.svg)](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/#labsTitle)
[![Paper 2: OED Zenodo DOI](https://img.shields.io/badge/Paper%202%20DOI-10.5281%2Fzenodo.22896856-024dad.svg)](https://doi.org/10.5281/zenodo.22896856)
[![Patent Pending](https://img.shields.io/badge/Patent%20Pending-TR%202026%2F016285-red.svg)](https://epats.turkpatent.gov.tr)
[![Paper 1: Zenodo Concept DOI](https://img.shields.io/badge/Paper%201%20DOI-10.5281%2Fzenodo.22774934-024dad.svg)](https://doi.org/10.5281/zenodo.22774934)
[![Companion Paper: WERR](https://img.shields.io/badge/Companion%20Paper-WERR-8b5cf6.svg)](https://github.com/pCwOrM/werr)
[![The Gauntlet Benchmarks](https://img.shields.io/badge/The%20Gauntlet-Zero--VRAM%20Supremacy-brightgreen.svg)](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/benchmarks.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> 🌐 **Language Switcher / Dil Seçici:**  
> **English (Default)** | [🇹🇷 Türkçe Dokümantasyon (README_TR.md)](README_TR.md)

---

## 🌟 Interactive Live Laboratories & Online Showcase

Explore the procedural fractal neural synthesis paradigm directly inside your web browser. All laboratories are **100% client-side, zero-dependency, and fully offline-capable**:

| Platform / Document | Type | Target Audience | Direct Live Link |
| :--- | :--- | :--- | :--- |
| 🏛️ **Paper 2: Orbital Error Dynamics (Preprint)** | Academic Paper & Patent | Global / AI & Physics | [**Zenodo: 10.5281/zenodo.22896856**](https://doi.org/10.5281/zenodo.22896856) &bull; [**PDF (7 Pages)**](docs/Orbital_Error_Dynamics_Preprint.pdf) &bull; **Patent Pending: TR 2026/016285** |
| ⚔️ **The Zero-VRAM Gauntlet** | Master Benchmark Wall | Researchers, Engineers & Challengers | [**Launch The Gauntlet (Benchmarks)**](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/benchmarks.html) |
| 🌐 **Official Web Portal** | Showcase | Global / Academic | [**Launch Web Portal**](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/) |
| 🚀 **Citizen & Public Experience Lab** | Live Simulation | General Public & Students | [**Launch Public Lab**](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/demos/interactive_lab.html) |
| 🔬 **128×128 4-Quadrant Research Lab** | Mathematical | Researchers & Engineers | [**Launch Research Lab**](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/demos/quadrant_visualizer.html) |
| 🐍 **Interactive Snake AI & 1v1 Arena** | Real-Time Reflex & Autopilot | Gamers, Engineers & Mobile | [**Launch Snake Arena**](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/demos/snake.html) |
| 🗣️ **Halka Sunum ve Teorik Rehber** | Dual-Layer Guide | Presenters & Educators | [**Open Presentation Guide (HTML)**](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/docs/Halka_Sunum_ve_Teorik_Rehber.html) |
| 🏛️ **Paper 1: Fractal Neural Synthesis** | Journal Under Review | Open Science | [**Zenodo: 10.5281/zenodo.22867037**](https://zenodo.org/records/22867037) &bull; *Chaos, Solitons & Fractals (Elsevier)* |
| ⚡ **Companion Paper: WERR (Edge Triage)** | Applied Edge NLP & Vision | Global / Applied AI | [**Zenodo: 10.5281/zenodo.22867426**](https://doi.org/10.5281/zenodo.22867426) &bull; [**GitHub: pCwOrM/werr**](https://github.com/pCwOrM/werr) |
| 🧠 **Live Dual-Cognition AI (answerr)** | Production Platform & API | Developers & End Users | [**answerr.me**](https://answerr.me) &bull; [**GitHub: pCwOrM/answerr**](https://github.com/pCwOrM/answerr) |

---

## 👥 Authors & Affiliations

* **Volkan Dağlı** *(Corresponding Author)*  
  Anadolu University, Eskişehir, Turkey & ITouch Systems, Mersin, Turkey &bull; ORCID: [0009-0000-1587-8703](https://orcid.org/0009-0000-1587-8703) &bull; GitHub: [`@pCwOrM`](https://github.com/pCwOrM)

* **Zerrin Dağlı**  
  Mersin University, Mersin, Turkey &bull; ORCID: [0000-0001-9490-6425](https://orcid.org/0000-0001-9490-6425)

* **Dağhan Dağlı**  
  Toros Science College, Mersin, Turkey &bull; ORCID: [0009-0003-2492-8313](https://orcid.org/0009-0003-2492-8313) &bull; GitHub: [`@Lexovian`](https://github.com/Lexovian)

*Correspondence:* Volkan Dağlı ([GitHub Repository](https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis) / [Zenodo Concept](https://doi.org/10.5281/zenodo.22774934)).

---

## 📌 Executive Summary

Modern deep artificial neural networks store millions or billions of parameters as unconstrained floating-point scalars across dense tensor matrices. While remarkably capable, this paradigm incurs immense storage requirements, memory bandwidth bottlenecks (the **"memory wall"**), and severe thermal/energy dissipation.

In biological systems, genetic encoding does not store neural connectomes point-by-point. The human genome contains approximately 750 MB of genetic code, yet orchestrates the development of an estimated $10^{11}$ neurons and $10^{14}$ synaptic junctions via self-similar recursive developmental rules.

This research proposes and empirically demonstrates an alternative paradigm: **deriving synaptic weights and threshold biases procedurally from the non-linear visual morphology of the Mandelbrot fractal set ($\mathcal{M}$)**.

By specifying a 3-parameter coordinate tuple $\Theta = (c_x, c_y, \text{zoom})$ in the complex plane, a $128 \times 128$ pixel patch is sampled via the quadratic escape recurrence $z_{n+1} = z_n^2 + c$. Through **4-Quadrant Partitioning**, the non-escaping "dark area" (convergent pixel ratio) of four sub-quadrants is mapped directly to synaptic weights ($w_1, w_2, w_3$) and neuron bias ($b$).

```text
Complex Plane Coordinate: Θ = (cx, cy, log10 z) [24 Bytes]
                     │
                     ▼
       ┌───────────────────────────┐
       │  z_{n+1} = z_n^2 + c      │ ──► 128×128 Escape Patch
       └───────────────────────────┘
                     │
                     ▼
        [4-Quadrant Partitioning]
                     │
                     ▼
Synaptic Weights (w1, w2, w3) + Bias (b)  ──► Non-Linear Decision Contours
(ZERO persistent tensor storage in RAM/VRAM)   (100% Linear Gates, 100% XOR)
```

---

## 🔬 Key Scientific Milestones (Preprint Scope)

1. **$128 \times 128$ Pareto Resolution Standard:** Matches the convergence precision of $256 \times 256$ within $\pm 0.08\%$ while evaluating **15 times faster** ($\approx 15.6$ ms), completely filtering the quantization noise of lower resolutions ($32 \times 32$).
2. **100% Linear Boolean Classification:** All canonical linearly separable boolean gates (AND, OR, NAND, NOR) converged to **100% classification accuracy** across independent random seeds ($48 \pm 12$ generations with zero convergence failures).
3. **100% Non-Linear XOR Resolution:** The historically intractable XOR problem was solved with **100% empirical accuracy** using a two-layer composite fractal network, generating a smooth non-linear 2D decision contour.
4. **Constant $O(1)$ Storage Scaling vs. Linear $O(W)$:** Conventional neural networks store explicit weight arrays that grow linearly with network depth and width ($O(W)$). In contrast, procedural fractal synthesis maintains a constant **24-byte metadata footprint ($O(1)$)** regardless of synthesized layer width.
5. **The Systems Compute-Memory Trade-off:** We establish an explicit systems trade-off: persistent storage is completely eliminated ($O(1)$) at the expense of procedural generation latency ($O(N^2 \cdot M_{\max})$ FLOPs). This makes the architecture exceptionally advantageous for **memory-constrained edge microcontrollers**, **steganographic/obfuscated AI**, and **analog optical/photonic co-processors**.
6. **The Escape Horizon Principle:** Formulates how biological motor learning (e.g., mastering hammering in 300 trials instead of 1000 via sharp error boundary feedback) mathematically mirrors the topological boundary $\partial \mathcal{M}$ (the Julia-Fatou bifurcation locus) dividing homeostatic convergence from chaotic divergence.

---

## 🏛️ Paper 1: Fractal Neural Synthesis (Journal Extension)

> **Publication Status:** Under peer review in *Chaos, Solitons & Fractals* (Elsevier). Author preprint and reproducible replication package permanently archived at Zenodo ([10.5281/zenodo.22774934](https://doi.org/10.5281/zenodo.22774934) &bull; [v3.0 Record](https://zenodo.org/records/22867037)).

The journal manuscript expands the foundational paradigm to continuous topological manifolds and rigorous comparative baselines:
* **Continuous Topological Manifolds:** Generalization to non-convex distributions (Two-Moons and Two-Spirals) using Quadtree decomposition and analytical recurrence offsets.
* **Comparative Baseline Evaluation:** Comprehensive benchmarking against standard MLPs trained via Adam/Backpropagation across $K=10$ repeated trials.
* **Attractor Basin Dynamics:** Detailed mathematical analysis of macroscopic functional attractor basins overcoming local Lyapunov micro-sensitivity ($\Delta c \sim 10^{-7}$).

---

## 🌌 Flagship Paper 2: Orbital Error Dynamics (OED) — Zero-Storage AI with Adaptive Immune Gating

[![Paper 2 Zenodo DOI](https://img.shields.io/badge/Paper%202%20DOI-10.5281%2Fzenodo.22896856-024dad.svg)](https://doi.org/10.5281/zenodo.22896856)
[![Çatı DOI](https://img.shields.io/badge/Concept%20DOI-10.5281%2Fzenodo.22896855-blue.svg)](https://doi.org/10.5281/zenodo.22896855)
[![Patent Pending](https://img.shields.io/badge/Patent%20Pending-TR%202026%2F016285-red.svg)](https://epats.turkpatent.gov.tr)
[![Preprint PDF](https://img.shields.io/badge/Preprint%20PDF-7%20Pages%20(Open%20Access)-10b981.svg)](docs/Orbital_Error_Dynamics_Preprint.pdf)

> **Official Research Preprint & National Patent Application:**  
> **Title:** *Orbital Error Dynamics: Self-Organized Criticality, Ephemeral Parameter Resonance, and Non-Linear Biological Ontologies in Zero-Storage Neural Synthesis*  
> **Authors:** Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı  
> **Permanent Zenodo Record:** [https://doi.org/10.5281/zenodo.22896856](https://doi.org/10.5281/zenodo.22896856) &bull; **Çatı DOI:** [10.5281/zenodo.22896855](https://doi.org/10.5281/zenodo.22896855)  
> **Official Patent Pending:** Turkish Patent and Trademark Office (TÜRKPATENT), Application No: **`2026/016285`**, Priority Date: **September 22, 2026**.

<p align="center">
  <img src="figures/fig5_dual_brain_cybernetics.png" alt="OED Dual-Brain Cybernetics" width="85%" />
</p>

### Core Scientific Innovations
1. **The Bent Sine Wave Hypothesis:** Proves that while unperturbed linear waves represent static equilibrium death ($\frac{dx}{dt} = 0$) and harmonic waves represent conservative repetition, living intelligence emerges when waves curl inward through environmental drag toward the main cardioid cusp ($c = 1/4$).
2. **Observer Horizon Geometry in Parameter Space:** Identifies the critical boundary shoulder loci $\mathbf{X}_{upper} = (0.25, +0.18)$ and $\mathbf{X}_{lower} = (0.25, -0.18)$ surveying forward quantum potential fields ($\text{Re}(c) > 0.25$) while anchored to somatic dissipation axes ($\text{Im}(c) \to 0$), with radial escape fluxes $\mathbf{v}_{escape}$ acting as expressive boundary signals.
3. **Biomimetic Perturbed Jump Operator ($\Omega_{\mathrm{tunneling}}$):** Translates mammalian fertilization zinc sparks (Duncan et al., 2016) into an empirical heavy-tailed Cauchy jump operator ($\Omega \sim \text{Cauchy}(0, \gamma)$) escaping non-convex saddle traps during gradient stagnation (Jin et al., 2017).
4. **Dual-Brain Cybernetics & CD4+ Immune Gating:** Couples slow $O(1) = 24$-byte central parameter planning ($\Theta$) with high-frequency enteric/visceral sensory streams shielded by adaptive CD4+ regulatory T-cell tolerance masks ($M_{CD4}$), attenuating adversarial noise spikes.
5. **Complex 4-Quadrant Genetic Base Decomposition:** Maps the 4-nucleotide genetic basis ($A, T, C, G$) across the quadrants of $\mathbb{C}$, synthesizing multi-dimensional weight vectors $W = [w_1, w_2, w_3, b]^T$ from scalar coordinates without matrix storage.
6. **Hardware Equivalence with Analog Optical Co-Processors:** Formulates sub-nanosecond optical forward propagation using Spatial Light Modulators (SLM), 4f Fourier lens systems, and dark-basin CMOS photodetectors at the speed of light.

### Rigorous Empirical Multi-Seed Benchmark (80/20 Train/Test Split)
| Architecture / Model | Clean Test Accuracy (Mean $\pm$ Std) | Adversarial / Toxin Attack | Persistent Memory Footprint | Optimization Scheme |
| :--- | :---: | :---: | :---: | :--- |
| **Standard Logistic Regression (GLM)** | **84.33% $\pm$ 4.55%** | 82.67% $\pm$ 4.78% | 32 Bytes (4 Floats, $O(W)$) | Direct gradient descent on $W$ |
| **OED (Zero-Storage Synthesis)** | 77.33% $\pm$ 5.01% | 56.67% $\pm$ 6.24% (Unshielded) | **24 Bytes ($O(1)$ constant)** | Boundary parameter surfing + Zinc Spark |
| **OED + CD4+ Immune Gating Shield** | 77.33% $\pm$ 5.01% | **66.67% $\pm$ 8.23% (Protected)** | **24 Bytes ($O(1)$ constant)** | Adaptive threshold attenuation |

### Reproduce OED Experiments
```bash
# Run the 5-seed empirical benchmark with 80/20 train/test split
python experiments/simulate_oed_rigorous.py

# Regenerate all 7 publication figures (300 DPI)
python scripts/generate_clean_scientific_figures.py
```

---

## 🌐 Companion Applied Ecosystem: WERR (Reflex Engine) & answerr (Dual-Cognition Platform)

Building upon the foundational zero-storage fractal parameter synthesis introduced in this project, our research team has engineered an applied companion architecture for high-throughput edge triage and dual-cognition software execution:

> **Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains**  
> *Authors:* Volkan Dağlı, Dr. Zerrin Dağlı, Dağhan Dağlı  
> *Zenodo Permanent Concept DOI:* [![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22867425-024dad.svg)](https://doi.org/10.5281/zenodo.22867425) &bull; *arXiv Submission:* `arXiv:submit/8106948`  
> *Engine Repository:* [github.com/pCwOrM/werr](https://github.com/pCwOrM/werr) &bull; *Live Decision Lab:* [pcworm.github.io/werr](https://pcworm.github.io/werr/)  
> *Platform & Workspace:* [github.com/pCwOrM/answerr](https://github.com/pCwOrM/answerr) &bull; *Production Portal:* [answerr.me](https://answerr.me)

### Key Synergies & Cross-Domain Translation
1. **From Geometric Boundaries to NLP Reflex Triage:** While this foundational work derives synaptic weights from $128 \times 128$ Mandelbrot escape patches for decision boundaries, [werr](https://github.com/pCwOrM/werr) translates fractal boundary dynamics into ultra-fast, zero-tensor semantic triage (System-1 reflex arcs).
2. **Dual-Cognition Workspace Integration:** [answerr](https://github.com/pCwOrM/answerr) pairs microsecond `werr` reflexes with cloud LLM (Google Gemini) deliberation, providing a production glassmorphic workspace and REST API at `api.answerr.me:4431`.
3. **Empirical World-Record Benchmarks:** The mathematical zero-storage fractal derivation demonstrated in this project directly powers `werr`'s verified international achievements:
   * **WindTunnel WebMCP:** 100% success rate (49/49 tasks solved) across 8 production web applications with 3.35 ms latency, 0 Bytes VRAM, and $0.0000 cost ([nekuda-ai/WindTunnel#25](https://github.com/nekuda-ai/WindTunnel/issues/25)).
   * **JevBench v1.2:** Global Rank #1 World Record (Overall Score: 81.65, 100/100 speed, 100/100 cost, 2.76 ms latency) ([fstandhartinger/jevbench#10](https://github.com/fstandhartinger/jevbench/issues/10)).
   * **Continuous Reflex Loop (Snake AI):** 273–302 moves/second real-time closed-loop reflex throughput (3.7× faster than Laya-MLX on Apple M3 Max) with zero VRAM ([mizorewww/laya-mlx#3](https://github.com/mizorewww/laya-mlx/issues/3)).
   * **Computer Vision Tracking (Jevenator 2):** 27.8× faster than Maisa djev with 0 false positives across 840 sequential video tracking decisions ([mmastrac/jevenator2#1](https://github.com/mmastrac/jevenator2/issues/1)).
4. **Dual-Endpoint API Serving:** [answerr](https://github.com/pCwOrM/answerr) exposes production reflex serving via `https://api.answerr.me:4431`, including the dedicated JevBench TypeSafe wire format endpoint (`POST /v1/systemone`) and the `/v1/decide` reflex gateway.
5. **Deterministic Edge AI Resilience:** The ecosystem completely eliminates persistent multi-gigabyte weight matrices, enabling sub-millisecond execution directly on microcontrollers, edge routers, and resource-constrained nodes without cloud API reliance.
6. **Reproducibility & Open Science:** Complete replication packages, dynamic calibration filters, and open telemetry benchmarks are openly accessible across our Zenodo archives.

---

## 📂 Repository Architecture

```text
mandelbrot-fractal-neural-synthesis/
│
├── README.md                           # Primary English Documentation (This File)
├── README_TR.md                        # Kapsamlı Türkçe Dokümantasyon
├── index.html                          # GitHub Pages Official Web Portal
├── LICENSE                             # MIT Open Source License
├── requirements.txt                    # Minimal Python Dependencies
├── .zenodo.json                        # Automated Zenodo Open Science Metadata
├── .gitignore                          # Clean Version Control Filter
│
├── src/                                # Core Simulation & Research Algorithms
│   ├── mandelbrot_core.py              # 128x128 sampling & dark area integration
│   ├── fractal_neuron.py               # Single-neuron logic gate solver
│   ├── xor_composite_network.py        # 2-layer composite non-linear network
│   ├── gate_optimizer.py               # Evolutionary coordinate search engine
│   └── benchmark_resolutions.py        # 32x32 to 256x256 Pareto trade-off analysis
│
├── demos/                              # Interactive Web Labs (100% Client-Side & Standalone)
│   ├── interactive_lab.html            # Scenario interface (Smart Door, Safe, Light, Alarm)
│   ├── quadrant_visualizer.html        # Technical 128x128 4-quadrant mathematical research lab
│   ├── snake.html                      # Interactive Snake Lab, 1v1 AI Arena & Mobile Touch D-pad
│   ├── terminal_snake.py               # Standalone Terminal Snake reflex visualizer
│   └── terminal_snake_arena.py         # Dual-agent competitive arena harness
│
├── docs/                               # Outreach, Technical Reports & Paper Sources
│   ├── Mandelbrot_Fractal_Neural_Synthesis_IEEE_Paper_EN.html # Live Paper HTML
│   ├── Mandelbrot_Fractal_Neural_Synthesis_IEEE_Paper_EN.pdf  # Publication PDF (2.11 MB)
│   ├── Halka_Sunum_ve_Teorik_Rehber.html                      # Dual-layer speaker & theory guide
│   ├── Mandelbrot_Akademik_Teknik_Raporu.html                 # Comprehensive technical monograph
│   └── ...                                                    # Markdown sources and guides
│
└── figures/                            # Publication Figures & Benchmarks
    ├── quadrant_weights_128.png        # 4-Quadrant partitioning schematic
    ├── resolution_comparison_128.png   # Resolution Pareto trade-off curves
    ├── gate_solutions_128.png          # Linear decision planes (AND, OR, NAND, NOR)
    ├── xor_complete_network_128.png    # Non-linear XOR 2-layer composite network
    └── zoom_weight_curve.png           # Continuous parameter modulation via zoom
```

---

## 🚀 Quick Start & Empirical Replication

```bash
# 1. Clone the repository
git clone https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis.git
cd mandelbrot-fractal-neural-synthesis

# 2. Install minimal dependencies
pip install -r requirements.txt

# 3. Verify discrete logic gate convergence (100% accuracy)
python -m src.fractal_neuron

# 4. Verify composite non-linear XOR network (100% accuracy)
python -m src.xor_composite_network

# 5. Run resolution benchmark analysis
python -m src.benchmark_resolutions

# 6. Launch interactive lab locally in your default browser (zero server required!)
# On Windows:
start demos/interactive_lab.html
# On macOS:
open demos/interactive_lab.html
# On Linux:
xdg-open demos/interactive_lab.html
```

---

## 📖 Citations

If you utilize this research, procedural weight generation methodology, or interactive visualizers, please cite our official preprints:

```bibtex
@article{dagli2026orbital,
  title={Orbital Error Dynamics: Self-Organized Criticality, Ephemeral Parameter Resonance, and Non-Linear Biological Ontologies in Zero-Storage Neural Synthesis},
  author={Da{\u{g}}l{\i}, Volkan and Da{\u{g}}l{\i}, Zerrin and Da{\u{g}}l{\i}, Da{\u{g}}han},
  journal={Zenodo Open Science Archive},
  year={2026},
  doi={10.5281/zenodo.22896856},
  url={https://doi.org/10.5281/zenodo.22896856},
  note={Patent Pending: Turkish Patent and Trademark Office TR 2026/016285}
}

@article{dagli2026mandelbrot,
  title={Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries},
  author={Da{\u{g}}l{\i}, Volkan and Da{\u{g}}l{\i}, Zerrin and Da{\u{g}}l{\i}, Da{\u{g}}han},
  journal={Zenodo Open Science Archive},
  year={2026},
  doi={10.5281/zenodo.22774934},
  url={https://doi.org/10.5281/zenodo.22774934}
}
```

---

## 📜 License & Open Science
This project is open-source under the [MIT License](LICENSE).  
The manuscript and technical documentation are distributed under [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
