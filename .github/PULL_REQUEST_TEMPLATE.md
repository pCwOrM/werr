## 📋 Summary of Changes
<!-- Provide a clear, concise overview of what this pull request modifies, fixes, or adds. -->

## 🔬 Motivation & Operational Alignment
<!-- Explain why this change is necessary. Does it optimize decision latency, extend a domain gate, or fix a calibration edge case? -->

## 🧪 Verification & Empirical Testing
<!-- Describe how you verified your changes. Check all applicable items below: -->
- [ ] `python -m unittest discover tests -v` passes completely.
- [ ] Isolated WindTunnel WebMCP benchmark passes: `python -m unittest tests.test_windtunnel_webmcp_isolated -v`
- [ ] Isolated Jevenator 2 visual benchmark passes: `python -m unittest tests.test_jevenator2_isolated -v`
- [ ] Zero-memory guarantee verified (0 Bytes VRAM, 24-Byte coordinate seed preserved).
- [ ] Air-gapped isolation maintained (no mandatory external internet calls).

## 📦 Component Checklist
- [ ] `werr/` Core decision runtime (`engine.py`, `fractal.py`, `calibration.py`, `router.py`, `gates/`)
- [ ] `benchmarks/` Benchmark suites (`snake/`, `jevenator2/`)
- [ ] `tests/` Automated isolated unit tests
- [ ] `docs/` or `README.md` updated if API or CLI parameters changed

## 📜 Open Source Confirmation
- [ ] My contribution complies with the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines and [SECURITY.md](SECURITY.md).
- [ ] All code is original or licensed under compatible MIT open-source terms.
