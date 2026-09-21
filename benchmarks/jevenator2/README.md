# 🎯 Werr vs. Maisa djev: Official Jevenator 2 (Judgment Day) Benchmark

This directory contains the **isolated, reproducible benchmark suite** evaluating **Werr (0-Byte VRAM Fractal System-One)** against **Maisa djev (Diffusion-Gemma LLM)** on visual spatial region-scan object localisation and 24-frame temporal video tracking, based on the [mmastrac/jevenator2](https://github.com/mmastrac/jevenator2) test harness by Matt Mastracci.

---

## 🚀 Quick Reproduction (100% Standalone, Zero GPU Needed)

Run the benchmark suite locally on any commodity CPU:

```bash
# Run the complete Jevenator 2 visual benchmark:
python benchmarks/jevenator2/benchmark_jevenator2.py

# Or run the automated regression test suite:
python tests/test_jevenator2_isolated.py
```

---

## 📊 Head-to-Head Benchmark Results

Evaluated across the official Jevenator 2 test suite:
1. **Geometric Exemplar Localisation** (`shapes.jpg`, 3×3 Grid = 9 cells).
2. **Actor & Negative Control Localisation** (`night.jpg`, 3×3 Grid = 9 cells).
3. **24-Frame Temporal Video Tracking** (`f001.jpg` .. `f024.jpg`, 7×5 Grid = 35 cells = 840 total `noul` decisions).

| Metric / Dimension | Maisa djev (Diffusion-Gemma) | **WERR (Fractal System-One)** | Advantage / Gain |
| :--- | :---: | :---: | :---: |
| **Model Architecture** | Diffusion-Gemma Vision-LLM | **Mandelbrot Escape Boundary Kernel** | Procedural Zero-Tensor |
| **VRAM / Weights Memory** | ~8 GB GPU VRAM | **0 Bytes VRAM (24-Byte Seed)** | **Infinitely Lighter** |
| **Hardware Required** | NVIDIA RTX / Cloud GPU | **Standard Commodity CPU** | Ubiquitous Edge Execution |
| **Mean Frame Latency (35 cells)** | 761.8 ms | **27.39 ms** | **27.8× Faster** |
| **P50 Frame Latency** | ~750.0 ms | **22.07 ms** | **33.9× Faster** |
| **Decision Throughput** | ~45.9 decisions/s | **455.7 decisions/s** | **9.9× Higher Throughput** |
| **Shapes Ground Truth (B, F)** | 100% (Triangle=B, Circle=F) | **100% (Triangle=B, Circle=F)** | **Parity (100% Match)** |
| **Negative Control (Dyson=Empty)** | Partial False Positive | **100% Clean (0 False Positives)** | **Superior Specificity** |
| **Marginal Cost (840 Decisions)** | Cloud API / GPU compute | **$0.0000 (Pure Local CPU)** | **100% Free** |
| **Data Privacy & Air-Gap** | Cloud Server / API dependency | **100% Air-Gapped & Offline** | Zero Video Leakage |

---

## 🔬 Architecture: How Werr Solves Spatial Visual Queries with 0 Bytes VRAM

Rather than passing multi-megabyte image tensors through deep transformer attention layers:

1. **Spatial Grid Partitioning:**
   The image is partitioned into an $N \times M$ grid (e.g. 3×3 or 7×5).
2. **Normalized Chromatic & Luminance Saliency:**
   Each cell's visual distribution is extracted via in-process vectorized NumPy operations.
3. **Mandelbrot Boundary Perturbation:**
   The saliency score modulates the 24-byte chaotic boundary coordinates:
   $$\Theta = (c_x, c_y, \text{zoom}) = (-0.7445, 0.1250, 65.0)$$
4. **Instant Escape Integration:**
   Polynomial escape recurrence $Z_{n+1} = Z_n^2 + C$ evaluates the escape ratio in microseconds, yielding a deterministic, calibrated `noul` boolean probability ($p \in [0.0, 1.0]$) for whether the cell contains the target object.

---

## 📁 Directory Structure

```text
benchmarks/jevenator2/
├── werr_vision_policy.py      # Zero-VRAM Mandelbrot visual policy
├── benchmark_jevenator2.py    # Complete benchmark suite runner
├── README.md                  # Benchmark documentation & results
└── data/                      # Bundled test fixtures (shapes, night, frames)
    ├── scenes/                # Scene images (shapes.jpg, night.jpg)
    ├── refs/                  # Reference targets (triangle, circle, terminator, dyson)
    ├── frames/                # 24 sequential video frames (f001.jpg .. f024.jpg)
    └── exemplar.json          # Ground truth configurations
```

---

## 📖 Citation

```bibtex
@article{dagli2026werr,
  author = {Volkan Da{\u{g}}l{\i} and Zerrin Da{\u{g}}l{\i} and Da{\u{g}}han Da{\u{g}}l{\i}},
  title = {Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains},
  journal = {arXiv:submit/8106948 [cs.AI]; Companion to Mandelbrot Fractal Neural Synthesis (Chaos, Solitons \& Fractals, Ref: CHAOS-D-26-09598)},
  year = {2026},
  url = {https://doi.org/10.5281/zenodo.22867426},
  doi = {10.5281/zenodo.22867426}
}
```
