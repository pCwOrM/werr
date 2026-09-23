---
license: bsl-1.1
task_categories:
- text-classification
- zero-shot-classification
- feature-extraction
language:
- en
- tr
tags:
- edge-ai
- zero-vram
- fractal-neural-synthesis
- reflex-ai
- system-1
- mandelbrot
- decision-making
size_categories:
- 1K<n<10K
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: timestamp
    dtype: string
  - name: received_at
    dtype: string
  - name: source
    dtype: string
  - name: version
    dtype: string
  - name: seed
    struct:
    - name: cx
      dtype: float64
    - name: cy
      dtype: float64
    - name: zoom
      dtype: float64
  - name: state_summary
    dtype: string
  - name: questions
    list:
    - name: name
      dtype: string
    - name: type
      dtype: string
    - name: instruction
      dtype: string
    - name: decision
      dtype: string
    - name: probability
      dtype: float64
    - name: confidence
      dtype: float64
    - name: probabilities
      dtype: string
  - name: latency_ms
    dtype: float64
  splits:
  - name: train
    num_bytes: 1462486
    num_examples: 1205
---

# WERR Open Decisions Benchmark Dataset

Official benchmark dataset accompanying the research paper:  
**"Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains"**  
[arXiv:2609.25498](https://arxiv.org/abs/2609.25498)

## 📌 Dataset Summary

`werr_open_decisions` contains **1,205 verified decision trajectories** and over **3,200 evaluation questions** evaluated using the **WERR (Waves & Errors)** machine-native zero-VRAM reflex engine and the production [answerr.me](https://answerr.me) platform.

Unlike conventional neural networks storing millions of static tensor parameters, each decision is procedurally synthesized from a **24-byte Mandelbrot coordinate seed** $\Theta = (c_x, c_y, \text{zoom})$ evaluating non-linear escape dynamics along the chaotic boundary of the Mandelbrot set $\mathbb{M}$.

### Decision Primitives:
1. **`noul` (Boolean / Binary):** Instant binary triage (e.g. permit / reject, anomaly detection, panic trip).
2. **`choice` (Categorical):** Multi-class routing across discrete destination microservices.
3. **`score` (Ordinal / Continuous):** Multi-tier risk severity scoring (0–3 scale).

## 🚀 Usage

```python
from datasets import load_dataset

# Load directly from Hugging Face Hub
dataset = load_dataset("pCwOrM/werr_open_decisions")

# Inspect the first decision
print(dataset["train"][0])
```

## 📊 Dataset Structure

Each JSONL record represents an operational decision event:
- `id`: Monotonic event identifier.
- `seed`: 24-byte coordinate seed `(cx, cy, zoom)` on the complex plane $\mathbb{C}$.
- `state_summary`: Operational state features (user role, error rates, frequency, telemetry).
- `questions`: Array of strongly-typed decision probes (`noul`, `choice`, `score`) with computed confidence and probability distributions.
- `latency_ms`: Measured end-to-end evaluation latency on CPU hardware (sub-2ms reflex execution).

## 🏛️ Citation

```bibtex
@article{dagli2026universal,
  title={Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains},
  author={Da{\u{g}}l{\i}, Volkan and Da{\u{g}}l{\i}, Zerrin and Da{\u{g}}l{\i}, Da{\u{g}}han},
  journal={arXiv preprint arXiv:2609.25498},
  year={2026},
  url={https://arxiv.org/abs/2609.25498}
}
```

## 📜 License
Licensed under the **Business Source License 1.1 (BSL 1.1)**. Converts to Apache 2.0 on 2030-01-01. Free for academic, educational, and research benchmarking.
Corporate Licensor: **ITouch Systems** (ITouch Bilişim Sistemleri Ltd. Şti., Çukurova Teknokent). Contact: `ask@answerr.me` / `info@itouch.com.tr`.
