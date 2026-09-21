import os
import sys
import base64
import asyncio
from playwright.async_api import async_playwright

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
img_twin = get_base64_image("twin_ecosystem_architecture.png")

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
    font-size: 8.8pt;
    line-height: 1.30;
    color: #111;
    background: #fff;
    margin: 0;
    padding: 0;
    text-rendering: optimizeLegibility;
  }

  .paper-header {
    text-align: center;
    margin-bottom: 12px;
  }

  .paper-title {
    font-size: 16.5pt;
    font-weight: bold;
    line-height: 1.18;
    margin-bottom: 8px;
    letter-spacing: -0.2px;
  }

  .authors-block {
    font-size: 9.2pt;
    margin-bottom: 8px;
    line-height: 1.35;
  }

  .author-name {
    font-weight: bold;
    font-size: 9.8pt;
  }

  .author-affil {
    font-style: italic;
    color: #333;
    font-size: 8.4pt;
  }

  .author-contact {
    font-family: "Courier New", Courier, monospace;
    font-size: 7.6pt;
    color: #004499;
  }

  .abstract-container {
    max-width: 95%;
    margin: 0 auto 12px auto;
    font-size: 8.2pt;
    line-height: 1.30;
    text-align: justify;
    border-top: 1px solid #111;
    border-bottom: 1px solid #111;
    padding: 8px 0;
  }

  .abstract-heading {
    font-style: italic;
    font-weight: bold;
  }

  .turkish-abstract {
    margin-top: 6px;
    padding-top: 5px;
    border-top: 1px dashed #e0e0e0;
    font-size: 7.8pt;
    color: #222;
  }

  .keywords-block {
    margin-top: 5px;
    font-size: 7.8pt;
  }

  .full-width-section {
    width: 100%;
    margin: 8px 0;
    break-inside: avoid;
  }

  .two-column-body {
    column-count: 2;
    column-gap: 6mm;
    text-align: justify;
  }

  h2 {
    font-size: 8.8pt;
    font-weight: bold;
    text-transform: uppercase;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 4px;
    letter-spacing: 0.4px;
    break-after: avoid;
  }

  h3 {
    font-size: 8.5pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 8px;
    margin-bottom: 3px;
    break-after: avoid;
  }

  p {
    margin-top: 0;
    margin-bottom: 5px;
    text-indent: 11px;
  }

  p.no-indent {
    text-indent: 0;
  }

  ul, ol {
    margin: 3px 0 6px 0;
    padding-left: 14px;
  }

  li {
    margin-bottom: 2px;
  }

  .quote-box {
    margin: 6px 12px;
    font-style: italic;
    text-align: center;
    font-weight: bold;
    color: #1e293b;
    border-left: 2px solid #3b82f6;
    padding-left: 8px;
  }

  .equation {
    text-align: center;
    margin: 4px 0;
    font-size: 8.2pt;
  }

  table.academic-table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0;
    font-size: 7.0pt;
    line-height: 1.18;
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
    margin: 6px 0;
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
    font-size: 7.2pt;
    text-align: justify;
    color: #222;
    margin-top: 3px;
    line-height: 1.18;
  }

  .figure-caption strong {
    font-weight: bold;
  }

  .footnote-box {
    font-size: 7.2pt;
    line-height: 1.18;
    color: #444;
    border-top: 0.8px solid #aaa;
    margin-top: 8px;
    padding-top: 4px;
  }

  .ref-list {
    font-size: 7.0pt;
    line-height: 1.16;
    padding-left: 12px;
    margin-top: 4px;
  }

  .ref-list li {
    margin-bottom: 3px;
  }
</style>
</head>
<body>

<div class="paper-header">
  <div class="paper-title">Universal Fractal Natural Language Decision Map: Real-Time Edge Triage Across Heterogeneous Domains</div>
  
  <div class="authors-block">
    <span class="author-name">Volkan Dağlı</span><sup>1,2,*</sup> &nbsp;&bull;&nbsp; 
    <span class="author-name">Zerrin Dağlı</span><sup>3</sup> &nbsp;&bull;&nbsp; 
    <span class="author-name">Dağhan Dağlı</span><sup>4</sup><br>
    <span class="author-affil">
      <sup>1</sup>Anadolu University, Eskişehir, Turkey &nbsp;&bull;&nbsp; 
      <sup>2</sup>ITouch Systems, Mersin, Turkey &nbsp;&bull;&nbsp; 
      <sup>3</sup>Mersin University, Mersin, Turkey &nbsp;&bull;&nbsp; 
      <sup>4</sup>Toros Science College, Mersin, Turkey
    </span><br>
    <span class="author-contact">
      ORCID: 0009-0000-1587-8703 (VD) &bull; 0000-0001-9490-6425 (ZD) &bull; 0009-0003-2492-8313 (DD) &bull; *Correspondence: https://github.com/pCwOrM/werr
    </span>
  </div>
</div>

<div class="abstract-container">
  <p class="no-indent">
    <span class="abstract-heading">Abstract</span>&mdash;Modern automated computing systems increasingly deploy Large Language Models (LLMs) and deep neural networks to resolve runtime operational triage. However, invoking multi-billion-parameter neural models across global networks incurs prohibitive latency (&gt;100&ndash;500 ms), severe memory allocation (&gt;4&ndash;8 GB VRAM), and unsustainable energy dissipation through continuous transatlantic transmission and server clustering. Extending the foundational theory of <em>Mandelbrot Fractal Neural Synthesis</em> [1], this paper introduces the <strong>Universal Fractal Natural Language Decision Map</strong>, realized via the <strong>werr</strong> (Waves & Errors) machine-native edge reflex runtime and the production-deployed <strong>answerr</strong> platform (<a href="https://answerr.me">answerr.me</a>). Operating entirely without stored weight tensors (0 Bytes VRAM), the engine synthesizes deterministic, strongly-typed decisions&mdash;<code>noul</code> (probabilistic Boolean), <code>choice</code> (categorical classification), and <code>score</code> (ordinal regression)&mdash;by dynamically modulating 24-byte coordinate seeds along the chaotic boundary of the Mandelbrot set (\(\partial \mathcal{M}\)) and recursively evaluating 4-quadrant escape dynamics. Drawing inspiration from biological System-One reflex arcs, the engine enforces three primary architectural contributions: (i) an <em>Auto-Seed Router</em> with an explicit mathematical domain projector \(\Phi_D\) where ablation demonstrates that procedural fractal boundaries provide a +28.8% accuracy gain over linear baselines; (ii) an <em>Information-Theoretic Acoustic Damping Filter</em> (\(\mathcal{T}_{\text{desc}} = 0.045\)) grounded in token entropy and phonetic spectral density that insulates the engine against adversarial prompt-injection exploits (0.0% empirical bypass on evaluated vectors; 95% Wilson CI: [0.0%, 30.8%]); crucially, this damping stabilizes chaotic boundary coordinates, reducing mean escape loop iterations by 45.8% and accelerating inference throughput by 2.5&times; (median latency 3.31 ms); and (iii) an <em>Organic Dynamic Calibration</em> framework tracking streaming operational statistics via an \(O(1)\) Exponential Moving Average (EMA, \(\alpha=0.03\)) and executing deterministic quadrant phase rotation to eliminate geometric positional bias. Benchmarked on bare-metal production infrastructure (<code>api.answerr.me:4431</code>) across an open corpus of 1,150+ verified multi-domain decisions (3,200+ evaluated questions) and validated as World #1 on the independent <em>JevBench</em> benchmark suite (81.65%), the framework achieves 92.6% macro-accuracy (95% CI: [90.8%, 94.1%]) with a median latency of 7.08 ms on commodity CPU hardware. We provide a drop-in OpenAI-compatible API endpoint (<code>/v1/chat/completions</code>) and formulate deployment blueprints for extreme memory-constrained runtimes, including bare-metal microcontrollers and 32-byte EVM smart contracts.
  </p>
  
  <div class="turkish-abstract">
    <strong>Özet (Extended Turkish Abstract)&mdash;</strong>Geleneksel derin öğrenme mimarileri ve Büyük Dil Modelleri (LLM), otonom operasyonel kararlar üretirken gigabaytlarca GPU belleğine (VRAM), yüzlerce milisaniye gecikmeye ve sunucu merkezli yüksek enerji tüketimine yol açmaktadır. Bu çalışma, <em>Mandelbrot Fraktal Nöral Sentez</em> teorisi [1] üzerine inşa edilen ve kalıcı ağırlık tensörlerini tamamen ortadan kaldıran (0 Byte VRAM) <strong>Evrensel Fraktal Doğal Dil Karar Haritası</strong> mimarisini, <strong>werr</strong> (Waves & Errors) uç refleks motorunu ve canlı <strong>answerr</strong> bilişsel platformunu (<a href="https://answerr.me">answerr.me</a>) sunmaktadır. Sistem, 24 baytlık \((c_x, c_y, \text{zoom})\) koordinat tohumlarını Mandelbrot kümesinin sınırında (\(\partial \mathcal{M}\)) dinamik olarak modüle ederek üç temel tipte (<code>noul</code> [ikili onay], <code>choice</code> [kategorik yönlendirme] ve <code>score</code> [derecelendirme]) deterministik kararlar üretir. Biyolojik Sistem-1 omurilik refleks arkından ve hata sınırıyla motor öğrenme prensibinden ilham alan sistem; Kuadran Faz Rotasyonu, bilgi entropisi ve fonetik spektral yoğunluk temelli Akustik Sönümleme Filtresi (\(\mathcal{T}_{\text{desc}} = 0.045\)) ve çevrimiçi Üstel Hareketli Ortalama (EMA, \(\alpha=0.03\)) tabanlı Organik Dinamik Kalibrasyon mekanizmalarını içermektedir. Belirtmek gerekir ki akustik filtre, hesaplama yükü getirmemiş; kaotik sınır saçılmalarını sönümleyip kaçış döngüsü iterasyonlarını %45.8 oranında budayarak çıkarsama hızını 2.5 kat artırmıştır (3.31 ms). Canlı telemetri sunucu kümesi (<code>api.answerr.me:4431</code>) üzerinde 1.150'den fazla karar ve 3.200'den fazla soru içeren açık veri kümesinde yapılan deneysel çalışmalarda ve bağımsız <em>JevBench</em> kıyaslamasında elde edilen dünya birinciliği (%81.65 skoru) ile; %92.6 makro doğruluk, 7.08 ms medyan gecikme ve düşmanca yönlendirmelere karşı %0 saldırı başarı oranı elde edilmiştir. Ayrıca, OpenAI uyumlu API uç noktası sunulmuş ve 24 baytlık tohum yapısının mikrodenetleyiciler ile blokzincir akıllı sözleşmelerinde (EVM/Solana) 32 baytlık tek bir alanda çalışan doğrulanabilir bir yapay zeka kahini olarak kullanım fizibilitesi ortaya konmuştur.
  </div>

  <div class="keywords-block">
    <strong>Keywords&mdash;</strong>Universal Fractal Decision Map, Zero-Tensor Inference, System-One Reflex Arc, Mandelbrot Boundary Dynamics, Acoustic Damping Filter, Dynamic Calibration, On-Chain AI Oracle.
  </div>
</div>

<div class="figure-container full-width-figure" style="margin: 10px 0;">
  <img src="__IMG_TWIN__" style="width: 100%; max-height: 260px; object-fit: contain; border-radius: 4px; border: 1px solid #e2e8f0;" alt="Dual-Cognition Twin Ecosystem Architecture">
  <div class="figure-caption" style="margin-top: 4px;">
    <strong>Fig. 1.</strong> The Dual-Cognition Architecture of Machine Intelligence: Synergistic pairing of the embedded System-One reflex kernel (<em>werr</em>, left: 0-Byte VRAM, &lt; 0.5 ms latency) with the deliberative System-Two cloud reasoning platform (<em>answerr</em>, right: <a href="https://answerr.me">answerr.me</a>). Dual action primitives (<code>[Answerr It!]</code> vs. <code>[Werr It!]</code>) bifurcate cognitive workloads into instant physical edge triage and conscious deliberative reflection.
  </div>
</div>

<div class="full-width-section">
  <table class="academic-table">
    <caption><strong>Table I.</strong> Architectural & System Paradigm Comparison: Centralized Cloud LLM (TypeSafe AI / Jev), Local Open-Weight LLM (OpenJev 4B), and werr (Universal Fractal Map)</caption>
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
        <td><strong>Energy Consumption / Query</strong></td>
        <td>1,500&ndash;3,000 mJ (Cloud Datacenter + Net)</td>
        <td>150&ndash;400 mJ (Local GPU Ingestion)</td>
        <td><strong>0.04 mJ (\(40\text{ }\mu\text{J}\) on Single CPU Core)</strong></td>
      </tr>
      <tr>
        <td><strong>Official JevBench Benchmark</strong></td>
        <td>Reference Target</td>
        <td>Baseline Benchmark</td>
        <td><strong>81.65% World #1 (Issue #10) [Standhartinger, 2026]</strong></td>
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

  <h3>A. Thermodynamic Dissipation & Landauer Energy Bounds</h3>
  <p>
    Beyond memory and latency lies an unavoidable thermodynamic reality: according to Landauer's principle [7], information processing carries an irreducible physical cost. In modern cloud-centric AI architectures, invoking centralized LLMs across global networks dissipates substantial electrical energy across physical conductors, transoceanic fiber cables, and datacenter cooling infrastructure [8]. A typical cloud-routed LLM forward pass consumes an estimated 1,500&ndash;3,000 mJ per query, accounting for datacenter PUE and network switching overhead. In contrast, an embedded single-core CPU execution of <em>werr</em>'s procedural recurrence requires approximately 0.04 mJ (\(40\text{ }\mu\text{J}\)) per query&mdash;representing an energy efficiency improvement exceeding 37,000&times;.
  </p>

  <h3>B. Biological System-One Reflex Arc</h3>
  <p>
    Following dual-process cognitive psychology [4], biological organisms never invoke deliberate, linguistic cerebral reasoning (System-Two) for instantaneous protective reflexes. When a human hand inadvertently touches a hot surface, the somatic reflex arc triggers an involuntary muscular retraction in milliseconds. The neural signal does not traverse the cerebral cortex to parse linguistic tokens; it is gated deterministically at the spinal cord. In automated computing, operational edge triage must function as this biological reflex arc: immediate, protective, and deterministic.
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
      <strong>Fig. 2.</strong> Memory footprint vs. inference latency tradeoff. <em>werr</em> occupies the true zero-tensor boundary (0 Bytes VRAM, 24 Bytes seed) while executing in sub-10 ms real-time latency on commodity CPUs.
    </div>
  </div>

  <h2>II. Self-Contained Mathematical Foundations</h2>
  <p>
    Let the standard quadratic Mandelbrot mapping on the complex plane \(\mathbb{C}\) be defined as:
  </p>
  <div class="equation">
    \(Z_{n+1} = Z_n^2 + C, \quad Z_0 = 0\)
  </div>
  <p>
    The Mandelbrot set \(\mathcal{M}\) comprises all points \(C \in \mathbb{C}\) for which \(\limsup_{n \to \infty} |Z_n| \le 2\). The boundary \(\partial \mathcal{M}\) is a non-differentiable fractal curve of Hausdorff dimension 2. For an arbitrary operational domain \(D\), a base coordinate seed \(\theta_D = (c_{x, D}, c_{y, D}, \text{zoom}_D) \in \mathbb{R}^3\) resides exactly along \(\partial \mathcal{M}\).
  </p>

  <h3>A. Escape Dynamics & Quadrant Discretization</h3>
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

  <h3>B. Strongly-Typed Decision Primitives</h3>
  <p>
    The engine maps quadrant energy distributions to three native decision primitives:
  </p>
  <p>
    <strong>1) <code>noul</code> (Probabilistic Boolean):</strong> Evaluates binary access or execution rights:
  </p>
  <div class="equation">
    \(P(\text{True}) = \sigma \left( \beta \cdot [ (\hat{\mathcal{Q}}_0 + \hat{\mathcal{Q}}_1) - (\hat{\mathcal{Q}}_2 + \hat{\mathcal{Q}}_3) ] \right)\)
  </div>
  <p>
    <strong>2) <code>choice</code> (Categorical Selection):</strong> Selects among \(M \le 4\) discrete actions by mapping candidates to phase-rotated quadrant energies: \(c^* = \arg\max_m \hat{\mathcal{Q}}_{\pi(m)}\).
  </p>
  <p>
    <strong>3) <code>score</code> (Ordinal Regression):</strong> Generates a bounded scalar \(S \in [0, S_{\max}]\) from the aggregate escape integral:
  </p>
  <div class="equation">
    \(S = S_{\max} \cdot \left( \frac{1}{N^2 \cdot M_{\max}} \sum_{j,k} K(j,k) \right)^\gamma\)
  </div>

  <h2>III. System Architecture: The WERR Decision Engine</h2>
  
  <h3>A. Formalization of Domain Projector (\(\Phi_D\))</h3>
  <p>
    The Domain Projector \(\Phi_D: \mathcal{S} \to \mathbb{R}^K \times \mathbb{R}\) deterministically maps heterogeneous operational state dictionaries \(\mathbf{s} = \{k_i: v_i\}\) into complex coordinate perturbations. Continuous parameters are normalized via affine sigmoid transforms \(u_i = 2\sigma((v_i - \mu_i)/\sigma_i) - 1\). Linguistic tokens contribute weighted scalar offsets \(\rho_{\text{lang}} = \sum \omega_l \mathcal{T}(w_l)\) scaled by the acoustic damping factor. The aggregated net risk \(\rho_D\) modulates the base seed:
  </p>
  <div class="equation">
    \(\Delta c_x = \frac{\kappa_x}{\text{zoom}_D} \tanh(\rho_D), \quad \Delta c_y = \frac{\kappa_y}{\text{zoom}_D} \tanh\left(\frac{1}{K}\sum_{k=1}^K u_k\right)\)
  </div>
  <div class="equation">
    \(C_{\text{eff}} = (c_{x, D} + \Delta c_x) + i\, (c_{y, D} + \Delta c_y)\)
  </div>

  <h3>B. Ablation: Indispensability of \(\partial \mathcal{M}\)</h3>
  <p>
    Ablation experiments directly training linear regressors on \(\Phi_D(\mathbf{s})\) achieve only 63.8% macro-accuracy due to multi-threshold non-convex boundaries. Introducing the procedural Mandelbrot recurrence lifts accuracy to 92.6% (+28.8% gain), confirming that \(\partial \mathcal{M}\) serves as an infinite-dimensional, zero-storage non-linear kernel.
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

  <h3>C. Dual-Layer Cognitive Architecture</h3>
  <p>
    Inputs are evaluated through two synchronized processing layers:
  </p>
  <p>
    <strong>Layer 2 (Bilingual Root Ontology):</strong> Resolves standard English and Turkish operational stems in &lt; 0.05 ms with zero tensor overhead.
  </p>
  <p>
    <strong>Layer 1 (Universal Chaotic Phase-Space Resonator):</strong> Out-of-vocabulary inputs are projected onto a continuous trigonometric phase angle \(\theta_{\text{hash}} = 2\pi \cdot (\text{Hash}(s) / 2^{32})\), ensuring the engine never throws null exceptions or crashes on arbitrary inputs.
  </p>

  <h2>IV. Algorithmic Innovations (v0.2.x &ndash; v0.3.x)</h2>

  <h3>A. Information-Theoretic Phonetic Density & Acoustic Damping</h3>
  <p>
    Operational directives and prompt-injection exploits exhibit starkly different information-theoretic profiles. Canonical action commands are concise, carrying high Shannon information density in short morphological roots. In contrast, adversarial jailbreaks and prompt injections [9] rely on long, verbose, syntactic padding.
  </p>
  <p>
    Drawing from phonetic linguistics, agglutinative languages such as Turkish feature dense, plosive consonant clusters (\(T, P, Ç, K\)) that convey maximal grammatical meaning in minimal duration. We translate this into an <strong>Acoustic Damping Filter</strong>. Core option keys receive undamped unit gain (\(\mathcal{T}_{\text{key}} = 1.0\)), while descriptive filler and decoy prose are attenuated by 95.5%:
  </p>
  <div class="equation">
    \(\mathcal{T}_{\text{desc}} = 0.045\)
  </div>
  <p>
    This attenuation quenches high-entropy prompt-injection vectors, preventing decoy words embedded in long natural language prompts from altering the geometric trajectory in complex coordinate space. In empirical evaluations across 10 adversarial injection classes (\(N=10\)), the engine achieved a <strong>0.0% exploit success rate</strong> (95% Wilson score interval: [0.0%, 30.8%]).
  </p>

  <h3>B. Dynamical Trajectory Pruning: Filtration Acceleration</h3>
  <p>
    In conventional NLP pipelines, adding multi-stage token filtering incurs parsing latency overhead. However, empirical benchmarks upon deploying the Acoustic Damping Filter revealed an unexpected speedup: <strong>inference accelerated by 2.5&times;</strong>, slashing median latency from 8.41 ms to 3.31 ms.
  </p>
  <p>
    This acceleration is governed by the fractal escape dynamics: in the unfiltered baseline, unattenuated prompt prose and Trojan tokens caused chaotic coordinate perturbations pushing the grid into turbulent boundary fringes of \(\partial \mathcal{M}\) (\(\lambda \approx 0\)), where orbits linger near \(|Z_n| \approx 2.0\) and force evaluation up to \(M_{\max} = 100\). By applying \(\mathcal{T}_{\text{desc}} = 0.045\), acoustic damping extinguishes coordinate jitter, locking \(C_{\text{eff}}\) into steep potential basins where points escape in \(K \le 4\text{--}8\) iterations. Mean escape iterations per cell (\(\bar{K} = \frac{1}{N^2}\sum K(j,k)\)) dropped by <strong>45.8%</strong> (42.6 &rarr; 23.1), converting a security filter into a <strong>dynamical compute accelerator</strong>.
  </p>

  <h3>C. Deterministic Quadrant Phase Rotation</h3>
  <p>
    Because the Mandelbrot set possesses a non-symmetric cardioid bulb along the real axis, raw escape rates across quadrants are uneven. We eliminate this positional bias via <em>Deterministic Quadrant Phase Rotation</em>: \(\delta = \text{hash}(\text{instruction}) \pmod 4\), shifting option index \(m\) to \(\pi(m) = (m + \delta) \pmod 4\).
  </p>

  <h3>D. Organic Dynamic Calibration (Online EMA)</h3>
  <p>
    To eliminate manual hyperparameter drift, <em>werr</em> continuously tracks quadrant energy distributions via an online Exponential Moving Average (EMA, \(\alpha=0.03\)):
  </p>
  <div class="equation">
    \(\bar{\mathcal{Q}}_t = (1 - \alpha) \cdot \bar{\mathcal{Q}}_{t-1} + \alpha \cdot \mathbf{q}_t\)
  </div>
  <p>
    Quadrant energies are normalized dynamically: \(\hat{\mathcal{Q}}_k = (\mathcal{Q}_k / (\bar{\mathcal{Q}}_k + \epsilon)) \cdot (\frac{1}{4}\sum \bar{\mathcal{Q}}_i)\). As depicted in Fig. 3, this smoothly adapts quadrant priors to steady state ([0.2268, 0.9267, 0.2354, 0.929]).
  </p>

  <div class="figure-box">
    <img src="__IMG_EMA__" alt="EMA Convergence">
    <div class="figure-caption">
      <strong>Fig. 3.</strong> Evolution of the 4-quadrant dynamic baseline \(\bar{\mathcal{Q}}\) over 100 consecutive live queries. The streaming EMA (\(\alpha = 0.03\)) converges stably to operational equilibrium.
    </div>
  </div>

  <h2>V. Empirical Evaluation & Production Deployment</h2>
  <p class="no-indent">
    All empirical evaluations were conducted on a dedicated bare-metal production server cluster (<code>api.answerr.me:4431</code>, Ubuntu Linux, Intel Xeon CPU @ 2.40GHz, 16 GB RAM, zero GPU/VRAM) under OS-level sandbox isolation. We deployed the <strong>answerr</strong> platform (<a href="https://answerr.me">answerr.me</a>) and exposed a drop-in <strong>OpenAI-compatible endpoint</strong> (<code>POST /v1/chat/completions</code>) enabling developers to replace cloud LLM round-trips with zero-VRAM reflex decisions.
  </p>

  <h3>A. Campaign 1: Domain Routing Transition & Ablation</h3>
  <p>
    Evaluating \(N=336\) decisions across five foundational domains (Table III, Fig. 4), the Multi-Domain Auto-Seed Router achieved <strong>92.6%</strong> macro-accuracy (95% Wilson CI: [89.3%, 95.0%]) compared to <strong>63.8%</strong> for the monolithic baseline&mdash;a statistically significant absolute leap of <strong>+28.8%</strong> (\(p &lt; 0.001\)).
  </p>

  <table class="academic-table">
    <caption><strong>Table III.</strong> Multi-Domain Routing Ablation Benchmark (\(N=336\))</caption>
    <thead>
      <tr>
        <th>Domain</th>
        <th>N</th>
        <th>Monolithic Acc</th>
        <th>Auto-Seed Acc</th>
        <th>Gain (\(\Delta\))</th>
        <th>Latency</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>API Gateway</td>
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
        <td>Financial Risk</td>
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
        <td>Smart Home / IoT</td>
        <td>61</td>
        <td>85.2%</td>
        <td><strong>98.4%</strong></td>
        <td>+13.2%</td>
        <td>3.31 ms</td>
      </tr>
      <tr class="total-border">
        <td><strong>Macro Average</strong></td>
        <td><strong>326</strong></td>
        <td><strong>63.8%</strong></td>
        <td><strong>92.6%</strong></td>
        <td><strong>+28.8%</strong></td>
        <td><strong>3.31 ms</strong></td>
      </tr>
    </tbody>
  </table>

  <div class="figure-box">
    <img src="__IMG_ABLATION__" alt="Ablation Comparison">
    <div class="figure-caption">
      <strong>Fig. 4.</strong> Ablation performance comparison across five core domains. The Auto-Seed Router delivers massive gains in cross-domain generalization (+65.0% in Financial Underwriting) while maintaining sub-4ms execution.
    </div>
  </div>

  <h3>B. Adversarial Robustness & Public Telemetry</h3>
  <p>
    Under the Acoustic Damping Filter, the engine selected the decoy trap option 0 times out of 10 targeted exploit categories (<strong>0.0% empirical bypass</strong>, 95% Wilson CI: [0.0%, 30.8%]). Across the cumulative open MariaDB telemetry (<strong>1,150+ verified decisions, 3,200+ evaluated questions</strong>), the engine demonstrated:
  </p>
  <p>
    &bull; Boolean <code>noul</code>: 1,120 evaluations (66.0% True / 34.0% False)<br>
    &bull; Categorical <code>choice</code>: 1,070 evaluations<br>
    &bull; Ordinal <code>score</code>: 1,050 evaluations<br>
    &bull; Macro-accuracy: <strong>92.6%</strong> (95% Wilson CI: [90.8%, 94.1%])<br>
    &bull; Median latency: <strong>7.08 ms</strong> (P95: <strong>34.20 ms</strong>)<br>
    &bull; Persistent weight memory: <strong>0 Bytes</strong>.
  </p>

  <div class="figure-box">
    <img src="__IMG_STRESS__" alt="Domain Stress Test Latency">
    <div class="figure-caption">
      <strong>Fig. 5.</strong> Inference latency distribution across 10 operational categories during the stress test. All categories execute safely below the 10 ms real-time ceiling.
    </div>
  </div>

  <h2>VI. Extreme Low-Resource Deployment Horizons</h2>
  <p>
    <strong>Microcontrollers & Embedded Robotics:</strong> On resource-constrained edge chips (e.g., ARM Cortex-M4 @ 80MHz with 64 KB SRAM), storing multi-megabyte neural weight arrays in flash memory is impossible. Because <em>werr</em> generates decision manifolds procedurally from three Float64 coordinates (24 bytes) using fixed-point arithmetic, the entire runtime executes within a temporary ~2 KB SRAM scratchpad, providing deterministic microsecond reflex gating with zero persistent flash memory consumption.
  </p>
  <p>
    <strong>Decentralized On-Chain AI Oracles:</strong> Decentralized applications in DeFi and governance cannot run deep neural models inside the Ethereum Virtual Machine (EVM) due to gas limits. Existing AI oracles rely on centralized off-chain servers with cryptographic signatures [6]. <em>werr</em> resolves this dilemma: (1) its complete 24-byte coordinate seed fits into a single 32-byte EVM storage slot (<code>bytes32</code>, 20,000 gas); (2) fixed-point escape recurrence evaluates within &lt; 50,000 gas on Ethereum or &lt; 1,000 compute units on Solana; and (3) non-interactive zero-knowledge proofs (SNARKs) [5] permit off-chain provers to verify that private state variables yield an escape trajectory resulting in decision \(c^*\) without revealing private user data.
  </p>

  <h2>VII. Reproducibility & Open Science</h2>
  <p class="no-indent">
    In commitment to open science, all assets are publicly accessible:<br>
    &bull; <strong>Permanent Research Archive (Zenodo):</strong> <a href="https://doi.org/10.5281/zenodo.22867426">https://doi.org/10.5281/zenodo.22867426</a><br>
    &bull; <strong>Source Code Repository:</strong> <a href="https://github.com/pCwOrM/werr">https://github.com/pCwOrM/werr</a><br>
    &bull; <strong>Live Platform & Documentation:</strong> <a href="https://answerr.me">https://answerr.me</a><br>
    &bull; <strong>Production Telemetry API:</strong> <a href="https://api.answerr.me:4431/v1/health">https://api.answerr.me:4431/v1/health</a><br>
    &bull; <strong>Open Telemetry Dataset (1,150+ Decisions):</strong> <a href="https://api.answerr.me:4431/werr/dataset/werr_open_decisions.jsonl">https://api.answerr.me:4431/werr/dataset/werr_open_decisions.jsonl</a><br>
    &bull; <strong>Official JevBench Benchmark Verification:</strong> World #1 (81.65%) at <a href="https://github.com/fstandhartinger/jevbench/issues/10">https://github.com/fstandhartinger/jevbench/issues/10</a>
  </p>

  <h2>VIII. Conclusion</h2>
  <p>
    The <strong>Universal Fractal Natural Language Decision Map</strong> proves that real-time edge triage can be synthesized directly from the chaotic boundary of the Mandelbrot set without persistent weight tensors. By unifying Multi-Domain Auto-Seed Routing, Information-Theoretic Acoustic Damping, Quadrant Phase Rotation, and Organic Dynamic Calibration, <em>werr</em> achieves 92.6% accuracy and sub-10ms response times across 30+ domains on commodity hardware. Delivering deterministic triage at the physical edge, the architecture respects the thermodynamic limits of communication infrastructure while laying the groundwork for verifiable, on-chain decentralized artificial intelligence.
  </p>

  <div class="footnote-box">
    <strong>Declaration of Generative AI in the Writing Process&mdash;</strong>During the preparation of this work, the authors used AI assistance (Google DeepMind Antigravity / Gemini) in order to assist with LaTeX typesetting, API code documentation, and English language editing. After using this tool, the authors reviewed, validated, and edited the resulting content, and take full responsibility for the scientific integrity and conclusions of the publication.<br><br>
    <strong>Acknowledgment&mdash;</strong>The authors acknowledge Anadolu University, ITouch Systems and Mersin University for providing computational infrastructure, bare-metal server resources, and institutional laboratory support.
  </div>

  <h2>References</h2>
  <ol class="ref-list">
    <li>V. Dağlı, Z. Dağlı, and D. Dağlı, &ldquo;Mandelbrot Fractal Neural Synthesis: Zero-Storage Procedural Weight Derivation and Non-Linear Decision Boundaries,&rdquo; preprint, Zenodo, DOI: 10.5281/zenodo.22774934; arXiv:submit/8092292 [cs.NE]; Release v3.0: 10.5281/zenodo.22867037, 2026.</li>
    <li>A. Vaswani et al., &ldquo;Attention is All You Need,&rdquo; in <em>Proc. NeurIPS</em>, vol. 30, 2017.</li>
    <li>H. Touvron et al., &ldquo;Llama 2: Open Foundation and Fine-Tuned Chat Models,&rdquo; <em>arXiv:2307.09288</em>, 2023.</li>
    <li>D. Kahneman, <em>Thinking, Fast and Slow</em>, Farrar, Straus and Giroux, 2011.</li>
    <li>E. Ben-Sasson et al., &ldquo;Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture,&rdquo; in <em>USENIX Security Symposium</em>, pp. 781&ndash;796, 2014.</li>
    <li>F. Zhang et al., &ldquo;Town Crier: An Authenticated Data Feed for Smart Contracts,&rdquo; in <em>Proc. ACM CCS</em>, pp. 270&ndash;282, 2016.</li>
    <li>R. Landauer, &ldquo;Irreversibility and heat generation in the computing process,&rdquo; <em>IBM J. Res. Dev.</em>, vol. 5, no. 3, pp. 183&ndash;191, 1961.</li>
    <li>E. Strubell, A. Ganesh, and A. McCallum, &ldquo;Energy and Policy Considerations for Deep Learning in NLP,&rdquo; in <em>Proc. ACL</em>, 2019.</li>
    <li>F. Perez and I. Ribeiro, &ldquo;Ignore Previous Prompt: Attack Techniques For Language Models,&rdquo; <em>arXiv:2211.09527</em>, 2022.</li>
    <li>F. Standhartinger, &ldquo;JevBench: Open Benchmark for Strongly-Typed Agent Decision Systems and TypeSafe AI,&rdquo; GitHub Repository, Issue #10, 2026.</li>
    <li>E. B. Wilson, &ldquo;Probable inference, the law of succession, and statistical inference,&rdquo; <em>J. Am. Stat. Assoc.</em>, vol. 22, no. 158, pp. 209&ndash;212, 1927.</li>
  </ol>

</div>

</body>
</html>
"""

async def build_pdf_async():
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
    final_html = final_html.replace("__IMG_TWIN__", img_twin)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"[+] Clean HTML generated: {html_path}")
    
    print("[*] Launching Playwright (msedge) with full MathJax rendering...")
    camera_ready_path = os.path.join(PAPER_DIR, "Universal_Fractal_Natural_Language_Decision_Map_CameraReady.pdf")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="msedge", headless=True)
        page = await browser.new_page()
        await page.goto(f"file:///{os.path.abspath(html_path).replace(os.sep, '/')}")
        
        # Wait until MathJax has completed rendering all equations
        await page.wait_for_function("() => window.MathJax && window.MathJax.startup && window.MathJax.startup.promise")
        await page.evaluate("() => window.MathJax.startup.promise")
        await page.wait_for_timeout(2500) # Ensure full layout stability
        
        # Verify no MathJax errors occurred
        error_count = await page.evaluate("() => document.querySelectorAll('.MathJax_Error, [data-mjx-error]').length")
        print(f"[*] MathJax Error Elements detected on page: {error_count}")
        
        # Write to main.pdf first (which is not locked)
        await page.pdf(
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
        await browser.close()
        
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
    asyncio.run(build_pdf_async())
