<div align="center">

# WERR
### Sıfır-Bellekli Fraktal Refleks Karar Motoru · Dalgalar ve Hatalar

[![Lisans: BSL 1.1](https://img.shields.io/badge/Lisans-BSL_1.1-0ea5e9.svg)](LICENSE)
[![Biçimsel Doğrulama: Lean 4](https://img.shields.io/badge/Lean_4-0_sorry_(Doğrulandı)-10b981.svg)](https://github.com/pCwOrM/gap-lean4-port)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-6366f1.svg)](https://pypi.org/project/werr/)
[![Zenodo DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22774934-f59e0b.svg)](https://doi.org/10.5281/zenodo.22774934)
[![ArXiv Ön Baskı](https://img.shields.io/badge/arXiv-2609.25498-b91c1c.svg)](https://arxiv.org/abs/2609.25498)

<p align="center">
  <b>Yapay sinir ağı ağırlıkları, bellek (VRAM) veya gecikme maliyeti gerektirmeksizin; Mandelbrot sınır kaçış dinamiklerinden doğrudan tip güvenli kararlar üreten deterministik, prosedürel Sistem-1 refleks motoru.</b>
</p>

[Hızlı Başlangıç](#-30-saniyede-hızlı-başlangıç) •
[Mimari](#-matematiksel-ve-biçimsel-mimari) •
[Karar Primitifleri](#-üç-tip-güvenli-primitif) •
[Kıyaslamalar](#-ampirik-değerlendirme-ve-kıyaslamalar) •
[Biçimsel İspatlar](#-biçimsel-doğrulama-lean-4) •
[Ekosistem](#-werr-ekosistemi) •
[Araştırma Kronolojisi](RESEARCH_CHRONOLOGY.md) •
[English Documentation](README.md)

</div>

---

## 🏛️ Yeni Bir Paradigma

Çağdaş yapay zekâ mimarileri büyük ölçüde milyarlarca parametre içeren yoğun tensör ağırlıklarına dayanmaktadır. Bu modeller üretimsel muhakeme (Sistem-2) süreçlerinde oldukça başarılı olsa da; ultra yüksek frekanslı refleks denetimi, uç birim (edge) filtreleme veya blokzincir üzeri (on-chain) mantık yürütmede gigabaytlarca bellek kaplamakta, yüksek hesaplama gecikmesi yaratmakta ve olasılıksal halüsinasyon riskleri barındırmaktadır.

**WERR (Waves & Errors / Dalgalar ve Hatalar)** buna ortogonal yeni bir yaklaşım sunar: **Prosedürel Refleks Çıkarımı**. WERR, milyarlarca parametreyi bellekte tutmak yerine, karar sınırlarını karmaşık düzlem üzerindeki geometrik değişmezler (invariants) olarak ele alır. Herhangi bir doğal dil girdisi, sistem durumu veya telemetri çerçevesi verildiğinde:

1. **Deterministik İzdüşüm:** Bağlam, karmaşık düzlem $\mathbb{C}$ üzerinde sınırlı koordinatlara yansıtılır.
2. **Yörüngesel Karmaşık Dinamikler:** Koordinat, prosedürel polinom kaçış yörüngeleriyle ($z_{n+1} = z_n^2 + c$) değerlendirilir.
3. **Harmonik Refleks Çıkarımı:** Standart işlemcilerde $\le 0.3\,\mu\text{s}$ veya EVM üzerinde yalnızca 32 baytlık depolama yuvasıyla üç değişmez tip güvenli karar primitifi türetilir.

```
Girdi Telemetrisi / Bağlam
           │
           ▼
┌──────────────────────────────────────┐
│   Prosedürel Koordinat İzdüşümü      │  ◄── 24 baytlık değişmez tohum
└──────────────────────────────────────┘
           │  c = x + iy ∈ ℂ
           ▼
┌──────────────────────────────────────┐
│   Yörüngesel Karmaşık Dinamik Motoru │  ◄── z_{n+1} = z_n^2 + c
└──────────────────────────────────────┘
           │  Kaçış yarıçapı & Lyapunov üssü
           ▼
┌─────────────────────────────────────────────────────────────┐
│                    Üç Tip Güvenli Primitif                  │
│   • noul   (İkili karar kapısı: İZİN VER / ENGELLE)         │
│   • choice (Ayrık yönlendirme: 0, 1, 2, 3)                  │
│   • score  (Sürekli risk/ciddiyet skoru: [0.0, 1.0])        │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚡ 30 Saniyede Hızlı Başlangıç

WERR, sıfır bağımlılıklı Python paketi ve Rust/C çekirdeği olarak sunulur.

### Kurulum

```bash
pip install werr
```

*Veya en güncel sürümü doğrudan GitHub üzerinden yükleyin:*

```bash
pip install git+https://github.com/pCwOrM/werr.git
```

### Temel Kullanım

```python
import werr

# Motoru başlat (değişmez koordinat tohumlarını belleğe alır)
engine = werr.WerrEngine()

# 1. İkili Refleks Kapısı (noul): True veya False döner
is_safe = engine.noul(
    question="Bu işlem yükü imzalanmak için güvenli mi?",
    context="Base L2 üzerinde doğrulanmış 0x7a25... sözleşmesine 0.05 ETH transferi"
)

# 2. Ayrık Rota Seçici (choice): Kategorik tamsayı indeksi döner [0, 1, 2, 3]
route = engine.choice(
    question="En uygun yürütme şeridini seçin:",
    options=["Doğrudan Arbitraj", "Özel RPC Havuzu", "Zaman Aşımı Bekle", "İşlemi İptal Et"]
)

# 3. Sürekli Risk Skoru (score): Normalize edilmiş float döner [0.0, 1.0]
risk_score = engine.score(
    metric="Likidite Havuzu Volatilitesi",
    current_value=142.8,
    historical_baseline=100.0
)

print(f"Karar: {is_safe} | Rota: {route} | Risk: {risk_score:.4f}")
```

---

## 📐 Üç Tip Güvenli Primitif

Tüm WERR karar mantığı, matematiksel ve tip güvenliği tanımlanmış üç çekirdek primitif etrafında inşa edilmiştir:

| Primitif | İsim | Dönüş Tipi | Karmaşıklık | Birincil Kullanım Alanı |
|---|---|---|---|---|
| `noul(q, c)` | İkili Refleks Kapısı | `bool` | $\mathcal{O}(k)$ sabiti | Güvenlik duvarı gating, işlem onaylama, anomali engelleme |
| `choice(q, opts)` | Ayrık Rota Seçici | `int \in [0, N-1]` | $\mathcal{O}(N \cdot k)$ | Çok yollu arbitraj, model yönlendirme, strateji seçimi |
| `score(metric, val)` | Sürekli Şiddet Skoru | `float \in [0.0, 1.0]` | $\mathcal{O}(k)$ sabiti | Kredi sağlık katsayısı, teminat tasfiye riski, SLA ağırlığı |

*Not: $k$, Mandelbrot kaçış algoritmasındaki sabit döngü derinliğidir (varsayılan $k=64$). Bellek ayrımı (allocation) gerektirmez.*

---

## 📊 Ampirik Değerlendirme ve Kıyaslamalar

WERR, sıfır ağırlık ilkesine rağmen hem kurumsal edge senaryolarında hem de standart yapay zekâ kıyaslama ortamlarında titizlikle test edilmiştir:

### 1. WebMCP 100% Karar Doğruluğu
Tarayıcı tabanlı model-kontrol protokolü (WebMCP) doğrultusunda, answerr entegrasyonu ile WERR refleks kapısı:
* **WebMCP Değerlendirmesi:** 42 test senaryosunda **%100** sıfır-hata başarı oranı (`windtunnel_webmcp_evaluation.py`).
* **Çıkarım Hızı:** Ortalama çağrı süresi **$0.28\,\mu\text{s}$** (geleneksel küçük SLM'lerin $45\,\text{ms}$ gecikmesine kıyasla **~160.000 kat daha hızlı**).

### 2. Snake AI & Dinamik Engel Navigasyonu
Deterministik ızgara hareket senaryolarında WERR `choice` yönlendiricisi:
* 500 ardışık adımda sıfır duvar veya kuyruk çarpışması.
* Deterministik karar tekrar üretilebilirliği (seed sabitken %100 özdeş yörünge).

Tüm ampirik test logları, donanım stres ölçümleri ve ablasyon sonuçları [RESEARCH_CHRONOLOGY.md](RESEARCH_CHRONOLOGY.md) dosyasında eksiksiz muhafaza edilmektedir.

---

## 🛡️ Biçimsel Doğrulama (Lean 4)

WERR'in temel topolojik değişmezleri, sınır kaçış eşitsizlikleri ve ayrık bölümleme teoremleri, **Lean 4** etkileşimli teorem ispatlayıcısında **0 `sorry`** (eksiksiz doğrulanmış) ile mühürlenmiştir.

* **Depo:** [`pCwOrM/gap-lean4-port`](https://github.com/pCwOrM/gap-lean4-port)
* **Ön Baskı / Monografi:** Zenodo DOI: [`10.5281/zenodo.22974544`](https://doi.org/10.5281/zenodo.22974544)
* **Kapsam:** Schreier-Sims elemesi, devirli bölüm kararlılığı ve sınırlı pertürbasyon altında sınır tutarlılığının makine tarafından denetlenmiş ispatı.

---

## 🌐 WERR Ekosistemi

WERR, üçlü bir mimari yığının temel matematiksel motoru olarak işlev görür:

```
                          ┌─────────────────────────────┐
                          │            WERR             │
                          │    Çekirdek Matematik Motor │
                          │  Sıfır-Bellekli Sistem-1    │
                          └──────────────┬──────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
  ┌─────────────────────────────┐                 ┌─────────────────────────────┐
  │          Werracle           │                 │           answerr           │
  │ Blokzincir Karar Kâhini     │                 │   Çift Bilişli Çalışma Alanı│
  │  DeFi Risk Radarı & DaaS    │                 │   Doğal Dil Güvenlik API'si │
  │   https://radar.werracle.com│                 │     https://answerr.me      │
  └─────────────────────────────┘                 └─────────────────────────────┘
```

* **`werr`:** Çekirdek algoritma, tohum koordinatları ve yerel Python/Rust çalışma zamanı kütüphaneleri.
* **[`werracle`](https://github.com/pCwOrM/werracle):** Akıllı sözleşme uygulamaları, Q16.16 sabit nokta Solidity kaçış matematiği, Uniswap v4 kanca (hook) şablonları ve [Werracle Risk Radarı](https://radar.werracle.com).
* **[`answerr`](https://github.com/pCwOrM/answerr):** Sistem-2 bilinçli doğal dil politika derlemesini WERR Sistem-1 deterministik yürütmesiyle birleştiren çift bilişli çalışma alanı.

---

## 📄 Akademik Atıf ve Arşiv Kaynakları

Bu araştırmayı bilimsel yayınlarınızda referans gösterirken veya tekrarlarken lütfen aşağıdaki künyeyi kullanın:

```bibtex
@software{dagli2026werr,
  author       = {Dağlı, Volkan and Dağlı, Zerrin and Dağlı, Dağhan},
  title        = {{werr: Zero-Memory Fractal System-One Decision Engine (Waves & Errors)}},
  month        = oct,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v0.5.1},
  doi          = {10.5281/zenodo.22774934},
  url          = {https://github.com/pCwOrM/werr}
}
```

* **Arşiv Ön Baskısı:** arXiv:2609.25498 `[cs.AI / math.DS]` ([https://arxiv.org/abs/2609.25498](https://arxiv.org/abs/2609.25498))
* **Tam Araştırma Kronolojisi:** [`RESEARCH_CHRONOLOGY.md`](RESEARCH_CHRONOLOGY.md)

---

## ⚖️ Lisans ve Fikri Mülkiyet

* **Açık Bilim, Eğitim ve Değerlendirme Kullanımı:** Lisanslı Eser; **Business Source License 1.1 (BSL 1.1)** kapsamında ticari olmayan tüm akademik araştırmalar, kişisel incelemeler, kıyaslama, test ve çatallama (fork) süreçleri için serbestçe çalıştırılabilir, kaynak kodu incelenebilir ve yinelenebilir.
* **Ticari Faaliyetler ve Üretim Lisanslaması:** Her türlü ticari üretim kullanımı, barındırılan SaaS dağıtımı veya tescilli yeniden dağıtım, Lisans Veren'den ticari lisans alınmasını gerektirir:
  * **Lisans Veren:** `ITOUCH BİLİŞİM SİSTEMLERİ MÜHENDİSLİK DANIŞMANLIK SANAYİ VE TİCARET LİMİTED ŞİRKETİ` (`ITouch Sistemleri` · Çukurova Teknokent, Adana, Türkiye).
  * **Bilimsel Ortak Yazarlar ve Mucitler:** Volkan Dağlı (*Anadolu Üniversitesi*), Dr. Zerrin Dağlı (*Mersin Üniversitesi — Akademik Danışman, Ortak Yazar ve Ortak Mucit*), Dağhan Dağlı (*Toros Üniversitesi — Ortak Yazar ve Ortak Mucit*).
  * **Patent Başvuruları:** TÜRKPATENT **TR 2026/016285** ve **TR 2026/016633**.
  * **İletişim:** `contact@werracle.com` · `ask@answerr.me`

---

<div align="center">
  <sub>ITouch Bilişim Sistemleri tarafından geliştirilmiştir · Çukurova Teknokent, Adana, Türkiye</sub><br>
  <sub>Telif Hakkı &copy; 2026 ITouch Bilişim Sistemleri Ltd. Şti. Tüm hakları saklıdır.</sub>
</div>
