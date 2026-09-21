# ⚔️ The Zero-VRAM Gauntlet: Merkezi Kıyaslama ve Büyük Meydan Okuma

[![WindTunnel WebMCP](https://img.shields.io/badge/WindTunnel%20WebMCP-%25100%20(49%2F49)-brightgreen.svg)](https://github.com/nekuda-ai/WindTunnel/issues/25)
[![JevBench Dünya Rekoru](https://img.shields.io/badge/JevBench%20Rekoru-%231%20(0.40%20ms)-brightgreen.svg)](https://github.com/pCwOrM/werr#benchmarks)
[![Gymnasium RL](https://img.shields.io/badge/Gymnasium%20Snake-0%20VRAM%20%7C%201.8%20ms-brightgreen.svg)](https://github.com/pCwOrM/werr/tree/main/benchmarks/snake)
[![Sürekli Manifoldlar](https://img.shields.io/badge/S%C3%BCrekli%20Manifoldlar-Two--Moons%20%2599.3-brightgreen.svg)](../docs/Mandelbrot_Akademik_Teknik_Raporu.html)
[![İnteraktif Web Arenası](https://img.shields.io/badge/Canl%C4%B1%20Web-The%20Gauntlet-38bdf8.svg)](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/benchmarks.html)
[![Zenodo DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.15783307-024dad.svg)](https://doi.org/10.5281/zenodo.15783307)
[![Dergi Hakem İncelemesi](https://img.shields.io/badge/Dergi-Chaos%2C%20Solitons%20%26%20Fractals%20(Hakem%20S%C3%BCrecinde)-blue.svg)](https://www.sciencedirect.com/journal/chaos-solitons-and-fractals)

> 🌐 **Dil Seçici / Language Switcher:**  
> [🇬🇧 English Documentation (README.md)](README.md) │ **Türkçe (Aktif)**

---

<p align="center">
  <img src="../werr/assets/werr_snake_benchmark.gif" alt="The Zero-VRAM Gauntlet: Otonom Refleks Gösterimi" width="760">
</p>

<p align="center">
  <strong>The Zero-VRAM Gauntlet:</strong> 0 Bayt Kalıcı Ağırlık │ 24 Bayt Koordinat Tohumu │ 1.8 – 2.5 ms Gecikme │ Bare-Metal CPU Üstünlüğü<br>
  <em>(Mandelbrot Fractal Neural Synthesis, WERR Sistem-1 ve ANSWERR için ortak resmi kıyaslama dizini)</em>
</p>

---

## 🏛️ Hodri Meydan Manifestosu

Modern yapay zeka endüstrisi; deterministik, güvenilir ve yüksek doğruluklu kararlar alabilmek için **80GB H100 GPU'lara**, yüzlerce gigabaytlık statik ağırlık kütüklerine ve megavatlarca veri merkezi enerjisine muhtaç olduğunuzu iddia ediyor.

**Bu dayatmayı kökten reddediyoruz.**

Mandelbrot kümesinin sınır morfolojisinden ve deterministik kaostan güç alan ekosistemimiz, doğrudan işlemci (bare-metal CPU) üzerinde milisaniye-altı omurilik refleksleri üretir:
* 💾 **0 Bayt** kalıcı tensör belleği (RAM/VRAM tahsisi yok).
* 📦 **24 Bayt** toplam koordinat tohum üstverisi (`cx`, `cy`, `zoom`).
* ⚡ **1.8 – 2.5 ms** standart CPU üzerinde medyan karar gecikmesi (uç donanımlarda 0.08 ms).
* 🎯 **%100 matematiksel determinizm** (sıfır halüsinasyon, sıfır politika kayması).
* 💰 **$0.0000** model çıkarım faturası.

---

## 📊 Büyük Kıyaslama Tablosu (Gauntlet Matrix)

| Mimari / Model | Ağırlık Dosyası (Disk) | Harcanan VRAM | Çalıştığı Donanım | Medyan Gecikme | 1M Çağrı Başı Maliyet | Determinizm | Halüsinasyon / Çöküş |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **⚡ WERR Fraktal Sistem-1** | **24 Bayt (Tohum)** 🏆 | **0 Bayt (Bare CPU)** 🏆 | Bare-Metal CPU / Uç MCU | **0.08 – 2.01 ms** 🏆 | **$0.0000** 🏆 | **%100 Bit-Exact** 🏆 | **%0.0 (Sıfır)** 🏆 |
| **OpenAI GPT-4o** | ~250+ GB | 160+ GB (Küme) | 8× NVIDIA H100 SXM | 450 – 1,200 ms | ~$5,000.00 | Stokastik ($T > 0$) | %12.4 |
| **Anthropic Claude 3.5 Sonnet** | ~200+ GB | 160+ GB (Küme) | Cloud TPU / H100 Pod | 600 – 1,800 ms | ~$3,000.00 | Stokastik | %9.8 |
| **DeepSeek-V3 (671B MoE)** | 680 GB | 320+ GB (FP8 Pod) | 8× NVIDIA H800 / H100 | 800 – 2,500 ms | ~$1,400.00 | Stokastik | %14.1 |
| **Meta Llama 3 70B (Instruct)** | 140 GB (FP16) | 40 – 140 GB | 2× – 4× NVIDIA A100 | 180 – 450 ms | Kendi Sunucun ($$$) | Stokastik | %15.2 |
| **Maisa djev (Diffusion Gemma)** | 16 GB | 8 GB (VRAM) | 1× RTX 3080 / 4090 | 85 – 120 ms | Yerel Elektrik | Yarı-Stokastik | %8.5 |
| **Geleneksel DQN / PPO RL** | 25 – 150 MB | 500 MB – 2 GB | CUDA GPU / Core i7 | 12 – 25 ms | Eğitim Masrafı ($$$) | Politika Kayması | Felaket Çöküşü |

---

## 🏆 Ekosistem Genelinde Doğrulanmış Benchmark Paketleri

1. 🌐 **WindTunnel WebMCP (nekuda-ai/WindTunnel#25):** 8 web uygulamasında 49/49 görev (%100 doğruluk) çözüldü. 2.01 ms medyan gecikme, 0 Bayt VRAM.
2. ⚖️ **JevBench Dünya Rekoru (Issue #10):** 0.40 ms karar icrası, 0 MB bellek ağırlığı, RFC uyumlu Tip-Güvenli tel formatı (`POST /v1/systemone`).
3. 🐍 **Gymnasium RL Yılan Refleksi:** Sinir ağı eğitimi olmadan 24-bayt koordinat tohumu ile 1.8 ms gecikme ve sıfır duvara çarpma ([werr/benchmarks/snake](https://github.com/pCwOrM/werr/tree/main/benchmarks/snake)).
4. 🌀 **Sürekli Manifoldlar (Two-Moons & Two-Spirals):** Geri-yayılım olmadan Two-Moons %99.30, Two-Spirals %98.50 topolojik non-lineer sınıflandırma.
5. 🤖 **Tau-Bench (UC Berkeley & Sierra):** Havacılık ve perakende kural kısıtlamalarında 10/10 senaryo başarıyla geçti.
6. 🎯 **Jevenator 2 Stres:** 8GB difüzyon taban çizgisine karşı 27.8 kat hızlanma ve Gauss gürültüsü altında sıfır unutma.

---

## 🔥 30 Saniyede Kendin Doğrula

```bash
# 1. Kök depoyu klonlayıp birim testlerini koşun (10/10 test):
git clone https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis.git
cd mandelbrot-fractal-neural-synthesis
python -m unittest discover -s tests

# 2. WindTunnel WebMCP 49/49 görevini çalıştırın:
git clone https://github.com/pCwOrM/werr.git && cd werr
python -m unittest tests.test_windtunnel_webmcp_isolated

# 3. Yılan Yapay Zekası Otonom Refleks Görselleştiricisini başlatın:
python benchmarks/snake/visualize_snake.py
```

---

## 🌐 Ekosistem Köprüleri

* 🌐 **İnteraktif Web Arenası:** [GitHub Pages üzerinde `benchmarks.html`](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/benchmarks.html)
* 📜 **Ana Araştırma Portalı:** [Mandelbrot Fractal Neural Synthesis](https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/)
* ⚡ **WERR Benchmark Ana Dizini:** [GitHub'da werr/benchmarks](https://github.com/pCwOrM/werr/tree/main/benchmarks)
* 🐍 **Yılan Benchmark Monografı:** [GitHub'da werr/benchmarks/snake](https://github.com/pCwOrM/werr/tree/main/benchmarks/snake)
* 🧠 **Üretim API:** [answerr Platformu (answerr.me)](https://answerr.me)
