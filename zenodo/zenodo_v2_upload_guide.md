# Zenodo Sürüm 2.0 (v2) Yükleme Kılavuzu (Adım Adım)

Bu kılavuz, **Mandelbrot Fractal Neural Synthesis** çalışmanızın Zenodo üzerindeki mevcut kaydını (**DOI: 10.5281/zenodo.22774935**) **Sürüm 2.0 (Version 2)** olarak güncellemeniz için hazırlanmıştır.

Masaüstünüzde yalnızca bu işlem için gereken 4 dosyanın yer aldığı temiz bir klasör oluşturuldu:
📂 **`C:\Users\maat\Desktop\ZENODO_V2_YUKLENECEKLER`**

---

## 📦 Yüklenecek 4 Temel Dosya

| # | Dosya Adı | Boyut | Açıklama |
|---|---|---|---|
| 1 | `Mandelbrot_Fractal_Neural_Synthesis_IEEE_Paper_EN.pdf` | ~977 KB | Q1 hakem revizyonlu, Algoritma 1 sözde kodlu, Quadtree ölçeklenebilirlikli ana İngilizce makale |
| 2 | `Mandelbrot_Fractal_Paper_arXiv_Bundle.zip` | ~731 KB | Tüm LaTeX kaynakları (`main.tex`, `references.bib`) ve yüksek çözünürlüklü vektör/PNG şekiller |
| 3 | `interactive_lab.html` | ~100 KB | Çift Dilli (TR / EN) Halk ve Kullanıcı Deneyimi Simülatörü |
| 4 | `quadrant_visualizer.html` | ~35 KB | Çift Dilli (TR / EN) 128x128 4-Çeyrek Araştırma Laboratuvarı |

---

## 📋 Adım Adım Yükleme Talimatı

### 1. Adım: Zenodo Kaydınıza Gidin
1. Tarayıcınızda şu adresi açın: **https://zenodo.org/records/22774935**
2. Sağ üst köşeden **"Log in"** &rarr; **"Log in with GitHub"** (`pCwOrM`) ile giriş yapın.

### 2. Adım: "New version" Butonuna Tıklayın
1. Makale sayfasının sağ üst panelinde yer alan turuncu **"New version"** butonuna tıklayın.
2. Zenodo, 1. sürümdeki tüm yazar, kurum ve lisans bilgilerini kopyalayarak otomatik bir **Taslak (Draft)** oluşturacaktır.

### 3. Adım: Dosyaları Güncelleyin (Files Bölümü)
1. Açılan taslak sayfada **"Files"** bölümünü bulun.
2. Eski sürümdeki dosyaları çöp kutusu simgesine tıklayarak silin.
3. Masaüstünüzdeki **`C:\Users\maat\Desktop\ZENODO_V2_YUKLENECEKLER`** klasöründe bulunan **4 dosyayı** sürükleyip bu alana bırakın.
4. Dosyaların yüklenmesinin tamamlandığından (yeşil tik) emin olun.

### 4. Adım: Temel Bilgileri Güncelleyin (Basic Info)
* **Digital Object Identifier (DOI):** Dokunmayın (Zenodo v2 için otomatik yeni sürüm DOI'si atayacaktır; ana Concept DOI'niz her iki sürümü de kapsar).
* **Publication date:** Bugünün tarihi (Örn: `2026-09-17`)
* **Title:**  
  `Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries`
* **Version:**  
  `2.0.0`
* **Language:**  
  `eng`
* **Description (Açıklama Kutusu):**  
  Aşağıdaki iki dilli metni kopyalayıp kutunun içine yapıştırın:

```markdown
# Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries

## What's New in Version 2.0 (Major Revision & Q1 Readiness)
- **Systems Trade-Off Framing:** Reframed the central research question from raw parameter fitting to fundamental systems architecture: trading deterministic local compute (O(M) escape iterations) for extreme memory footprint elimination (>99.99999998% reduction).
- **Formal Algorithmic Specification:** Added formal pseudocode (Algorithm 1: Coordinate-Space Evolutionary Synthesis) defining deterministic spatial exploration, quadrant area integration, and synaptic mapping.
- **Quadtree Tensor Scalability (Section IV-F):** Introduced multi-scale 2^p x 2^p recursive spatial partitioning and seed-offset generation to scale synthesis from single neurons to dense weight matrices (W in R^{d_out x d_in}).
- **Non-Linear Topological Context:** Grounded the non-linear XOR solution within Minsky & Papert's (1969) perceptron limitations.
- **Bilingual Standalone Labs (TR / EN):** Both interactive labs now feature client-side Turkish/English bilingual toggle switches with localStorage persistence.

---

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
4. **Müstakil Açık Kaynak Laboratuvarı:** Çalışma, hiçbir sunucuya veya harici kütüphaneye ihtiyaç duymadan internetsiz çalışan, Türkçe/İngilizce çift dilli interaktif web simülatörleriyle doğrulanmıştır.

Official GitHub Repository: https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis
Live Interactive Labs: https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/
License: Creative Commons Attribution 4.0 International (CC-BY-4.0)
```

### 5. Adım: Yazarları ve Bağlantıları Kontrol Edin
* **Creators:** 
  1. `Dağlı, Volkan` (ITouch Systems, Turkey)
  2. `Dağlı, Zerrin` (Mersin University, Mersin, Turkey) - ORCID: `0000-0001-9490-6465`
  3. `Dağlı, Dağhan` (Toros Science College, Turkey)
* **License:** `Creative Commons Attribution 4.0 International` (CC-BY-4.0)
* **Related identifiers:** 
  - `https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis` (isSupplementTo)

### 6. Adım: Yayınlayın (Publish)
1. Sayfanın en üstündeki veya altındaki mavi **"Publish"** butonuna tıklayın.
2. Açılan onay kutusuna onay verin.

🎉 **Tebrikler!** Zenodo Version 2.0 yayına girmiş olacaktır. Ana DOI'niz her zaman en son sürüme yönlendirecektir.
