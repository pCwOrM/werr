import os
import shutil
import zipfile

BASE_DIR = r"c:\Users\maat\Documents\antigravity\wevv"
PAPER_DIR = os.path.join(BASE_DIR, "paper")
FIGURES_DIR = os.path.join(PAPER_DIR, "figures")

DESKTOP_DIR = r"C:\Users\maat\Desktop"
ZENODO_PKG_DIR = os.path.join(DESKTOP_DIR, "ZENODO_WERR_YUKLEME_PAKETI")
ARXIV_PKG_DIR = os.path.join(DESKTOP_DIR, "ARXIV_WERR_YUKLEME_PAKETI")

os.makedirs(ZENODO_PKG_DIR, exist_ok=True)
os.makedirs(ARXIV_PKG_DIR, exist_ok=True)

# 1. Create arXiv Bundle ZIP
arxiv_zip_path = os.path.join(ARXIV_PKG_DIR, "werr_arxiv_bundle.zip")
with zipfile.ZipFile(arxiv_zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write(os.path.join(PAPER_DIR, "main.tex"), "main.tex")
    zf.write(os.path.join(PAPER_DIR, "references.bib"), "references.bib")
    for fig in os.listdir(FIGURES_DIR):
        fp = os.path.join(FIGURES_DIR, fig)
        if os.path.isfile(fp):
            zf.write(fp, os.path.join("figures", fig))

print(f"[+] Created arXiv Bundle ZIP: {arxiv_zip_path} ({os.path.getsize(arxiv_zip_path) // 1024} KB)")

# Also copy arXiv bundle to Zenodo package
shutil.copy2(arxiv_zip_path, os.path.join(ZENODO_PKG_DIR, "werr_arxiv_bundle.zip"))

# Copy camera ready PDF to Zenodo package
pdf_src = os.path.join(PAPER_DIR, "Universal_Fractal_Natural_Language_Decision_Map_CameraReady.pdf")
pdf_dest = os.path.join(ZENODO_PKG_DIR, "Universal_Fractal_Natural_Language_Decision_Map_CameraReady.pdf")
shutil.copy2(pdf_src, pdf_dest)
print(f"[+] Mirrored Camera-Ready PDF to Zenodo Package: {pdf_dest} ({os.path.getsize(pdf_dest) // 1024} KB)")

# Also copy PDF to arXiv package for easy author reference
try:
    shutil.copy2(pdf_src, os.path.join(ARXIV_PKG_DIR, "Universal_Fractal_Natural_Language_Decision_Map_AuthorReview.pdf"))
except Exception as e:
    print(f"[*] Notice: AuthorReview.pdf is in use ({e}), skipping overwrite.")

# 2. Generate Zenodo Description HTML
zenodo_html = """<h2>Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains</h2>
<p>
This open-science research package presents the complete theoretical framework, empirical replication pipeline, and bare-metal production benchmarks for the <strong>Universal Fractal Natural Language Decision Map</strong>, realized via the <strong>werr</strong> (Waves &amp; Errors) machine-native edge reflex runtime and the production-deployed <strong>answerr</strong> cognitive platform (<a href="https://answerr.me" target="_blank" rel="noopener">https://answerr.me</a>).
</p>

<h3>Key Architectural &amp; Empirical Milestones</h3>
<ol>
  <li><strong>Zero-Tensor Inference (0 Bytes VRAM):</strong> Operates entirely without stored neural weight matrices by dynamically synthesizing deterministic decision manifolds from 24-byte coordinate seeds ((c<sub>x</sub>, c<sub>y</sub>, zoom)) along the chaotic boundary of the Mandelbrot set (&part;M).</li>
  <li><strong>Formal Domain Projector (&Phi;<sub>D</sub>) &amp; Non-Linear Boundary Necessity:</strong> Maps operational state dictionaries to complex coordinate perturbations. Ablation benchmarks demonstrate that passing state projections through &part;M lifts macro-accuracy from 63.8% (linear baseline) to 92.6% (+28.8% absolute gain; 95% Wilson CI: [90.8%, 94.1%]).</li>
  <li><strong>Information-Theoretic Acoustic Damping Filter (T<sub>desc</sub> = 0.045):</strong> Grounds decision robustness in token entropy and phonetic spectral density. High-entropy decoy filler is attenuated by 95.5%, yielding a 0.0% exploit bypass rate against targeted prompt-injection attacks (95% Wilson CI: [0.0%, 30.8%]).</li>
  <li><strong>Dynamical Trajectory Pruning (2.5&times; Speedup):</strong> Basin stabilization reduces mean escape loop iterations by 45.8% (K: 42.6 &rarr; 23.1), accelerating inference throughput from 8.41 ms to 3.31 ms median latency on commodity CPU hardware.</li>
  <li><strong>JevBench Benchmark Evaluation:</strong> Evaluated on the independent JevBench public test split (Issue #10) with an 81.65% self-run score, outperforming dense 4B models while requiring 0 Bytes VRAM.</li>
  <li><strong>Open Telemetry &amp; Production API:</strong> Backed by an open-science corpus of 1,150+ verified decisions (3,200+ evaluated questions) across 30+ domains and a drop-in OpenAI-compatible API endpoint (<code>/v1/chat/completions</code>) at <code>api.answerr.me:4431</code>.</li>
</ol>

<h3>Authors &amp; Affiliations</h3>
<ul>
  <li><strong>Volkan Dağlı</strong> (Corresponding Author) &bull; Anadolu University &amp; ITouch Systems, Turkey &bull; ORCID: 0009-0000-1587-8703</li>
  <li><strong>Dr. Zerrin Dağlı</strong> &bull; Mersin University, Mersin, Turkey &bull; ORCID: 0000-0001-9490-6425</li>
  <li><strong>Dağhan Dağlı</strong> &bull; Toros Science College, Mersin, Turkey &bull; ORCID: 0009-0003-2492-8313</li>
</ul>

<h3>Related Identifiers</h3>
<ul>
  <li><strong>Foundational Companion Theory:</strong> <a href="https://doi.org/10.5281/zenodo.22774934" target="_blank" rel="noopener">10.5281/zenodo.22774934</a> (Mandelbrot Fractal Neural Synthesis)</li>
  <li><strong>Source Code Repository:</strong> <a href="https://github.com/pCwOrM/werr" target="_blank" rel="noopener">https://github.com/pCwOrM/werr</a></li>
  <li><strong>Cognitive Web Platform:</strong> <a href="https://answerr.me" target="_blank" rel="noopener">https://answerr.me</a></li>
  <li><strong>Production Telemetry API:</strong> <a href="https://api.answerr.me:4431/v1/health" target="_blank" rel="noopener">https://api.answerr.me:4431/v1/health</a></li>
  <li><strong>JevBench Benchmark Evaluation:</strong> <a href="https://github.com/fstandhartinger/jevbench/issues/10" target="_blank" rel="noopener">Issue #10</a></li>
</ul>

<p><strong>License:</strong> Creative Commons Attribution 4.0 International (CC-BY-4.0)</p>
"""

with open(os.path.join(ZENODO_PKG_DIR, "ZENODO_ACIKLAMA_METNI.html"), "w", encoding="utf-8") as f:
    f.write(zenodo_html)

# 3. Generate Zenodo Step-by-Step Guide
zenodo_guide = """# WERR Makalesi Zenodo Yükleme ve DOI Alma Rehberi

Bu paket, **Universal Fractal Natural Language Decision Map** makalesinin Zenodo'ya yüklenerek anında kalıcı ve değiştirilemez bir **CERN DOI**'si alınması için hazırlanmıştır.

---

## 🚀 Adım Adım Yükleme Talimatı

1. **Zenodo'ya Giriş Yapın:**
   - [https://zenodo.org/deposit/new](https://zenodo.org/deposit/new) adresine gidin.
   - ORCID veya GitHub hesabınız (`@pCwOrM`) ile oturum açın.

2. **Dosyaları Yükleyin (Files):**
   - `Universal_Fractal_Natural_Language_Decision_Map_CameraReady.pdf` (Ana makale dosyası)
   - `werr_arxiv_bundle.zip` (Açık bilim kaynak kod ve figür paketi)

3. **Temel Bilgiler (Basic Information):**
   - **Resource type:** `Publication` -> `Preprint` (veya `Working paper`)
   - **Title:** `Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains`
   - **Publication date:** `2026-09-21`

4. **Yazarlar (Creators):**
   1. **Family name:** `Dağlı`, **Given names:** `Volkan`
      - **Affiliation:** `Anadolu University & ITouch Systems, Turkey`
      - **ORCID:** `0009-0000-1587-8703`
   2. **Family name:** `Dağlı`, **Given names:** `Zerrin`
      - **Affiliation:** `Mersin University, Mersin, Turkey`
      - **ORCID:** `0000-0001-9490-6425`
   3. **Family name:** `Dağlı`, **Given names:** `Dağhan`
      - **Affiliation:** `Toros Science College, Mersin, Turkey`
      - **ORCID:** `0009-0003-2492-8313`

5. **Açıklama (Description):**
   - Klasördeki `ZENODO_ACIKLAMA_METNI.html` dosyasının içeriğini kopyalayıp Zenodo'nun Description alanına yapıştırın.

6. **Anahtar Kelimeler (Keywords):**
   - `Universal Fractal Decision Map`
   - `Zero-Tensor Inference`
   - `System-One Reflex Arc`
   - `Mandelbrot Boundary Dynamics`
   - `Acoustic Damping Filter`
   - `Dynamic Calibration`
   - `Edge AI`
   - `On-Chain AI Oracle`

7. **İlişkili Tanımlayıcılar (Related Identifiers):**
   - **Identifier:** `10.5281/zenodo.22774934` | **Relation:** `isDerivedFrom` | **Scheme:** `DOI` *(Temel Çatı DOI)*
   - **Identifier:** `https://github.com/pCwOrM/werr` | **Relation:** `isSupplementTo` | **Scheme:** `URL`
   - **Identifier:** `https://answerr.me` | **Relation:** `isDocumentedBy` | **Scheme:** `URL`

8. **Yayınlama (Publish):**
   - Sayfanın altındaki **"Publish"** butonuna tıklayın.
   - Tebrikler! Anında `10.5281/zenodo.XXXXXXX` formatında resmi CERN DOI'niz üretilmiş olacaktır.

---

## 📌 Sonraki Adım: arXiv'e Gönderme
Zenodo DOI'nizi aldıktan sonra, `C:\\Users\\maat\\Desktop\\ARXIV_WERR_YUKLEME_PAKETI` klasöründeki rehberi açarak arXiv başvurunuzu tamamlayın.
"""

with open(os.path.join(ZENODO_PKG_DIR, "ZENODO_YUKLEME_REHBERI_TR.md"), "w", encoding="utf-8") as f:
    f.write(zenodo_guide)

# 4. Generate arXiv Step-by-Step Guide
arxiv_guide = """# WERR Makalesi arXiv Yükleme Rehberi

Zenodo'dan kalıcı DOI'nizi aldıktan sonra, bu paketi kullanarak makaleyi arXiv'e yükleyebilirsiniz.

---

## 📁 Yükleme Paketi İçeriği
- `werr_arxiv_bundle.zip`: arXiv sisteminin otomatik olarak derleyeceği temiz `main.tex`, `references.bib` ve `figures/` klasörünü içeren arşiv.
- `Universal_Fractal_Natural_Language_Decision_Map_AuthorReview.pdf`: İnceleme ve kontrol amaçlı PDF.

---

## 🚀 Adım Adım arXiv Başvurusu

1. **arXiv'e Giriş Yapın:**
   - [https://arxiv.org/submit](https://arxiv.org/submit) adresine gidin.
   - Giriş yapın ve **"Start New Submission"** butonuna tıklayın.

2. **Kategori Seçimi (Subject Classifications):**
   - **Primary Category:** `Computer Science - Artificial Intelligence` (`cs.AI`)
   - **Secondary Categories (Cross-lists):**
     - `Computer Science - Neural and Evolutionary Computing` (`cs.NE`)
     - `Computer Science - Computation and Language` (`cs.CL`)

3. **Dosya Yükleme (Files):**
   - Klasördeki `werr_arxiv_bundle.zip` dosyasını seçip yükleyin ve unpack ettirin.
   - arXiv derleyicisini çalıştırın ("Auto-Detect / pdflatex"). Çıktı önizlemesini doğrulayın.

4. **Meta Veriler (Metadata):**
   - **Title:** `Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains`
   - **Authors:** `Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı`
   - **Abstract:** Makaledeki İngilizce Abstract metnini yapıştırın.
   - **Comments:** `10 pages, 5 figures, 3 tables. Companion to Mandelbrot Fractal Neural Synthesis. Live portal: https://answerr.me; Source code: https://github.com/pCwOrM/werr`
   - **Related DOI / External Identifier (KRİTİK ADIM):**
     - Alınan resmi CERN Zenodo DOI numarasını girin: `10.5281/zenodo.22867426`
     - Bu adım, arXiv moderatörlerine ve otomatik tarayıcılara makalenin CERN altyapısında tescilli bir açık bilim yayını olduğunu kanıtlayarak moderasyon kuyruğundaki bekleme süresini minimuma indirir.

5. **Onay ve Gönderim (Submit):**
   - Önizleme PDF'ini kontrol edin ve gönderimi onaylayın.
"""

with open(os.path.join(ARXIV_PKG_DIR, "ARXIV_YUKLEME_REHBERI_TR.md"), "w", encoding="utf-8") as f:
    f.write(arxiv_guide)

print(f"[+] All submission bundles generated successfully:")
print(f"    - Zenodo package: {ZENODO_PKG_DIR}")
print(f"    - arXiv package : {ARXIV_PKG_DIR}")
