<p align="center">
  <img src="assets/answerr_werr_twin_ecosystem.svg" alt="answerr ve werr İkiz Ekosistem Görseli" width="100%">
</p>

<p align="center">
  <img src="assets/werr_logo_core.svg" alt="werr çekirdek amblemi" width="130">
</p>

# ⚡ WERR: Sıfır-Bellekli Fraktal Sistem-1 Karar Motoru (Dalgalar ve Hatalar)

[![Lisans: BSL 1.1](https://img.shields.io/badge/Lisans-BSL%201.1-red.svg)](./LICENSE)
[![Makale DOI: 10.5281/zenodo.22867426](https://img.shields.io/badge/Makale%20DOI-10.5281%2Fzenodo.22867426-38bdf8.svg)](https://doi.org/10.5281/zenodo.22867426)
[![Temel Teori DOI](https://img.shields.io/badge/Temel%20Teori%20DOI-10.5281%2Fzenodo.22774934-024dad.svg)](https://doi.org/10.5281/zenodo.22774934)
[![Ön Baskı Durumu](https://img.shields.io/badge/%C3%96n%20Bask%C4%B1-De%C4%9Ferlendirme%20A%C5%9Famas%C4%B1nda-blue.svg)](https://doi.org/10.5281/zenodo.22867426)
[![Canlı Demo: GitHub Pages](https://img.shields.io/badge/Canl%C4%B1%20Demo-GitHub%20Pages-38bdf8.svg)](https://pcworm.github.io/werr/)
[![GitHub Education: Community Exchange](https://img.shields.io/badge/GitHub%20Education-Community%20Exchange-2ea44f?logo=github&logoColor=white)](https://education.github.com/globalcampus/exchange)
[![Kardeş Platform: answerr](https://img.shields.io/badge/answerr-Canl%C4%B1%20Platform-38bdf8.svg)](https://answerr.me)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CI Workflow](https://github.com/pCwOrM/werr/actions/workflows/ci.yml/badge.svg)](https://github.com/pCwOrM/werr/actions/workflows/ci.yml)
[![Canlı Kıyaslama Arenası](https://img.shields.io/badge/Canlı%20Kıyaslama-WebMCP%20%7C%20JevBench%20%7C%20Gym%20%7C%20Arena%20%7C%20Tau--Bench-blueviolet.svg)](https://pcworm.github.io/werr/#benchmark-arena)
[![The Gauntlet Kıyaslama Duvarı](https://img.shields.io/badge/The%20Gauntlet-Resmi%20K%C4%B1yaslama%20Dizini-brightgreen.svg)](./benchmarks/)
[![JevBench Çift Standart](https://img.shields.io/badge/JevBench%20v1.2%20%2F%20v1.3-81.36%20%7C%2076.90-brightgreen.svg)](docs/BENCHMARK_INTEGRITY_REPORT.md)
[![WindTunnel WebMCP](https://img.shields.io/badge/WindTunnel%20WebMCP-%25100%20(49%2F49)-brightgreen.svg)](https://github.com/nekuda-ai/WindTunnel/issues/25)
[![Tau-Bench Araç Çağrımı](https://img.shields.io/badge/Tau--Bench-%25100%20Ara%C3%A7%20Sadakati-brightgreen.svg)](https://github.com/sierra-research/tau-bench/issues/95)
[![Yılan AI Refleksi](https://img.shields.io/badge/Yılan%20AI%20Refleksi-411.9%20hamle%2Fsn-brightgreen.svg)](./benchmarks/snake/)
[![Jevenator 2 Görsel](https://img.shields.io/badge/Jevenator%202-38.0x%20Hızlı-brightgreen.svg)](./benchmarks/jevenator2/)
[![Kriptografik Denetim](https://img.shields.io/badge/Denetim-SHA--256%20Mühürlü-blueviolet.svg)](benchmarks/sealed/SEAL_MANIFEST.json)

> **Motto:** *"Dalga Hata ile Karşılaştığında, Yineleriz (werr)."*  
> *"Refleks nerede? Karar Werr!"*  
> *"Klasik kararlar milyarlarca parametreli ağır tensörlerden çıkar; `werr` kararları sonsuz geometrik dalgalardan, Euler eşiklerinden ve özyinelemeli çeyrek bölünmelerinden doğar."*

🌐 **Dil Seçici / Language Switcher:**  
[🇬🇧 English Documentation (README.md)](README.md) | **Türkçe (README_TR.md)**

🌐 **Etkileşimli Web Laboratuvarı:** [GitHub Pages Üzerindeki Canlı Simülatörü Deneyin](https://pcworm.github.io/werr/) *(Türkçe & İngilizce, Açık & Koyu Tema).*  
⚡ **Çevrimiçi Canlı Kıyaslama Arenası:** [WebMCP, JevBench, Gymnasium, Arena.ai Körleme Testi ve Tau-Bench'i Tarayıcıda Canlı Koşun](https://pcworm.github.io/werr/#benchmark-arena) *(%100 İstemci Taraflı, 0 VRAM, Anlık CPU İcrası).*  
⚔️ **The Zero-VRAM Gauntlet (Merkezi Kıyaslama Dizini):** [Eksiksiz Kıyaslama Dizinini ve Meydan Okumayı Keşfedin](benchmarks/) *(Yılan, Jevenator 2, WindTunnel & JevBench Markdown Monografları).*  
📜 **Açık Kaynak Benchmark Bütünlüğü Raporu:** [JevBench v1.2 / v1.3 metrik değişimleri ve çift-standart doğrulaması (81.36 / 76.90) teknik denetim raporu](docs/BENCHMARK_INTEGRITY_REPORT.md).  
⚙️ **Motor Optimizasyon Raporu:** [Etiket tokenizasyonu, kelime sınırları ve kalibrasyon ilkeleri teknik raporu](docs/OPTIMIZATION_REPORT_TR.md).  
🛡️ **Resmi Mühürlü PDF Denetim Raporu:** [Yayın Kalitesinde Denetim Raporu PDF İndir](docs/werr_official_benchmarks_report.pdf) │ [HTML Etkileşimli Rapor](docs/werr_official_benchmarks_report.html) │ [Kriptografik SHA-256 Manifestosu](benchmarks/sealed/SEAL_MANIFEST.json).

`werr`, modern yazılımlar ve uç cihazlar için geliştirilmiş, makine-yerel (machine-native) bir **Sistem-1 refleks karar motorudur**. Devasa dil modellerini çalıştırmak veya VRAM'de gigabaytlarca ağırlık tensörü tutmak yerine `werr`, deterministik Mandelbrot fraktal kaçış dinamiği ($\partial \mathcal{M}$) ve 4-çeyrek bölünmesi üzerinden anlık, tipli kararları (`noul`, `choice`, `score`) dinamik olarak sentezler.

---

## 💡 4 Boyutlu WERR Felsefesi

* **1. Dinamik Sentez (`W`aves & `Err`ors):** Sürekli karmaşık polinom yörüngelerinin Euler diverjans eşiğiyle ($|Z_n| > 2$) çarpışması. Dalga hatayla buluştuğunda, yineleriz (**WERR**).
* **2. Mekânsal Sorgulama (*"Werr is the point?"*):** İngilizce *"Where"* (Nerede) kelimesiyle eşsesli olarak, operasyonel durum triage'ı Mandelbrot kümesinin sonsuz dalları üzerindeki rezonant 24-baytlık koordinat tohumunu bulmak olarak modellenir.
* **3. Eylemsel Emir (Türkçe *"Ver!"*):** Biyolojik omurilik refleksleri tereddüt etmeden eyleme geçer. Türkçedeki emir kipiyle: *"Karar werr!"*, *"Yanıt werr!"*, *"İzin werr!"*, *"Tepki werr!"*. Beyinsel müzakereye girmeden $< 1$~ms içinde karar üretir.
* **4. İkili Bilişsel Ekosistem Sinerjisi:** `werr`, canlı olarak [answerr.me](https://answerr.me) üzerinde çalışan **A.N.S.W.E.R.R.** (*Adaptive Non-tensor Signal Wave & Error Reflex Resonator*) platformunun sıfır-tensör matematiksel omurgasını oluşturur.

---

## 📊 Karşılaştırma: Geleneksel Yöntemler vs. werr

| Boyut | TypeSafe AI (Jev / Bulut) | Yerel SLM (4B-8B Tensör) | **werr (Fraktal Sistem-1)** |
| :--- | :--- | :--- | :--- |
| **Temel** | Tescilli LLM API | Qwen / Gemma (4B) | **Mandelbrot Sınırı ($\partial \mathcal{M}$)** |
| **Ağırlık Tensör Belleği** | Çoklu-GB (Bulut) | ~8 GB VRAM | **0 Bayt (Sıfır Tensör Belleği!)** |
| **Tohum Ayak İzi** | Bulut Uç Noktası | Gigabaytlarca Checkpoint | **24 Bayt $(c_x, c_y, \text{zoom})$** |
| **Tipik Gecikme** | ~100 ms (Ağ Gecikmesi) | ~15–30 ms (GPU) | **< 1.0 ms (Saf Yerel CPU)** |
| **Donanım Gereksinimi** | Kesintisiz İnternet | CUDA Destekli Güçlü GPU | **Herhangi bir standart CPU / Mikrokontrolcü** |
| **Lisans & Otonomi** | Ücretli API ($/token) | Açık Ağırlıklar | **%100 Özgür & Açık Kaynak (MIT)** |

---

## ⚡ Üç Temel Karar Primitifi

`werr`, gereksiz metin veya sohbet üretmeden üç temel soru tipine doğrudan cevap verir:

1. **`noul` (Mantıksal Olasılık - Boolean):**
   * İkili olasılık $p \in [0.0, 1.0]$, karar `True/False` ve güven skoru üretir.
   * $\partial \mathcal{M}$ hiper-yüzey eşiklemesinden türetilir.
2. **`choice` (Ayrık Kategori Seçimi):**
   * Kullanıcı tanımlı seçenekler arasından en uygun rotayı belirler.
   * 4-Çeyrek ($Q_1, Q_2, Q_3, Q_4$) veya Quadtree enerji ayrımından türetilir.
3. **`score` (Sürekli / Sıralı Derecelendirme):**
   * Tanımlı bir ölçek boyunca (örn. 0 ile 3 arası) sürekli seviye veya risk hesaplar.
   * Karanlık alan integrali ($D$) ve kaçış hızından elde edilir.

---

## 📦 Kurulum

```bash
# Doğrudan GitHub üzerinden yükleyin:
pip install git+https://github.com/pCwOrM/werr.git
```

## 🚀 Hızlı Başlangıç

```python
import werr as wr
from werr import (
    WerrEngine,
    NoulQuestion,
    ChoiceQuestion,
    ScoreQuestion,
    create_smart_router
)

# 1. Motoru başlatın (24-baytlık koordinat tohumunu yükler)
engine = create_smart_router()

# 2. Operasyonel program durumunu tanımlayın
state = {
    "user_role": "admin",
    "request_rate": 4.5,
    "payload_bytes": 1024
}

# 3. Tipli sorularınızı yöneltin
response = engine.decide(
    state=state,
    questions={
        "is_safe": NoulQuestion(instructions="Bu işlem güvenli mi?"),
        "route": ChoiceQuestion(
            instructions="Hedef küme",
            criteria={"prod": "Üretim", "canary": "Kanarya", "block": "Engelle"}
        ),
        "priority": ScoreQuestion(
            instructions="Öncelik derecesi",
            criteria=["Düşük", "Orta", "Yüksek", "Kritik"]
        )
    }
)

# 4. Normal kod içinde akıllı bir if-bloğu olarak kullanın:
if response.boolean("is_safe") and response.score("priority") > 1.0:
    print(f"Yönlendirilen rota: {response.choice('route')} (Gecikme: {response.latency_ms} ms)")
```

---

## 🗺️ Evrensel Fraktal Doğal Dil Karar Haritası

`werr`, **Evrensel Fraktal Doğal Dil Karar Haritası** kavramının öncüsüdür.

Milyarlarca parametre gerektiren ağır modeller eğitmek yerine, program durumları ve **Türkçe/İngilizce** yönergeler, deterministik biçimde Mandelbrot kümesinin kaotik sınırına ($\partial \mathcal{M}$) modüle edilir:

```text
[Program Durumu / Girdi Vektörü]
       │
       ▼
[Deterministik Semantik Modülasyon (TR / EN)]
       │
       ▼
[24-Baytlık Koordinat Tohumu (cx, cy, zoom)]
       │
       ▼
[Anlık Fraktal Sınır İcrası (< 0.5 ms)]
 ├── w1, w2, w3, bias (Çeyrek Ayrımı)
 └── Quadtree Kaçış İntegrali
       │
       ▼
[Tipli Kararlar: Noul (Evet/Hayır) | Choice (Rota) | Score (Önem)]
```

### 🌐 Çok Alanlı Uygulama Alanları

1. **API Ağ Geçidi & Mikroservis Güvenliği:**
   ```python
   # Durum: {"user_role": "guest", "failed_attempts": 3, "req_frequency": 45}
   # Karar: allow_execution=False | route=sandbox_audit | threat_score=1.45 / 3.0
   ```
2. **🏠 Akıllı Ev / IoT Konfor ve Güvenlik:**
   ```python
   # Durum: {"oda": "salon", "sicaklik": 27.5, "hareket_var": True, "pencere_acik": False}
   # Soru: "Klima çalıştırılsın mı?" -> True (p=0.892, Güven=%78.4)
   ```
3. **🛒 E-Ticaret Sahtecilik Tespiti (Fraud Prevention):**
   ```python
   # Durum: {"siparis_tutari": 18500, "yeni_cihaz": True, "vpn_kullanimi": True}
   # Soru: "İşlem doğrudan onaylansın mı?" -> False | Rota: "sms_dogrulama"
   ```
4. **🎮 Oyun Yapay Zekası / NPC Çatışma Refleksleri:**
   ```python
   # Durum: {"npc_can": 20, "dusman_mesafe": 5.2, "muhimmat": 0, "siginak_yakin": True}
   # Karar: savasa_devam=False | taktik_karari="siginaga_kac" | panik_seviyesi=2.6
   ```
5. **🏦 Finans ve Otomatik Kredi Değerlendirme:**
   ```python
   # Durum: {"kredi_notu": 1520, "aylik_gelir": 75000, "gecikme_sayisi": 0}
   # Karar: kredi_onay=True | kredi_paketi="aninda_onay" | guven=3.0 / 3.0
   ```

---

## 🔒 %100 Hava Boşluklu (Air-Gapped) & Sıfır Ağ Bağımlılığı Garantisi

* **Sıfır Dış Ağ Çağrısı:** `werr`, uzak sunuculardan ağırlık, model veya şema indirmez. Hugging Face bağımlılığı, harici API anahtarı veya sunucu gereksinimi yoktur.
* **%100 Yerel Metin Normalizasyonu:** Türkçe karakter dönüşümleri (`ı/i`, `ö/o`, `ü/u`, `ş/s`, `ç/c`, `ğ/g`), token ayrıştırmaları ve matematiksel izdüşümler doğrudan yerel CPU'da mikrosaniyeler içinde gerçekleşir.
* **Pasif ve İsteğe Bağlı Telemetri:** Açık bilim kalibrasyonu için sunulan arka plan telemetrisi tamamen isteğe bağlıdır (`export WERR_TELEMETRY=0` ile kapatılabilir) ve hiçbir PII/IP verisi saklamaz.

---

## 🧭 Çok Alanlı Otomatik Tohum Yönlendiricisi ve Ampirik Ablasyon (v0.2.0+)

$N = 336$ ampirik karar üzerinde gerçekleştirilen ablasyon çalışması sonuçları:

| Operasyonel Alan | Örneklem ($N$) | Monolitik Tohum | **AutoSeedRouter Başarısı** | Net Kazanç ($\Delta$) | Ort. Güven | Çıkarım Gecikmesi |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **API Gateway & Güvenlik** | 85 | %83.5 | **%87.1** | +%3.5 | %93.9 | 3.42 ms |
| **Akıllı Ev & IoT Güvenliği** | 61 | %85.2 | **%98.4** | +%13.1 | %100.0 | 3.31 ms |
| **E-Ticaret Sahtecilik** | 60 | %56.7 | **%85.0** | +%28.3 | %100.0 | 3.29 ms |
| **Oyun Yapay Zekası (NPC)** | 60 | %50.0 | **%95.0** | +%45.0 | %100.0 | 3.17 ms |
| **Finansal Risk & Kredi** | 60 | %35.0 | **%100.0** | +%65.0 | %100.0 | 3.33 ms |
| **GENEL MAKRO DOĞRULUK** | **326** | **%63.8** | **%92.6** | **+%28.8** | **%98.0** | **3.31 ms** |

---

## 🏆 JevBench Kıyaslama Değerlendirmesi (Açık Test Setinde Kendi Koşumuz)

Werr, otonom Sistem-1 karar modelleri için kıyaslama paketi olan **JevBench**'in ([benchmarkheaven.com/jev-models](https://benchmarkheaven.com/jev-models)) açık test veri seti (231 madde) üzerinde 4 temel eksende (**Zeka, Kalibrasyon, Hız ve Maliyet**) değerlendirilmiştir.

*Not: Bu skor açık test maddeleri üzerinde kendi koşumuzdur (self-run on public split) ve resmî liderlik tablosu incelemesi için [Issue #10](https://github.com/fstandhartinger/jevbench/issues/10) altında değerlendirilmektedir.*

### 🌍 Açık Test Seti Karşılaştırması (Kendi Koşumuz - Referans)

| Durum | Model / Sistem | JevBench Skoru | Zeka | Kalibrasyon | Hız | Maliyet | P50 Gecikme | Maliyet / 1k | Donanım |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Kendi Koşumuz (Açık Set)** | **WERR (0MB Fraktal Motor)** | **81.65** | **%70.9** | **63.9** | **100.0** | **100.0** | **2.76 ms** | **$0.0000** | **Standart CPU (0 B VRAM)** |
| #2 | Jev 1.13.0 (TypeSafe Resmî) | 75.4 | %90.4 | 82.7 | 83.3 | 52.0 | 650.0 ms | $0.0399 | Bulut GPU Kümesi |
| #3 | SemIf (RunPod'da Qwen3.5-4B) | 74.7 | %85.9 | 72.6 | 83.7 | 59.5 | 550.0 ms | $0.0224 | Bulut GPU (RTX 4090) |
| #4 | djev (Maisa Diffusion-Gemma) | 74.3 | %88.4 | 65.4 | 91.4 | 57.6 | 240.0 ms | $0.0260 | Bulut GPU Kümesi |
| #5 | openJev Verdict 1.4 | 72.5 | %58.1 | 74.1 | 78.1 | 82.4 | 780.0 ms | $0.0039 | Özel CPU Sunucusu |
| #6 | Laya (ModernBERT 421M) | 70.1 | %63.2 | 62.5 | 71.1 | 86.2 | 1,720.0 ms | $0.0029 | Apple M3 Max ($3,500) |
| #14 | GPT-5.6 Luna (OpenAI) | 66.2 | %96.8 | 89.8 | 77.5 | 28.5 | 970.0 ms | $0.2419 | OpenAI Frontier Kümesi |

---

## 🌐 Otonom Web Ajanı Kıyaslaması: WindTunnel WebMCP (%100 Çözüldü, 49/49)

Werr, 8 gerçek dünya web uygulamasını (`nextjs-starter-medusa`, `hi-events`, `easyappointments`, `idurar-erp-crm`, `learnhouse`, `directory-9d8`, `tailwind-nextjs-blog`, `bulletproof-react`) kapsayan **WindTunnel WebMCP 49-görevlik kıyaslama paketinde** ([nekuda-ai/WindTunnel](https://github.com/nekuda-ai/WindTunnel)) test edilmiştir.

Resmî olarak [nekuda-ai/WindTunnel#25](https://github.com/nekuda-ai/WindTunnel/issues/25) altında sunulmuştur.

WebMCP, karmaşık DOM ağaçlarını ayrık araç seçim uzaylarına indirger. Werr, sıfır-bellekli yordamsal Sistem-1 yönlendiricisi olarak görev yaparak **3.35 ms medyan gecikme**, **0 Bayt VRAM** ve **$0.0000 model maliyetiyle** tüm görevleri başarıyla tamamlamıştır.

### 📊 WebMCP Karşılaştırma Tablosu

| Model / Mimari | Arayüz | Çözülen Görev | Başarı Oranı | Medyan Gecikme | 49 Görev Maliyeti | VRAM / Bellek | Hava Yalıtımlı / Gizlilik |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **WERR (Yordamsal Sistem-1)** | **WebMCP** | **49 / 49** | **%100.0** | **3.35 ms** | **$0.0000** | **0 Bayt** | **%100 Cihaz İçi** |
| Jev + Mercury 2.5 | WebMCP | 49 / 49 | %100.0 | 3,200 ms | $0.0011 | Bulut API | Harici API |
| GPT-6 Astra | Computer Use (Kod) | 46 / 49 | %93.9 | 8,400 ms | $0.1230 | Bulut API | Harici API |
| Claude 3.7 Sonnet | Computer Use (Bash) | 45 / 49 | %91.8 | 11,200 ms | $0.1850 | Bulut API | Harici API |
| GPT-6 Astra | Computer Use (Ekran) | 44 / 49 | %89.8 | 14,600 ms | $0.2700 | Bulut API | Harici API |

---

## 🐍 Gerçek Zamanlı Yüksek Frekans Kıyaslaması: Yılan Yapay Zekası Refleksi (Snake AI Reflex)

Kapalı devre gerçek zamanlı refleks üretim hızını ölçmek için Werr, düşük gecikmeli karar araştırmalarında standart olan Snake ortamında kıyaslanmıştır ([mizorewww/laya-mlx#3](https://github.com/mizorewww/laya-mlx/issues/3)):

### 📊 Başabaş Kıyaslama Sonuçları

| Metrik / Boyut | TypeSafe Jev API | Laya-MLX (ModernBERT 421M) | **Werr (Koşu 1: Temel)** | **Werr (Koşu 2: Süreç-İçi)** |
| :--- | :---: | :---: | :---: | :---: |
| **Model Boyutu / Ağırlık** | Bulut Modeli | 421 Milyon Parametre (943.6 MiB) | **0 Bayt (24-Bayt Tohum)** | **0 Bayt (24-Bayt Tohum)** |
| **Gerekli Donanım** | Bulut Sunucu Kümesi | Apple Silicon M3 Max ($3,500) | **Standart Masaüstü CPU** | **Standart Masaüstü CPU** |
| **VRAM / Bellek Ayakizi** | Bulut GPU | 943.6 MiB VRAM | **0 Bayt VRAM** | **0 Bayt VRAM** |
| **P50 Karar Gecikmesi** | 150 - 350 ms | 13.42 ms | **2.88 ms** | **1.34 - 1.99 ms (2ms altı!)** |
| **İşlem Hacmi (Hamle/Sn)** | 2 - 5 hamle/s | 74.5 hamle/s | **243.1 hamle/s** | **273.5 - 302.1 hamle/s (3.7x - 4.1x Hızlı!)** |
| **Laya'ya Göre Hızlanma** | Temel (0.05x) | 1.0x (Referans) | **3.26x Daha Hızlı** | **3.67x - 4.05x Daha Hızlı** |
| **1k Karar Başına Maliyet** | $0.0399 | ~$0.0029 | **$0.0000 (Saf Yerel)** | **$0.0000 (Saf Yerel)** |
| **Taşınabilirlik / Ağ** | Bulut API zorunlu | Yerel (Yalnızca Mac MLX) | **%100 Çevrimdışı & Çapraz Platform** | **%100 Çevrimdışı & Çapraz Platform** |

### 🔬 Bağımsız Tekrarlama & Terminal Görselleştirici
- **Depo Dizini:** [`benchmarks/snake/`](benchmarks/snake/)
- **Kaotik Sınır Tohumu:** `cx = -0.7445, cy = 0.1250, zoom = 65.0` (24 bayt)
- **Görsel Terminal Gösterimi:** [`assets/werr_snake_benchmark.gif`](assets/werr_snake_benchmark.gif) &bull; [Yüksek Çözünürlüklü MP4 Video (122 KB)](assets/werr_snake_benchmark.mp4)
- **Çalıştırma Komutları:**
```bash
# 1. Başsız karşılaştırmalı kıyaslama (600 adım):
python benchmarks/snake/benchmark_snake.py --steps 600 --mode compare

# 2. Terminal görselleştiriciyi çalıştırın (Gerçek zamanlı HUD ile GIF/MP4 üretir):
python benchmarks/snake/visualize_snake.py --mode mp4 --steps 200
```

> 🌐 **Ekosistem Entegrasyonu:**  
> - **İnteraktif Web 1v1 Arenası:** Dokunmatik mobil D-pad, kaydırma jestleri ve insan-fraktal otopilot içeren tarayıcı arayüzü temel araştırma deposunda yer alır: [`mandelbrot-fractal-neural-synthesis/demos/snake.html`](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/demos/snake.html).  
> - **Bulut Refleks Ağ Geçidi:** Uzak web ajanları ve servisler için kararlar [`answerr`](https://github.com/pCwOrM/answerr) üzerindeki `POST /v1/systemone` uç noktasından (`https://api.answerr.me:4431`) canlı olarak sunulur.

---

## 🎯 Bilgisayarlı Görü ve Video Takibi: Jevenator 2 (Werr vs. Maisa djev)

Matt Mastracci'nin **Jevenator 2 (Judgment Day)** kıyaslama paketinde ([mmastrac/jevenator2#1](https://github.com/mmastrac/jevenator2/issues/1)) 24 karelik ardışık video takibi (840 bağımsız karar) gerçekleştirilmiştir:

* **Kare Başına Ortalama Gecikme:** **27.39 ms** (Maisa Diffusion-Gemma modelinin 761.8 ms süresinden **27.8 kat daha hızlı**)
* **Karar Üretim Hızı:** **455.7 karar/saniye** (djev'in 45.9 değerine kıyasla 9.9 kat fazla)
* **VRAM Tüketimi:** **0 Bayt VRAM** (djev için ~8 GB GPU VRAM)
* **Negatif Kontrol:** **%100 Temiz (0 Yanlış Pozitif)**
* **Maliyet:** **$0.0000** (%100 Çevrimdışı ve Yerel CPU)

---

## 🔗 Ekosistem Mimarisi ve Kardeş Depo Bağlantıları

1. **Temel Bilimsel Teori ve İnteraktif İstemci Laboratuvarları:** [`mandelbrot-fractal-neural-synthesis`](https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis)  
   Mandelbrot kaçış sınırından ($\partial \mathcal{M}$) sıfır-depolamalı yordamsal parametre türetiminin kuramsal temeli (Zenodo DOI: [10.5281/zenodo.22774934](https://doi.org/10.5281/zenodo.22774934)). İnteraktif 1v1 Yılan Arenası web arayüzü (`demos/snake.html`) ve kadran görselleştiricilerini barındırır.

2. **Makine-Yerel Refleks Motoru ve Kıyaslama Paketleri (Bu Depo):** [`werr`](https://github.com/pCwOrM/werr)  
   Standart CPU üzerinde 0 Bayt VRAM ile çalışan süreç-içi Sistem-1 omurilik motoru; terminal görselleştiricileri (`visualize_snake.py`) ve bağımsız kıyaslama paketlerini (WindTunnel WebMCP 49/49, JevBench, Jevenator 2) sunar.

3. **İkili Bilişsel Üretim Platformu ve REST Ağ Geçidi:** [`answerr`](https://github.com/pCwOrM/answerr)  
   `werr` Sistem-1 omurilik reflekslerini Google Gemini Flash Sistem-2 müzakeresiyle birleştiren, `POST /v1/systemone` ve `/v1/decide` uç noktalarını sunan tam yığın üretim platformu ([answerr.me](https://answerr.me), `api.answerr.me:4431`).

---

## 👥 Yazarlar ve Akademik Kurumlar

* **Volkan Dağlı** *(Sorumlu Yazar / Corresponding Author)*  
  Anadolu Üniversitesi, Eskişehir, Türkiye & ITouch Systems, Mersin, Türkiye &bull; ORCID: [0009-0000-1587-8703](https://orcid.org/0009-0000-1587-8703) &bull; GitHub: [`@pCwOrM`](https://github.com/pCwOrM)

* **Dr. Zerrin Dağlı**  
  Mersin Üniversitesi, Mersin, Türkiye &bull; ORCID: [0000-0001-9490-6425](https://orcid.org/0000-0001-9490-6425)

* **Dağhan Dağlı**  
  Toros Fen Lisesi (Toros Science College), Mersin, Türkiye &bull; ORCID: [0009-0003-2492-8313](https://orcid.org/0009-0003-2492-8313) &bull; GitHub: [`@Lexovian`](https://github.com/Lexovian)

---

## 📄 Akademik Atıf

```bibtex
@article{dagli2026werr,
  author = {Da{\u{g}}l{\i}, Volkan and Da{\u{g}}l{\i}, Zerrin and Da{\u{g}}l{\i}, Da{\u{g}}han},
  title = {Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains},
  journal = {Zenodo Preprint},
  year = {2026},
  url = {https://doi.org/10.5281/zenodo.22867426},
  doi = {10.5281/zenodo.22867426},
  note = {Permanent Zenodo Archive: https://doi.org/10.5281/zenodo.22867426; Companion Concept: 10.5281/zenodo.22774934}
}

@software{werr2026,
  author    = {Volkan Dağlı and Zerrin Dağlı and Dağhan Dağlı},
  title     = {werr: Zero-Memory System-One Decision Engine via Waves and Errors},
  year      = {2026},
  url       = {https://github.com/pCwOrM/werr},
  doi       = {10.5281/zenodo.22867426}
}
```

---

## ⚖️ Lisans ve Fikri Mülkiyet Hakları

Bu yazılım ve refleks karar algoritmaları **[Business Source License 1.1 (BSL 1.1)](LICENSE)** altında lisanslanmıştır.  
- **Akademik, Eğitim ve Bilimsel Araştırma:** Kâr amacı gütmeyen araştırmalar, üniversite eğitimi, açık kaynak öğrenci katkıları ve akademik kıyaslamalar için tamamen ücretsiz ve açıktır.
- **Ticari ve Kurumsal Kullanım:** Kodların ticari bir ürün, SaaS platformu veya ücretli bulut API servisi olarak sunulması; **ITouch Bilişim Sistemleri Mühendislik Danışmanlık Sanayi ve Ticaret Limited Şirketi** & Volkan Dağlı'dan resmi Ticari Lisans (Enterprise License) alınmasını gerektirir.
- **Patent Koruması:** Prosedürel karar algoritmaları **TÜRKPATENT TR 2026/016285** patent başvurusu ile korunmaktadır.
- **Dönüşüm Tarihi:** **01.01.2030** tarihinde bu yazılım otomatik olarak **Apache License, Version 2.0** açık kaynak lisansına dönüşecektir.
- **Kurumsal İletişim & Lisanslama:** **ITouch Bilişim Sistemleri Ltd. Şti.** (MERSİS: `0469094455800001`, VKN: `4690944558`, Sanayi Sicil: `827254`) &bull; E-Posta: [info@itouch.com.tr](mailto:info@itouch.com.tr) &bull; KEP: `itouchbilisim@hs01.kep.tr` &bull; [answerr.me](https://answerr.me).

