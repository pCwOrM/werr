# Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.pending-blue.svg)](https://zenodo.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Status: Preprint](https://img.shields.io/badge/Publication-Zenodo%20%2F%20arXiv%20Preprint-green.svg)](#)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Demos](https://img.shields.io/badge/Interactive%20Labs-100%25%20Standalone-purple.svg)](./demos/)

> 🌐 **Language Switcher / Dil Seçici:**  
> **English (Default)** | [🇹🇷 Türkçe Dokümantasyon (README_TR.md)](README_TR.md)

---

## 👥 Authors & Affiliations

* **Volkan Dağlı** *(Corresponding Author)*  
  ITouch Systems, Turkey &bull; Zenodo: [`@itouch`](https://zenodo.org/)

* **Zerrin Dağlı**  
  Mersin University, Mersin, Turkey &bull; ORCID: [0000-0001-9490-6465](https://orcid.org/0000-0001-9490-6465) &bull; Zenodo: [`@zdagli`](https://zenodo.org/)

* **Dağhan Dağlı**  
  Toros Science College, Turkey &bull; Zenodo: [`@Lexovian`](https://zenodo.org/)

*Correspondence & inquiries:* Inquiries and collaboration requests should be directed via the official research repository or Zenodo.

---

## 📌 Executive Summary

Modern deep neural networks store billions or trillions of parameters as unconstrained floating-point scalars across large static tensor matrices. For instance, a 70B parameter LLM demands $\sim 140$ GB of high-speed VRAM simply to hold weights in memory, causing severe memory bandwidth bottlenecks ("the memory wall") and massive power consumption.

This research proposes and empirically demonstrates an alternative paradigm: **deriving synaptic weights and activation thresholds dynamically from the visual morphology of the Mandelbrot fractal set ($\mathcal{M}$)**. 

By querying a 3-parameter coordinate tuple $\Theta = (c_x, c_y, \text{zoom})$ in the complex plane, a $128 \times 128$ pixel window is sampled via the classic iterative quadratic escape equation ($z_{n+1} = z_n^2 + c$). Through **4-Quadrant Partitioning**, four functional parameters ($w_1, w_2, w_3, \text{bias}$) are synthesized on demand from the non-escaping "dark area" (black pixel ratio).

### Key Scientific Milestones:
1. **$128 \times 128$ Resolution Standard:** Matches the convergence precision of $256 \times 256$ within $\pm 0.08\%$ while executing **15 times faster** ($\approx 15.6$ ms).
2. **100% Linear Gate Classification:** All canonical linear logic gates (AND, OR, NAND, NOR) converged to 100% classification accuracy.
3. **100% Non-Linear XOR Resolution:** The historically intractable XOR problem was solved with 100% accuracy using a two-layer composite fractal network, generating a continuous non-linear 2D decision contour.
4. **24-Byte Zero-Weight Footprint:** Eliminates persistent weight tensor storage entirely. A functional decision unit is defined by only **24 bytes** (three Float64 coordinates), representing a **$>99.99999998\%$ memory reduction** over conventional weight matrices.
5. **The Escape Horizon & Error Boundary Principle:** Formulates how biological motor learning (e.g., mastering hammering in 300 trials instead of 1000 via sharp error boundary feedback) mathematically mirrors the topological boundary $\partial \mathcal{M}$ dividing homeostatic convergence from chaotic divergence.

---

## 📊 Benchmark: Conventional LLM vs. Fractal Synthesis

| Dimension | Conventional Deep Learning (LLM) | Mandelbrot Fractal Neural Synthesis (Ours) |
| :--- | :--- | :--- |
| **Parameter Storage Model** | Static Weight Tensor Matrix (RAM/VRAM) | **Procedural On-Demand Synthesis from Geometry** |
| **Storage per Decision Cell** | 12 - 64 Bytes (Weights & Bias Tensors) | **24 Bytes Total $(c_x, c_y, \text{zoom})$** |
| **Persistent Weight Matrix** | Billions of Float16/Float32 values | **0 Bytes (No matrix written to persistent storage)** |
| **70B Parameter Equivalent** | $\sim 140$ GB VRAM (Memory Wall Bottleneck) | **Compact Coordinate Sequence** |
| **Memory Reduction** | Baseline (0%) | **>99.99999998% Storage Savings** |
| **Hardware Horizon** | Memory-bound GPUs (Von Neumann bottleneck) | **Photonic / Optical Co-processors ($< 1$ ns, zero electrical resistance)** |

---

## 📂 Repository Architecture

```text
mandelbrot-fractal-neural-synthesis/
│
├── README.md                           # Primary English Documentation
├── README_TR.md                        # Kapsamlı Türkçe Dokümantasyon
├── LICENSE                             # MIT Open Source License
├── requirements.txt                    # Minimal Python Dependencies
├── .zenodo.json                        # Zenodo Automated Metadata Standard
├── .gitignore                          # Clean Version Control Filter
│
├── src/                                # Core Simulation & Research Algorithms
│   ├── mandelbrot_core.py              # 128x128 sampling & dark area integration
│   ├── fractal_neuron.py               # Single-neuron logic gate solver
│   ├── xor_composite_network.py        # 2-layer composite non-linear network
│   ├── gate_optimizer.py               # Evolutionary random-walk coordinate search
│   └── benchmark_resolutions.py        # 32x32 to 256x256 Pareto trade-off analysis
│
├── demos/                              # Interactive Web Labs (100% Offline & Standalone)
│   ├── interactive_lab.html            # Public outreach scenario interface (Doors, Safes, Lights, Alarms)
│   └── quadrant_visualizer.html        # Technical 128x128 4-quadrant mathematical research widget
│
├── zenodo/                             # Official Zenodo Open Science Publication Deposit Package
│   ├── .zenodo.json                    # Deposit configuration
│   ├── zenodo_deposit_guide.md         # 5-minute Zenodo submission & instant DOI guide
│   └── Mandelbrot_Fractal_Neural_Synthesis_Preprint.pdf # Camera-ready Preprint (Bilingual Abstract)
│
├── arxiv/                              # LaTeX Source Package for arXiv / Overleaf
│   ├── main.tex                        # IEEE format paper source
│   ├── references.bib                  # BibTeX references
│   ├── figures/                        # High-resolution figures
│   └── Mandelbrot_Fractal_Paper_arXiv_Bundle.zip # Drag-and-drop submission bundle
│
├── docs/                               # Outreach & Academic Monograph Documents
│   ├── Halka_Anlatim_Rehberi.html      # Public presentation guide
│   ├── Halka_Anlatim_Rehberi.pdf       # Printable A4 public presentation PDF
│   ├── halka_anlatim_rehberi.md        # Public guide markdown source
│   ├── Mandelbrot_Akademik_Teknik_Raporu.html # Full academic technical report
│   └── Mandelbrot_Akademik_Teknik_Raporu.pdf  # Printable A4 academic report PDF
│
└── figures/                            # Publication Figures
    ├── quadrant_weights_128.png        # 4-Quadrant partitioning schematic
    ├── resolution_comparison_128.png   # 32x32 to 256x256 benchmark curves
    ├── gate_solutions_128.png          # Decision planes for OR, AND, NAND, NOR
    ├── xor_complete_network_128.png    # Composite 2-layer non-linear network
    ├── zoom_weight_curve.png           # Continuous weight modulation via zoom
    └── mandelbrot_patches.png          # Morphological landscape patches
```

---

## 🎮 Interactive Visualizers (Zero Dependencies)

The repository provides two self-contained, standalone web applications that require **no server, no installation, and no internet connection**:

1. **Public Outreach Lab (`demos/interactive_lab.html`):**
   * Real-world decision scenarios: 🚪 Smart Door (OR), 🏦 Bank Vault (AND), 💡 Staircase Switch (XOR), 🚨 Fire Alarm (NAND).
   * Live biological neuron rendering with active axon firing.
   * Light/Dark mode switcher with persistent preferences.
   * One-click `.TXT` 24-byte memory log export.
2. **Technical 4-Quadrant Research Widget (`demos/quadrant_visualizer.html`):**
   * Real-time $128 \times 128$ Mandelbrot exploration with dynamic zoom.
   * Live Quadrant readout ($Q_1 	o w_1, Q_2 	o w_2, Q_3 	o w_3, Q_4 	o b$).
   * Dynamic boolean truth table verification ($\hat{y} = \sigma(w_1 x_1 + w_2 x_2 + b)$).

---

## 🚀 Reproduction & Quick Start

```bash
# Clone the repository
git clone https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis.git
cd mandelbrot-fractal-neural-synthesis

# Install minimal requirements
pip install -r requirements.txt

# Run gate verification
python src/fractal_neuron.py

# Run non-linear XOR solution
python src/xor_composite_network.py

# Open interactive lab directly in your browser
start demos/interactive_lab.html
```

---

## 📖 Citation

If you use this research or replicate our findings, please cite:

```bibtex
@article{dagli2026fractal,
  title={Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries},
  author={Da{\u{g}}l{\i}, Volkan and Da{\u{g}}l{\i}, Zerrin and Da{\u{g}}l{\i}, Da{\u{g}}han},
  journal={Zenodo / arXiv Preprint},
  year={2026},
  doi={10.5281/zenodo.pending},
  url={https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis}
}
```

---

## 📜 License
This project is open-source under the [MIT License](LICENSE).
