# Contributing to WERR

Thank you for your interest in contributing to **WERR (Waves & Errors)** — the open-source zero-memory, machine-native System-One fractal decision engine!

We welcome contributions ranging from edge optimizers, hardware porting (C/Rust/EVM), and new domain gates to empirical benchmark replications and documentation enhancements.

---

## 🏛️ Open Science & Architectural Guarantees

WERR operates under strict foundational contracts. Any proposed pull request must adhere to these non-negotiables:

1. **Zero-Memory Tensor Contract:** Core decision loops must NOT allocate persistent multi-megabyte matrix weights or tensor parameter arrays. Coordinates are parameterized by a 24-byte tuple $\Theta = (c_x, c_y, \text{zoom})$.
2. **Sub-Millisecond Execution:** Edge reflexes and domain gates must execute in low-millisecond/sub-millisecond timeframes on commodity CPU architectures.
3. **Deterministic Reproducibility:** Given identical state inputs and coordinate seeds, decisions must evaluate identically across all platforms and operating systems.
4. **Strict Air-Gap Capability:** The core engine must function with zero network access and zero external cloud dependencies.

---

## 🛠️ Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/pCwOrM/werr.git
cd werr
git checkout -b feature/your-feature-name
```

### 2. Set Up Python Environment
We recommend Python 3.10, 3.11, or 3.12:
```bash
python -m venv .venv

# On Linux/macOS:
source .venv/bin/activate

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Install package in editable mode with dependencies:
pip install -e .
pip install flake8 pytest Pillow
```

### 3. Run Automated Tests & Benchmarks
Ensure all isolated tests pass cleanly before submitting your changes:
```bash
# Run unit test suite:
python -m unittest discover tests -v

# Run isolated WindTunnel WebMCP benchmark:
python -m unittest tests.test_windtunnel_webmcp_isolated -v

# Run isolated Jevenator 2 visual localization benchmark:
python -m unittest tests.test_jevenator2_isolated -v

# Run Snake reflex gameplay benchmark:
python benchmarks/snake/benchmark_snake.py --steps 300 --mode compare
```

---

## 🌿 Contribution Workflow

1. **Issues First:** For non-trivial architectural changes or new gate proposals, please open an issue or check existing issues to discuss the implementation strategy.
2. **Code Standards:**
   - Adhere to PEP 8 standards.
   - Vectorize numerical loops with NumPy.
   - Keep external dependencies minimal (standard library + NumPy preferred).
3. **Commit Standards:**
   We follow conventional commit format:
   - `feat:` New decision gate, primitive, or runtime feature
   - `fix:` Bug fix or calibration adjustment
   - `perf:` Throughput acceleration or latency reduction
   - `docs:` Documentation and benchmark updates
   - `test:` New test cases or benchmark scenarios
4. **Pull Requests:** Ensure PRs fill out the [PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) completely.
