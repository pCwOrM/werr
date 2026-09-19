# 📋 MECHSRV wevv 2nd Wave (Batch #2, Scenarios #21 – #40) Telemetry Report

**Date:** September 19, 2026  
**Target Host:** `mechsrv.itouch.fi` (`pcworm@mechsrv:2222`)  
**Test Suite:** Batch #2 (Scenarios #21 – #40)  
**Environment:** `/home/pcworm/myenv`  
**Working Directory:** `wevv/runner/`  
**Engine Version:** v0.2.0 (`AutoSeedRouter: True`)

---

## 🚀 Batch #2 Execution Summary

To prevent duplicate samples following the initial 1–20 baseline runs, the **Batch #2 (Scenarios #21 – #40)** architecture was deployed with extreme edge cases and stress distributions:

- **API Gateway & Security (#21–40):** Advanced roles (`pentester`, `crawler`, `malware_agent`, `auditor`), zero-day DDoS anomaly patterns.
- **Smart Home & IoT (#21–40):** Novel zones (`attic`, `greenhouse`, `nursery`, `server_rack`), freezing/combustion anomalies, toxic CO2 elevations.
- **E-Commerce Fraud (#21–40):** Advanced account tiers (`compromised_token`, `dormant_revived`, `enterprise`), multi-hop proxy chains.
- **Game AI (#21–40):** Specialized tactical units (`infiltrator`, `drone_operator`, `berserker`), zero-ammo last-stand defensive retreats.
- **Financial Risk (#21–40):** Heterogeneous applicant profiles (`retiree`, `gig_worker`, `startup_founder`), extreme debt-to-income leverage and outlier loan requests.

---

## 📊 Performance & Decision Metrics (Batch #2)

| Metric | Value |
| :--- | :--- |
| **Total Scenarios Evaluated** | **100 (Scenarios #21 – #40)** |
| **Total Execution Duration** | **3.21 seconds** |
| **Mean Inference Latency** | **7.734 ms / decision** |
| **Approval Rate (Allowed: True)** | **47 / 100 (47.0%)** |
| **Tensor Memory Footprint** | **0 Bytes (True Zero-Memory CPU Execution)** |

### Decision Distributions
- **Route Pipeline Distribution (`route`):**  
  `{'drop_packet': 20, 'eco_mode': 20, 'instant_capture': 5, 'step_up_3ds': 15, 'suppressing_fire': 7, 'take_cover': 10, 'flank_attack': 3, 'auto_approve': 7, 'manual_underwrite': 13}`
- **Threat / Default Severity Grading (`severity`):**  
  `{Low (0): 14, Medium (1): 32, High (2): 14, Critical (3): 40}`

---

## 💾 MariaDB Telemetry & Open Dataset Verification

### 1. Database Ingestion Volume
- **Pre-Test Total Ingested Records:** `231` (plus 5 diagnostic probes: 236)
- **Post-Batch #2 Total Ingested Records:** **`336`** (+100 Batch #2 records ingested without loss)
- **Latest Record Timestamp:** `2026-09-19 02:48:19 UTC`

### 2. Tail Inspection (Batch #2 Ingested Records)
```text
+-----+----------------+-----------+----------+-------------+------------------+---------------------+
| id  | category       | active_cx | active_cy| active_zoom | decision_time_ms | created_at          |
+-----+----------------+-----------+----------+-------------+------------------+---------------------+
| 359 | Financial Risk | -0.740500 | 0.070676 |       55.86 |             6.23 | 2026-09-19 02:48:19 |
| 358 | Financial Risk | -0.740500 | 0.070686 |       55.53 |             6.01 | 2026-09-19 02:48:19 |
| 357 | Financial Risk | -0.740500 | 0.070665 |       56.23 |             8.93 | 2026-09-19 02:48:19 |
| 356 | Financial Risk | -0.740500 | 0.070654 |       56.63 |             6.57 | 2026-09-19 02:48:19 |
| 355 | Financial Risk | -0.740500 | 0.070641 |       57.05 |             7.45 | 2026-09-19 02:48:19 |
| 354 | Financial Risk | -0.740501 | 0.068593 |       63.13 |             6.92 | 2026-09-19 02:48:19 |
| 353 | Financial Risk | -0.740501 | 0.068974 |       61.98 |            11.19 | 2026-09-19 02:48:19 |
| 352 | Financial Risk | -0.740503 | 0.068182 |       64.14 |             6.21 | 2026-09-19 02:48:19 |
| 351 | Financial Risk | -0.740503 | 0.067742 |       64.97 |             6.32 | 2026-09-19 02:48:19 |
| 350 | Financial Risk | -0.740514 | 0.067273 |       65.96 |             6.07 | 2026-09-19 02:48:19 |
+-----+----------------+-----------+----------+-------------+------------------+---------------------+
```

### 3. Category Breakdown & Dynamic Coordinate Hopping (Last 100 Records)
```text
+------------------------+-------+--------------------+-----------+-----------+-------------+
| category               | count | avg_decision_ms    | active_cx | active_cy | active_zoom |
+------------------------+-------+--------------------+-----------+-----------+-------------+
| Financial Risk         |    20 |               7.57 | -0.743020 |  0.061135 |        54.1 |
| Game AI & Combat       |    20 |               9.02 | -0.751381 |  0.120816 |        58.6 |
| E-Commerce Fraud       |    20 |               8.00 | -0.755587 |  0.079838 |        63.1 |
| Smart Home & IoT       |    20 |               6.33 | -0.747446 |  0.108974 |        78.9 |
| API Gateway & Security |    20 |               7.75 | -0.747002 |  0.131383 |       108.0 |
+------------------------+-------+--------------------+-----------+-----------+-------------+
```

---

## 🔬 Cumulative Empirical Ablation Study ($N = 336$, 326 Evaluated Scenarios)

Comprehensive out-of-sample evaluation comparing the monolithic baseline seed against the Multi-Domain Auto-Seed Router over all 336 empirical telemetry records:

```text
============================================================================================
EMPIRICAL ABLATION STUDY: MONOLITHIC SEED VS. MULTI-DOMAIN AUTO-SEED ROUTER (N=336)
============================================================================================
Domain             | N    | Baseline Monolithic Acc | Auto-Seed Router Acc | Net Gain | Conf   | Pure Latency
--------------------------------------------------------------------------------------------
api_security       | 85   |          83.5%          |        87.1%         |  +3.5%   | 93.9%  |   3.42 ms
ecommerce_fraud    | 60   |          56.7%          |        85.0%         | +28.3%   | 100.0% |   3.29 ms
financial_risk     | 60   |          35.0%          |       100.0%         | +65.0%   | 100.0% |   3.33 ms
game_combat        | 60   |          50.0%          |        95.0%         | +45.0%   | 100.0% |   3.17 ms
iot_safety         | 61   |          85.2%          |        98.4%         | +13.1%   | 100.0% |   3.31 ms
--------------------------------------------------------------------------------------------
OVERALL AGGREGATE  | 326  |          63.8%          |        92.6%         | +28.8%   | 98.0%  |   3.31 ms
============================================================================================
```
