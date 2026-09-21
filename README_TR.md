<p align="center">
  <img src="assets/answerr_werr_twin_ecosystem.svg" alt="answerr ve werr İkiz Ekosistem Görseli" width="100%">
</p>

<p align="center">
  <img src="assets/werr_logo_core.svg" alt="werr çekirdek amblemi" width="130">
</p>

# ⚡ WERR: Sıfır-Bellekli Fraktal Sistem-1 Karar Motoru (Dalgalar ve Hatalar)

[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](./LICENSE)
[![Canlı Demo: GitHub Pages](https://img.shields.io/badge/Canl%C4%B1%20Demo-GitHub%20Pages-38bdf8.svg)](https://pcworm.github.io/werr/)
[![Temel Araştırma: DOI](https://img.shields.io/badge/Temel%20Ara%C5%9Ft%C4%B1rma-DOI%3A%2010.5281%2Fzenodo.22867037-green.svg)](https://doi.org/10.5281/zenodo.22867037)
[![Kardeş Platform: answerr](https://img.shields.io/badge/answerr-Canl%C4%B1%20Platform-38bdf8.svg)](https://answerr.me)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CI Workflow](https://github.com/pCwOrM/werr/actions/workflows/ci.yml/badge.svg)](https://github.com/pCwOrM/werr/actions/workflows/ci.yml)

> **Motto:** *"Dalga Hata ile Karşılaştığında, Yineleriz (werr)."*  
> *"Refleks nerede? Karar Werr!"*  
> *"Klasik kararlar milyarlarca parametreli ağır tensörlerden çıkar; `werr` kararları sonsuz geometrik dalgalardan, Euler eşiklerinden ve özyinelemeli çeyrek bölünmelerinden doğar."*

🌐 **Dil Seçici / Language Switcher:**  
[🇬🇧 English Documentation (README.md)](README.md) | **Türkçe (README_TR.md)**

🌐 **Etkileşimli Web Laboratuvarı:** [GitHub Pages Üzerindeki Canlı Simülatörü Deneyin](https://pcworm.github.io/werr/) *(Türkçe & İngilizce, Açık & Koyu Tema).*

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

## 🔗 Temel Araştırma ve Kardeş Projelerle Bağlantı

1. **Temel Bilimsel Teori:** [`mandelbrot-fractal-neural-synthesis`](https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis) — Ağırlıkların Mandelbrot kaçış dinamiğinden türetilmesinin matematiksel ispatı (*Chaos, Solitons & Fractals*, Zenodo DOI: `10.5281/zenodo.22867037`).
2. **Canlı Çalışma Alanı & Platform:** [`answerr`](https://github.com/pCwOrM/answerr) — `werr` Sistem-1 refleks çekirdeğini Gemini LLM Sistem-2 ile buluşturan canlı platform ([answerr.me](https://answerr.me)).

---

## 📄 Akademik Atıf

```bibtex
@software{werr2026,
  author    = {Volkan Dağlı and Zerrin Dağlı and Dağhan Dağlı},
  title     = {werr: Zero-Memory System-One Decision Engine via Waves and Errors},
  year      = {2026},
  url       = {https://github.com/pCwOrM/werr},
  doi       = {10.5281/zenodo.22867426}
}
```

## ⚖️ Lisans

Bu proje **MIT Lisansı** altında yayımlanmıştır. Detaylar için [LICENSE](./LICENSE) dosyasına bakabilirsiniz.
