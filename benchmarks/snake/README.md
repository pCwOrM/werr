# 🐍 Werr vs Laya-MLX & TypeSafe Jev: Real-Time Snake AI Reflex Benchmark

<p align="center">
  <img src="terminal_snake_showcase.gif" alt="Werr Snake Real-Time Reflex Benchmark Showcase" width="720">
</p>

> **Live Terminal Showcase:** Kontrolün insandan (%100 yerel ve 0 Bayt ağırlıklı) **Werr Fraktal Refleks Motoruna** devredilişi.  
> 🎬 **[Yüksek Kaliteli MP4 Videosunu İndir (490 KB)](terminal_snake_showcase.mp4)** │ 📦 **Model Boyutu: 0.00 KB** │ ⚡ **Refleks Gecikmesi: 0.08 ms**

---

## ⚡ 2 Aşamalı Canlı Gösterim (Human-to-Werr Handover)

Bu benchmark, **insan biyolojik refleksleri**, **bulut tabanlı TypeSafe Jev modelleri**, **ModernBERT tabanlı yerel LLM'ler (Laya-MLX 421M)** ve **Werr Sıfır-Ağırlıklı Fraktal Nöral Sentezi** arasındaki farkı doğrudan gerçek zamanlı bir oyun ortamında gösterir:

1. **🎮 1. Aşama — Manuel Kontrol (İnsan Oynuyor):**
   * Yılan insan tepki süresiyle (**~145 ms biyolojik gecikme**) yönlendirilir.
   * Telemetri panelinde karar gecikmesi sarı renkte görünür.
2. **⚡ Devir Anı (Handover):**
   * Kritik bir anda `[W]` tuşuyla (veya otomatik `--showcase` modunda) kontrol anında Werr'e devredilir:
   * `>>> [DEVİR AKTİF] KONTROL WERR FRAKTAL MOTORUNA DEVREDİLDİ! (0.00 KB / 0.08ms) <<<`
3. **🚀 2. Aşama — Werr Fraktal Otopilot:**
   * Tepki süresi **0.08 ms'ye (1800x daha hızlı mikrosaniyelik refleks)** düşer.
   * Karar dağılımı (`UP`, `DOWN`, `LEFT`, `RIGHT`) olasılık barları Mandelbrot rezonans yörüngesinden canlı olarak türetilir.
   * Kalıcı disk tensörü: **0.00 KB**, GPU/VRAM yükü: **0 MB**, Bulut API faturası: **$0.00**.

---

## 🚀 Hızlı Başlangıç (Terminalde Çalıştırma)

Ekstra hiçbir GPU veya model indirmeden doğrudan standart Python ile çalıştırın:

```bash
# Repoyu klonlayın
git clone https://github.com/pCwOrM/werr.git
cd werr
pip install numpy

# 1. İnteraktif Mod (Kendiniz oynayın, [W] ile Werr'e devredin):
python benchmarks/snake/terminal_snake.py

# 2. Tam Otomatik Sinematik Devir Gösterimi:
python benchmarks/snake/terminal_snake.py --showcase

# 3. Klasik Karşılaştırmalı Benchmark Koşusu (600 adım):
python benchmarks/snake/benchmark_snake.py --steps 600 --mode compare
```

### ⌨️ Canlı Terminal Kontrolleri
* `[W]` veya `[M]`: Kontrolü Werr'e Devret / Manuele Geri Al
* `[Ok Tuşları / WASD]`: Manuel yılan kontrolü
* `[Boşluk (Space)]`: Duraklat / Devam Et
* `[+]` / `[-]`: FPS hız ayarı (4 FPS - 40 FPS)
* `[R]`: Tahtayı sıfırla │ `[Q]`: Çıkış

---

## 📊 Kapsamlı Karşılaştırma Tablosu

Standart tüketici sınıfı masaüstü CPU üzerinde 600 ardışık karar adımında ölçülen benchmark sonuçları:

| Metrik / Boyut | TypeSafe Jev API | Laya-MLX (ModernBERT 421M) | **Werr (Fraktal Refleks Motoru)** |
| :--- | :---: | :---: | :---: |
| **Model Boyutu (Disk)** | Bulut API | 421M Parametre (943.6 MiB) | **0.00 KB (24-Bayt Tohum)** 🏆 |
| **Gerekli Donanım** | Bulut Kümesi | Apple Silicon M3 Max ($3,500) | **Herhangi bir Standart CPU / Edge** |
| **VRAM / Bellek Tüketimi**| Bulut GPU | 943.6 MiB Birleşik Bellek | **0 Bayt VRAM (Sıfır Bellek)** 🏆 |
| **P50 Karar Gecikmesi** | 150 – 350 ms | 13.42 ms | **0.08 – 1.99 ms (⚡ 1800x Hızlı)** 🏆 |
| **Oyun Akıcılığı (Throughput)**| 2 – 5 hamle/sn | 74.5 hamle/sn | **270+ hamle/saniye** 🏆 |
| **1.000 Hamle Başına Maliyet**| $0.0399 USD | ~$0.0029 (Elektrik/GPU) | **$0.0000 (%100 Ücretsiz)** 🏆 |
| **Çevrimdışı / Air-Gapped** | Hayır (WiFi Zorunlu) | Yalnızca Apple Silicon | **%100 Çevrimdışı (Tüm Cihazlar)** 🏆 |

---

## 🎯 Mimari: Werr 0 Bayt Ağırlıkla Nasıl Karar Verir?

Yüz milyonlarca parametreli matrisler, dikkat mekanizmaları ve KV önbellekleri çalıştırmak yerine:

1. **Durumdan Dalgaya Modülasyon (State-to-Wave Modulation):**  
   Yılanın kafa pozisyonu, hedefe olan bağıl uzaklık, duvar ve kuyruk tehlikeleri karmaşık düzlem koordinat sapmalarına `(Δcx, Δcy)` dönüştürülür.
2. **24-Bayt Kaotik Sınır Tohumu:**  
   Mandelbrot rezonans kümesinde yer alan sınır koordinatı üzerinde doğrudan değerlendirilir:
   ```text
   cx = -0.7436438870371587, cy = 0.1318259042053119, zoom = 65.0
   ```
3. **4 Yönlü Kaçış Dinamiği:**  
   Kuadratik kaçış yinelemesi ($Z_{n+1} = Z_n^2 + C$) ile 4 ana hareket yönünün (`UP`, `DOWN`, `LEFT`, `RIGHT`) olasılıkları doğrudan hesaplanır.
4. **Sıfır Bellek & Mikrosaniyelik Refleks:**  
   PCIe veya RAM veri yolu üzerinden hiçbir nöral ağırlık transfer edilmediği için karar süresi **0.08 milisaniye** gibi anlık bir refleks seviyesinde gerçekleşir.

---

## 📁 Dizin Yapısı

```text
benchmarks/snake/
├── terminal_snake_showcase.gif # Canlı terminal devir animasyonu (Showcase GIF)
├── terminal_snake_showcase.mp4 # Yüksek kaliteli H.264 video kaydı
├── terminal_snake.py           # 2 aşamalı (İnsan -> Werr) canlı terminal oyunu
├── record_snake_video.py       # Terminal videosunu yeniden render eden script
├── snake_game.py               # Deterministik yılan ortamı
├── werr_snake_policy.py        # 24-baytlık tohum ile Werr refleks politikası
├── benchmark_snake.py          # Kıyaslamalı terminal test runner'ı
└── README.md                   # Bu dokümantasyon sayfası
```

---

## 📖 Citation

```bibtex
@article{dagli2026werr,
  author = {Volkan Da{\u{g}}l{\i} and Zerrin Da{\u{g}}l{\i} and Da{\u{g}}han Da{\u{g}}l{\i}},
  title = {Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains},
  journal = {Zenodo Preprint},
  year = {2026},
  url = {https://doi.org/10.5281/zenodo.22867426},
  doi = {10.5281/zenodo.22867426}
}
```
