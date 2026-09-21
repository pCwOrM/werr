# Security Policy

## Supported Versions

The following table outlines the lifecycle and security support status of releases for the **Mandelbrot Fractal Neural Synthesis** project:

| Version | Supported          | Security Maintenance Status |
| ------- | ------------------ | --------------------------- |
| 3.0.x   | :white_check_mark: | Full Active Support         |
| 2.0.x   | :x:                | Deprecated (superseded)     |
| < 2.0   | :x:                | Archived                    |

---

## Reporting a Vulnerability

We take the security and integrity of our open-source codebase, client-side web laboratories, and empirical reproduction packages very seriously.

If you discover a security vulnerability, execution vulnerability, or supply-chain issue, please **do not open a public GitHub issue**. Instead, follow responsible disclosure:

1. **GitHub Private Security Advisory (Preferred):**
   Navigate to the [Security Advisories tab](https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis/security/advisories) on GitHub and click **"Report a vulnerability"**.

2. **Direct Researcher Contact:**
   Contact the corresponding author privately:
   - **Volkan Dağlı**
   - Via GitHub: [`@pCwOrM`](https://github.com/pCwOrM)

### What to Include in Your Report
To help us triage and resolve the issue quickly, please include:
- A detailed description of the vulnerability and its potential impact.
- Exact steps to reproduce, minimal proof of concept (PoC), or demonstration script.
- Affected components (e.g., core Python engine, client-side HTML/JS laboratory, or automation pipeline).
- Any proposed mitigations or patch suggestions if available.

### Response Timeline
- **Acknowledgment:** Within 48 hours of initial receipt.
- **Triage & Assessment:** Within 5 business days.
- **Resolution & Patch Deployment:** Critical patches will be released alongside an advisory credit and changelog notice.

---

## Client-Side Security & Data Privacy Guarantee
The interactive laboratories (`interactive_lab.html` and `quadrant_visualizer.html`) are designed to be **100% client-side, zero-dependency, and offline-capable**:
- No telemetry, analytics, cookies, or remote server calls are made during fractal weight derivation or simulation.
- Your local parameters and simulation sessions never leave your browser sandbox.
