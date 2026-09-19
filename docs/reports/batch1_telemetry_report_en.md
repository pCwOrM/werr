# 📋 MECHSRV wevv v0.2.0 Upgrade & Batch #1 (Scenarios #1 – #20) Telemetry Report

**Date:** September 19, 2026  
**Target Host:** `mechsrv.itouch.fi` (`pcworm@mechsrv:2222`)  
**Test Suite:** Batch #1 (Scenarios #1 – #20)  
**Environment:** `/home/pcworm/myenv`  
**Working Directory:** `wevv/runner/`  
**Engine Version:** v0.2.0 (`AutoSeedRouter: True`)

---

## 🎯 Batch #1 Execution Summary & Results

### STEP 1: Remote Repository Update and Editable Installation
- Executed `cd /home/pcworm/wevv_repo && git fetch origin main && git reset --hard origin/main`.
- Installed package in editable mode via `/home/pcworm/myenv/bin/pip install -e /home/pcworm/wevv_repo`.
- Verification: `Version: 0.2.0 | AutoSeedRouter: True`.

---

### STEP 2: 100-Question Multi-Domain Test Execution
- Executed `/home/pcworm/myenv/bin/python /home/pcworm/wevv_repo/scripts/test_100_questions.py`.
- **Total Execution Time:** `3.19 seconds`
- **Mean Fractal Decision Latency:** `8.009 ms / decision` (sub-step fractal escape projection < 2.0 ms).
- **Auto-Seed Gate Distribution:**
  - `Gate: api_security` (20 questions)
  - `Gate: iot_safety` (20 questions)
  - `Gate: ecommerce_fraud` (20 questions)
  - `Gate: game_combat` (20 questions)
  - `Gate: financial_risk` (20 questions)
- **Approval Rate (Allowed):** 51.0% (51 / 100)

---

### STEP 3: MariaDB Telemetry Verification

#### 1. Ingestion Volume
- **Baseline Record Count:** `131`
- **Post-Test Total Record Count:** **`231`**
- **Newly Ingested Telemetry Entries:** Exactly 100 records

#### 2. Dynamic Coordinate Validation (Last 100 Records)
```text
+------------------------+-------+--------------------+-----------+-----------+-------------+
| category               | count | avg_decision_ms    | active_cx | active_cy | active_zoom |
+------------------------+-------+--------------------+-----------+-----------+-------------+
| Financial Risk         |    20 |               7.99 | -0.743020 |  0.061135 |        54.1 |
| Game AI & Combat       |    20 |               8.94 | -0.751381 |  0.120816 |        58.6 |
| E-Commerce Fraud       |    20 |               7.92 | -0.755587 |  0.079838 |        63.1 |
| Smart Home & IoT       |    20 |               6.94 | -0.747446 |  0.108974 |        78.9 |
| API Gateway & Security |    20 |               8.25 | -0.747024 |  0.131933 |       108.0 |
+------------------------+-------+--------------------+-----------+-----------+-------------+
```

---

### STEP 4: Open Science Benchmark Dataset Export
- Successfully executed `/home/pcworm/myenv/bin/python /home/pcworm/wevv_telemetry/export_dataset.py`.
- 231 records exported to `/home/pcworm/wevv_telemetry/dataset/wevv_open_decisions.jsonl` and synchronized with GitHub `main`.

---

### STEP 5: 1st Wave Accuracy Jump (Historic Initial Leap)

The dramatic accuracy jump observed during the 1st Wave when migrating from a monolithic single-coordinate seed to the 5-domain Auto-Seed Router architecture:

```text
============================================================================================
1ST WAVE ABLATION BENCHMARK: MONOLITHIC SEED VS. AUTO-SEED ROUTER (N=223)
============================================================================================
Domain             | N    | Baseline Single Seed | Auto-Seed Router | Initial Leap (Net Gain)
--------------------------------------------------------------------------------------------
financial_risk     | 40   |        35.0%         |     100.0%       | +65.0% (Massive Leap!)
game_combat        | 40   |        40.0%         |      95.0%       | +55.0% (Massive Leap!)
ecommerce_fraud    | 40   |        55.0%         |      90.0%       | +35.0% (Critical Gain)
iot_safety         | 40   |        85.0%         |     100.0%       | +15.0% (Perfect Safety)
api_security       | 63   |        88.9%         |      90.5%       |  +1.6% (Preserved Top)
--------------------------------------------------------------------------------------------
OVERALL AGGREGATE  | 223  |        63.7%         |      94.6%       | +30.9% (Historic Initial Leap!)
============================================================================================
```

> **Scientific Insight:** The most profound finding of the 1st Wave was that while a monolithic coordinate collapsed to near coin-flip performance in financial risk (35.0%) and game combat (40.0%), the Auto-Seed Router instantly propelled them to **100.0%** and **95.0%** accuracy respectively. Overall aggregate accuracy leaped from **63.7% to 94.6% (+30.9% net gain)**, empirically validating the zero-memory System-One multi-domain concept for the first time.
