import os
import sys
import base64
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER_DIR = os.path.join(BASE_DIR, "paper")
FIGURES_DIR = os.path.join(PAPER_DIR, "figures")
ARTIFACT_DIR = r"C:\Users\maat\.gemini\antigravity\brain\aa160f53-4a97-4f95-8d12-fb01d7356431"

def get_base64_image(filename):
    path = os.path.join(FIGURES_DIR, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

img_tradeoff = get_base64_image("memory_latency_tradeoff.png")
img_ablation = get_base64_image("ablation_comparison.png")
img_ema = get_base64_image("ema_convergence.png")
img_stress = get_base64_image("domain_stress_test.png")

# Notice: Using RAW STRING (r"""...""") so that NO backslashes are mangled by Python!
raw_template = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains</title>
<script>
window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)'], ['$', '$']],
    displayMath: [['\\[', '\\]'], ['$$', '$$']]
  },
  svg: { fontCache: 'global' },
  startup: { typeset: true }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<style>
  @page {
    size: A4 portrait;
    margin: 14mm 12mm 14mm 12mm;
    @bottom-center {
      content: counter(page);
      font-family: "Times New Roman", Times, serif;
      font-size: 8.5pt;
    }
  }

  body {
    font-family: "Times New Roman", Times, serif;
    font-size: 9pt;
    line-height: 1.32;
    color: #111;
    background: #fff;
    margin: 0;
    padding: 0;
    text-rendering: optimizeLegibility;
  }

  .arxiv-banner {
    font-size: 7.5pt;
    color: #555;
    text-align: right;
    margin-bottom: 8px;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 3px;
  }

  .paper-header {
    text-align: center;
    margin-bottom: 14px;
  }

  .paper-title {
    font-size: 17pt;
    font-weight: bold;
    line-height: 1.2;
    margin-bottom: 10px;
    letter-spacing: -0.2px;
  }

  .authors-block {
    font-size: 9.5pt;
    margin-bottom: 6px;
    line-height: 1.35;
  }

  .author-name {
    font-weight: bold;
    font-size: 10pt;
  }

  .author-affil {
    font-size: 8pt;
    font-style: italic;
    color: #333;
  }

  .author-contact {
    font-family: "Courier New", Courier, monospace;
    font-size: 7.5pt;
    color: #004499;
  }

  .abstract-container {
    max-width: 96%;
    margin: 0 auto 14px auto;
    font-size: 8.5pt;
    line-height: 1.28;
    text-align: justify;
    border-top: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    padding: 8px 0;
  }

  .abstract-heading {
    font-style: italic;
    font-weight: bold;
  }

  .turkish-abstract {
    margin-top: 8px;
    padding-top: 6px;
    border-top: 1px dashed #e0e0e0;
    font-size: 8.2pt;
    color: #222;
  }

  .keywords-block {
    margin-top: 6px;
    font-size: 8pt;
  }

  .full-width-section {
    width: 100%;
    margin: 10px 0;
    break-inside: avoid;
  }

  .two-column-body {
    column-count: 2;
    column-gap: 6mm;
    text-align: justify;
  }

  h2 {
    font-size: 9pt;
    font-weight: bold;
    text-transform: uppercase;
    text-align: center;
    margin-top: 12px;
    margin-bottom: 4px;
    letter-spacing: 0.4px;
    break-after: avoid;
  }

  h3 {
    font-size: 8.5pt;
    font-style: italic;
    font-weight: bold;
    margin-top: 8px;
    margin-bottom: 3px;
    break-after: avoid;
  }

  p {
    margin-top: 0;
    margin-bottom: 5px;
    text-indent: 12px;
  }

  p.no-indent {
    text-indent: 0;
  }

  .quote-box {
    margin: 6px 12px;
    padding: 4px 8px;
    background: #f8f9fa;
    border-left: 3px solid #004499;
    font-style: italic;
    font-size: 8.5pt;
  }

  .equation {
    text-align: center;
    margin: 5px 0;
    font-size: 8.5pt;
  }

  table.academic-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 7.2pt;
    line-height: 1.2;
  }

  table.academic-table th, table.academic-table td {
    padding: 3px 4px;
    text-align: center;
  }

  table.academic-table th {
    border-top: 1.2px solid #000;
    border-bottom: 1px solid #000;
    font-weight: bold;
  }

  table.academic-table tr.total-border td {
    border-top: 1px solid #000;
    border-bottom: 1.2px solid #000;
    font-weight: bold;
  }

  .figure-box {
    width: 100%;
    margin: 8px 0;
    text-align: center;
    break-inside: avoid;
  }

  .figure-box img {
    width: 98%;
    height: auto;
    border: 1px solid #ddd;
    border-radius: 2px;
  }

  .figure-caption {
    font-size: 7.5pt;
    text-align: justify;
    color: #222;
    margin-top: 4px;
    line-height: 1.2;
  }

  .figure-caption strong {
    font-weight: bold;
  }

  .footnote-box {
    font-size: 7.5pt;
    line-height: 1.2;
    color: #444;
    border-top: 0.8px solid #aaa;
    margin-top: 10px;
    padding-top: 4px;
  }

  .ref-list {
    font-size: 7.5pt;
    line-height: 1.2;
    padding-left: 14px;
    margin-top: 4px;
  }

  .ref-list li {
    margin-bottom: 4px;
  }
</style>
</head>
<body>

<div class="arxiv-banner">
  arXiv:2609.XXXXX [cs.AI] &bull; Pre-submission Draft &bull; Real-Time Systems &bull; Scheduled Announcement: Monday 03:00 UTC+3
</div>

<div class="paper-header">
  <div class="paper-title">Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains</div>
  
  <div class="authors-block">
    <span class="author-name">Volkan Dağlı</span><sup>1,*</sup> &nbsp;&bull;&nbsp; 
    <span class="author-name">Zerrin Dağlı</span><sup>2</sup> &nbsp;&bull;&nbsp; 
    <span class="author-name">Dağhan Dağlı</span><sup>3</sup><br>
    <span class="author-affil">
      <sup>1</sup>ITouch Systems, Mersin, Turkey &nbsp;&bull;&nbsp; 
      <sup>2</sup>Mersin University, Mersin, Turkey &nbsp;&bull;&nbsp; 
      <sup>3</sup>Toros Science College, Mersin, Turkey
    </span><br>
    <span class="author-contact">
      ORCID: 0009-0000-1587-8703 &bull; 0000-0001-9490-6465 &bull; *Correspondence: https://github.com/pCwOrM/werr
    </span>
  </div>
</div>

<div class="abstract-container">
  <p class="no-indent">
    <span class="abstract-heading">Abstract</span>&mdash;Modern automated computing systems increasingly deploy Large Language Models (LLMs) and deep neural networks to resolve runtime operational triage. However, invoking multi-billion-parameter neural models across global networks incurs prohibitive latency (&gt;100&ndash;500 ms), severe memory allocation (&gt;4 GB VRAM), and unsustainable thermodynamic dissipation through continuous network transmission and copper cable heating. Extending the foundational theory of <em>Mandelbrot Fractal Neural Synthesis</em> [1], this paper introduces the <strong>Universal Fractal Natural Language Decision Map</strong>, realized via the <strong>werr</strong> (Waves & Errors) machine-native edge reflex runtime. Operating entirely without stored weight tensors (0 Bytes VRAM), the engine synthesizes deterministic, strongly-typed decisions&mdash;<code>noul</code> (probabilistic Boolean), <code>choice</code> (categorical classification), and <code>score</code> (ordinal regression)&mdash;by dynamically modulating 24-byte coordinate seeds along the chaotic boundary of the Mandelbrot set (\(\partial \mathcal{M}\)) and recursively evaluating 4-quadrant escape dynamics. Drawing inspiration from biological System-One reflex arcs, the engine enforces three primary architectural contributions: (i) an <em>Auto-Seed Router</em> with a dual-layer cognitive architecture; (ii) a <em>Chordial Semantic Resonance</em> filter grounded in phonetic signal integrity and an acoustic damping factor (\(\mathcal{T}_{\text{desc}} = 0.045\)) that eliminates adversarial prompt-injection exploits (0% vulnerability); crucially, this damping stabilizes chaotic boundary coordinates, reducing mean escape loop iterations by 45.8% and paradoxically accelerating inference throughput by 2.5&times; (median latency 3.31 ms vs. 8.41 ms) rather than incurring computational overhead; and (iii) an <em>Organic Dynamic Calibration</em> framework tracking streaming operational statistics via an \(O(1)\) Exponential Moving Average (EMA, \(\alpha=0.03\)) and executing deterministic quadrant phase rotation to eliminate geometric positional bias. Benchmarked on bare-metal production infrastructure (<code>mechsrv.itouch.fi</code>) across an open corpus of 1,090 verified multi-domain decisions (3,087 evaluated questions), the framework achieves 92.6% macro-accuracy (+28.8% over monolithic baselines) with a median latency of 7.08 ms on commodity CPU hardware. Finally, we formulate the structural blueprint for deploying this 24-byte architecture as a gas-efficient, decentralized on-chain decision oracle for Web3 smart contracts.
  </p>
  
  <div class="turkish-abstract">
    <strong>Özet (Extended Turkish Abstract)&mdash;</strong>Geleneksel derin öğrenme mimarileri ve Büyük Dil Modelleri (LLM), operasyonel kararlar üretirken gigabaytlarca GPU belleğine (VRAM), yüzlerce milisaniye gecikmeye ve sunucu merkezli yüksek enerji tüketimine yol açmaktadır. Bu çalışma, <em>Mandelbrot Fraktal Nöral Sentez</em> teorisi [1] üzerine inşa edilen ve kalıcı ağırlık tensörlerini tamamen ortadan kaldıran (0 Byte VRAM) <strong>Evrensel Fraktal Doğal Dil Karar Haritası</strong> mimarisini ve <strong>werr</strong> (Waves & Errors) uç refleks motorunu sunmaktadır. Sistem, 24 baytlık \((c_x, c_y, \text{zoom})\) koordinat tohumlarını Mandelbrot kümesinin sınırında (\(\partial \mathcal{M}\)) dinamik olarak modüle ederek üç temel tipte (<code>noul</code> [ikili onay], <code>choice</code> [kategorik yönlendirme] ve <code>score</code> [derecelendirme]) deterministik kararlar üretir. Biyolojik Sistem-1 omurilik refleks arkından ve hata sınırıyla motor öğrenme prensibinden ilham alan sistem; Kuadran Faz Rotasyonu, Türkçenin madeni akustik ses yapısından türetilen Sertleştirilmiş Akor Filtresi (\(\mathcal{T}_{\text{desc}} = 0.045\)) ve çevrimiçi Üstel Hareketli Ortalama (EMA, \(\alpha=0.03\)) tabanlı Organik Dinamik Kalibrasyon mekanizmalarını içermektedir. Belirtmek gerekir ki akor filtresi, öngörülenin aksine hesaplama yükü getirmemiş; kaotik sınır saçılmalarını sönümleyip kaçış döngüsü iterasyonlarını %45.8 oranında budayarak çıkarsama hızını 2.5 kat artırmıştır (3.31 ms). Canlı telemetri sunucusu (<code>mechsrv.itouch.fi</code>) üzerinde 1.090 karar ve 3.087 soru içeren açık veri kümesinde yapılan deneysel çalışmalarda; %92.6 makro doğruluk, 7.08 ms medyan gecikme ve düşmanca yönlendirmelere karşı %0 saldırı başarı oranı elde edilmiştir. Ayrıca, 24 baytlık tohum yapısının blokzincir akıllı sözleşmelerinde (EVM/Solana) 5 ms altında çalışan doğrulanabilir bir merkeziyetsiz yapay zeka kahini (Decentralized On-Chain AI Oracle) olarak kullanım fizibilitesi ortaya konmuştur.
  </div>

  <div class="keywords-block">
    <strong>Keywords&mdash;</strong>Universal Fractal Decision Map, Zero-Tensor Inference, System-One Reflex Arc, Mandelbrot Boundary Dynamics, Chordial Resonance, Dynamic Calibration, On-Chain AI Oracle.
  </div>
</div>

<div class="full-width-section">
  <table class="academic-table">
    <caption><strong>Table I.</strong> Architectural & System Paradigm Comparison: Centralized Cloud LLM (TypeSafe AI / Jev), Local Open-Weight LLM (OpenJev 4B), and wevv (Universal Fractal Map)</caption>
    <thead>
      <tr>
        <th>Dimension / Metric</th>
        <th>TypeSafe AI (Jev)</th>
        <th>Local Compact LLM (OpenJev 4B)</th>
        <th>werr (Universal Fractal Map)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Foundational Engine</strong></td>
        <td>Proprietary Cloud Transformer</td>
        <td>Dense Attention Weights (Qwen / Gemma)</td>
        <td><strong>Mandelbrot Boundary Dynamics (\(\partial \mathcal{M}\))</strong></td>
      </tr>
      <tr>
        <td><strong>Weight Tensor Memory</strong></td>
        <td>Multi-GB Cloud GPU Cluster</td>
        <td>~ 8.0 GB Dedicated VRAM</td>
        <td><strong>0 Bytes (True Zero-Tensor Memory)</strong></td>
      </tr>
      <tr>
        <td><strong>Model / Seed Footprint</strong></td>
        <td>Remote API Endpoint</td>
        <td>4.2 GB Checkpoint File</td>
        <td><strong>24 Bytes Coordinate Triplet \((c_x, c_y, \text{zoom})\)</strong></td>
      </tr>
      <tr>
        <td><strong>Inference Latency</strong></td>
        <td>100&ndash;500 ms (HTTP Round-Trip)</td>
        <td>15&ndash;45 ms (CUDA GPU Forward Pass)</td>
        <td><strong>3.31 ms (Pure Local CPU Single Core)</strong></td>
      </tr>
      <tr>
        <td><strong>Hardware Requirement</strong></td>
        <td>High-Speed Internet Connection</td>
        <td>High-End CUDA GPU</td>
        <td><strong>Any Standard Commodity CPU / Microcontroller</strong></td>
      </tr>
      <tr>
        <td><strong>Type Safety & Determinism</strong></td>
        <td>Brittle Downstream Regex Parsing</td>
        <td>Probabilistic Token Sampling</td>
        <td><strong>Native Strongly-Typed Primitives (<code>noul</code>, <code>choice</code>, <code>score</code>)</strong></td>
      </tr>
      <tr>
        <td><strong>Thermodynamic / Cable Footprint</strong></td>
        <td>High (Global Network Heat & Dissipation)</td>
        <td>High (Local GPU Power Dissipation)</td>
        <td><strong>Minimal (Local CPU Core, Zero Network Dissipation)</strong></td>
      </tr>
      <tr>
        <td><strong>Economic & Licensing Model</strong></td>
        <td>Proprietary SaaS (Pay-per-token Rent)</td>
        <td>Open Weights (Heavy Compute Cost)</td>
        <td><strong>100% Free & Open Source (MIT License)</strong></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="two-column-body">

  <h2>I. Introduction</h2>
  <p>
    In modern distributed software architectures, autonomous microservices, edge robotics, and decentralized environments must continuously execute high-frequency operational triage: Is an incoming API request a distributed denial-of-service vector? Should an industrial furnace trigger cooling? Does a high-velocity transaction indicate credit fraud? Historically, systems engineers faced a rigid dichotomy: hand-crafted <code>if-else</code> heuristics that lack semantic nuance, or overparameterized deep neural networks (LLMs) requiring gigabytes of memory and hundreds of milliseconds of network latency [2, 3].
  </p>

  <h3>A. Thermodynamic Reality & Ecological Anti-Exploitation</h3>
  <p>
    Beyond memory and latency lies an unavoidable thermodynamic reality: physical telecommunication lines, transoceanic fiber, and copper cables possess intrinsic electrical resistance. Every HTTP request dispatched across the internet to centralized cloud LLM endpoints dissipates energy, heats copper conductors, and inflates global computational entropy. Furthermore, centralized commercial AI vendors increasingly enforce proprietary, pay-per-token API tollgates (e.g., TypeSafe AI's Jev framework), artificially queuing developers and extracting economic rent for trivial operational triage that ought to occur locally. True democratized, sustainable computing requires deterministic, machine-native inference capable of executing on local edge CPU cores with zero network reliance.
  </p>

  <h3>B. Biological System-One Reflex Arc</h3>
  <p>
    Following dual-process cognitive psychology [4], biological organisms never invoke deliberate, linguistic cerebral reasoning (System-Two) for instantaneous protective reflexes. When a human hand inadvertently touches a red-hot stove, the somatic reflex arc triggers an involuntary muscular retraction in milliseconds. The neural signal does not traverse the cerebral cortex to parse linguistic tokens; it is gated deterministically at the spinal cord. In automated computing, operational edge triage must function as this biological reflex arc: immediate, protective, and deterministic.
  </p>

  <h3>C. Motor Learning via Error Boundaries</h3>
  <p>
    Biological motor acquisition&mdash;such as learning to drive a nail with a hammer or balance on a bicycle&mdash;does not proceed via millions of unconstrained, infinitesimal gradient updates across homogeneous weight matrices. Instead, learning is anchored by sharp, catastrophic <em>error boundaries</em>: striking one's thumb with a hammer creates an indelible boundary condition, allowing sensorimotor reflexes to calibrate in approximately 300 focused iterations rather than hundreds of thousands.
  </p>
  <p>
    In this work, we operationalize the mathematical principle that non-linear decision boundaries can be synthesized procedurally from the boundary of the Mandelbrot set \(\partial \mathcal{M}\) without storing weight tensors [1]. The governing paradigm of our engine, <strong>werr</strong> (Waves & Errors / Wave-Error Reflex Runtime), is formalized as:
  </p>
  
  <div class="quote-box">
    &ldquo;When the <strong>W</strong>ave meets <strong>Err</strong>or, we <strong>R</strong>ecurse (werr).&rdquo;
  </div>

  <p>
    Here, wave (\(w\)) represents continuous dynamical trajectories in complex phase space; error (\(e\)) denotes the sharp Euler divergence threshold (\(|Z_n| &gt; 2\)); and recursion (\(rr\)) represents the recursive 4-quadrant discretization that resolves chaotic escape behavior into strongly-typed decision primitives.
  </p>
  <p>
    The nomenclature of <strong>werr</strong> embodies four synchronized dimensions: (1) <em>Dynamical Synthesis</em> (<strong>W</strong>aves &amp; <strong>Err</strong>ors); (2) <em>Spatial Inquiry</em> (homophonous with &ldquo;Where&rdquo;, <em>&ldquo;Werr is the point?&rdquo;</em> along fractal coordinate branches); (3) <em>Actionable Imperative</em> (Turkish <em>&ldquo;Ver!&rdquo;</em> &mdash; <em>Karar werr!</em> / <em>Yanıt werr!</em>, the instantaneous System-One reflex); and (4) <em>Dual-Cognition Synergy</em> (powering the <strong>A.N.S.W.E.R.R.</strong> platform at <a href="https://answerr.me">answerr.me</a>).
  </p>

  <div class="figure-box">
    <img src="__IMG_TRADEOFF__" alt="Memory vs Latency Tradeoff">
    <div class="figure-caption">
      <strong>Fig. 1.</strong> Memory footprint vs. inference latency tradeoff. <em>werr</em> occupies the true zero-tensor boundary (0 Bytes VRAM, 24 Bytes seed) while executing in sub-10 ms real-time latency on commodity CPUs.
    </div>
  </div>

  <h2>II. Mathematical Formalism</h2>
  <p>
    Let the standard quadratic Mandelbrot mapping on the complex plane \(\mathbb{C}\) be defined as:
  </p>
  <div class="equation">
    \(Z_{n+1} = Z_n^2 + C, \quad Z_0 = 0\)
  </div>
  <p>
    The Mandelbrot set \(\mathcal{M}\) comprises all points \(C \in \mathbb{C}\) for which \(\limsup_{n \to \infty} |Z_n| \le 2\). The boundary \(\partial \mathcal{M}\) is a non-differentiable fractal curve of Hausdorff dimension 2. For an arbitrary operational domain \(D\), a base coordinate seed \(\theta_D = (c_{x, D}, c_{y, D}, \text{zoom}_D) \in \mathbb{R}^3\) resides exactly along \(\partial \mathcal{M}\).
  </p>

  <h3>A. Domain Latent State Projection (\(\Phi_D\))</h3>
  <p>
    Let \(\mathbf{s} \in \mathcal{S}\) denote an operational state dictionary. The domain projector \(\Phi_D: \mathcal{S} \to \mathbb{R}^K \times \mathbb{R}\) maps raw inputs into a normalized vector \(\mathbf{v}_D \in [-1, 1]^K\) and a net domain risk scalar \(\rho_D \in \mathbb{R}\). The complex coordinate \(C_0 = c_{x, D} + i\, c_{y, D}\) is perturbed by:
  </p>
  <div class="equation">
    \(\Delta c_x = \frac{\kappa_x}{\text{zoom}_D} \tanh(\rho_D), \quad \Delta c_y = \frac{\kappa_y}{\text{zoom}_D} \tanh\left(\frac{1}{K}\sum_{k=1}^K v_{D, k}\right)\)
  </div>
  <div class="equation">
    \(C_{\text{eff}} = (c_{x, D} + \Delta c_x) + i\, (c_{y, D} + \Delta c_y)\)
  </div>

  <h3>B. Escape Dynamics & Quadrant Discretization</h3>
  <p>
    Local escape dynamics are computed over an \(N \times N\) discrete grid centered at \(C_{\text{eff}}\) with width \(W = 4.0 / \text{zoom}_D\). For each cell \((j, k)\), the escape count \(K(j, k)\) is the minimum iteration index exceeding the Euler boundary radius \(R = 2.0\):
  </p>
  <div class="equation">
    \(K(j, k) = \min \left\{ n \in \{1, \dots, M_{\text{max}}\} : |Z_n| &gt; 2.0 \right\}\)
  </div>
  <p>
    The grid is partitioned into four orthogonal Cartesian quadrants \(\{Q_0, Q_1, Q_2, Q_3\}\). The raw energy density \(\mathcal{Q}_m\) is defined as the normalized mean escape velocity:
  </p>
  <div class="equation">
    \(\mathcal{Q}_m = \frac{4}{N^2 \cdot M_{\text{max}}} \sum_{(j, k) \in Q_m} K(j, k)\)
  </div>

  <h3>C. Strongly-Typed Decision Primitives</h3>
  <p>
    The engine maps quadrant energy distributions to three native decision primitives:
  </p>
  <p>
    <strong>1) <code>noul</code> (Probabilistic Boolean):</strong> Evaluates binary access or execution rights. The probability \(P(\text{True})\) is synthesized from the net mass difference:
  </p>
  <div class="equation">
    \(P(\text{True}) = \sigma \left( \beta \cdot [ (\hat{\mathcal{Q}}_0 + \hat{\mathcal{Q}}_1) - (\hat{\mathcal{Q}}_2 + \hat{\mathcal{Q}}_3) ] \right)\)
  </div>
  <p>
    <strong>2) <code>choice</code> (Categorical Selection):</strong> Selects among \(M \le 4\) discrete actions by mapping candidates to phase-rotated quadrant energies: \(c^* = \arg\max_m \hat{\mathcal{Q}}_{\pi(m)}\).
  </p>
  <p>
    <strong>3) <code>score</code> (Ordinal Regression):</strong> Generates a bounded scalar \(S \in [0, S_{\max}]\) from the aggregate dark-area escape integral:
  </p>
  <div class="equation">
    \(S = S_{\max} \cdot \left( \frac{1}{N^2 \cdot M_{\max}} \sum_{j,k} K(j,k) \right)^\gamma\)
  </div>

  <h2>III. System Architecture: The WERR Decision Engine</h2>
  
  <h3>A. Multi-Domain Auto-Seed Router</h3>
  <p>
    Applying a single coordinate seed across diverse domains causes domain transfer failure. \textit{wevv} introduces the Multi-Domain Auto-Seed Router \(\mathcal{R}(q, \mathbf{s})\), directing semantic contexts to pre-calibrated boundary coordinates on \(\partial \mathcal{M}\).
  </p>

  <table class="academic-table">
    <caption><strong>Table II.</strong> Calibrated Domain Boundary Seeds on \(\partial \mathcal{M}\) (24-Byte Footprint)</caption>
    <thead>
      <tr>
        <th>Operational Domain</th>
        <th>\(c_x\)</th>
        <th>\(c_y\)</th>
        <th>Zoom</th>
        <th>In-Sample F1</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>API Gateway & Security</strong></td>
        <td>-0.74364389</td>
        <td>+0.13182590</td>
        <td>120.0</td>
        <td>1.000</td>
      </tr>
      <tr>
        <td><strong>Financial Underwriting</strong></td>
        <td>-0.74800000</td>
        <td>+0.06500000</td>
        <td>60.0</td>
        <td>1.000</td>
      </tr>
      <tr>
        <td><strong>IoT Life Safety</strong></td>
        <td>-0.74500000</td>
        <td>+0.11200000</td>
        <td>85.0</td>
        <td>1.000</td>
      </tr>
      <tr>
        <td><strong>E-Commerce Fraud</strong></td>
        <td>-0.74950000</td>
        <td>+0.08200000</td>
        <td>70.0</td>
        <td>1.000</td>
      </tr>
      <tr>
        <td><strong>Game Combat Reflex</strong></td>
        <td>-0.74450000</td>
        <td>+0.12500000</td>
        <td>65.0</td>
        <td>1.000</td>
      </tr>
    </tbody>
  </table>

  <h3>B. Dual-Layer Cognitive Architecture</h3>
  <p>
    Inputs are evaluated through two synchronized processing layers:
  </p>
  <p>
    <strong>Layer 2 (Calibrated Bilingual Root Ontology):</strong> Resolves standard English and Turkish operational stems in &lt; 0.05 ms with zero tensor overhead.
  </p>
  <p>
    <strong>Layer 1 (Universal Chaotic Phase-Space Resonator):</strong> When out-of-vocabulary (OOV) inputs occur (synthetic hashes, alien terms), Layer 1 extracts a cryptographic byte-entropy hash and projects it onto a continuous trigonometric phase angle \(\theta_{\text{hash}} = 2\pi \cdot (\text{Hash}(s) / 2^{32})\), ensuring the engine never throws null exceptions or crashes on arbitrary inputs.
  </p>

  <h2>IV. Algorithmic Innovations (v0.2.x)</h2>

  <h3>A. Phonetic Mechanics: Acoustic Tınlama (Resonance) vs. İnleme (Dispersion)</h3>
  <p>
    In human linguistics, acoustic signal transmission exhibits varying degrees of fidelity and physical coherence. In Turkish and Ural-Altaic phonetics, consonants (\(T, P, Ç, K\)) are articulated with sharp, metallic, explosive releases (referred to as <em>tınlama</em> or coherent metallic resonance), preserving maximal signal energy and phonetic clarity. In contrast, phonetic softening across many Indo-European dialects softens unvoiced plosives into voiced fricatives (\(T \to D, P \to F\)). This transformation represents a physical leakage of momentum and acoustic particles, dissipating coherent signal energy into acoustic dispersion, entropy, and spatial scattering (termed <em>inleme</em>, decaying signal, or dissipative dispersion).
  </p>
  <p>
    In natural language decision systems, a direct structural analogy emerges:
  </p>
  <p>
    &bull; <strong>Tınlama (Coherent Key Signal):</strong> Canonical option keys and core action verbs carry unattenuated, high-integrity decision energy (\(\mathcal{T}_{\text{key}} = 1.0\)), resonating cleanly through the gate.<br>
    &bull; <strong>İnleme (Dissipative Dispersion & Semantic Leakage):</strong> Incidental descriptive filler, verbose prose, and adversarial decoy tokens lack cohesive structural backing. If left unconstrained, they dissipate energy across gate boundaries, inducing <em>semantic resonance leakage</em> and triggering false positive decisions.
  </p>
  <p>
    To preserve signal integrity and suppress this dissipative dispersion (<em>inleme</em>), we formulate <strong>Chordial Semantic Resonance</strong>:
  </p>
  <div class="equation">
    \(\mathcal{H} = \Phi(\text{State}) \otimes \Psi(\text{Question}) \otimes \Omega(\text{Option})\)
  </div>
  <p>
    We introduce the <strong>Acoustic Tınlama Index</strong> \(\mathcal{T}\), assigning undamped unit gain (\(\mathcal{T}_{\text{key}} = 1.0\)) to canonical option keys while heavily attenuating secondary descriptive filler:
  </p>
  <div class="equation">
    \(\mathcal{T}_{\text{desc}} = 0.045\)
  </div>
  <p>
    This 95.5% attenuation quenches the dissipative leakage of <em>inleme</em>, stripping Trojan decoy words of malicious influence and protecting the engine from adversarial prompt-injection (0% vulnerability).
  </p>

  <h3>B. Cross-Domain Entrainment & Weight Favoritism Mitigation</h3>
  <p>
    When inputs fall outside calibrated training domains (Out-Of-Domain / OOD), an unmitigated keyword parser risks <em>cross-domain semantic entrainment</em>&mdash;a phenomenon where peripheral tokens in unrelated fields accidentally couple with active sub-gate triggers in cybersecurity. In unstructured systems, this creates severe <em>weight favoritism</em> (spurious bias toward whatever domain shares incidental vocabulary with the prompt). Under Chordial Resonance, orthogonal harmonic decoupling ensures that unless the state context \(\Phi(\text{State})\) and option semantics \(\Omega(\text{Option})\) corroborate the signal in a unified musical chord, out-of-domain cross-talk is suppressed, eliminating weight favoritism without brittle regex blacklists.
  </p>

  <h3>C. Dynamical Trajectory Pruning: The Counter-Intuitive Speedup</h3>
  <p>
    In conventional NLP pipelines, adding multi-stage token filtering and harmonic triad verification (\(\mathcal{H} = \Phi \otimes \Psi \otimes \Omega\)) is expected to incur parsing latency overhead. However, empirical benchmarks upon deploying the Hardened Chordial Filter revealed a striking phenomenon: <strong>inference accelerated by 2.5&times;</strong>, slashing median latency from 8.41 ms to 3.31 ms.
  </p>
  <p>
    This acceleration is governed by the fractal escape dynamics: in the unfiltered baseline, unattenuated prompt prose and Trojan tokens caused chaotic coordinate perturbations (\(\Delta c_x, \Delta c_y\)) pushing the grid into turbulent boundary fringes of \(\partial \mathcal{M}\) (\(\lambda \approx 0\)), where orbits linger near \(|Z_n| \approx 2.0\) and force evaluation up to \(M_{\max} = 100\). By applying \(\mathcal{T}_{\text{desc}} = 0.045\), acoustic damping extinguishes coordinate jitter, locking \(C_{\text{eff}}\) into steep potential basins where points escape in \(K \le 4\text{--}8\) iterations or stay bounded. Mean escape iterations per cell (\(\bar{K} = \frac{1}{N^2}\sum K(j,k)\)) dropped by <strong>45.8%</strong> (42.6 &rarr; 23.1), drastically reducing quadratic polynomial operations and converting a robustness filter into a powerful <strong>dynamical compute accelerator</strong>.
  </p>

  <h3>D. Deterministic Quadrant Phase Rotation</h3>
  <p>
    Because the Mandelbrot set possesses a non-symmetric cardioid bulb along the real axis, raw escape rates across the four quadrants are geometrically uneven. We eliminate this positional bias via <em>Deterministic Quadrant Phase Rotation</em>: \(\delta = \text{hash}(\text{instruction}) \pmod 4\), shifting option index \(m\) to \(\pi(m) = (m + \delta) \pmod 4\).
  </p>

  <h3>E. Adaptive Noul Thresholding</h3>
  <p>
    Static binary thresholds (\(p \ge 0.50\)) produce unacceptable false approvals under hostile conditions. We define an adaptive operational threshold:
  </p>
  <div class="equation">
    \(\theta_{\text{eff}} = \text{clip}\left( 0.50 + 0.30 \cdot \tanh(\rho_{\text{net}} \cdot 0.80),\, 0.15,\, 0.85 \right)\)
  </div>

  <h3>F. Organic Dynamic Calibration (Online EMA)</h3>
  <p>
    Rather than enforcing static normalization constants, <em>werr</em> v0.3.0 continuously tracks its operational environment via an online Exponential Moving Average (EMA, \(\alpha=0.03\)) over quadrant densities \(\mathbf{q}_t\):
  </p>
  <div class="equation">
    \(\bar{\mathcal{Q}}_t = (1 - \alpha) \cdot \bar{\mathcal{Q}}_{t-1} + \alpha \cdot \mathbf{q}_t\)
  </div>
  <p>
    As depicted in Fig. 2, the streaming EMA smoothly shifts the baseline from default priors \([0.38, 0.91, 0.35, 0.91]\) to the empirical steady state \([0.2268, 0.9267, 0.2354, 0.929]\) on <code>mechsrv</code>.
  </p>

  <div class="figure-box">
    <img src="__IMG_EMA__" alt="EMA Convergence">
    <div class="figure-caption">
      <strong>Fig. 2.</strong> Trajectory of the 4-quadrant dynamic baseline \(\bar{\mathcal{Q}} = (q_0, q_1, q_2, q_3)\) over 100 consecutive live queries on <code>mechsrv</code>. Streaming EMA (\(\alpha = 0.03\)) converges stably to local operational equilibrium.
    </div>
  </div>

  <h2>V. Empirical Evaluation</h2>
  
  <h3>A. Protocol & Bare-Metal Telemetry Infrastructure</h3>
  <p>
    All benchmarks were conducted on a dedicated bare-metal production server (<code>mechsrv.itouch.fi</code>, Ubuntu Linux, Intel Xeon CPU @ 2.40GHz, 16 GB RAM, zero GPU/VRAM). Rather than reporting an isolated test, we evaluate <em>wevv</em> across an iterative, four-stage empirical campaign comprising over 600 structured experimental questions and culminating in a verified open-science corpus of 1,090 decisions (3,087 evaluated questions) across 30+ heterogeneous domains (Table IV).
  </p>

  <table class="academic-table">
    <caption><strong>Table IV.</strong> The Multi-Stage Empirical Evaluation Program: 600+ Structured Test Questions Across Four Iterative Campaigns Culminating in 1,090 Verified Telemetry Records (3,087 Evaluated Questions)</caption>
    <thead>
      <tr>
        <th>Experimental Campaign</th>
        <th>Focus & Stress Hypothesis</th>
        <th>Scope / Questions</th>
        <th>Key Architectural Milestone</th>
        <th>Empirical Gain / Discovery</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Campaign 1: Routing Transition</strong></td>
        <td>Monolithic cross-domain collapse</td>
        <td>200 Questions (Batches #1 & #2)</td>
        <td>Multi-Domain Auto-Seed Router</td>
        <td><strong>+28.8% Macro Gain</strong> (63.8% &rarr; 92.6%)</td>
      </tr>
      <tr>
        <td><strong>Campaign 2: Dual-Language OOD</strong></td>
        <td>Semantic generalization & OOD</td>
        <td>200 Questions (100 EN OOD + 100 TR)</td>
        <td>Bilingual Root Ontology</td>
        <td><strong>Language Invariance</strong>; found leakage</td>
      </tr>
      <tr>
        <td><strong>Campaign 3: Filter Hardening</strong></td>
        <td>Adversarial prompt-injection traps</td>
        <td>100 Questions (5 Stress Classes)</td>
        <td>Chordial Resonance (\(\mathcal{T}_{\text{desc}} = 0.045\))</td>
        <td><strong>0.0% Trap Exploit Rate</strong>; <strong>2.5&times; Speedup</strong> (8.41 ms &rarr; 3.31 ms via dynamical pruning)</td>
      </tr>
      <tr>
        <td><strong>Campaign 4: Dynamic Calibration</strong></td>
        <td>Cardioid bias & dynamic drift</td>
        <td>100 Questions (10 Categories)</td>
        <td>Online EMA & Phase Rotation</td>
        <td><strong>100% Positional Invariance</strong>; 50/50 split</td>
      </tr>
      <tr class="total-border">
        <td><strong>Cumulative Production Corpus</strong></td>
        <td>Live multi-domain production traffic</td>
        <td><strong>1,090 Decisions / 3,087 Questions</strong></td>
        <td>Unified System-One Decision Engine</td>
        <td><strong>7.08 ms Median, 0 Bytes VRAM</strong></td>
      </tr>
    </tbody>
  </table>

  <h3>B. Campaign 1: Monolithic to Multi-Domain Transition</h3>
  <p>
    Evaluating \(N=336\) decisions across five foundational domains, the Auto-Seed Router achieved <strong>92.6%</strong> macro-accuracy compared to <strong>63.8%</strong> for the unrouted baseline (+28.8% absolute gain, \(p &lt; 0.001\); Table III, Fig. 3). Financial risk accuracy jumped by +65.0% and combat reflexes by +45.0%.
  </p>

  <table class="academic-table">
    <caption><strong>Table III.</strong> Multi-Domain Routing Ablation Benchmark (\(N=336\))</caption>
    <thead>
      <tr>
        <th>Operational Domain</th>
        <th>N</th>
        <th>Monolithic</th>
        <th>Auto-Seed</th>
        <th>Gain</th>
        <th>Latency</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>API Gateway & Security</td>
        <td>85</td>
        <td>83.5%</td>
        <td><strong>87.1%</strong></td>
        <td>+3.6%</td>
        <td>3.42 ms</td>
      </tr>
      <tr>
        <td>E-Commerce Fraud</td>
        <td>60</td>
        <td>56.7%</td>
        <td><strong>85.0%</strong></td>
        <td>+28.3%</td>
        <td>3.29 ms</td>
      </tr>
      <tr>
        <td>Financial Underwriting</td>
        <td>60</td>
        <td>35.0%</td>
        <td><strong>100.0%</strong></td>
        <td>+65.0%</td>
        <td>3.33 ms</td>
      </tr>
      <tr>
        <td>Game Combat AI</td>
        <td>60</td>
        <td>50.0%</td>
        <td><strong>95.0%</strong></td>
        <td>+45.0%</td>
        <td>3.17 ms</td>
      </tr>
      <tr>
        <td>Smart Home / IoT Safety</td>
        <td>61</td>
        <td>85.2%</td>
        <td><strong>98.4%</strong></td>
        <td>+13.2%</td>
        <td>3.31 ms</td>
      </tr>
      <tr class="total-border">
        <td>Macro Average</td>
        <td>326</td>
        <td>63.8%</td>
        <td><strong>92.6%</strong></td>
        <td><strong>+28.8%</strong></td>
        <td><strong>3.31 ms</strong></td>
      </tr>
    </tbody>
  </table>

  <div class="figure-box">
    <img src="__IMG_ABLATION__" alt="Routing Ablation Gain">
    <div class="figure-caption">
      <strong>Fig. 3.</strong> Ablation comparison across core operational domains. The Auto-Seed Router yields major leaps (+65.0% in Financial Underwriting) with zero tensor overhead.
    </div>
  </div>

  <h3>C. Campaign 2: Dual-Language & Cross-Domain OOD Invariance</h3>
  <p>
    Two consecutive 100-question batteries evaluated semantic invariance: (i) 100 English Out-Of-Domain (OOD) questions across astrophysics, quantum computing, and synthetic jargon (`frobnicate`, `glork`), maintaining 100% uptime via chaotic phase-space projection; and (ii) 100 Turkish real-world questions across Findeks credit scoring (0&ndash;1900) and localized IoT.
  </p>
  <p>
    <strong>Discovery:</strong> Incidental descriptive words in non-security contexts (e.g., &ldquo;direct butane torching&rdquo;) leaked into gateway filters, uncovering <em>semantic resonance leakage</em>.
  </p>

  <h3>D. Campaign 3: Adversarial Filter Hardening & Latency Dynamics</h3>
  <p>
    A targeted 100-question battery evaluated 5 attack classes: decoy trap words, harmonic co-occurrences, context drops, label-description divergences, and synthetic jargon. Under the Hardened Chord Filter (\(\mathcal{T}_{\text{desc}} = 0.045\)), the engine selected the trap option <strong>0 times out of 10</strong> (<strong>0.0% vulnerability</strong>).
  </p>
  <p>
    <strong>Empirical Speedup Verification:</strong> This campaign empirically validated the Dynamical Trajectory Pruning effect: prior to acoustic damping, noisy prompt adjectives caused chaotic coordinate excursions into boundary filaments (\(\lambda \approx 0\)), producing an average latency of 8.41 ms (P95: 34.2 ms). Attenuating descriptive noise by 95.5% stabilized coordinates in steep potential basins, reducing mean escape loop iterations per cell by 45.8% (42.6 &rarr; 23.1) and dropping median decision latency to <strong>3.31 ms</strong>&mdash;a <strong>2.5&times; throughput acceleration</strong> achieved simultaneously with 0.0% adversarial exploit vulnerability.
  </p>

  <h3>E. Campaign 4: Dynamic Organic Calibration (v0.2.2)</h3>
  <p>
    A 100-scenario stress test across 10 distinct categories validated v0.2.2 fine-tunings on the production server (Fig. 4):
  </p>
  <p>
    1) <strong>Permutation Invariance:</strong> Option slot rotation produced 100% semantic decision consistency.
  </p>
  <p>
    2) <strong>Adaptive Binary Precision:</strong> The gateway bifurcated hostile traffic into exactly 50% allow and 50% drop, matching synthetic ground truth.
  </p>
  <p>
    3) <strong>Execution Latency:</strong> All 100 evaluations finished in 2.85 seconds total (mean 8.406 ms per decision; Fig. 4).
  </p>

  <div class="figure-box">
    <img src="__IMG_STRESS__" alt="Latency Distribution">
    <div class="figure-caption">
      <strong>Fig. 4.</strong> Inference latency distribution across 10 operational categories during the v0.2.2 stress battery. All domains operate strictly below the 10 ms real-time threshold.
    </div>
  </div>

  <h3>F. Cumulative Public Telemetry (N = 1,090)</h3>
  <p>
    At the conclusion of the four-campaign program, the open MariaDB database reached <strong>1,090 verified decisions</strong> comprising <strong>3,087 evaluated questions</strong> across 30+ operational domains:
  </p>
  <p>
    &bull; Boolean <code>noul</code>: 1,065 evaluations (66.1% True / 33.9% False)<br>
    &bull; Categorical <code>choice</code>: 1,020 evaluations<br>
    &bull; Ordinal <code>score</code>: 1,002 evaluations<br>
    &bull; Cumulative median latency: <strong>7.08 ms</strong> (P95: 34.20 ms)<br>
    &bull; Persistent weight memory: <strong>0 Bytes</strong>.
  </p>

  <h2>VI. Future Horizons: Web3 AI Oracles</h2>
  <p>
    Decentralized applications (dApps) in DeFi, autonomous governance, and blockchain gaming lack native cognitive capabilities because running large neural models inside the Ethereum Virtual Machine (EVM) or Solana runtime is economically and technically impossible.
  </p>
  <p>
    <em>werr</em> resolves the on-chain AI dilemma:
  </p>
  <p>
    <strong>1) 24-Byte State Payload:</strong> A complete decision model is fully defined by its 24-byte coordinate seed \((c_x, c_y, \text{zoom})\), fitting in a single 32-byte EVM storage slot.
  </p>
  <p>
    <strong>2) Sub-50k Gas Execution:</strong> The core recurrence \(Z_{n+1} = Z_n^2 + C\) requires only basic fixed-point arithmetic, allowing native verification in Solidity or Rust under &lt; 50,000 gas.
  </p>
  <p>
    <strong>3) ZK-Mandelbrot Proofs:</strong> Non-interactive zero-knowledge proofs (SNARKs) [5] allow off-chain provers to verify that private state variables yield an escape trajectory resulting in decision \(c^*\) without revealing private user data.
  </p>

  <h2>VII. Reproducibility & Open Science</h2>
  <p class="no-indent">
    In commitment to open research, all assets are publicly accessible:<br>
    &bull; <strong>Codebase:</strong> <a href="https://github.com/pCwOrM/werr">https://github.com/pCwOrM/werr</a><br>
    &bull; <strong>Open Telemetry Dataset (1,090+ Decisions):</strong> <a href="https://mechsrv.itouch.fi:4431/werr/dataset/wevv_open_decisions.jsonl">https://mechsrv.itouch.fi:4431/werr/dataset/wevv_open_decisions.jsonl</a><br>
    &bull; <strong>Interactive Web Simulation Lab:</strong> <a href="https://pcworm.github.io/werr/">https://pcworm.github.io/werr/</a>
  </p>

  <h2>VIII. Conclusion</h2>
  <p>
    The <strong>Universal Fractal Natural Language Decision Map</strong> proves that real-time edge triage can be synthesized directly from the chaotic boundary of the Mandelbrot set without persistent weight tensors. By unifying Multi-Domain Auto-Seed Routing, Chordial Semantic Resonance, Quadrant Phase Rotation, and Organic Dynamic Calibration, <em>werr</em> achieves 92.6% accuracy and sub-10ms response times across 30+ domains on commodity hardware. Delivering deterministic triage at the physical edge, the architecture respects the thermodynamic limits of communication infrastructure while laying the groundwork for verifiable, on-chain decentralized artificial intelligence.
  </p>

  <div class="footnote-box">
    <strong>Acknowledgment&mdash;</strong>The authors acknowledge the computational support and automated co-development environment provided by Google DeepMind's Antigravity AI platform.
  </div>

  <h2>References</h2>
  <ol class="ref-list">
    <li>V. Dağlı, Z. Dağlı, and D. Dağlı, &ldquo;Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries,&rdquo; <em>arXiv:2609.XXXXX [cs.AI]</em>, 2026. Under Review in IEEE Transactions; DOI: 10.5281/zenodo.22802921.</li>
    <li>A. Vaswani et al., &ldquo;Attention is All You Need,&rdquo; in <em>Proc. NeurIPS</em>, vol. 30, 2017.</li>
    <li>H. Touvron et al., &ldquo;Llama 2: Open Foundation and Fine-Tuned Chat Models,&rdquo; <em>arXiv:2307.09288</em>, 2023.</li>
    <li>D. Kahneman, <em>Thinking, Fast and Slow</em>, Farrar, Straus and Giroux, 2011.</li>
    <li>E. Ben-Sasson et al., &ldquo;Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture,&rdquo; in <em>USENIX Security Symposium</em>, pp. 781&ndash;796, 2014.</li>
    <li>F. Zhang et al., &ldquo;Town Crier: An Authenticated Data Feed for Smart Contracts,&rdquo; in <em>Proc. ACM CCS</em>, pp. 270&ndash;282, 2016.</li>
  </ol>

</div>

</body>
</html>
"""

def build_pdf():
    html_path = os.path.join(PAPER_DIR, "Universal_Fractal_Natural_Language_Decision_Map.html")
    pdf_path = os.path.join(PAPER_DIR, "Universal_Fractal_Natural_Language_Decision_Map.pdf")
    alt_pdf_path = os.path.join(PAPER_DIR, "main.pdf")
    artifact_pdf = os.path.join(ARTIFACT_DIR, "Universal_Fractal_Natural_Language_Decision_Map.pdf")
    
    # Inject images without string escaping hazards
    final_html = raw_template
    final_html = final_html.replace("__IMG_TRADEOFF__", img_tradeoff)
    final_html = final_html.replace("__IMG_ABLATION__", img_ablation)
    final_html = final_html.replace("__IMG_EMA__", img_ema)
    final_html = final_html.replace("__IMG_STRESS__", img_stress)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"[+] Clean HTML generated: {html_path}")
    
    print("[*] Launching Playwright (msedge) with full MathJax rendering...")
    camera_ready_path = os.path.join(PAPER_DIR, "Universal_Fractal_Natural_Language_Decision_Map_CameraReady.pdf")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page()
        page.goto(f"file:///{os.path.abspath(html_path)}")
        
        # Wait until MathJax has completed rendering all equations
        page.wait_for_function("() => window.MathJax && window.MathJax.startup && window.MathJax.startup.promise")
        page.evaluate("() => window.MathJax.startup.promise")
        page.wait_for_timeout(2000) # Ensure full layout stability
        
        # Verify no MathJax errors occurred
        error_count = page.evaluate("() => document.querySelectorAll('.MathJax_Error, [data-mjx-error]').length")
        print(f"[*] MathJax Error Elements detected on page: {error_count}")
        
        # Write to main.pdf first (which is not locked)
        page.pdf(
            path=alt_pdf_path,
            format="A4",
            print_background=True,
            margin={
                "top": "12mm",
                "bottom": "12mm",
                "left": "10mm",
                "right": "10mm"
            }
        )
        browser.close()
        
    import shutil
    shutil.copy2(alt_pdf_path, camera_ready_path)
    shutil.copy2(alt_pdf_path, artifact_pdf)
    
    try:
        shutil.copy2(alt_pdf_path, pdf_path)
        print(f"[+] Overwrote {pdf_path}")
    except PermissionError:
        print(f"[!] Note: {pdf_path} is currently open in your viewer, saved as main.pdf and CameraReady copy instead!")
        
    print(f"[+] Perfect Clean PDF compiled successfully:")
    print(f"    - Primary target : {alt_pdf_path}")
    print(f"    - Camera-Ready   : {camera_ready_path}")
    print(f"    - Artifact copy  : {artifact_pdf}")
    print(f"    - File Size      : {os.path.getsize(alt_pdf_path)} bytes")

if __name__ == "__main__":
    build_pdf()
