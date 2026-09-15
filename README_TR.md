# Fraktal Nöron Sentezi: Mandelbrot Geometrisinden Sıfır-Bellekli Ağırlık ve Karar Türetimi

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.beklemede-blue.svg)](https://zenodo.org/)
[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](./LICENSE)
[![Yayın: Zenodo / arXiv](https://img.shields.io/badge/Yayın-Zenodo%20%2F%20arXiv%20Preprint-green.svg)](#)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![İnteraktif Laboratuvar](https://img.shields.io/badge/İnteraktif%20Laboratuvar-Sunucusuz%20%26%20Çevrimdışı-purple.svg)](./demos/)

> 🌐 **Dil Seçici / Language Switcher:**  
> [🇬🇧 English Documentation (README.md)](README.md) | **Türkçe (Aktif)**

---

## 👥 Yazarlar ve Akademik Kurumlar

* **Volkan Dağlı** *(Sorumlu Yazar / Corresponding Author)*  
  ITouch Systems, Türkiye &bull; Zenodo: [`@itouch`](https://zenodo.org/)

* **Zerrin Dağlı**  
  Mersin Üniversitesi, Mersin, Türkiye &bull; ORCID: [0000-0001-9490-6465](https://orcid.org/0000-0001-9490-6465) &bull; Zenodo: [`@zdagli`](https://zenodo.org/)

*İletişim & Yazışma:* Resmi GitHub araştırma deposu üzerinden yürütülmektedir.

---

## 📌 Yönetici Özeti (Executive Summary)

Günümüz derin öğrenme sistemleri (örneğin ChatGPT gibi Büyük Dil Modelleri), milyarlarca ve trilyonlarca parametreyi bellek çiplerinde (GPU VRAM) bağımsız sayılar olarak saklamak zorundadır. Örneğin 70 milyar parametreli bir model, yalnızca ağırlıklarını bellekte tutabilmek için $\sim 140$ GB yüksek hızlı VRAM tüketir. Bu durum devasa bir bellek bant genişliği darboğazına (*Memory Wall*) ve muazzam enerji israfına yol açar.

Bu araştırma, bu soruna radikal ve doğadan ilham alan bir alternatif sunar: **Yapay sinir ağı ağırlıklarını ve eşik değerlerini bellekte hiç saklamadan, deterministik Mandelbrot fraktal kümesinin ($\mathcal{M}$) görsel morfolojisinden ihtiyaç anında canlı türetmek.**

Karmaşık düzlemdeki üç parametreli bir koordinat penceresi $\Theta = (c_x, c_y, \text{zoom})$ seçilerek, klasik kuadratik kaçış denklemi ($z_{n+1} = z_n^2 + c$) üzerinden $128 \times 128$ piksellik bir fraktal pencere taranır. Geliştirdiğimiz **4-Quadrant (Dört Çeyrek) Bölümleme Metodu** ile, pencerenin dört köşesindeki siyah adacık (ıraksamayan kararlı alan) oranları doğrudan sinir hücresinin ağırlıklarına ($w_1, w_2, w_3$) ve sapma (bias) değerine dönüştürülür.

### Temel Bilimsel Başarılar:
1. **$128 \times 128$ Çözünürlük Standardı:** $32 \times 32$'deki pikselleşme gürültüsünü yok ederek $256 \times 256$ çözünürlüğün kararlılığını $\%0.08$ farkla yakalamış ve **15 kat daha hızlı** ($\approx 15.6$ ms) çalışmıştır.
2. **%100 Mantık Kapısı Başarısı:** Tüm temel doğrusal mantık kapıları (AND, OR, NAND, NOR) %100 sınıflandırma doğruluğuyla çözülmüştür.
3. **Doğrusal Olmayan XOR Çözümü:** 1969'da Minsky ve Papert'in *"tek katmanlı yapay zeka bunu çözemez"* dediği ünlü XOR problemi, iki katmanlı kompozit fraktal ağımızla **%100 doğrulukla** çözülmüş ve pürüzsüz 2D karar yüzeyi elde edilmiştir.
4. **24-Bayt Sıfır-Bellek Modeli:** Kalıcı tensör matrisi boyutu **0 Byte**'tır! Fonksiyonel bir karar hücresi yalnızca **24 baytlık** (üç adet Float64 koordinat) bir kütükle tanımlanmakta; geleneksel modellere kıyasla **%99.99999998+ bellek tasarrufu** sağlamaktadır.
5. **Kaçış Ufku ve Hata Kümesi İlkesi:** İnsanın çekiç vururken parmağına 1-2 kez vurup canı yandığında hata sınırını kilitleyerek 1000 yerine 300 adımda öğrenmesi gibi; Mandelbrot'un matematiksel kaçış sınırı $\partial \mathcal{M}$ de yapay nörona en keskin karar eşiğini doğal olarak sunar.

---

## 📊 Kıyaslama Tablosu: Klasik LLM vs. Fraktal Sentez Modelimiz

| Boyut | Standart Derin Öğrenme (LLM) | Fraktal Nöron Sentez Modelimiz |
| :--- | :--- | :--- |
| **Parametre Saklama Modeli** | Statik Ağırlık Matrisi (RAM / VRAM) | **Sonsuz Geometriden Canlı Türetim** |
| **Karar Hücresi Başına Bellek** | 12 - 64 Byte (Tensör Ağırlıkları) | **Yalnızca 24 Byte $(c_x, c_y, \text{zoom})$** |
| **Kalıcı Ağırlık Matrisi** | Milyarlarca Float16 / Float32 değeri | **0 Byte (Hiçbir matris diske yazılmaz!)** |
| **70B Eşdeğer Model İzi** | $\sim 140$ GB VRAM (Memory Wall Sınırı) | **Kompakt Koordinat Dizisi** |
| **Bellek Tasarrufu** | Referans (%0) | **%99.99999998+ Tasarruf** |
| **Gelecek Donanım İmkânı** | Isınan GPU'lar, dev santraller | **Fotonik / Optik Çiplerle $< 1$ ns, sıfır elektrik** |

---

## 📂 Depo Mimarisi

```text
mandelbrot-fractal-neural-synthesis/
│
├── README.md                           # Ana İngilizce Dokümantasyon
├── README_TR.md                        # Kapsamlı Türkçe Dokümantasyon (Bu Dosya)
├── LICENSE                             # MIT Açık Kaynak Lisansı
├── requirements.txt                    # Minimal Python Bağımlılıkları
├── .zenodo.json                        # Zenodo Otomatik Metadata Standardı
├── .gitignore                          # Sürüm Kontrol Filtresi
│
├── src/                                # Temel Araştırma & Simülasyon Kodları
│   ├── mandelbrot_core.py              # 128x128 tarama ve karanlık alan integrali
│   ├── fractal_neuron.py               # Tek nöronlu mantık kapısı çözücü
│   ├── xor_composite_network.py        # 2 katmanlı kompozit XOR ağı
│   ├── gate_optimizer.py               # Rastgele yürüyüşlü koordinat arama motoru
│   └── benchmark_resolutions.py        # 32x32 - 256x256 Pareto başarım analizi
│
├── demos/                              # İnteraktif Web Laboratuvarları (%100 Çevrimdışı & Bağımsız)
│   ├── interactive_lab.html            # Senaryo arayüzü (Akıllı Kapı, Kasa, Lamba, Alarm)
│   └── quadrant_visualizer.html        # İlk geliştirilen 128x128 teknik 4-çeyrek araştırma widget'ı
│
├── zenodo/                             # Resmi Zenodo Açık Bilim Yayın Paketi
│   ├── .zenodo.json                    # Zenodo metadata şablonu
│   ├── zenodo_deposit_guide.md         # 5 dakikada Zenodo yükleme ve kalıcı DOI rehberi
│   └── Mandelbrot_Fractal_Neural_Synthesis_Preprint.pdf # Baskıya hazır makale (Türkçe Özetli)
│
├── arxiv/                              # arXiv / Overleaf LaTeX Kaynak Paketi
│   ├── main.tex                        # IEEE formatında makale kaynak kodu
│   ├── references.bib                  # BibTeX kaynakçası
│   ├── figures/                        # 6 adet yüksek çözünürlüklü makale şekli
│   └── Mandelbrot_Fractal_Paper_arXiv_Bundle.zip # Tek tıkla yükleme paketi
│
├── docs/                               # Halka Anlatım & Monograf Belgeleri
│   ├── Halka_Anlatim_Rehberi.html      # Halka sunum rehberi web arayüzü
│   ├── Halka_Anlatim_Rehberi.pdf       # Yazdırılabilir A4 sunum rehberi (PDF)
│   ├── halka_anlatim_rehberi.md        # Sunum rehberi metin kaynağı
│   ├── Mandelbrot_Akademik_Teknik_Raporu.html # Geniş akademik teknik monograf
│   └── Mandelbrot_Akademik_Teknik_Raporu.pdf  # A4 formatında monograf PDF'i
│
└── figures/                            # Yayın Şekilleri
    ├── quadrant_weights_128.png        # 4-Quadrant şematik gösterimi
    ├── resolution_comparison_128.png   # Çözünürlük başarım eğrileri
    ├── gate_solutions_128.png          # OR, AND, NAND, NOR karar düzlemleri
    ├── xor_complete_network_128.png    # 2 katmanlı kompozit XOR ağı
    ├── zoom_weight_curve.png           # Zoom ile sürekli ağırlık modülasyonu
    └── mandelbrot_patches.png          # Fraktal morfoloji örnekleme pencereleri
```

---

## 🎮 İnteraktif Laboratuvarlar (Sıfır Bağımlılık)

Depoda, hiçbir sunucu kurulumu gerektirmeden, internetsiz ortamda doğrudan çift tıklanarak çalışan **iki bağımsız görsel simülatör** yer alır:

1. **Halka Açık Deneyim Laboratuvarı (`demos/interactive_lab.html`):**
   * 4 gerçek hayat senaryosu: 🚪 Akıllı Kapı (OR), 🏦 Banka Kasası (AND), 💡 Merdiven Lambası (XOR), 🚨 Yangın Alarmı (NAND).
   * Biyolojik nöron çizimi ve canlı akson ateşleme animasyonu.
   * ☀️ Açık Mod / 🌙 Koyu Mod değiştirici.
   * Tek tıkla 24 baytlık `.TXT` hafıza kütüğü indirme.
2. **Teknik 4-Quadrant Araştırma Widget'ı (`demos/quadrant_visualizer.html`):**
   * Canlı $128 \times 128$ Mandelbrot tuvali ve hassas Zoom kaydırıcısı.
   * 4 çeyrek ($Q_1 	o w_1, Q_2 	o w_2, Q_3 	o w_3, Q_4 	o b$) canlı katsayı panelleri.
   * Anlık doğruluk tablosu hesabı ($\hat{y} = \sigma(w_1 x_1 + w_2 x_2 + b)$).

---

## 🚀 Hızlı Başlangıç & Deneyleri Tekrarlama

```bash
# Depoyu klonlayın
git clone https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis.git
cd mandelbrot-fractal-neural-synthesis

# Gerekli minimal kütüphaneleri yükleyin
pip install -r requirements.txt

# Mantık kapıları deneyini çalıştırın
python src/fractal_neuron.py

# 2 katmanlı XOR ağını çalıştırın
python src/xor_composite_network.py

# İnteraktif arayüzü doğrudan tarayıcınızda açın (Sunucu gerekmez!)
start demos/interactive_lab.html
```

---

## 📖 Atıf (Citation)

Bu araştırmayı çalışmalarınızda kullanmak veya atıfta bulunmak için:

```bibtex
@article{dagli2026fractal,
  title={Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries},
  author={Da{\u{g}}l{\i}, Volkan and Da{\u{g}}l{\i}, Zerrin and Da{\u{g}}l{\i}, Da{\u{g}}han},
  journal={Zenodo / arXiv Preprint},
  year={2026},
  doi={10.5281/zenodo.beklemede},
  url={https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis}
}
```

---

## 📜 Lisans
Bu araştırma ve kod tabanı [MIT Lisansı](LICENSE) kapsamında açık kaynak olarak sunulmuştur.
