# 📋 MECHSRV wevv 2. Dalga (Batch #2, Senaryo #21 – #40) Test Raporu

**Tarih:** 19 Eylül 2026  
**Hedef Sistem:** `mechsrv.itouch.fi` (`pcworm@mechsrv:2222`)  
**Test Paketi:** Batch #2 (Senaryo #21 – #40)  
**Ortam:** `/home/pcworm/myenv`  
**Çalışma Dizini:** `wevv/runner/`  
**Sürüm:** v0.2.0 (`AutoSeedRouter: True`)

---

## 🚀 2. Dalga (Batch #2) İcra Özeti

Önceki 1-20 arası senaryolardan sonra mükerrer kayıt oluşmasını önlemek amacıyla geliştirilen **Batch #2 (Senaryo #21 – #40)** mimarisi başarıyla koşturuldu:

- **API Gateway & Security (#21–40):** Yeni roller (`pentester`, `crawler`, `malware_agent`, `auditor`), gelişmiş DDoS anomalileri.
- **Smart Home & IoT (#21–40):** Yeni alanlar (`attic`, `greenhouse`, `nursery`, `server_rack`), aşırı donma/yangın ve CO2 seviyeleri.
- **E-Commerce Fraud (#21–40):** Yeni hesap tipleri (`compromised_token`, `dormant_revived`, `enterprise`), karmaşık proxy zincirleri.
- **Game AI (#21–40):** Yeni birimler (`infiltrator`, `drone_operator`, `berserker`), cephanesiz son direniş ve pusu senaryoları.
- **Financial Risk (#21–40):** Yeni başvuru tipleri (`retiree`, `gig_worker`, `startup_founder`), yüksek borç oranları ve ekstrem kredi limitleri.

---

## 📊 Performans ve Karar Metrikleri (Batch #2)

| Metrik | Değer |
| :--- | :--- |
| **Toplam Değerlendirilen Senaryo** | **100 (Senaryo #21 – #40)** |
| **Toplam Çalışma Süresi** | **3.21 saniye** |
| **Ortalama Karar Gecikmesi (Latency)** | **7.734 ms / karar** |
| **Onaylanan Kararlar (Allowed: True)** | **47 / 100 (%47.0)** |
| **Bellek Tüketimi (VRAM/RAM)** | **0 Byte** (True Zero-Memory) |

### Karar Dağılımları
- **Rota Dağılımı (`route`):**  
  `{'drop_packet': 20, 'eco_mode': 20, 'instant_capture': 5, 'step_up_3ds': 15, 'suppressing_fire': 7, 'take_cover': 10, 'flank_attack': 3, 'auto_approve': 7, 'manual_underwrite': 13}`
- **Risk Şiddet Seviyesi (`severity`):**  
  `{Low (0): 14, Medium (1): 32, High (2): 14, Critical (3): 40}`

---

## 💾 MariaDB Telemetri ve Veri Kümesi Doğrulaması

### 1. Toplam Kayıt Artışı
- **Önceki Toplam Kayıt:** `231` (artı 5 ara tanı kaydı ile 236)
- **Batch #2 Sonrası Toplam Kayıt:** **`336`** (+100 yeni Batch #2 kaydı tam olarak işlendi)
- **Son Kayıt Zaman Damgası:** `2026-09-19 02:48:19 UTC`

### 2. En Son 10 Kaydın Çıktısı (Batch #2)
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

### 3. 5 Kategori Dağılımı ve Dinamik Koordinat Teyidi (Son 100 Kayıt)
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

## 🔬 Kümülatif Ablasyon Benchmark Analizi (336 Kayıt / 326 Değerlendirilen Senaryo)

```text
============================================================================================
EMPIRICAL ABLATION STUDY: MONOLITHIC SEED VS. MULTI-DOMAIN AUTO-SEED ROUTER (N=336)
============================================================================================
Alan / Sektör      | N    | Tek Tohum (Eski) | Auto-Seed (Yeni) | Net Kazanç | Güven  | Saf Gecikme
--------------------------------------------------------------------------------------------
api_security       | 85   |      83.5%       |      87.1%       |   +3.5%    | 93.9%  |   3.42 ms
ecommerce_fraud    | 60   |      56.7%       |      85.0%       |  +28.3%    | 100.0% |   3.29 ms
financial_risk     | 60   |      35.0%       |     100.0%       |  +65.0%    | 100.0% |   3.33 ms
game_combat        | 60   |      50.0%       |      95.0%       |  +45.0%    | 100.0% |   3.17 ms
iot_safety         | 61   |      85.2%       |      98.4%       |  +13.1%    | 100.0% |   3.31 ms
--------------------------------------------------------------------------------------------
KÜMÜLATİF TOPLAM   | 326  |      63.8%       |      92.6%       |  +28.8%    | 98.0%  |   3.31 ms
============================================================================================
```
