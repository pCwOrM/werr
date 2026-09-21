# Security Policy

## Supported Versions

The following table outlines the lifecycle and security support status of releases for the **WERR** project:

| Version | Supported          | Security Maintenance Status |
| ------- | ------------------ | --------------------------- |
| 0.3.x   | :white_check_mark: | Current Active Release      |
| 0.2.x   | :x:                | Deprecated (superseded)     |
| < 0.2   | :x:                | Archived                    |

---

## Reporting a Vulnerability

We take the security, deterministic safety guarantees, and zero-leakage air-gapped isolation of the WERR runtime very seriously.

If you discover a security vulnerability, prompt bypass, side-channel leakage, or denial-of-service issue in the engine or server runtime, please **do not open a public GitHub issue**. Instead, follow responsible disclosure:

1. **GitHub Private Security Advisory (Preferred):**
   Navigate to the [Security Advisories tab](https://github.com/pCwOrM/werr/security/advisories) on GitHub and click **"Report a vulnerability"**.

2. **Direct Researcher Contact:**
   Contact the project maintainers privately:
   - **pCwOrM / Volkan Dağlı**
   - Via GitHub: [`@pCwOrM`](https://github.com/pCwOrM)
   - Email: `contact@itouchsystems.com`

### What to Include in Your Report
To help us triage and resolve the issue quickly, please include:
- A clear description of the vulnerability and its operational impact.
- Minimal proof of concept (PoC) code or sample JSON request triggering the condition.
- Affected component (e.g., `werr.engine`, `werr.server`, `werr.router`, or edge gates).
- Proposed fix or mitigation if known.

### Response Timeline
- **Acknowledgment:** Within 48 hours.
- **Triage & Assessment:** Within 5 business days.
- **Remediation & Release:** Critical security patches will be prioritized with an advisory update and version bump.

---

## Zero Data Leakage & Air-Gapped Operation Guarantee

The WERR runtime is designed for strict physical and zero-trust air-gapped environments:
- **Zero Cloud Dependence:** All decision synthesis occurs 100% in-process via local polynomial escape loops.
- **Opt-out Telemetry:** Telemetry is strictly metadata-only (no state payload, no prompts, no PII) and can be completely silenced via `--no-telemetry` CLI flag or `WERR_TELEMETRY=0` environment variable.
- **Zero Weight Memory:** No neural weight tensors exist in memory, preventing memory-scraping model extraction attacks.
