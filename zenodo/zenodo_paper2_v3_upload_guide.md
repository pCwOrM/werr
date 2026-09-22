# Zenodo Sürüm 3.0 (v3.0) Yükleme Kılavuzu (Paper 2 - OED)

Bu kılavuz, **Orbital Error Dynamics (OED)** çalışmanızın Zenodo üzerindeki kaydını (**Concept DOI: 10.5281/zenodo.22896855**) **Sürüm 3.0 (Version 3.0)** olarak güncellemeniz için hazırlanmıştır.

Masaüstünüzde yükleme için hazır temiz klasör oluşturuldu:  
📂 **`C:\Users\maat\Desktop\ZENODO_PAPER2_V3_YUKLEME`**

---

## 📦 Yüklenecek 2 Temel Dosya

| # | Dosya Adı | Boyut | Açıklama |
|---|---|---|---|
| 1 | `Orbital_Error_Dynamics_Preprint.pdf` | ~2.33 MB | **Tam 7 Sayfa**, sıfır etiket sızıntılı, Student-$t$ güven aralıklı, Li et al. (2018) / Ha et al. (2017) / Chen et al. (2015) literatür karşılaştırmalı, TÜRKPATENT TR 2026/016285 patent bildirimli ana preprint. |
| 2 | `zenodo_bundle_orbital_error_dynamics.zip` | ~4.29 MB | Tam LaTeX kaynakları (`main.tex`, `references.bib`), 300 DPI 7 adet orijinal yayın figürü ve %100 tekrarlanabilir bağımsız Python simülasyon kodu (`simulate_oed_rigorous.py`). |

---

## 📋 Adım Adım Yükleme Talimatı

### 1. Adım: Zenodo Kaydınıza Gidin
1. Tarayıcınızda Zenodo'yu açın: **https://zenodo.org**
2. Sağ üstten **"Log in"** &rarr; **"Log in with GitHub"** (`pCwOrM`) ile giriş yapın.
3. Profilinizden **"My dashboard"** veya doğrudan Paper 2 kaydınıza gidin (Concept DOI: `10.5281/zenodo.22896855`).

### 2. Adım: "New version" Butonuna Tıklayın
1. Sayfanın sağ üst panelinde yer alan turuncu **"New version"** butonuna tıklayın.
2. Zenodo otomatik olarak v3 için yeni bir **Taslak (Draft)** oluşturacaktır.

### 3. Adım: Dosyaları Güncelleyin (Files Bölümü)
1. **"Files"** bölümüne gelin.
2. Önceki sürümden kalan eski dosyaları çöp kutusu simgesine tıklayarak silin.
3. Masaüstünüzdeki **`C:\Users\maat\Desktop\ZENODO_PAPER2_V3_YUKLEME`** klasöründe bulunan **2 dosyayı** sürükleyip bu alana bırakın:
   - `Orbital_Error_Dynamics_Preprint.pdf`
   - `zenodo_bundle_orbital_error_dynamics.zip`
4. Yüklemenin tamamlandığını (yeşil tik) görün.

### 4. Adım: Temel Bilgileri Güncelleyin (Basic Info)

* **Publication date:** `2026-09-22`
* **Title:**  
  `Orbital Error Dynamics: Self-Organized Criticality, Ephemeral Parameter Resonance, and Non-Linear Biological Ontologies in Zero-Storage Neural Synthesis`
* **Version:**  
  `3.0.0`
* **Language:**  
  `eng`
* **Description (Açıklama Kutusu):**  
  Aşağıdaki HTML metnini kopyalayıp Zenodo açıklama kutusuna yapıştırın:

```html
<p><b>Abstract</b> &mdash; Modern deep artificial neural networks treat parameters as static, unconstrained floating-point scalar matrices stored permanently in physical memory and optimized through empirical loss minimization (<i>L</i> &rarr; 0). While computationally powerful, this classical paradigm incurs severe Von Neumann memory bandwidth bottlenecks, thermodynamic inefficiencies, and representation collapse. In this work, we propose a foundational theoretical paradigm shift: <i>Existence is an active set of non-vanishing errors (&Escr;)</i>, and biological intelligence is an ongoing, non-equilibrium resistance against dynamic attractor collapse rather than passive convergence to zero loss.</p>

<p>Building upon our initial procedural framework, we formulate <b>Orbital Error Dynamics (OED)</b>, an analytical framework wherein synaptic weights are not stored masses (<i>O</i>(<i>W</i>)), but transient topological resonances (<i>O</i>(1)) sampled dynamically from the complex quadratic polynomial map <i>z</i><sub><i>n</i>+1</sub> = <i>z</i><sub><i>n</i></sub><sup>2</sup> + <i>c</i>. We introduce the <b>Bent Sine Wave Hypothesis</b>, demonstrating that while unperturbed linear waves are static and harmonic waves are repetitively conservative, living non-equilibrium systems emerge when waves curl inward through environmental drag toward the main cardioid cusp (<i>c</i> = 1/4). We analyze the <b>Observer Horizon Geometry</b> in parameter space, identifying sub-boundary interior resonance shoulder loci <b>X</b><sub>upper</sub> = (0.25, +0.18) and <b>X</b><sub>lower</sub> = (0.25, -0.18) positioned between the central fixed-point basin and the true analytic boundary at <i>c</i> = 0.25 &plusmn; 0.50<i>i</i>, surveying radiant uncommitted potential fields while anchored to somatic dissipation axes.</p>

<p>To overcome non-convex stagnation without loss zeroing, we formalize a <b>Biomimetic Perturbed Jump Operator (&Omega;<sub>tunneling</sub>)</b> inspired by mammalian fertilization zinc sparks. We further formulate an enteric-cranial <b>Dual-Brain Cybernetic Architecture</b> incorporating adaptive CD4+ regulatory immune gating masks (<i>M</i><sub>CD4</sub>) for streaming noise stabilization, and decompose the 4-nucleotide genetic basis (<i>A, T, C, G</i>) directly across the quadrants of the complex plane (&Copf;). Finally, multi-seed empirical validation on the non-linear Two-Moons manifold (5 seeds, 80/20 train/test split, consistent 32 &times; 32 sampling grid, zero test-time updates and zero label leakage) demonstrates that procedural parameterization from a 24-byte seed achieves 77.67% &plusmn; 5.35% clean test accuracy (within an 8.00-point paired difference of an unconstrained gradient-descent baseline at 85.67% &plusmn; 5.35%, 95% CI of paired difference: [-1.07%, 17.07%]), while under distribution shift (&Nscr;(1.2, 0.4)), OED preserves 71.33% &plusmn; 3.80% test accuracy compared to 80.33% &plusmn; 7.21% for the baseline, alongside conceptual equivalence with a proposed analog optical co-processor theoretically modeled for sub-nanosecond evaluation.</p>

<p><b>Version 3.0 Revision Notes (Methodological Rigor & Prior Art Integration):</b> This revised preprint incorporates comprehensive peer and community review feedback: (1) <i>Zero Label Leakage Protocol:</i> Test evaluations are conducted in 100% pure feedforward inference with zero test-time gradient steps and zero label access; (2) <i>Consistent Grid Resolution:</i> Standardized sampling resolution to a uniform 32&times;32 grid across training and evaluation; (3) <i>Finite Difference Step & Gradient Dynamics:</i> Verified &delta; = 0.02 traversing discrete pixel boundaries, achieving 0.0% zero-gradient epochs (0/250) and 0.0% Zinc Spark invocations with T = 50 epochs; (4) <i>Rigorous Statistical Reporting:</i> Exact Student-t distributions for N=5 (t_4 = 2.776), paired differences and 95% Confidence Intervals reported for both clean and distribution shift regimes; (5) <i>Literature & Prior Art Integration:</i> Contextualized against intrinsic dimension projections (Li et al., 2018), HyperNetworks (Ha et al., 2017), and HashedNets (Chen et al., 2015), substantiating the distinct O(1) non-linear dynamical formulation and patent claims (TR 2026/016285); and (6) <i>Clarified CD4+ Immune Gating:</i> Formulated as an active cybernetic defense mechanism for online streaming data against anomalous sensory shocks.</p>

<p><b>🏛️ Official Patent Priority Notice:</b><br>
The procedural weight derivation architectures, the adaptive CD4+ immune gating mask mechanism, and the zero-storage hardware co-processor implementations disclosed in this record and associated preprint files are subject to an official national priority patent application:<br>
• <b>Patent Office:</b> Turkish Patent and Trademark Office (TÜRKPATENT)<br>
• <b>Application Number:</b> 2026/016285<br>
• <b>Official Priority Timestamp:</b> September 22, 2026 (14:42:15 UTC+3)<br>
• <b>Applicant:</b> Volkan Dağlı<br>
• <b>Inventors:</b> Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı<br>
• <b>Official Repository:</b> <a href="https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis">https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis</a></p>
```

### 5. Adım: Ek Alanları Kontrol Edin
* **Creators:**
  1. `Dağlı, Volkan` (Anadolu University & ITouch Systems) — ORCID: `0009-0000-1587-8703`
  2. `Dağlı, Zerrin` (Mersin University) — ORCID: `0000-0001-9490-6425`
  3. `Dağlı, Dağhan` (Toros Science College) — ORCID: `0009-0003-2492-8313`
* **Keywords:**
  `Orbital Error Dynamics`, `Mandelbrot Fractal Neural Synthesis`, `Zero-Storage AI`, `Self-Organized Criticality`, `Non-Equilibrium Thermodynamics`, `Perturbed Gradient Descent`, `Zinc Spark`, `Enteric Cybernetics`, `CD4+ Immune Gating`, `Non-Linear Manifolds`, `Complex Dynamics`
* **License:** `Creative Commons Attribution 4.0 International` (CC-BY-4.0)

### 6. Adım: Yayınlayın (Publish)
1. Sayfanın en altındaki mavi **"Publish"** butonuna tıklayın.
2. Açılan modal onay kutusunda **"Publish"** diyerek yayını tamamlayın.
