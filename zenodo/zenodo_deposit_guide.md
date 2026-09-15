# Zenodo Yayınlama & Kalıcı DOI Alma Rehberi (Step-by-Step Zenodo Deposit Guide)

Bu rehber, **Mandelbrot Fractal Neural Synthesis** çalışmanızı CERN destekli uluslararası açık bilim platformu **Zenodo**'ya yükleyerek anında kalıcı bir **DOI (Digital Object Identifier)** numarası almanız için hazırlanmıştır.

---

## 🌟 Neden Zenodo?
* **Anında Kalıcı DOI:** arXiv onay/endorsement sürecini beklemeden dakikalar içinde resmi, taranabilir ve atıf alabilir bir DOI (örn: `10.5281/zenodo.xxxxxxx`) üretir.
* **Uluslararası İndekslenme:** DataCite, OpenAIRE, Google Scholar ve uluslararası akademik veritabanları tarafından otomatik taranır.
* **YÖK ve TÜBİTAK Uyumluluğu:** Akademik teşvik, doçentlik ve akademik jüriler için geçerli uluslararası preprint / teknik rapor kaydı oluşturur.
* **GitHub Entegrasyonu:** Deponuzdaki `.zenodo.json` dosyası sayesinde tüm yazarlar, ORCID numaraları ve kurumlar tek tıkla otomatik doldurulur.

---

## 📋 5 Dakikada Zenodo'ya Yükleme Adımları

### 1. Adım: Giriş Yapın
1. [zenodo.org](https://zenodo.org/) adresine gidin.
2. Sağ üstteki **"Log in"** butonuna tıklayın.
3. **"Log in with GitHub"** seçeneğini seçin (Antigravity'de bağlı olan `pCwOrM` GitHub hesabınızla doğrudan tek tıkla giriş yapabilirsiniz).

### 2. Adım: Yeni Kayıt (New Upload) Başlatın
1. Üst menüdeki yeşil **"New upload"** butonuna tıklayın.
2. Açılan sayfadaki **"Files"** bölümüne şu 4 dosyayı sürükleyip bırakın:
   * 📄 `zenodo/Mandelbrot_Fractal_Neural_Synthesis_Preprint.pdf` (Nihai Akademik Makale - Önizleme için ana dosya)
   * 📦 `arxiv/Mandelbrot_Fractal_Paper_arXiv_Bundle.zip` (Tüm LaTeX Kaynakları & Şekiller)
   * 🌐 `demos/interactive_lab.html` (Müstakil İnteraktif Senaryo Laboratuvarı)
   * 🌐 `demos/quadrant_visualizer.html` (Teknik 128x128 4-Çeyrek Araştırma Widget'ı)

### 3. Adım: Temel Bilgileri Doldurun (Otomatik Bilgiler)
* **Resource type:** `Publication` → `Preprint` (veya `Technical note`)
* **Title:**  
  `Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries`
* **Authors (Yazarlar - Zenodo'da Dr. gibi unvanlar yazılmaz, Family name / Given names ayrı kutulardır):**
  1. Family name: `Dağlı`, Given names: `Volkan` • Affiliation: `ITouch Systems, Turkey`
  2. Family name: `Dağlı`, Given names: `Zerrin` • Affiliation: `Mersin University, Mersin, Turkey` • ORCID: `0000-0001-9490-6465`
* **Description (Açıklama):**  
  Aşağıdaki iki dilli metni (İngilizce + Genişletilmiş Türkçe Özet) tek parça halinde Description kutusuna kopyalayıp yapıştırın.

---

### 4. Adım: Description Alanına Yapıştırılacak Metin (İki Dilli)

```markdown
# Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries

## English Abstract
Modern deep learning architectures store billions or trillions of parameters as independent floating-point scalars across dense tensor arrays, trained via backpropagation. While exceptionally capable, this paradigm incurs severe storage footprints, memory bandwidth bottlenecks ("the memory wall"), and excessive energy consumption. 

In this work, we propose and empirically validate an alternative weight generation paradigm: deriving synaptic weights and threshold biases procedurally from the non-linear visual morphology of the Mandelbrot fractal set. By specifying a 3-parameter coordinate tuple (cx, cy, zoom) in the complex plane, a 128x128 pixel patch is sampled via the quadratic escape recurrence z = z^2 + c. Using our 4-Quadrant Partitioning method, non-escaping dark areas directly determine synaptic weights and biases.

Key Results:
1. 128x128 resolution eliminates discretization noise within 0.08% of 256x256 while executing 15x faster (~15.6 ms).
2. All fundamental linear logic gates (AND, OR, NAND, NOR) achieved 100% accuracy.
3. The historically non-linear XOR problem was resolved with 100% accuracy using a 2-layer composite fractal network.
4. An entire functional decision cell requires ZERO persistent weight tensors, retaining only 24 bytes of coordinate metadata, yielding >99.99999998% memory reduction compared to conventional weight arrays.
5. The "Escape Horizon Principle" links biological motor error boundaries (e.g., mastering hammering or balance via catastrophic edge feedback) to the topological boundary of the Mandelbrot set.

---

## Genişletilmiş Türkçe Özet (Extended Turkish Abstract)
Bu çalışma, derin öğrenme modellerinde milyonlarca parametreyi bellek çiplerinde statik sayılar olarak saklamak yerine; deterministik kaosun ve fraktal geometrinin en bilinen örneği olan Mandelbrot kümesinden (z = z^2 + c) ihtiyaç anında canlı türeten yeni bir yapay zeka paradigmasını teorik ve deneysel olarak kanıtlamaktadır.

Temel Bulgular ve Yenilikler:
1. **24-Bayt Sıfır-Bellek Modeli:** Bir karar hücresi için hiçbir tensör matrisi saklanmaz. Yalnızca 24 baytlık (üç Float64 koordinat: cx, cy, zoom) bir konum tutularak %99.99999998+ bellek tasarrufu sağlanır.
2. **Hata Kümesi ve Kaçış Ufku İlkesi:** İnsanın çekiç vururken eline 1-2 kez vurup canı yandığında hata sınırını kilitleyerek 1000 yerine 300 adımda öğrenmesi gibi; Mandelbrot'un matematiksel kaçış sınırı da yapay nörona en keskin karar eşiğini doğal olarak sunar.
3. **%100 Doğruluk:** OR, AND, NAND, NOR kapıları tek nöronla; yapay zeka tarihinde tek nöronun çözemediği ünlü XOR problemi ise 2 katmanlı kompozit fraktal ağımızla %100 doğrulukla çözülmüştür.
4. **Müstakil Açık Kaynak Laboratuvarı:** Çalışma, hiçbir sunucuya veya harici kütüphaneye ihtiyaç duymadan internetsiz ortamda çalışan interaktif bir web simülatörüyle doğrulanmıştır.

Official GitHub Repository: https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis
License: MIT / CC-BY-4.0
```

---

### 5. Adım: Yayınlayın (Publish)
1. Sayfanın en altındaki **"Publish"** butonuna basın.
2. Zenodo size anında **`10.5281/zenodo.xxxxxxx`** formatında resmi bir DOI atayacaktır!
3. Bu DOI'yi CV'nize, GitHub README dosyanıza ve makale atıflarınıza ekleyebilirsiniz.
