# Contributing to Mandelbrot Fractal Neural Synthesis

Thank you for your interest in contributing to the **Mandelbrot Fractal Neural Synthesis** open science research initiative! We welcome contributions ranging from bug fixes, documentation clarity, and new interactive demonstrations to algorithmic optimizations and benchmark replications.

---

## 🏛️ Open Science & Academic Integrity

This project serves as the official open-source codebase and empirical replication companion for peer-reviewed research in non-linear dynamical systems and procedural neural architectures.

When proposing algorithmic changes or benchmark extensions:
- **Reproducibility is Paramount:** Any modified or added algorithm must be reproducible across deterministic seeds.
- **Asymptotic Footprint:** Ensure procedural weight derivation preserves the $O(1)$ constant coordinate footprint without introducing persistent multi-tensor arrays unless explicitly designated as an external comparative baseline.

---

## 🛠️ Development Setup

### 1. Fork & Clone
```bash
git clone https://github.com/YOUR-USERNAME/mandelbrot-fractal-neural-synthesis.git
cd mandelbrot-fractal-neural-synthesis
git checkout -b feature/your-feature-name
```

### 2. Python Environment
We recommend Python 3.10 or 3.11 with a clean virtual environment:
```bash
python -m venv .venv

# On Linux/macOS:
source .venv/bin/activate

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Install minimal research dependencies:
pip install -r requirements.txt
pip install pytest flake8
```

### 3. Run Validation Tests & Benchmarks
Ensure all core tests and logic gate synthesizers pass before committing:
```bash
# Run automated test suite:
pytest tests/

# Verify discrete logic gate convergence:
python -m src.fractal_neuron

# Verify composite non-linear XOR network:
python -m src.xor_composite_network
```

---

## 🌿 Contribution Workflow

1. **Check Existing Issues:** Before embarking on a major feature, check the [Issues tab](https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis/issues) or open a new issue to discuss your proposal.
2. **Follow Code Standards:**
   - Adhere to PEP 8 standards.
   - Maintain clean, vectorized NumPy implementations rather than unvectorized nested Python loops where possible.
   - Keep docstrings informative with mathematical notation where appropriate.
3. **Commit Messages:**
   Use clear, conventional commit prefixes:
   - `feat:` for new capabilities or visualizer features
   - `fix:` for bug fixes
   - `perf:` for computational speed-ups
   - `docs:` for documentation updates
   - `test:` for adding or improving test coverage
   - `refactor:` for code restructuring without behavioral changes
4. **Submit a Pull Request:**
   - Push your branch to your fork.
   - Open a PR targeting `master` on `pCwOrM/mandelbrot-fractal-neural-synthesis`.
   - Fill out the PR template checklist completely.

---

## 🔬 Empirical Replication Reports

If you replicate the benchmarks (e.g., Two-Moons, Two-Spirals, or Pareto resolution trade-off) on different hardware platforms (ARM Cortex, Apple Silicon, RISC-V, or optical/photonic simulators), please submit a **Replication Report** issue with your hardware specifications, execution latency, and accuracy metrics. We enthusiastically highlight third-party hardware validations!

---

## 📖 Citation

If your contribution builds upon this research or incorporates parts of the codebase into your own published work, please cite the permanent Zenodo archive:

```bibtex
@article{dagli2026mandelbrot,
  title={Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries},
  author={Da{\u{g}}l{\u{i}}, Volkan and Da{\u{g}}l{\u{i}}, Zerrin and Da{\u{g}}l{\u{i}}, Da{\u{g}}han},
  year={2026},
  doi={10.5281/zenodo.22774934},
  url={https://doi.org/10.5281/zenodo.22774934}
}
```
