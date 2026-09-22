# 🧠 Learning WERR: Machine-Native Zero-VRAM Reflex AI

Welcome to the learning guide for **WERR (Waves & Errors)**!

This guide is designed for computer science students, AI researchers, and systems engineers who want to understand how **mathematical dynamics** can replace gigabyte-scale neural network weights for low-latency, deterministic System-1 reflex decisions.

---

## 🧭 1. What Problem Does WERR Solve?

In classical AI architectures:
* Even simple reflexive decisions (e.g., collision avoidance, packet routing, prompt triage) often query large models (LLMs or deep neural nets).
* This introduces multi-megabyte / gigabyte memory requirements, GPU VRAM dependency, and non-deterministic latencies (often 50ms – 2,000ms).

**WERR demonstrates an alternative paradigm:**
* A **System-1 Intuitive Reflex Engine** executing in **sub-millisecond (<2ms)** timeframes on commodity CPU hardware or client-side JavaScript.
* **Zero Tensor Allocation:** Instead of storing millions of matrix weights, decisions are parameterized by a compact **24-byte coordinate tuple**:
  $$\Theta = (c_x, c_y, \text{zoom})$$
* **Deterministic & Air-Gapped:** Runs with zero network calls and 100% mathematical reproducibility.

---

## 🔬 2. Core Concepts You Will Learn

### A. Dual-Process Cognition in AI
Following Daniel Kahneman's cognitive framework:
1. **System 1 (Fast, Reflexive):** Pattern recognition, spatial intuition, and immediate reactions without deliberation.
2. **System 2 (Slow, Deliberative):** Large Language Models (LLMs) and deep chain-of-thought reasoners.

WERR provides the machine-native substrate for **System 1**.

### B. Escape Dynamics as Decision Boundaries
Traditional networks partition state space using learned hyperplane weights ($W \cdot x + b$).  
WERR maps normalized multi-dimensional state vectors into the complex plane $\mathbb{C}$ and evaluates iterative polynomial escape trajectories:
$$Z_{n+1} = Z_n^2 + C$$
The escape velocity, Lyapunov exponent, and boundary curvature function as rich, continuous decision manifolds without storing weight matrices.

---

## 🚀 3. Quick Hands-On Tutorial

### Step 1: Run the Interactive Browser Demo
You don't need any complex installation to see WERR in action:
1. Clone this repository:
   ```bash
   git clone https://github.com/pCwOrM/werr.git
   cd werr
   ```
2. Open `index.html` in any web browser (Chrome, Firefox, Safari, Edge).
3. Observe real-time reflex decision latencies measured in sub-millisecond precision directly on your device's CPU/Canvas!

### Step 2: Run the Python Engine
```bash
# Set up a clean environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1

# Install in development mode
pip install -e .

# Run the test suite to observe deterministic evaluations
python -m unittest discover tests -v
```

### Step 3: Run the Snake Reflex Benchmark
```bash
python benchmarks/snake/benchmark_snake.py --steps 300 --mode compare
```
Observe how the zero-memory reflex engine steers the agent with zero VRAM overhead.

---

## 🧪 4. Suggested Student Experiments & Exercises

If you are exploring WERR for a course project, thesis, or open-source contribution:

1. **Latency Profiling:** Measure execution jitter across 10,000 iterations using high-precision timers (`time.perf_counter_ns()` in Python or `performance.now()` in JS).
2. **Edge Hardware Porting:** Try porting the core escape loop to C, Rust, or WebAssembly (WASM).
3. **Domain Gate Creation:** Implement a custom decision gate (e.g., network packet priority routing or game AI agent reflexes) following the patterns in `werr/gates/`.
4. **Solve Open Good First Issues:** Check out our [open issues](https://github.com/pCwOrM/werr/issues) labeled `good first issue`!

---

## 📚 5. Academic Foundations & Citations

WERR is built upon open-science research preprints and fractal synthesis theory:
* **Zenodo DOI:** [10.5281/zenodo.22867037](https://doi.org/10.5281/zenodo.22867037)
* **Research Trilogy:** [10.5281/zenodo.22900465](https://doi.org/10.5281/zenodo.22900465) & [10.5281/zenodo.22867426](https://doi.org/10.5281/zenodo.22867426)
