# 🌊 wevv: Zero-Memory Fractal System-One Decision Engine

> **Motto:** *"When the Wave hits Error (e), we Subdivide (vv)."*  
> *"Jev decisions come from 4B-parameter tensors; `wevv` decisions come from infinite geometric waves, Euler thresholds, and recursive subdivision."*

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

## 🔗 Architecture & Connection to Base Research

`wevv` is deeply coupled with the research codebase [`mandelbrot-fractal-neural-synthesis`](https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis). It imports core vectorized escape operators from `src/mandelbrot_core.py`. As new orbital dynamics, multi-layer fractal compositions, and photonic solvers are discovered, `wevv` directly inherits these breakthroughs!
