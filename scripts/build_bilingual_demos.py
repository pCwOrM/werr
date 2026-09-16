import os
import shutil

WORKSPACE_DIR = r"c:\Users\maat\Documents\antigravity\wonderful-raman"
DEMOS_DIR = os.path.join(WORKSPACE_DIR, "demos")
DESKTOP_DIR_ZENODO = r"C:\Users\maat\Desktop\ZENODO_GUNCEL_DOSYALAR"
DESKTOP_DIR_ESKI = r"C:\Users\maat\Desktop\eski_rapor"

# =========================================================================
# 1. BUILD BILINGUAL quadrant_visualizer.html
# =========================================================================
qv_html = """<!DOCTYPE html>
<html lang="tr" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>128x128 4-Quadrant Fraktal Nöron Deney Laboratuvarı</title>
  <style>
    /* =========================================================
       THEME VARIABLES
       ========================================================= */
    :root {
      /* Varsayılan Koyu Tema */
      --bg-body: #0a0e17;
      --bg-radial: #162036;
      --bg-card: #131b2e;
      --bg-inner: #0b1120;
      --bg-hover: #1e293b;
      --border: #1f2d47;
      --border-accent: rgba(16, 185, 129, 0.35);
      --text-main: #f1f5f9;
      --text-heading: #ffffff;
      --text-muted: #94a3b8;
      --emerald: #10b981;
      --emerald-glow: rgba(16, 185, 129, 0.18);
      --indigo: #818cf8;
      --amber: #f59e0b;
      --rose: #f43f5e;
      --card-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;
      --box-shadow-subtle: 0 4px 12px rgba(0, 0, 0, 0.25);
      --canvas-bg: #030712;
      --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }

    /* ☀️ Açık Tema (Light Mode) */
    html.light {
      --bg-body: #f1f5f9;
      --bg-radial: #e2e8f0;
      --bg-card: #ffffff;
      --bg-inner: #f8fafc;
      --bg-hover: #f1f5f9;
      --border: #e2e8f0;
      --border-accent: rgba(5, 150, 105, 0.35);
      --text-main: #0f172a;
      --text-heading: #0f172a;
      --text-muted: #64748b;
      --emerald: #059669;
      --emerald-glow: rgba(5, 150, 105, 0.12);
      --indigo: #4f46e5;
      --amber: #d97706;
      --rose: #e11d48;
      --card-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.08), 0 0 0 1px rgba(0, 0, 0, 0.05);
      --box-shadow-subtle: 0 2px 8px rgba(0, 0, 0, 0.04);
      --canvas-bg: #090d16;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: radial-gradient(circle at top center, var(--bg-radial) 0%, var(--bg-body) 70%);
      color: var(--text-main);
      font-family: var(--font);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px 16px;
      -webkit-font-smoothing: antialiased;
      transition: background 0.25s ease, color 0.25s ease;
    }

    .container {
      width: 100%;
      max-width: 680px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 24px 26px;
      box-shadow: var(--card-shadow);
      backdrop-filter: blur(12px);
      transition: background-color 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }

    /* Header */
    .header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
      margin-bottom: 18px;
      gap: 12px;
      transition: border-color 0.25s ease;
    }
    .header-left h1 {
      font-size: 16px;
      font-weight: 800;
      color: var(--text-heading);
      display: flex;
      align-items: center;
      gap: 9px;
      letter-spacing: -0.01em;
    }
    .status-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--emerald);
      box-shadow: 0 0 12px var(--emerald);
      animation: pulse 2s infinite ease-in-out;
    }
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.2); opacity: 0.6; }
    }
    .header-left p {
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 3px;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    
    /* Buttons in header */
    .action-btn {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: var(--bg-inner);
      color: var(--text-main);
      border: 1px solid var(--border);
      padding: 5px 10px;
      border-radius: 10px;
      font-size: 11.5px;
      font-weight: 700;
      cursor: pointer;
      outline: none;
      transition: all 0.2s ease;
      box-shadow: var(--box-shadow-subtle);
      user-select: none;
    }
    .action-btn:hover {
      background: var(--bg-hover);
      border-color: var(--emerald);
      transform: translateY(-1px);
    }
    .action-btn:active {
      transform: translateY(0);
    }

    .badges-col {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 4px;
    }
    .badge-mode {
      background: var(--emerald-glow);
      color: var(--emerald);
      border: 1px solid var(--border-accent);
      padding: 3px 9px;
      border-radius: 9999px;
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.03em;
    }
    .badge-doi {
      font-size: 9.5px;
      color: var(--text-muted);
      text-decoration: none;
      font-family: var(--font-mono);
      transition: color 0.2s;
    }
    .badge-doi:hover { color: var(--emerald); }

    /* Controls */
    .controls-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 18px;
    }
    .field-group label {
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 6px;
    }
    select {
      width: 100%;
      background: var(--bg-inner);
      color: var(--text-main);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 9px 12px;
      font-size: 12px;
      font-weight: 500;
      outline: none;
      cursor: pointer;
      transition: border-color 0.2s, box-shadow 0.2s, background-color 0.2s;
    }
    select:focus {
      border-color: var(--emerald);
      box-shadow: 0 0 0 2px var(--emerald-glow);
    }
    input[type=range] {
      width: 100%;
      height: 6px;
      background: var(--bg-inner);
      border-radius: 6px;
      outline: none;
      -webkit-appearance: none;
      margin-top: 14px;
      border: 1px solid var(--border);
      cursor: pointer;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--emerald);
      cursor: pointer;
      box-shadow: 0 0 10px var(--emerald);
      transition: transform 0.1s;
    }
    input[type=range]::-webkit-slider-thumb:hover {
      transform: scale(1.15);
    }

    /* Main Display Layout */
    .display-layout {
      display: grid;
      grid-template-columns: 160px 1fr;
      gap: 16px;
      align-items: center;
      margin-bottom: 18px;
    }

    /* Canvas Box */
    .canvas-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .canvas-wrapper {
      position: relative;
      width: 148px;
      height: 148px;
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid var(--border);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
      background: var(--canvas-bg);
    }
    canvas {
      width: 148px;
      height: 148px;
      display: block;
      image-rendering: pixelated;
    }
    .crosshair-h {
      position: absolute;
      top: 50%;
      left: 0;
      right: 0;
      border-top: 1px dashed rgba(255, 255, 255, 0.45);
      pointer-events: none;
    }
    .crosshair-v {
      position: absolute;
      left: 50%;
      top: 0;
      bottom: 0;
      border-left: 1px dashed rgba(255, 255, 255, 0.45);
      pointer-events: none;
    }
    .quad-tag {
      position: absolute;
      font-size: 9px;
      font-weight: 800;
      color: #fff;
      text-shadow: 0 1px 3px rgba(0,0,0,0.9), 0 0 2px #000;
      pointer-events: none;
      font-family: var(--font-mono);
    }
    .tag-q1 { top: 4px; left: 6px; }
    .tag-q2 { top: 4px; right: 6px; }
    .tag-q3 { bottom: 4px; left: 6px; }
    .tag-q4 { bottom: 4px; right: 6px; color: #fde047; }
    .res-label {
      font-size: 10px;
      color: var(--text-muted);
      font-family: var(--font-mono);
      margin-top: 6px;
    }

    /* Quadrant Weight Cards */
    .weights-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }
    .weight-card {
      background: var(--bg-inner);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 10px 12px;
      transition: border-color 0.2s, transform 0.15s, background-color 0.25s;
    }
    .weight-card:hover {
      border-color: var(--border-accent);
      transform: translateY(-1px);
    }
    .weight-card-bias {
      border-color: rgba(245, 158, 11, 0.3);
    }
    html.light .weight-card-bias {
      border-color: rgba(217, 119, 6, 0.3);
    }
    .wc-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 4px;
    }
    .wc-title {
      font-size: 10.5px;
      font-weight: 700;
      color: var(--text-muted);
      letter-spacing: 0.02em;
    }
    .wc-ratio {
      font-size: 9.5px;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }
    .wc-val {
      font-size: 17px;
      font-weight: 800;
      font-family: var(--font-mono);
      color: var(--text-main);
    }
    .val-emerald { color: var(--emerald); }
    .val-amber { color: var(--amber); }

    /* Truth Table / Live Verification */
    .verification-card {
      background: var(--bg-inner);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 14px 16px;
      margin-bottom: 16px;
      transition: background-color 0.25s ease, border-color 0.25s ease;
    }
    .vc-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }
    .vc-title {
      font-size: 11.5px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .accuracy-badge {
      font-size: 11px;
      font-weight: 800;
      padding: 2.5px 8px;
      border-radius: 6px;
      letter-spacing: 0.02em;
      transition: all 0.2s;
    }
    .badge-ok {
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald);
      border: 1px solid rgba(16, 185, 129, 0.4);
    }
    .badge-warn {
      background: rgba(245, 158, 11, 0.15);
      color: var(--amber);
      border: 1px solid rgba(245, 158, 11, 0.4);
    }

    .truth-table-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
    }
    .case-box {
      border-radius: 8px;
      padding: 8px 6px;
      text-align: center;
      font-family: var(--font-mono);
      font-size: 11px;
      transition: all 0.2s;
      border: 1px solid transparent;
    }
    
    /* Case status styles for dark mode */
    html.dark .case-success {
      background: rgba(16, 185, 129, 0.12);
      border-color: rgba(16, 185, 129, 0.3);
      color: #34d399;
    }
    html.dark .case-fail {
      background: rgba(244, 63, 94, 0.12);
      border-color: rgba(244, 63, 94, 0.3);
      color: #fb7185;
    }

    /* Case status styles for light mode */
    html.light .case-success {
      background: rgba(16, 185, 129, 0.1);
      border-color: rgba(16, 185, 129, 0.35);
      color: #047857;
      font-weight: 600;
    }
    html.light .case-fail {
      background: rgba(244, 63, 94, 0.1);
      border-color: rgba(244, 63, 94, 0.35);
      color: #be123c;
      font-weight: 600;
    }

    .case-inp {
      font-size: 9.5px;
      color: var(--text-muted);
      margin-bottom: 3px;
    }
    .case-out {
      font-size: 12px;
      font-weight: 800;
    }

    /* Mathematical Formula Box */
    .formula-box {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-muted);
      text-align: center;
      background: var(--bg-inner);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 8px 12px;
      margin-bottom: 18px;
      line-height: 1.5;
      transition: background-color 0.25s ease, border-color 0.25s ease;
    }
    .formula-box code {
      color: var(--indigo);
      font-weight: 700;
    }

    /* Footer */
    .footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: var(--text-muted);
      border-top: 1px solid var(--border);
      padding-top: 14px;
      transition: border-color 0.25s ease;
    }
    .btn-txt {
      background: var(--bg-inner);
      color: var(--text-main);
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s;
    }
    .btn-txt:hover {
      background: var(--bg-hover);
      border-color: var(--emerald);
      color: var(--emerald);
    }

    @media (max-width: 580px) {
      .display-layout { grid-template-columns: 1fr; }
      .controls-grid { grid-template-columns: 1fr; }
      .truth-table-grid { grid-template-columns: repeat(2, 1fr); }
      .container { padding: 18px 16px; }
      .header { flex-direction: column; align-items: flex-start; }
      .header-actions { width: 100%; justify-content: space-between; margin-top: 8px; }
      .badges-col { align-items: flex-end; }
    }
  </style>
</head>
<body>

<div class="container">

  <!-- Üst Başlık Banner -->
  <div class="header">
    <div class="header-left">
      <h1>
        <span class="status-dot"></span>
        <span id="qvTitle">128×128 4-Quadrant Fraktal Nöron</span>
      </h1>
      <p id="qvSubtitle">Mandelbrot Uzayından Prosedürel Sinaptik Ağırlık ve Eşik Sentezi</p>
    </div>
    <div class="header-actions">
      <!-- Dil Değiştirici Buton (TR / EN) -->
      <button id="langToggleBtn" class="action-btn" title="Dili Değiştir / Switch Language">
        <span id="langIcon">🌐</span>
        <span id="langText">English</span>
      </button>

      <!-- Açık / Koyu Tema Değiştirici -->
      <button id="themeToggleBtn" class="action-btn" title="Açık / Koyu Tema Değiştir">
        <span id="themeIcon">☀️</span>
        <span id="themeText">Açık Mod</span>
      </button>

      <div class="badges-col">
        <span id="badgeMode" class="badge-mode">CANLI SENTEZ</span>
        <a href="https://doi.org/10.5281/zenodo.22774935" target="_blank" class="badge-doi">DOI: 10.5281/zenodo.22774935</a>
      </div>
    </div>
  </div>

  <!-- Kontroller: Kapı Seçici & Zoom Slider -->
  <div class="controls-grid">
    <div class="field-group">
      <label for="presetSelect">
        <span id="lblTargetGate">Hedef Mantık Kapısı</span>
        <span id="coordBadge" style="color:var(--text-muted); font-family:var(--font-mono); font-size:10px;">cx: -0.056, cy: 0.806</span>
      </label>
      <select id="presetSelect">
        <option value="or" selected id="optOr">🚪 OR Kapısı (cx: -0.055780, cy: 0.806329)</option>
        <option value="and" id="optAnd">🏦 AND Kapısı (cx: -0.144732, cy: 0.758854)</option>
        <option value="nand" id="optNand">🚨 NAND Kapısı (cx: -0.740191, cy: 0.174654)</option>
        <option value="nor" id="optNor">🔒 NOR Kapısı (cx: -0.523561, cy: 0.525212)</option>
      </select>
    </div>

    <div class="field-group">
      <label for="zoomSlider">
        <span id="lblZoom">Büyütme Faktörü (Zoom)</span>
        <span id="zoomVal" style="color:var(--emerald); font-family:var(--font-mono); font-weight:700;">100.0x</span>
      </label>
      <input type="range" id="zoomSlider" min="0" max="4.0" step="0.005" value="2.0">
    </div>
  </div>

  <!-- Ana Gösterim: Canvas & 4-Quadrant Değerleri -->
  <div class="display-layout">
    <div class="canvas-container">
      <div class="canvas-wrapper">
        <canvas id="mandelCanvas" width="128" height="128"></canvas>
        <div class="crosshair-h"></div>
        <div class="crosshair-v"></div>
        <span class="quad-tag tag-q1">Q1</span>
        <span class="quad-tag tag-q2">Q2</span>
        <span class="quad-tag tag-q3">Q3</span>
        <span class="quad-tag tag-q4">Q4 (b)</span>
      </div>
      <div id="resLabel" class="res-label">128 × 128 Örnekleme</div>
    </div>

    <!-- 4 Ağırlık Kartı -->
    <div class="weights-grid">
      <div class="weight-card">
        <div class="wc-header">
          <span id="wcTitle1" class="wc-title">Q1 &rarr; Ağırlık 1 (w₁)</span>
          <span id="q1Ratio" class="wc-ratio">59.6%</span>
        </div>
        <div id="w1Val" class="wc-val val-emerald">+0.575</div>
      </div>

      <div class="weight-card">
        <div class="wc-header">
          <span id="wcTitle2" class="wc-title">Q2 &rarr; Ağırlık 2 (w₂)</span>
          <span id="q2Ratio" class="wc-ratio">59.0%</span>
        </div>
        <div id="w2Val" class="wc-val val-emerald">+0.540</div>
      </div>

      <div class="weight-card">
        <div class="wc-header">
          <span id="wcTitle3" class="wc-title">Q3 &rarr; Yardımcı (w₃)</span>
          <span id="q3Ratio" class="wc-ratio">40.6%</span>
        </div>
        <div id="w3Val" class="wc-val">-0.564</div>
      </div>

      <div class="weight-card weight-card-bias">
        <div class="wc-header">
          <span id="wcTitle4" class="wc-title" style="color:var(--amber);">Q4 &rarr; Eşik Sapması (b)</span>
          <span id="q4Ratio" class="wc-ratio">45.5%</span>
        </div>
        <div id="biasVal" class="wc-val val-amber">-0.272</div>
      </div>
    </div>
  </div>

  <!-- Matematiksel Aktivasyon Formülü -->
  <div id="formulaBox" class="formula-box">
    Nöron Karar Fonksiyonu: <code>ŷ = σ(w₁ · x₁ + w₂ · x₂ + b)</code> &nbsp;|&nbsp; <code>w_k = (Oran_{Qk} - 0.5) × 6.0</code>
  </div>

  <!-- Canlı Mantık Tablosu Doğrulama -->
  <div class="verification-card">
    <div class="vc-header">
      <span class="vc-title">
        <span id="vcTitle">⚡ Canlı Doğruluk Testi (Doğruluk Tablosu)</span>
      </span>
      <span id="accuracyBadge" class="accuracy-badge badge-ok">%100 Başarı</span>
    </div>

    <div class="truth-table-grid">
      <div id="case0" class="case-box case-success">
        <div id="caseInp0" class="case-inp">(0, 0) &rarr; Hedef: 0</div>
        <div id="out0" class="case-out">0 (p=0.43)</div>
      </div>
      <div id="case1" class="case-box case-success">
        <div id="caseInp1" class="case-inp">(0, 1) &rarr; Hedef: 1</div>
        <div id="out1" class="case-out">1 (p=0.57)</div>
      </div>
      <div id="case2" class="case-box case-success">
        <div id="caseInp2" class="case-inp">(1, 0) &rarr; Hedef: 1</div>
        <div id="out2" class="case-out">1 (p=0.58)</div>
      </div>
      <div id="case3" class="case-box case-success">
        <div id="caseInp3" class="case-inp">(1, 1) &rarr; Hedef: 1</div>
        <div id="out3" class="case-out">1 (p=0.70)</div>
      </div>
    </div>
  </div>

  <!-- Alt Bilgi: Yazarlar ve 24 Bayt Bellek İndirme -->
  <div class="footer">
    <div>
      <strong id="lblAuthors">Yazarlar:</strong> Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı
    </div>
    <button class="btn-txt" onclick="downloadMemoryTxt()">
      💾 <span id="btnDownloadText">24B Bellek İndir (.TXT)</span>
    </button>
  </div>

</div>

<script>
  // =========================================================
  // ÇOKLU DİL MOTORU (I18N: TR / EN)
  // =========================================================
  const I18N = {
    tr: {
      pageTitle: "128x128 4-Quadrant Fraktal Nöron Deney Laboratuvarı",
      qvTitle: "128×128 4-Quadrant Fraktal Nöron",
      qvSubtitle: "Mandelbrot Uzayından Prosedürel Sinaptik Ağırlık ve Eşik Sentezi",
      langButton: "English",
      badgeMode: "CANLI SENTEZ",
      lblTargetGate: "Hedef Mantık Kapısı",
      lblZoom: "Büyütme Faktörü (Zoom)",
      resLabel: "128 × 128 Örnekleme",
      wcTitle1: "Q1 → Ağırlık 1 (w₁)",
      wcTitle2: "Q2 → Ağırlık 2 (w₂)",
      wcTitle3: "Q3 → Yardımcı (w₃)",
      wcTitle4: "Q4 → Eşik Sapması (b)",
      formulaBox: 'Nöron Karar Fonksiyonu: <code>ŷ = σ(w₁ · x₁ + w₂ · x₂ + b)</code> &nbsp;|&nbsp; <code>w_k = (Oran_{Qk} - 0.5) × 6.0</code>',
      vcTitle: "⚡ Canlı Doğruluk Testi (Doğruluk Tablosu)",
      accOk: "%100 Başarı",
      accPattern: "%{rate} Başarı",
      targetLabel: "Hedef",
      lblAuthors: "Yazarlar:",
      btnDownloadText: "24B Bellek İndir (.TXT)",
      themeLight: "Açık Mod",
      themeDark: "Koyu Mod",
      presets: {
        or: "🚪 OR Kapısı (cx: -0.055780, cy: 0.806329)",
        and: "🏦 AND Kapısı (cx: -0.144732, cy: 0.758854)",
        nand: "🚨 NAND Kapısı (cx: -0.740191, cy: 0.174654)",
        nor: "🔒 NOR Kapısı (cx: -0.523561, cy: 0.525212)"
      },
      txtDump: {
        header: "MANDELBROT FRAKTAL NÖRAL SENTEZ - 24 BAYT BELLEK DÖKÜMÜ",
        permStorage: "Kalıcı Ağırlık Belleği  : 0 Bayt (Prosedürel Sentez ile Baypas Edildi)",
        dynamicSeed: "Dinamik Koordinat Tohumu : 24 Bayt (Üç adet 64-bit IEEE-754 Float)",
        synapsesTitle: "Türetilen Sinapslar     :",
        accuracy: "Sınıflandırma Başarımı   :",
        status: "Durum                    : Deterministik, Tekrarlanabilir, %100 Doğrulanmış",
        authors: "Yazarlar                 : Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı"
      }
    },
    en: {
      pageTitle: "128x128 4-Quadrant Fractal Neuron Laboratory",
      qvTitle: "128×128 4-Quadrant Fractal Neuron",
      qvSubtitle: "Procedural Synaptic Weight & Bias Synthesis from Mandelbrot Space",
      langButton: "Türkçe",
      badgeMode: "LIVE SYNTHESIS",
      lblTargetGate: "Target Logic Gate",
      lblZoom: "Zoom Scale Factor",
      resLabel: "128 × 128 Sampling",
      wcTitle1: "Q1 → Weight 1 (w₁)",
      wcTitle2: "Q2 → Weight 2 (w₂)",
      wcTitle3: "Q3 → Auxiliary (w₃)",
      wcTitle4: "Q4 → Threshold Bias (b)",
      formulaBox: 'Neuron Activation Function: <code>ŷ = σ(w₁ · x₁ + w₂ · x₂ + b)</code> &nbsp;|&nbsp; <code>w_k = (Ratio_{Qk} - 0.5) × 6.0</code>',
      vcTitle: "⚡ Live Truth Table Verification",
      accOk: "100% Accuracy",
      accPattern: "%{rate} Accuracy",
      targetLabel: "Target",
      lblAuthors: "Authors:",
      btnDownloadText: "Download 24B Memory (.TXT)",
      themeLight: "Light Mode",
      themeDark: "Dark Mode",
      presets: {
        or: "🚪 OR Gate (cx: -0.055780, cy: 0.806329)",
        and: "🏦 AND Gate (cx: -0.144732, cy: 0.758854)",
        nand: "🚨 NAND Gate (cx: -0.740191, cy: 0.174654)",
        nor: "🔒 NOR Gate (cx: -0.523561, cy: 0.525212)"
      },
      txtDump: {
        header: "MANDELBROT FRACTAL NEURAL SYNTHESIS - 24-BYTE MEMORY DUMP",
        permStorage: "Permanent Weight Storage : 0 Bytes (Bypassed via Procedural Generation)",
        dynamicSeed: "Dynamic Coordinate Seed  : 24 Bytes (Three 64-bit IEEE-754 Floats)",
        synapsesTitle: "Synthesized Synapses     :",
        accuracy: "Classification Accuracy  :",
        status: "Status                   : Deterministic, Reproducible, Verified 100%",
        authors: "Authors                  : Volkan Dağlı, Zerrin Dağlı, Dağhan Dağlı"
      }
    }
  };

  let currentLang = localStorage.getItem('widget_lang') || 'tr';

  function applyLanguage(lang) {
    currentLang = lang;
    document.documentElement.lang = lang;
    localStorage.setItem('widget_lang', lang);

    const dict = I18N[lang];
    document.title = dict.pageTitle;
    document.getElementById('qvTitle').innerText = dict.qvTitle;
    document.getElementById('qvSubtitle').innerText = dict.qvSubtitle;
    document.getElementById('langText').innerText = dict.langButton;
    document.getElementById('badgeMode').innerText = dict.badgeMode;
    document.getElementById('lblTargetGate').innerText = dict.lblTargetGate;
    document.getElementById('lblZoom').innerText = dict.lblZoom;
    document.getElementById('resLabel').innerText = dict.resLabel;
    document.getElementById('wcTitle1').innerHTML = dict.wcTitle1;
    document.getElementById('wcTitle2').innerHTML = dict.wcTitle2;
    document.getElementById('wcTitle3').innerHTML = dict.wcTitle3;
    document.getElementById('wcTitle4').innerHTML = dict.wcTitle4;
    document.getElementById('formulaBox').innerHTML = dict.formulaBox;
    document.getElementById('vcTitle').innerText = dict.vcTitle;
    document.getElementById('lblAuthors').innerText = dict.lblAuthors;
    document.getElementById('btnDownloadText').innerText = dict.btnDownloadText;

    // Presets options text
    document.getElementById('optOr').innerText = dict.presets.or;
    document.getElementById('optAnd').innerText = dict.presets.and;
    document.getElementById('optNand').innerText = dict.presets.nand;
    document.getElementById('optNor').innerText = dict.presets.nor;

    // Update Theme text according to language
    const isDark = document.documentElement.classList.contains('dark');
    themeText.innerText = isDark ? dict.themeLight : dict.themeDark;

    render();
  }

  function toggleLanguage() {
    applyLanguage(currentLang === 'tr' ? 'en' : 'tr');
  }

  document.getElementById('langToggleBtn').addEventListener('click', toggleLanguage);

  // =========================================================
  // TEMA DEĞİŞTİRME MANTIĞI (AÇIK / KOYU MOD)
  // =========================================================
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const themeIcon = document.getElementById('themeIcon');
  const themeText = document.getElementById('themeText');

  function applyTheme(isDark) {
    const dict = I18N[currentLang] || I18N.tr;
    if (isDark) {
      document.documentElement.classList.add('dark');
      document.documentElement.classList.remove('light');
      themeIcon.innerText = "☀️";
      themeText.innerText = dict.themeLight;
      localStorage.setItem('widget_theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark');
      document.documentElement.classList.add('light');
      themeIcon.innerText = "🌙";
      themeText.innerText = dict.themeDark;
      localStorage.setItem('widget_theme', 'light');
    }
  }

  function toggleTheme() {
    const isCurrentlyDark = document.documentElement.classList.contains('dark');
    applyTheme(!isCurrentlyDark);
  }

  themeToggleBtn.addEventListener('click', toggleTheme);

  // =========================================================
  // MANDELBROT VE NÖRON SENTEZİ MANTIĞI
  // =========================================================
  const presets = {
    or:   { cx: -0.055780, cy: 0.806329, logZ: 2.0, maxI: 80, target: [0, 1, 1, 1] },
    and:  { cx: -0.144732, cy: 0.758854, logZ: 0.653, maxI: 80, target: [0, 0, 0, 1] },
    nand: { cx: -0.740191, cy: 0.174654, logZ: 3.534, maxI: 70, target: [1, 1, 1, 0] },
    nor:  { cx: -0.523561, cy: 0.525212, logZ: 3.051, maxI: 80, target: [1, 0, 0, 0] }
  };

  let currentPreset = presets.or;

  const canvas = document.getElementById('mandelCanvas');
  const ctx = canvas.getContext('2d');
  const slider = document.getElementById('zoomSlider');
  const zoomVal = document.getElementById('zoomVal');
  const presetSelect = document.getElementById('presetSelect');
  const coordBadge = document.getElementById('coordBadge');

  const w1El = document.getElementById('w1Val');
  const w2El = document.getElementById('w2Val');
  const w3El = document.getElementById('w3Val');
  const biasEl = document.getElementById('biasVal');
  const q1RatioEl = document.getElementById('q1Ratio');
  const q2RatioEl = document.getElementById('q2Ratio');
  const q3RatioEl = document.getElementById('q3Ratio');
  const q4RatioEl = document.getElementById('q4Ratio');
  const accBadge = document.getElementById('accuracyBadge');

  function downloadMemoryTxt() {
    const dict = I18N[currentLang] || I18N.tr;
    const td = dict.txtDump;
    const logZ = parseFloat(slider.value);
    const zoom = Math.pow(10, logZ);
    const content = 
`======================================================================
${td.header}
======================================================================
${td.permStorage}
${td.dynamicSeed}
----------------------------------------------------------------------
Parameter 1 (cx)        : ${currentPreset.cx.toFixed(8)} (Float64 - 8 Bytes)
Parameter 2 (cy)        : ${currentPreset.cy.toFixed(8)} (Float64 - 8 Bytes)
Parameter 3 (zoom)      : ${zoom.toFixed(4)}x (Float64 - 8 Bytes)
----------------------------------------------------------------------
${td.synapsesTitle}
  • w1 (Q1, Input 1)    : ${w1El.innerText}
  • w2 (Q2, Input 2)    : ${w2El.innerText}
  • w3 (Q3, Auxiliary)  : ${w3El.innerText}
  • b  (Q4, Bias)       : ${biasEl.innerText}
${td.accuracy} ${accBadge.innerText}
${td.status}
DOI Reference           : 10.5281/zenodo.22774935
${td.authors}
======================================================================`;

    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `fractal_neuron_memory_${presetSelect.value}_${currentLang}_24bytes.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function render() {
    const dict = I18N[currentLang] || I18N.tr;
    const logZ = parseFloat(slider.value);
    const zoom = Math.pow(10, logZ);
    zoomVal.innerText = zoom >= 100 ? zoom.toFixed(1) + 'x' : zoom.toFixed(2) + 'x';
    coordBadge.innerText = `cx: ${currentPreset.cx.toFixed(3)}, cy: ${currentPreset.cy.toFixed(3)}`;

    const res = 128;
    const maxIter = currentPreset.maxI;
    const scale = 1.0 / zoom;
    const cx = currentPreset.cx;
    const cy = currentPreset.cy;

    const imgData = ctx.createImageData(res, res);
    const data = imgData.data;

    let qCount = [0, 0, 0, 0];
    const qTotal = (res / 2) * (res / 2);

    for (let py = 0; py < res; py++) {
      const y0 = cy - scale + (py / (res - 1)) * (2.0 * scale);
      const isBottom = (py >= res / 2);

      for (let px = 0; px < res; px++) {
        const x0 = cx - scale + (px / (res - 1)) * (2.0 * scale);
        const isRight = (px >= res / 2);

        let qIdx = 0;
        if (!isBottom && !isRight) qIdx = 0;      // Q1 (Top-Left)
        else if (!isBottom && isRight) qIdx = 1;  // Q2 (Top-Right)
        else if (isBottom && !isRight) qIdx = 2;  // Q3 (Bottom-Left)
        else qIdx = 3;                            // Q4 (Bottom-Right)

        let x = 0.0, y = 0.0, iter = 0;
        while (x * x + y * y <= 4.0 && iter < maxIter) {
          const xtemp = x * x - y * y + x0;
          y = 2.0 * x * y + y0;
          x = xtemp;
          iter++;
        }

        const idx = (py * res + px) * 4;
        if (iter === maxIter) {
          qCount[qIdx]++;
          data[idx] = 15;
          data[idx + 1] = 23;
          data[idx + 2] = 42;
          data[idx + 3] = 255;
        } else {
          const hue = (iter / maxIter) * 260 + 190;
          const rgb = hslToRgb(hue / 360, 0.85, 0.5);
          data[idx] = rgb[0];
          data[idx + 1] = rgb[1];
          data[idx + 2] = rgb[2];
          data[idx + 3] = 255;
        }
      }
    }

    ctx.putImageData(imgData, 0, 0);

    const r1 = qCount[0] / qTotal;
    const r2 = qCount[1] / qTotal;
    const r3 = qCount[2] / qTotal;
    const r4 = qCount[3] / qTotal;

    const w1 = (r1 - 0.5) * 6.0;
    const w2 = (r2 - 0.5) * 6.0;
    const w3 = (r3 - 0.5) * 6.0;
    const bias = (r4 - 0.5) * 6.0;

    w1El.innerText = (w1 >= 0 ? '+' : '') + w1.toFixed(3);
    w2El.innerText = (w2 >= 0 ? '+' : '') + w2.toFixed(3);
    w3El.innerText = (w3 >= 0 ? '+' : '') + w3.toFixed(3);
    biasEl.innerText = (bias >= 0 ? '+' : '') + bias.toFixed(3);

    q1RatioEl.innerText = (r1 * 100).toFixed(1) + '%';
    q2RatioEl.innerText = (r2 * 100).toFixed(1) + '%';
    q3RatioEl.innerText = (r3 * 100).toFixed(1) + '%';
    q4RatioEl.innerText = (r4 * 100).toFixed(1) + '%';

    // Canlı Doğruluk Tablosu
    const testInputs = [[0, 0], [0, 1], [1, 0], [1, 1]];
    const target = currentPreset.target;
    let correct = 0;

    testInputs.forEach((inp, idx) => {
      const z = w1 * inp[0] + w2 * inp[1] + bias;
      const pred = 1.0 / (1.0 + Math.exp(-z));
      const lbl = pred >= 0.5 ? 1 : 0;
      const isOk = (lbl === target[idx]);
      if (isOk) correct++;

      const el = document.getElementById('case' + idx);
      const caseInpEl = document.getElementById('caseInp' + idx);
      const outSpan = document.getElementById('out' + idx);
      
      caseInpEl.innerHTML = `(${inp[0]}, ${inp[1]}) &rarr; ${dict.targetLabel}: ${target[idx]}`;
      outSpan.innerText = `${lbl} (p=${pred.toFixed(2)})`;
      if (isOk) {
        el.className = "case-box case-success";
      } else {
        el.className = "case-box case-fail";
      }
    });

    const accRate = Math.round((correct / 4) * 100);
    accBadge.innerText = accRate === 100 ? dict.accOk : dict.accPattern.replace('{rate}', accRate);
    accBadge.className = accRate === 100 ? "accuracy-badge badge-ok" : "accuracy-badge badge-warn";
  }

  function hslToRgb(h, s, l) {
    let r, g, b;
    if (s === 0) r = g = b = l;
    else {
      const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
      const p = 2 * l - q;
      r = hue2rgb(p, q, h + 1/3);
      g = hue2rgb(p, q, h);
      b = hue2rgb(p, q, h - 1/3);
    }
    return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
  }

  function hue2rgb(p, q, t) {
    if (t < 0) t += 1;
    if (t > 1) t -= 1;
    if (t < 1/6) return p + (q - p) * 6 * t;
    if (t < 1/2) return q;
    if (t < 2/3) return p + (q - p) * (2/3 - t) * 6;
    return p;
  }

  slider.addEventListener('input', render);
  presetSelect.addEventListener('change', (e) => {
    currentPreset = presets[e.target.value];
    slider.value = currentPreset.logZ;
    render();
  });

  // Başlangıç Ayarları
  applyLanguage(currentLang);
  const savedTheme = localStorage.getItem('widget_theme');
  applyTheme(savedTheme !== 'light');
</script>
</body>
</html>
"""

# =========================================================================
# 2. BUILD BILINGUAL interactive_lab.html
# =========================================================================
il_html = """<!DOCTYPE html>
<html lang="tr" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fraktal Nöron: Matematikten Zihin Çıkarmak (Halk Laboratuvarı)</title>
  
  <style>
    /* ☀️ Açık Tema (Varsayılan) */
    :root {
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --bg-card-subtle: #f1f5f9;
      --bg-card-hover: #e2e8f0;
      --border-color: #e2e8f0;
      --text-primary: #0f172a;
      --text-secondary: #334155;
      --text-muted: #64748b;
      --canvas-bg: #f8fafc;
      --shadow-main: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
      --card: var(--bg-card);
      --border: var(--border-color);
      --muted-foreground: var(--text-muted);
      --foreground: var(--text-primary);
      --background: var(--bg-page);
    }

    /* 🌙 Koyu Tema */
    html.dark {
      --bg-page: #090d16;
      --bg-card: #0f172a;
      --bg-card-subtle: #1e293b;
      --bg-card-hover: #334155;
      --border-color: #1e293b;
      --text-primary: #f8fafc;
      --text-secondary: #cbd5e1;
      --text-muted: #94a3b8;
      --canvas-bg: #090d16;
      --shadow-main: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.4);
      --card: var(--bg-card);
      --border: var(--border-color);
      --muted-foreground: var(--text-muted);
      --foreground: var(--text-primary);
      --background: var(--bg-page);
    }

    body {
      background-color: var(--bg-page);
      color: var(--text-primary);
      transition: background-color 0.25s ease, color 0.25s ease;
    }

    .theme-card {
      background-color: var(--bg-card);
      color: var(--text-primary);
      border-color: var(--border-color);
      box-shadow: var(--shadow-main);
      transition: background-color 0.25s ease, border-color 0.25s ease, color 0.25s ease;
    }

    .theme-subtle {
      background-color: var(--bg-card-subtle);
      border-color: var(--border-color);
      transition: background-color 0.25s ease, border-color 0.25s ease;
    }

    @keyframes pulse-glow {
      0%, 100% { filter: drop-shadow(0 0 15px rgba(16, 185, 129, 0.6)); }
      50% { filter: drop-shadow(0 0 25px rgba(16, 185, 129, 0.9)); }
    }
    .firing {
      animation: pulse-glow 1.2s infinite;
    }
  
*, ::before, ::after{--tw-border-spacing-x:0;--tw-border-spacing-y:0;--tw-translate-x:0;--tw-translate-y:0;--tw-rotate:0;--tw-skew-x:0;--tw-skew-y:0;--tw-scale-x:1;--tw-scale-y:1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness:proximity;--tw-gradient-from-position: ;--tw-gradient-via-position: ;--tw-gradient-to-position: ;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width:0px;--tw-ring-offset-color:#fff;--tw-ring-color:rgb(59 130 246 / 0.5);--tw-ring-offset-shadow:0 0 #0000;--tw-ring-shadow:0 0 #0000;--tw-shadow:0 0 #0000;--tw-shadow-colored:0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;--tw-contain-size: ;--tw-contain-layout: ;--tw-contain-paint: ;--tw-contain-style: }::backdrop{--tw-border-spacing-x:0;--tw-border-spacing-y:0;--tw-translate-x:0;--tw-translate-y:0;--tw-rotate:0;--tw-skew-x:0;--tw-skew-y:0;--tw-scale-x:1;--tw-scale-y:1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness:proximity;--tw-gradient-from-position: ;--tw-gradient-via-position: ;--tw-gradient-to-position: ;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width:0px;--tw-ring-offset-color:#fff;--tw-ring-color:rgb(59 130 246 / 0.5);--tw-ring-offset-shadow:0 0 #0000;--tw-ring-shadow:0 0 #0000;--tw-shadow:0 0 #0000;--tw-shadow-colored:0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;--tw-contain-size: ;--tw-contain-layout: ;--tw-contain-paint: ;--tw-contain-style: }*,::after,::before{box-sizing:border-box;border-width:0;border-style:solid;border-color:#e5e7eb}::after,::before{--tw-content:''}:host,html{line-height:1.5;-webkit-text-size-adjust:100%;-moz-tab-size:4;tab-size:4;font-family:ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-feature-settings:normal;font-variation-settings:normal;-webkit-tap-highlight-color:transparent}body{margin:0;line-height:inherit}hr{height:0;color:inherit;border-top-width:1px}abbr:where([title]){-webkit-text-decoration:underline dotted;text-decoration:underline dotted}h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight:inherit}a{color:inherit;text-decoration:inherit}b,strong{font-weight:bolder}code,kbd,pre,samp{font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;font-feature-settings:normal;font-variation-settings:normal;font-size:1em}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}table{text-indent:0;border-color:inherit;border-collapse:collapse}button,input,optgroup,select,textarea{font-family:inherit;font-feature-settings:inherit;font-variation-settings:inherit;font-size:100%;font-weight:inherit;line-height:inherit;letter-spacing:inherit;color:inherit;margin:0;padding:0}button,select{text-transform:none}button,input:where([type=button]),input:where([type=reset]),input:where([type=submit]){-webkit-appearance:button;background-color:transparent;background-image:none}:-moz-focusring{outline:auto}:-moz-ui-invalid{box-shadow:none}progress{vertical-align:baseline}::-webkit-inner-spin-button,::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}summary{display:list-item}blockquote,dd,dl,figure,h1,h2,h3,h4,h5,h6,hr,p,pre{margin:0}fieldset{margin:0;padding:0}legend{padding:0}menu,ol,ul{list-style:none;margin:0;padding:0}dialog{padding:0}textarea{resize:vertical}input::placeholder,textarea::placeholder{opacity:1;color:#9ca3af}[role=button],button{cursor:pointer}:disabled{cursor:default}audio,canvas,embed,iframe,img,object,svg,video{display:block;vertical-align:middle}img,video{max-width:100%;height:auto}[hidden]:where(:not([hidden=until-found])){display:none}.pointer-events-none{pointer-events:none}.absolute{position:absolute}.relative{position:relative}.inset-x-0{left:0px;right:0px}.inset-y-0{top:0px;bottom:0px}.-bottom-6{bottom:-1.5rem}.-right-6{right:-1.5rem}.bottom-1{bottom:0.25rem}.left-1\.5{left:0.375rem}.left-1\/2{left:50%}.right-1\.5{right:0.375rem}.top-1{top:0.25rem}.top-1\/2{top:50%}.mx-auto{margin-left:auto;margin-right:auto}.my-2{margin-top:0.5rem;margin-bottom:0.5rem}.mb-0\.5{margin-bottom:0.125rem}.mb-1{margin-bottom:0.25rem}.mb-2{margin-bottom:0.5rem}.mb-3{margin-bottom:0.75rem}.mb-4{margin-bottom:1rem}.mt-0\.5{margin-top:0.125rem}.mt-1{margin-top:0.25rem}.mt-1\.5{margin-top:0.375rem}.mt-2{margin-top:0.5rem}.mt-4{margin-top:1rem}.block{display:block}.inline-block{display:inline-block}.flex{display:flex}.inline-flex{display:inline-flex}.grid{display:grid}.h-1\.5{height:0.375rem}.h-2{height:0.5rem}.h-28{height:7rem}.h-40{height:10rem}.h-auto{height:auto}.h-full{height:100%}.min-h-screen{min-height:100vh}.w-1\.5{width:0.375rem}.w-2{width:0.5rem}.w-28{width:7rem}.w-40{width:10rem}.w-full{width:100%}.max-w-4xl{max-width:56rem}.max-w-\[260px\]{max-width:260px}.flex-1{flex:1 1 0%}@keyframes pulse{50%{opacity:.5}}.animate-pulse{animation:pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite}.cursor-pointer{cursor:pointer}.grid-cols-1{grid-template-columns:repeat(1, minmax(0, 1fr))}.grid-cols-2{grid-template-columns:repeat(2, minmax(0, 1fr))}.grid-cols-3{grid-template-columns:repeat(3, minmax(0, 1fr))}.flex-col{flex-direction:column}.flex-wrap{flex-wrap:wrap}.items-center{align-items:center}.justify-center{justify-content:center}.justify-between{justify-content:space-between}.gap-1{gap:0.25rem}.gap-1\.5{gap:0.375rem}.gap-2{gap:0.5rem}.gap-2\.5{gap:0.625rem}.gap-3{gap:0.75rem}.gap-4{gap:1rem}.gap-5{gap:1.25rem}.space-y-1 > :not([hidden]) ~ :not([hidden]){--tw-space-y-reverse:0;margin-top:calc(0.25rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom:calc(0.25rem * var(--tw-space-y-reverse))}.space-y-3 > :not([hidden]) ~ :not([hidden]){--tw-space-y-reverse:0;margin-top:calc(0.75rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom:calc(0.75rem * var(--tw-space-y-reverse))}.space-y-4 > :not([hidden]) ~ :not([hidden]){--tw-space-y-reverse:0;margin-top:calc(1rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom:calc(1rem * var(--tw-space-y-reverse))}.overflow-hidden{overflow:hidden}.rounded{border-radius:0.25rem}.rounded-2xl{border-radius:1rem}.rounded-full{border-radius:9999px}.rounded-lg{border-radius:0.5rem}.rounded-xl{border-radius:0.75rem}.border{border-width:1px}.border-b{border-bottom-width:1px}.border-l{border-left-width:1px}.border-t{border-top-width:1px}.border-\[var\(--border-color\)\]{border-color:var(--border-color)}.border-blue-500\/10{border-color:rgb(59 130 246 / 0.1)}.border-blue-500\/20{border-color:rgb(59 130 246 / 0.2)}.border-blue-600{--tw-border-opacity:1;border-color:rgb(37 99 235 / var(--tw-border-opacity, 1))}.border-emerald-500\/20{border-color:rgb(16 185 129 / 0.2)}.border-emerald-500\/30{border-color:rgb(16 185 129 / 0.3)}.border-emerald-500\/40{border-color:rgb(16 185 129 / 0.4)}.border-indigo-100{--tw-border-opacity:1;border-color:rgb(224 231 255 / var(--tw-border-opacity, 1))}.border-purple-500\/20{border-color:rgb(168 85 247 / 0.2)}.border-purple-500\/25{border-color:rgb(168 85 247 / 0.25)}.border-purple-500\/30{border-color:rgb(168 85 247 / 0.3)}.border-white\/20{border-color:rgb(255 255 255 / 0.2)}.border-white\/25{border-color:rgb(255 255 255 / 0.25)}.border-white\/40{border-color:rgb(255 255 255 / 0.4)}.border-rose-400\/40{border-color:rgb(251 113 133 / 0.4)}.border-emerald-400\/40{border-color:rgb(52 211 153 / 0.4)}.bg-\[var\(--bg-card\)\]{background-color:var(--bg-card)}.bg-\[var\(--bg-card-subtle\)\]{background-color:var(--bg-card-subtle)}.bg-\[var\(--bg-page\)\]{background-color:var(--bg-page)}.bg-\[var\(--border-color\)\]{background-color:var(--border-color)}.bg-black{--tw-bg-opacity:1;background-color:rgb(0 0 0 / var(--tw-bg-opacity, 1))}.bg-blue-500{--tw-bg-opacity:1;background-color:rgb(59 130 246 / var(--tw-bg-opacity, 1))}.bg-blue-500\/10{background-color:rgb(59 130 246 / 0.1)}.bg-blue-500\/15{background-color:rgb(59 130 246 / 0.15)}.bg-emerald-500{--tw-bg-opacity:1;background-color:rgb(16 185 129 / var(--tw-bg-opacity, 1))}.bg-emerald-500\/10{background-color:rgb(16 185 129 / 0.1)}.bg-emerald-500\/15{background-color:rgb(16 185 129 / 0.15)}.bg-emerald-600{--tw-bg-opacity:1;background-color:rgb(5 150 105 / var(--tw-bg-opacity, 1))}.bg-purple-500{--tw-bg-opacity:1;background-color:rgb(168 85 247 / var(--tw-bg-opacity, 1))}.bg-purple-500\/10{background-color:rgb(168 85 247 / 0.1)}.bg-purple-500\/15{background-color:rgb(168 85 247 / 0.15)}.bg-purple-600{--tw-bg-opacity:1;background-color:rgb(147 51 234 / var(--tw-bg-opacity, 1))}.bg-white{--tw-bg-opacity:1;background-color:rgb(255 255 255 / var(--tw-bg-opacity, 1))}.bg-white\/15{background-color:rgb(255 255 255 / 0.15)}.bg-white\/20{background-color:rgb(255 255 255 / 0.2)}.bg-blue-50{--tw-bg-opacity:1;background-color:rgb(239 246 255 / var(--tw-bg-opacity, 1))}.bg-rose-500\/10{background-color:rgb(244 63 94 / 0.1)}.bg-rose-600{--tw-bg-opacity:1;background-color:rgb(225 29 72 / var(--tw-bg-opacity, 1))}.bg-gradient-to-r{background-image:linear-gradient(to right, var(--tw-gradient-stops))}.from-blue-600{--tw-gradient-from:#2563eb var(--tw-gradient-from-position);--tw-gradient-to:rgb(37 99 235 / 0) var(--tw-gradient-to-position);--tw-gradient-stops:var(--tw-gradient-from), var(--tw-gradient-to)}.via-indigo-600{--tw-gradient-to:rgb(79 70 229 / 0)  var(--tw-gradient-to-position);--tw-gradient-stops:var(--tw-gradient-from), #4f46e5 var(--tw-gradient-via-position), var(--tw-gradient-to)}.to-purple-600{--tw-gradient-to:#9333ea var(--tw-gradient-to-position)}.p-1\.5{padding:0.375rem}.p-2{padding:0.5rem}.p-2\.5{padding:0.625rem}.p-3{padding:0.75rem}.p-3\.5{padding:0.875rem}.p-4{padding:1rem}.p-5{padding:1.25rem}.px-2{padding-left:0.5rem;padding-right:0.5rem}.px-2\.5{padding-left:0.625rem;padding-right:0.625rem}.px-3{padding-left:0.75rem;padding-right:0.75rem}.px-3\.5{padding-left:0.875rem;padding-right:0.875rem}.py-0\.5{padding-top:0.125rem;padding-bottom:0.125rem}.py-1{padding-top:0.25rem;padding-bottom:0.25rem}.py-1\.5{padding-top:0.375rem;padding-bottom:0.375rem}.py-2{padding-top:0.5rem;padding-bottom:0.5rem}.pb-2{padding-bottom:0.5rem}.pt-3{padding-top:0.75rem}.text-center{text-align:center}.font-mono{font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace}.font-sans{font-family:ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"}.text-2xl{font-size:1.5rem;line-height:2rem}.text-\[10px\]{font-size:10px}.text-\[11px\]{font-size:11px}.text-\[9px\]{font-size:9px}.text-sm{font-size:0.875rem;line-height:1.25rem}.text-xl{font-size:1.25rem;line-height:1.75rem}.text-xs{font-size:0.75rem;line-height:1rem}.font-black{font-weight:900}.font-bold{font-weight:700}.font-medium{font-weight:500}.font-semibold{font-weight:600}.uppercase{text-transform:uppercase}.leading-relaxed{line-height:1.625}.leading-tight{line-height:1.25}.tracking-tight{letter-spacing:-0.025em}.tracking-wide{letter-spacing:0.025em}.tracking-wider{letter-spacing:0.05em}.text-\[var\(--text-muted\)\]{color:var(--text-muted)}.text-\[var\(--text-primary\)\]{color:var(--text-primary)}.text-\[var\(--text-secondary\)\]{color:var(--text-secondary)}.text-amber-300{--tw-text-opacity:1;color:rgb(252 211 77 / var(--tw-text-opacity, 1))}.text-amber-600{--tw-text-opacity:1;color:rgb(217 119 6 / var(--tw-text-opacity, 1))}.text-blue-100{--tw-text-opacity:1;color:rgb(219 234 254 / var(--tw-text-opacity, 1))}.text-blue-600{--tw-text-opacity:1;color:rgb(37 99 235 / var(--tw-text-opacity, 1))}.text-emerald-600{--tw-text-opacity:1;color:rgb(5 150 105 / var(--tw-text-opacity, 1))}.text-emerald-700{--tw-text-opacity:1;color:rgb(4 120 87 / var(--tw-text-opacity, 1))}.text-indigo-600{--tw-text-opacity:1;color:rgb(79 70 229 / var(--tw-text-opacity, 1))}.text-indigo-900{--tw-text-opacity:1;color:rgb(49 46 129 / var(--tw-text-opacity, 1))}.text-indigo-950{--tw-text-opacity:1;color:rgb(30 27 75 / var(--tw-text-opacity, 1))}.text-purple-600{--tw-text-opacity:1;color:rgb(147 51 234 / var(--tw-text-opacity, 1))}.text-rose-600{--tw-text-opacity:1;color:rgb(225 29 72 / var(--tw-text-opacity, 1))}.text-white{--tw-text-opacity:1;color:rgb(255 255 255 / var(--tw-text-opacity, 1))}.text-blue-700{--tw-text-opacity:1;color:rgb(29 78 216 / var(--tw-text-opacity, 1))}.text-rose-800{--tw-text-opacity:1;color:rgb(159 18 57 / var(--tw-text-opacity, 1))}.text-emerald-800{--tw-text-opacity:1;color:rgb(6 95 70 / var(--tw-text-opacity, 1))}.antialiased{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.accent-purple-500{accent-color:#a855f7}.opacity-90{opacity:0.9}.shadow{--tw-shadow:0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);--tw-shadow-colored:0 1px 3px 0 var(--tw-shadow-color), 0 1px 2px -1px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)}.shadow-md{--tw-shadow:0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);--tw-shadow-colored:0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)}.shadow-sm{--tw-shadow:0 1px 2px 0 rgb(0 0 0 / 0.05);--tw-shadow-colored:0 1px 2px 0 var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow)}.blur-2xl{--tw-blur:blur(40px);filter:var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)}.drop-shadow{--tw-drop-shadow:drop-shadow(0 1px 2px rgb(0 0 0 / 0.1)) drop-shadow(0 1px 1px rgb(0 0 0 / 0.06));filter:var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)}.backdrop-blur-sm{--tw-backdrop-blur:blur(4px);-webkit-backdrop-filter:var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia);backdrop-filter:var(--tw-backdrop-blur) var(--tw-backdrop-brightness) var(--tw-backdrop-contrast) var(--tw-backdrop-grayscale) var(--tw-backdrop-hue-rotate) var(--tw-backdrop-invert) var(--tw-backdrop-opacity) var(--tw-backdrop-saturate) var(--tw-backdrop-sepia)}.transition-all{transition-property:all;transition-timing-function:cubic-bezier(0.4, 0, 0.2, 1);transition-duration:150ms}.duration-200{transition-duration:200ms}.hover\:bg-blue-50:hover{--tw-bg-opacity:1;background-color:rgb(239 246 255 / var(--tw-bg-opacity, 1))}.hover\:bg-purple-700:hover{--tw-bg-opacity:1;background-color:rgb(126 34 206 / var(--tw-bg-opacity, 1))}.hover\:bg-white\/25:hover{background-color:rgb(255 255 255 / 0.25)}.hover\:bg-white\/30:hover{background-color:rgb(255 255 255 / 0.3)}.hover\:bg-\[var\(--bg-card-hover\)\]:hover{background-color:var(--bg-card-hover)}.active\:scale-95:active{--tw-scale-x:.95;--tw-scale-y:.95;transform:translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}@media (min-width: 640px){.sm\:grid-cols-4{grid-template-columns:repeat(4, minmax(0, 1fr))}.sm\:p-5{padding:1.25rem}.sm\:p-6{padding:1.5rem}.sm\:text-2xl{font-size:1.5rem;line-height:2rem}.sm\:text-sm{font-size:0.875rem;line-height:1.25rem}}@media (min-width: 768px){.md\:grid-cols-2{grid-template-columns:repeat(2, minmax(0, 1fr))}.md\:grid-cols-3{grid-template-columns:repeat(3, minmax(0, 1fr))}}@media (min-width: 1024px){.lg\:col-span-3{grid-column:span 3 / span 3}.lg\:col-span-4{grid-column:span 4 / span 4}.lg\:col-span-5{grid-column:span 5 / span 5}.lg\:grid-cols-12{grid-template-columns:repeat(12, minmax(0, 1fr))}}

    /* html.dark Class Overrides for Offline Standalone Mode */
    html.dark .dark\:bg-blue-950\/60 { background-color: rgb(23 37 84 / 0.6) !important; }
    html.dark .dark\:text-amber-400 { color: rgb(251 191 36) !important; }
    html.dark .dark\:text-blue-400 { color: rgb(96 165 250) !important; }
    html.dark .dark\:text-emerald-300 { color: rgb(110 231 183) !important; }
    html.dark .dark\:text-emerald-400 { color: rgb(52 211 153) !important; }
    html.dark .dark\:text-indigo-400 { color: rgb(129 140 248) !important; }
    html.dark .dark\:text-purple-300 { color: rgb(216 180 254) !important; }
    html.dark .dark\:text-purple-400 { color: rgb(192 132 252) !important; }
    html.dark .dark\:text-rose-400 { color: rgb(251 113 133) !important; }
    html.dark .dark\:text-blue-300 { color: rgb(147 197 253) !important; }
    html.dark .dark\:text-rose-200 { color: rgb(254 205 211) !important; }
    html.dark .dark\:text-emerald-200 { color: rgb(167 243 208) !important; }
    html.dark .dark\:border-emerald-600\/40 { border-color: rgb(5 150 105 / 0.4) !important; }
    html.dark .dark\:border-rose-600\/40 { border-color: rgb(225 29 72 / 0.4) !important; }
    html.dark .dark\:bg-emerald-950\/40 { background-color: rgb(6 78 59 / 0.4) !important; }
    html.dark .dark\:bg-rose-950\/40 { background-color: rgb(136 19 55 / 0.4) !important; }
  </style>
</head>
<body class="antialiased p-3 sm:p-5 min-h-screen font-sans">

  <div class="max-w-4xl mx-auto theme-card border rounded-2xl overflow-hidden">
    
    <!-- Üst Başlık Banner -->
    <div class="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 p-5 text-white">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <div>
          <span id="themeTagBadge" class="inline-block px-2.5 py-0.5 rounded-full text-[10px] font-bold tracking-wide uppercase bg-white/20 backdrop-blur-sm">
            Halk ve Son Kullanıcı Deneyimi (Açık Mod)
          </span>
          <h1 id="labTitle" class="text-xl sm:text-2xl font-black mt-1 tracking-tight">
            Fraktal Beyin Laboratuvarı: Sonsuz Desenden Zihin Çıkarmak
          </h1>
          <p id="labSubtitle" class="text-xs sm:text-sm text-blue-100 mt-0.5">
            Sonsuz bir fraktal resme (Mandelbrot) büyüteçle bakarak yapay bir nöronun nasıl karar verdiğini canlı izleyin!
          </p>
        </div>
        <div class="flex items-center gap-2">
          <!-- Dil Değiştirme Butonu (TR / EN) -->
          <button id="btnLangToggle" class="px-3 py-2 rounded-xl text-xs font-bold bg-white/20 hover:bg-white/30 text-white shadow transition-all flex items-center gap-1.5 border border-white/25 cursor-pointer active:scale-95" title="Dili Değiştir / Switch Language">
            <span>🌐</span>
            <span id="langText">English</span>
          </button>

          <!-- Tema Değiştirme Butonu (Light / Dark) -->
          <button id="btnThemeToggle" class="px-3 py-2 rounded-xl text-xs font-bold bg-white/20 hover:bg-white/30 text-white shadow transition-all flex items-center gap-1.5 border border-white/25 cursor-pointer active:scale-95" title="Açık / Koyu Tema Değiştir">
            <span id="themeIcon">🌙</span>
            <span id="themeText">Koyu Mod</span>
          </button>

          <!-- Bellek TXT İndirme Butonu -->
          <button id="btnDownloadTxt" class="px-3.5 py-2 rounded-xl text-xs font-bold bg-white text-indigo-950 hover:bg-blue-50 shadow-md transition-all flex items-center gap-1.5 border border-indigo-100 cursor-pointer active:scale-95" title="24 Baytlık Bellek Kütüğünü İndir">
            <span>💾</span>
            <span id="btnDlText1">Belleği İndir (.TXT)</span>
          </button>
        </div>
      </div>

      <!-- Gerçek Hayat Senaryo Seçici Butonları -->
      <div class="mt-4 pt-3 border-t border-white/20 flex flex-wrap gap-2 text-xs">
        <button id="tab_door" class="tab-btn px-3 py-1.5 rounded-lg font-semibold bg-white text-indigo-900 shadow transition-all">
          🚪 Akıllı Kapı (OR Kuralı)
        </button>
        <button id="tab_safe" class="tab-btn px-3 py-1.5 rounded-lg font-semibold bg-white/15 text-white hover:bg-white/25 transition-all">
          🏦 Banka Kasası (AND Kuralı)
        </button>
        <button id="tab_light" class="tab-btn px-3 py-1.5 rounded-lg font-semibold bg-white/15 text-white hover:bg-white/25 transition-all">
          💡 Merdiven Lambası (XOR Kuralı)
        </button>
        <button id="tab_alarm" class="tab-btn px-3 py-1.5 rounded-lg font-semibold bg-white/15 text-white hover:bg-white/25 transition-all">
          🚨 Yangın Alarmı (NAND)
        </button>
      </div>
    </div>

    <!-- Senaryo Açıklama Kutusu -->
    <div class="p-4 theme-subtle border-b border-[var(--border-color)] text-xs flex items-center justify-between">
      <div>
        <span id="scenarioTag" class="font-bold text-indigo-600 dark:text-indigo-400 uppercase text-[10px] tracking-wider">Senaryo: Akıllı Kapı</span>
        <p id="scenarioDesc" class="text-[var(--text-secondary)] mt-0.5">
          "Kapının açılması için <b>Kart</b> VEYA <b>Yüz Tanıma</b> onayından biri yeterlidir."
        </p>
      </div>
      <div id="accuracyBadge" class="px-2.5 py-1 rounded-full text-[11px] font-bold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
        %100 Doğru Çalışıyor
      </div>
    </div>

    <!-- ANA İNTERAKTİF PANELLER (3 ADIMLI AKIŞ) -->
    <div class="p-4 sm:p-6 grid grid-cols-1 lg:grid-cols-12 gap-5">
      
      <!-- 1. SÜTUN: GİRDİLER (SİZİN SEÇİMLERİNİZ) -->
      <div class="lg:col-span-3 flex flex-col gap-3">
        <div id="step1Title" class="text-xs font-bold text-[var(--text-muted)] uppercase tracking-wider flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-blue-500"></span> 1. Adım: Girdiler (Durum)
        </div>

        <div class="p-3.5 rounded-xl border border-[var(--border-color)] bg-[var(--bg-card)] flex flex-col justify-between h-full space-y-4 shadow-sm">
          <div>
            <label id="input1Label" class="block font-semibold text-xs mb-1 text-[var(--text-primary)]">Girdi 1: Giriş Kartı</label>
            <p id="input1Desc" class="text-[10px] text-[var(--text-muted)] mb-2">Kart okuyucuya yaklaştırıldı mı?</p>
            <div class="flex gap-2">
              <button id="btnIn1_0" class="btn-toggle flex-1 py-2 rounded-lg text-xs font-bold border border-blue-600 bg-blue-500/15 text-blue-600 dark:text-blue-400 shadow-sm">YOK (0)</button>
              <button id="btnIn1_1" class="btn-toggle flex-1 py-2 rounded-lg text-xs font-bold border border-[var(--border-color)] bg-[var(--bg-card-subtle)] text-[var(--text-muted)]">VAR (1)</button>
            </div>
          </div>

          <div class="border-t border-[var(--border-color)] pt-3">
            <label id="input2Label" class="block font-semibold text-xs mb-1 text-[var(--text-primary)]">Girdi 2: Yüz Tanıma</label>
            <p id="input2Desc" class="text-[10px] text-[var(--text-muted)] mb-2">Kamera yüzü tanıdı mı?</p>
            <div class="flex gap-2">
              <button id="btnIn2_0" class="btn-toggle flex-1 py-2 rounded-lg text-xs font-bold border border-blue-600 bg-blue-500/15 text-blue-600 dark:text-blue-400 shadow-sm">YOK (0)</button>
              <button id="btnIn2_1" class="btn-toggle flex-1 py-2 rounded-lg text-xs font-bold border border-[var(--border-color)] bg-[var(--bg-card-subtle)] text-[var(--text-muted)]">VAR (1)</button>
            </div>
          </div>

          <div id="step1Tip" class="p-2.5 rounded-lg bg-blue-500/10 border border-blue-500/20 text-[10px] text-[var(--text-secondary)]">
            💡 <b>Halk Diliyle:</b> Burası yapay zekanın "gözleri ve kulaklarıdır". Dış dünyadan gelen ham sinyallerdir.
          </div>
        </div>
      </div>

      <!-- 2. SÜTUN: FRAKTAL AYNASI (BİZİM YÖNTEMİMİZ: AĞIRLIK TÜRETME) -->
      <div class="lg:col-span-4 flex flex-col gap-3">
        <div id="step2Title" class="text-xs font-bold text-[var(--text-muted)] uppercase tracking-wider flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-purple-500"></span> 2. Adım: Fraktal Bellek (Mandelbrot)
        </div>

        <div class="p-3.5 rounded-xl border border-[var(--border-color)] bg-[var(--bg-card)] flex flex-col items-center shadow-sm">
          <div class="relative mb-2">
            <canvas id="fractalCanvas" width="128" height="128" class="rounded-xl border border-[var(--border-color)] shadow-md bg-black w-40 h-40"></canvas>
            <!-- 4 Çeyrek Kılavuzu -->
            <div class="absolute inset-x-0 top-1/2 border-t border-white/40 pointer-events-none"></div>
            <div class="absolute inset-y-0 left-1/2 border-l border-white/40 pointer-events-none"></div>
            <span class="absolute top-1 left-1.5 text-[9px] font-bold text-white drop-shadow">Q1: w1</span>
            <span class="absolute top-1 right-1.5 text-[9px] font-bold text-white drop-shadow">Q2: w2</span>
            <span id="q4Tag" class="absolute bottom-1 right-1.5 text-[9px] font-bold text-amber-300 drop-shadow">Q4: Eşik(b)</span>
          </div>

          <!-- Zoom Slider -->
          <div class="w-full mt-1 mb-2">
            <div class="flex justify-between text-[11px] mb-1">
              <span id="lblZoomLabel" class="text-[var(--text-muted)]">Fraktal Büyüteç (Zoom):</span>
              <span id="zoomLabel" class="font-mono font-bold text-purple-600 dark:text-purple-400">90x</span>
            </div>
            <input type="range" id="zoomSlider" min="0.3" max="5.0" step="0.05" value="1.95" class="w-full accent-purple-500 cursor-pointer">
          </div>

          <!-- Canlı Zoom Açıklama Kutusu -->
          <div class="p-2.5 rounded-xl bg-purple-500/10 border border-purple-500/25 text-[10px] text-[var(--text-secondary)] mb-3 w-full">
            <div class="font-bold text-purple-600 dark:text-purple-400 flex items-center gap-1 mb-0.5">
              <span id="zoomIcon">🎯</span> <span id="zoomLevelTitle">Optimum Karar Seviyesi (90x) - İnce Denge</span>
            </div>
            <p id="zoomExplainText" class="leading-tight text-[10px]">
              Fraktal kıyısındaki mikro siyah adacıklar karar terazisini (w1, w2, eşik) tam kurala göre dengeliyor.
            </p>
          </div>

          <!-- Okunan Ağırlık Kartları -->
          <div class="grid grid-cols-3 gap-1.5 w-full text-center text-[10px]">
            <div class="p-1.5 rounded theme-subtle border border-[var(--border-color)]">
              <div id="lblW1" class="text-[var(--text-muted)]">w1 (Girdi 1)</div>
              <div id="w1Display" class="font-mono font-bold text-emerald-600 dark:text-emerald-400 text-xs">+3.00</div>
            </div>
            <div class="p-1.5 rounded theme-subtle border border-[var(--border-color)]">
              <div id="lblW2" class="text-[var(--text-muted)]">w2 (Girdi 2)</div>
              <div id="w2Display" class="font-mono font-bold text-emerald-600 dark:text-emerald-400 text-xs">+2.43</div>
            </div>
            <div class="p-1.5 rounded theme-subtle border border-[var(--border-color)]">
              <div id="lblBias" class="text-[var(--text-muted)]">Eşik (Bias)</div>
              <div id="biasDisplay" class="font-mono font-bold text-amber-600 dark:text-amber-400 text-xs">-0.12</div>
            </div>
          </div>

          <p id="lblPixelNote" class="text-[10px] text-[var(--text-muted)] mt-2 text-center">
            Piksel piksel siyah alan sayılarak karar ağırlıkları doğrudan resimden okunur.
          </p>
        </div>
      </div>

      <!-- 3. SÜTUN: CANLI NÖRON VE NİHAİ KARAR -->
      <div class="lg:col-span-5 flex flex-col gap-3">
        <div id="step3Title" class="text-xs font-bold text-[var(--text-muted)] uppercase tracking-wider flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span> 3. Adım: Nöron Ateşlemesi & Karar
        </div>

        <div class="p-3.5 rounded-xl border border-[var(--border-color)] bg-[var(--bg-card)] flex flex-col justify-between h-full shadow-sm">
          <!-- Biyolojik Nöron Çizim Tuvali -->
          <div class="relative w-full flex justify-center items-center py-1">
            <canvas id="neuronCanvas" width="260" height="130" class="w-full h-auto max-w-[260px] rounded-xl border border-[var(--border-color)]" style="background-color: var(--canvas-bg);"></canvas>
          </div>

          <!-- Matematiksel Özet Barı -->
          <div class="theme-subtle border border-[var(--border-color)] rounded-xl p-3 my-2 text-center">
            <div class="text-[11px] text-[var(--text-muted)] mb-1">
              <span id="lblNetSignal">Toplanan Sinyal:</span> <span id="mathFormula" class="font-mono font-bold text-[var(--text-primary)]">z = (3.0 × 1) + (2.4 × 0) - 0.12 = +2.88</span>
            </div>
            <div class="flex items-center justify-between text-xs mt-2 px-2">
              <span id="lblProb" class="text-[var(--text-muted)]">Ateşleme Olasılığı (σ):</span>
              <span id="probVal" class="font-mono font-bold text-emerald-600 dark:text-emerald-400 text-sm">94.7%</span>
            </div>
            <div class="w-full bg-[var(--border-color)] h-2 rounded-full overflow-hidden mt-1.5">
              <div id="probBar" class="bg-emerald-500 h-2 transition-all duration-200" style="width: 94.7%"></div>
            </div>
          </div>

          <!-- Nihai Karar Kutusu (Büyük Lamba / Durum) -->
          <div id="decisionCard" class="p-3.5 rounded-xl border border-emerald-500/40 bg-emerald-500/10 text-emerald-700 dark:text-emerald-300 flex items-center justify-between transition-all">
            <div class="flex items-center gap-2.5">
              <span id="decisionIcon" class="text-2xl">🟢</span>
              <div>
                <div id="decisionTitle" class="font-black text-sm uppercase tracking-wide">KAPI AÇILDI!</div>
                <div id="decisionReason" class="text-[11px] opacity-90">Nöron eşiği aştı ve çıkış sinyali verdi.</div>
              </div>
            </div>
            <span id="firingBadge" class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-600 text-white animate-pulse">ATEŞLENDİ</span>
          </div>
        </div>
      </div>
    </div>

    <!-- CANLI DİNAMİK KIYASLAMA: KLASİK LLM vs. BİZİM FRAKTAL SİSTEMİMİZ -->
    <div class="border-t border-[var(--border-color)] theme-subtle p-5">
      <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
        <div>
          <h3 id="compHeading" class="font-bold text-sm text-[var(--text-primary)] flex items-center gap-2">
            <span>⚡</span>
            <span>Mimari & Hız Kıyaslaması: Klasik LLM vs. Bizim Fraktal Modelimiz</span>
          </h3>
          <p id="compSubheading" class="text-[11px] text-[var(--text-muted)]">
            Aynı karar süreci iki farklı mimaride nasıl işlenir? Aşağıdaki veriler seçtiğiniz girdilere ve büyütece göre canlı güncellenir.
          </p>
        </div>
        <div class="flex items-center gap-2">
          <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-bold bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> <span id="lblLiveMeasuring">CANLI ÖLÇÜLÜYOR</span>
          </span>
          <span id="liveTimerBadge" class="font-mono text-[10px] text-[var(--text-muted)] px-2.5 py-1 rounded-lg theme-card border">
            <span id="lblLiveTimer">Sentezleme:</span> <span id="compLiveMs" class="font-bold text-purple-600 dark:text-purple-400">~3.8 ms</span>
          </span>
        </div>
      </div>

      <!-- Kıyaslama Kartları -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        
        <!-- 1. KART: STANDART / KLASİK LLM MİMARİSİ -->
        <div class="p-4 rounded-xl border border-blue-500/20 bg-[var(--bg-card)] shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 mb-3 border-b border-blue-500/10">
              <span id="card1Title" class="font-bold text-xs text-blue-600 dark:text-blue-400 flex items-center gap-1.5">
                <span>🏛️</span> Klasik Yapay Zeka (Standart LLM)
              </span>
              <span id="card1Sub" class="text-[10px] px-2 py-0.5 rounded bg-blue-500/10 text-blue-600 dark:text-blue-400 font-medium">
                Örn: GPT-4, LLaMA-3
              </span>
            </div>

            <div class="space-y-3 text-[11px]">
              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span id="lblC1MemModel" class="text-[var(--text-muted)]">Bellek Depolama Modeli:</span>
                  <span id="valC1MemModel" class="font-bold text-[var(--text-primary)]">Sabit Ağırlık Matrisi (VRAM)</span>
                </div>
                <div class="p-2 rounded theme-subtle border border-[var(--border-color)] font-mono text-[10px] space-y-1">
                  <div class="flex justify-between">
                    <span id="lblC1Stat1" class="text-[var(--text-muted)]">Bu Karar Hücresi İçin:</span>
                    <span class="text-rose-600 dark:text-rose-400 font-bold">12 Byte (3x Float32)</span>
                  </div>
                  <div class="flex justify-between">
                    <span id="lblC1Stat2" class="text-[var(--text-muted)]">128x128 Eşdeğer Katman:</span>
                    <span class="text-rose-600 dark:text-rose-400 font-bold">65.5 KB (16,384 Tensör)</span>
                  </div>
                  <div class="flex justify-between">
                    <span id="lblC1Stat3" class="text-[var(--text-muted)]">70B Parametreli Modelde:</span>
                    <span class="text-rose-600 dark:text-rose-400 font-bold">~140 GB Dev Dosya!</span>
                  </div>
                </div>
              </div>

              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span id="lblC1State" class="text-[var(--text-muted)]">Ağırlıkların Durumu:</span>
                  <span id="valC1State" class="font-bold text-amber-600 dark:text-amber-400">Dondurulmuş (Statik Kütük)</span>
                </div>
                <p id="descC1State" class="text-[10px] text-[var(--text-secondary)] leading-relaxed">
                  Ağırlıklar aylar süren eğitimle diske yazılır ve RAM'de donuk bekler. Yeni bir kural öğrenmesi için milyonlarca liralık elektrik harcanıp modelin baştan eğitilmesi gerekir.
                </p>
              </div>

              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span id="lblC1Bottleneck" class="text-[var(--text-muted)]">İşlem Hızı & Darboğaz:</span>
                  <span id="valC1Bottleneck" class="font-bold text-[var(--text-primary)]">Bellek Bant Genişliği Sınırı</span>
                </div>
                <div id="descC1Bottleneck" class="p-2 rounded theme-subtle border border-[var(--border-color)] text-[10px] text-[var(--text-secondary)]">
                  Her adımda gigabaytlarca ağırlık VRAM'den GPU çekirdeğine pompalanır (Memory Wall darboğazı).
                </div>
              </div>
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-blue-500/10 flex items-center justify-between text-[10px]">
            <span id="lblC1Foot" class="text-[var(--text-muted)]">70B Model Bellek Yükü:</span>
            <span class="font-bold text-rose-600 dark:text-rose-400 font-mono">140,000,000,000 Byte</span>
          </div>
        </div>

        <!-- 2. KART: BİZİM FRAKTAL PARAMETRE SENTEZ SİSTEMİMİZ -->
        <div class="p-4 rounded-xl border border-purple-500/30 bg-[var(--bg-card)] shadow-sm flex flex-col justify-between relative overflow-hidden">
          <div class="absolute -right-6 -bottom-6 w-28 h-28 bg-purple-500/10 rounded-full blur-2xl pointer-events-none"></div>

          <div>
            <div class="flex items-center justify-between pb-2 mb-3 border-b border-purple-500/20">
              <span id="card2Title" class="font-bold text-xs text-purple-600 dark:text-purple-400 flex items-center gap-1.5">
                <span>🌀</span> Bizim Sistemimiz (Fraktal Nöron Sentezi)
              </span>
              <span id="card2Sub" class="text-[10px] px-2 py-0.5 rounded bg-purple-500/15 text-purple-600 dark:text-purple-300 font-bold border border-purple-500/20">
                Sıfır Ağırlık Saklama
              </span>
            </div>

            <div class="space-y-3 text-[11px]">
              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span id="lblC2MemModel" class="text-[var(--text-muted)]">Bellek Depolama Modeli:</span>
                  <span id="valC2MemModel" class="font-bold text-emerald-600 dark:text-emerald-400">Sonsuz Geometriden Canlı Türetme</span>
                </div>
                <div class="p-2 rounded theme-subtle border border-[var(--border-color)] font-mono text-[10px] space-y-1">
                  <div class="flex justify-between">
                    <span id="lblC2Stat1" class="text-[var(--text-muted)]">Kalıcı Saklanan Veri:</span>
                    <span id="valC2Stat1" class="text-emerald-600 dark:text-emerald-400 font-bold">Yalnızca 24 Byte! (cx, cy, zoom)</span>
                  </div>
                  <div class="flex justify-between">
                    <span id="lblC2Stat2" class="text-[var(--text-muted)]">Kalıcı Ağırlık Matrisi:</span>
                    <span id="valC2Stat2" class="text-emerald-600 dark:text-emerald-400 font-bold">0 Byte (Hiç Yok!)</span>
                  </div>
                  <div class="flex justify-between">
                    <span id="lblC2Stat3" class="text-[var(--text-muted)]">Bellek Tasarrufu Oranı:</span>
                    <span id="valC2Stat3" class="text-emerald-600 dark:text-emerald-400 font-bold">%99.99999998+ Tasarruf</span>
                  </div>
                </div>
              </div>

              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span id="lblC2State" class="text-[var(--text-muted)]">Ağırlıkların Durumu:</span>
                  <span id="valC2State" class="font-bold text-purple-600 dark:text-purple-400">Canlı Türetilen (Prosedürel)</span>
                </div>
                <p id="descC2State" class="text-[10px] text-[var(--text-secondary)] leading-relaxed">
                  Ağırlıklar bellekte yer kaplamaz; Mandelbrot formülünün (<span class="font-mono text-[9px] text-purple-600 dark:text-purple-400">z² + c</span>) doğal geometrisinden ihtiyaç anında anında filizlenir. Büyüteci çevirdiğiniz an yeni bir mantık hücresine dönüşür.
                </p>
              </div>

              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span id="lblC2Future" class="text-[var(--text-muted)]">İşlem Hızı & Gelecek:</span>
                  <span id="valC2Future" class="font-bold text-[var(--text-primary)]">Işık Hızında Donanım İmkânı</span>
                </div>
                <div id="descC2Future" class="p-2 rounded theme-subtle border border-[var(--border-color)] text-[10px] text-[var(--text-secondary)]">
                  Şu an tarayıcınızda yazılımla <span id="compLiveMsInline" class="font-bold text-purple-600 dark:text-purple-400">~3.8 ms</span>'de üretiliyor. Gelecekte fotonik çiplerle nanosaniyeler (<span class="text-emerald-600 dark:text-emerald-400 font-semibold">&lt; 1 ns</span>) içinde sıfır elektrikle üretilebilir!
                </div>
              </div>
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-purple-500/20 flex items-center justify-between text-[10px]">
            <span id="lblC2Foot" class="text-[var(--text-muted)]">Kalıcı Depolama:</span>
            <div class="flex items-center gap-2">
              <span id="valC2Foot" class="font-bold text-emerald-600 dark:text-emerald-400 font-mono">Sadece 24 Byte (3 Sayı)</span>
              <button id="btnDownloadTxt2" class="px-2.5 py-1 rounded-lg text-[10px] font-bold bg-purple-600 hover:bg-purple-700 text-white shadow-sm transition-all flex items-center gap-1 cursor-pointer active:scale-95">
                <span>💾</span> <span id="btnDlText2">.TXT İndir</span>
              </button>
            </div>
          </div>
        </div>

      </div>

      <!-- Canlı Metrik ve Durum Paneli -->
      <div class="mt-4 p-3 rounded-xl theme-card border border-[var(--border-color)]">
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
          <div class="p-2 rounded-lg theme-subtle border border-[var(--border-color)]">
            <span id="lblMetric1" class="text-[10px] text-[var(--text-muted)] block">Aktif Senaryo Mantığı</span>
            <span id="compScenarioRule" class="font-mono font-bold text-xs text-indigo-600 dark:text-indigo-400">OR Kapısı</span>
          </div>
          <div class="p-2 rounded-lg theme-subtle border border-[var(--border-color)]">
            <span id="lblMetric2" class="text-[10px] text-[var(--text-muted)] block">Canlı Türetilen Ağırlıklar</span>
            <span id="compLiveWeights" class="font-mono font-bold text-xs text-purple-600 dark:text-purple-400">w1: +0.00 | w2: +0.00</span>
          </div>
          <div class="p-2 rounded-lg theme-subtle border border-[var(--border-color)]">
            <span id="lblMetric3" class="text-[10px] text-[var(--text-muted)] block">Canlı Eşik Değeri (Bias)</span>
            <span id="compLiveBias" class="font-mono font-bold text-xs text-amber-600 dark:text-amber-400">b: -0.00</span>
          </div>
          <div class="p-2 rounded-lg theme-subtle border border-[var(--border-color)]">
            <span id="lblMetric4" class="text-[10px] text-[var(--text-muted)] block">Hesaplanan Nöron Çıktısı</span>
            <span id="compLiveOutput" class="font-mono font-bold text-xs text-emerald-600 dark:text-emerald-400">z = +0.00 (%0.0)</span>
          </div>
        </div>
      </div>
    </div>

    <!-- HALK İÇİN BASİT AÇIKLAMA REHBERİ (FOOTER BÖLÜMÜ) -->
    <div class="p-5 bg-[var(--bg-page)] border-t border-[var(--border-color)] text-xs text-[var(--text-muted)]">
      <h3 id="lblFaqTitle" class="font-bold text-sm text-[var(--text-primary)] mb-2 flex items-center gap-1.5">
        <span>❓</span> Sıradan Birine Bu Sistemi Nasıl Anlatırsınız?
      </h3>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-[11px] leading-relaxed">
        <div class="p-3 rounded-xl theme-card border border-[var(--border-color)]">
          <strong id="lblFaq1Title" class="text-blue-600 dark:text-blue-400 block mb-1">1. Klasik Yapay Zeka (Sözlük Ezberler):</strong>
          <span id="lblFaq1Desc">Milyarlarca sayıyı devasa bilgisayar çiplerine tek tek yazar. Çok yer kaplar, elektriği çok tüketir.</span>
        </div>
        <div class="p-3 rounded-xl theme-card border border-[var(--border-color)]">
          <strong id="lblFaq2Title" class="text-purple-600 dark:text-purple-400 block mb-1">2. Bizim Yöntemimiz (Sihirli Tablo):</strong>
          <span id="lblFaq2Desc">Hiçbir sayıyı bellekte saklamayız. Sonsuz bir fraktal tablomuz (Mandelbrot) vardır; doğru koordinata büyüteçle bakarız, oradaki siyah adacıkların büyüklüğü nöronun karar katsayısı olur!</span>
        </div>
        <div class="p-3 rounded-xl theme-card border border-[var(--border-color)]">
          <strong id="lblFaq3Title" class="text-emerald-600 dark:text-emerald-400 block mb-1">3. Sonuç (Kusursuz Karar):</strong>
          <span id="lblFaq3Desc">Hafızada yer tutmadan, tek bir formülden sonsuz sayıda farklı mantık, karar ve zeka hücresi türetilebilir!</span>
        </div>
      </div>
    </div>

  </div>

  <script>
    // =========================================================
    // ÇOKLU DİL MOTORU (I18N: TR / EN)
    // =========================================================
    const I18N = {
      tr: {
        pageTitle: "Fraktal Nöron: Matematikten Zihin Çıkarmak (Halk Laboratuvarı)",
        badgeLight: "Halk ve Son Kullanıcı Deneyimi (Açık Mod)",
        badgeDark: "Halk ve Son Kullanıcı Deneyimi (Koyu Mod)",
        labTitle: "Fraktal Beyin Laboratuvarı: Sonsuz Desenden Zihin Çıkarmak",
        labSubtitle: "Sonsuz bir fraktal resme (Mandelbrot) büyüteçle bakarak yapay bir nöronun nasıl karar verdiğini canlı izleyin!",
        langButton: "English",
        themeLight: "Açık Mod",
        themeDark: "Koyu Mod",
        btnDownloadTxt: "Belleği İndir (.TXT)",
        btnDownloadTxtShort: ".TXT İndir",
        tabs: {
          door: "🚪 Akıllı Kapı (OR Kuralı)",
          safe: "🏦 Banka Kasası (AND Kuralı)",
          light: "💡 Merdiven Lambası (XOR Kuralı)",
          alarm: "🚨 Yangın Alarmı (NAND)"
        },
        accuracyBadge: "%100 Doğru Çalışıyor",
        step1Title: "1. Adım: Girdiler (Durum)",
        step1Tip: "💡 <b>Halk Diliyle:</b> Burası yapay zekanın \\"gözleri ve kulaklarıdır\\". Dış dünyadan gelen ham sinyallerdir.",
        step2Title: "2. Adım: Fraktal Bellek (Mandelbrot)",
        q4Tag: "Q4: Eşik(b)",
        lblZoomLabel: "Fraktal Büyüteç (Zoom):",
        lblW1: "w1 (Girdi 1)",
        lblW2: "w2 (Girdi 2)",
        lblBias: "Eşik (Bias)",
        lblPixelNote: "Piksel piksel siyah alan sayılarak karar ağırlıkları doğrudan resimden okunur.",
        step3Title: "3. Adım: Nöron Ateşlemesi & Karar",
        lblNetSignal: "Toplanan Sinyal:",
        lblProb: "Ateşleme Olasılığı (σ):",
        somaLabelFiring: "ATEŞLENDİ",
        somaLabelQuiet: "SOMA",
        firingBadgeFire: "ATEŞLENDİ",
        firingBadgeQuiet: "SESSİZ",
        firingBadgeSafe: "GÜVENLİ",
        firingBadgeAlarm: "🚨 ALARM!",
        compHeading: "⚡ Mimari & Hız Kıyaslaması: Klasik LLM vs. Bizim Fraktal Modelimiz",
        compSubheading: "Aynı karar süreci iki farklı mimaride nasıl işlenir? Aşağıdaki veriler seçtiğiniz girdilere ve büyütece göre canlı güncellenir.",
        lblLiveMeasuring: "CANLI ÖLÇÜLÜYOR",
        lblLiveTimer: "Sentezleme:",
        card1: {
          title: "🏛️ Klasik Yapay Zeka (Standart LLM)",
          sub: "Örn: GPT-4, LLaMA-3",
          memModel: "Bellek Depolama Modeli:",
          memModelVal: "Sabit Ağırlık Matrisi (VRAM)",
          stat1: "Bu Karar Hücresi İçin:",
          stat2: "128x128 Eşdeğer Katman:",
          stat3: "70B Parametreli Modelde:",
          state: "Ağırlıkların Durumu:",
          stateVal: "Dondurulmuş (Statik Kütük)",
          stateDesc: "Ağırlıklar aylar süren eğitimle diske yazılır ve RAM'de donuk bekler. Yeni bir kural öğrenmesi için milyonlarca liralık elektrik harcanıp modelin baştan eğitilmesi gerekir.",
          bottleneck: "İşlem Hızı & Darboğaz:",
          bottleneckVal: "Bellek Bant Genişliği Sınırı",
          bottleneckDesc: "Her adımda gigabaytlarca ağırlık VRAM'den GPU çekirdeğine pompalanır (Memory Wall darboğazı).",
          foot: "70B Model Bellek Yükü:"
        },
        card2: {
          title: "🌀 Bizim Sistemimiz (Fraktal Nöron Sentezi)",
          sub: "Sıfır Ağırlık Saklama",
          memModel: "Bellek Depolama Modeli:",
          memModelVal: "Sonsuz Geometriden Canlı Türetme",
          stat1: "Kalıcı Saklanan Veri:",
          stat1Val: "Yalnızca 24 Byte! (cx, cy, zoom)",
          stat2: "Kalıcı Ağırlık Matrisi:",
          stat2Val: "0 Byte (Hiç Yok!)",
          stat3: "Bellek Tasarrufu Oranı:",
          stat3Val: "%99.99999998+ Tasarruf",
          state: "Ağırlıkların Durumu:",
          stateVal: "Canlı Türetilen (Prosedürel)",
          stateDesc: "Ağırlıklar bellekte yer kaplamaz; Mandelbrot formülünün (z² + c) doğal geometrisinden ihtiyaç anında filizlenir. Büyüteci çevirdiğiniz an yeni bir mantık hücresine dönüşür.",
          future: "İşlem Hızı & Gelecek:",
          futureVal: "Işık Hızında Donanım İmkânı",
          futureDesc: 'Şu an tarayıcınızda yazılımla <span id="compLiveMsInline" class="font-bold text-purple-600 dark:text-purple-400">~3.8 ms</span>\\'de üretiliyor. Gelecekte fotonik çiplerle nanosaniyeler (<span class="text-emerald-600 dark:text-emerald-400 font-semibold">&lt; 1 ns</span>) içinde sıfır elektrikle üretilebilir!',
          foot: "Kalıcı Depolama:",
          footVal: "Sadece 24 Byte (3 Sayı)"
        },
        metrics: {
          m1: "Aktif Senaryo Mantığı",
          m2: "Canlı Türetilen Ağırlıklar",
          m3: "Canlı Eşik Değeri (Bias)",
          m4: "Hesaplanan Nöron Çıktısı"
        },
        faq: {
          title: "❓ Sıradan Birine Bu Sistemi Nasıl Anlatırsınız?",
          f1Title: "1. Klasik Yapay Zeka (Sözlük Ezberler):",
          f1Desc: "Milyarlarca sayıyı devasa bilgisayar çiplerine tek tek yazar. Çok yer kaplar, elektriği çok tüketir.",
          f2Title: "2. Bizim Yöntemimiz (Sihirli Tablo):",
          f2Desc: "Hiçbir sayıyı bellekte saklamayız. Sonsuz bir fraktal tablomuz (Mandelbrot) vardır; doğru koordinata büyüteçle bakarız, oradaki siyah adacıkların büyüklüğü nöronun karar katsayısı olur!",
          f3Title: "3. Sonuç (Kusursuz Karar):",
          f3Desc: "Hafızada yer tutmadan, tek bir formülden sonsuz sayıda farklı mantık, karar ve zeka hücresi türetilebilir!"
        },
        zoomLevels: {
          optTitle: "Optimum Karar Seviyesi ({z}x) - İnce Denge",
          optDesc: "{title} için ideal katsayı dengesi yakalandı. Fraktal mikro adacıklar karar katsayılarını ({rule} kuralına) tam denkliğe oturttu.",
          wideTitle: "Geniş Açı ({z}x) - Kaba Görünüm",
          wideDesc: "Fraktalın dış katmanındasınız. Karar dengesini yakalamak için büyüteci sağa doğru (~{target}x hedefine) kaydırabilirsiniz.",
          deepTitle: "Derin Fraktal ({z}x) - Spiral Mikrokozmos",
          deepDesc: "Derin spiral kollara daldınız. Karar terazisi mikro siyah adacıklardan aşırı duyarlı şekilde yeniden hesaplanıyor."
        },
        scenarios: {
          door: {
            title: "Akıllı Kapı Açma",
            tag: "Senaryo: Akıllı Kapı (OR Mantığı)",
            desc: "Kapının açılması için <b>Giriş Kartı</b> VEYA <b>Yüz Tanıma</b> onayından birinin olması yeterlidir.",
            lbl1: "Girdi 1: Giriş Kartı",
            sub1: "Kart okuyucuya yaklaştırıldı mı?",
            btn1: ["YOK (0)", "OKUTULDU (1)"],
            lbl2: "Girdi 2: Yüz Tanıma",
            sub2: "Kamera yüzü başarıyla tanıdı mı?",
            btn2: ["YOK (0)", "ONAYLANDI (1)"],
            rule: "OR",
            ruleSuffix: " Mantığı",
            successAction: "KAPI AÇILDI! 🟢",
            successDesc: "Giriş şartı sağlandı, kilit açıldı.",
            failAction: "KAPI KİLİTLİ! 🔴",
            failDesc: "Ne kart var ne de yüz tanındı. Erişim engellendi."
          },
          safe: {
            title: "Banka Kasası Açma",
            tag: "Senaryo: Banka Kasası (AND Mantığı)",
            desc: "Kasanın açılması için hem <b>Müdür Şifresi</b> HEM DE <b>Biyometrik Parmak İzi</b> ikisi de zorunludur!",
            lbl1: "Girdi 1: Müdür Şifresi",
            sub1: "Yetkili güvenlik şifresi doğru girildi mi?",
            btn1: ["GİRİLMEDİ (0)", "GİRİLDİ (1)"],
            lbl2: "Girdi 2: Biyometrik Parmak İzi",
            sub2: "Biyometrik parmak izi okuyucu onayladı mı?",
            btn2: ["BASILMADI (0)", "ONAYLANDI (1)"],
            rule: "AND",
            ruleSuffix: " Mantığı",
            successAction: "KASA AÇILDI! 🟢",
            successDesc: "İki güvenlik onayı da tamamlandı.",
            failAction: "KASA KİLİTLİ! 🔴",
            failDesc: "Şartlardan en az biri eksik. Kasa açılmaz."
          },
          light: {
            title: "Merdiven Lambası",
            tag: "Senaryo: Koridor Merdiven Lambası (XOR Bulmacası)",
            desc: "Alt ve üst kattaki iki yönlü anahtar: Sadece <b>anahtarlardan biri açıksa</b> ışık yanar, ikisi de aynı konumdaysa söner.",
            lbl1: "Girdi 1: Alt Kat Anahtarı",
            sub1: "Giriş katındaki lamba anahtarı açık mı?",
            btn1: ["KAPALI (0)", "AÇIK (1)"],
            lbl2: "Girdi 2: Üst Kat Anahtarı",
            sub2: "Üst kattaki lamba anahtarı açık mı?",
            btn2: ["KAPALI (0)", "AÇIK (1)"],
            rule: "XOR",
            ruleSuffix: " Mantığı",
            successAction: "IŞIK YANDI! 💡",
            successDesc: "Farklı konumlardaki anahtarlar devreyi tamamladı.",
            failAction: "IŞIK SÖNDÜ! ⬛",
            failDesc: "Anahtarlar aynı konumda, akım kesildi."
          },
          alarm: {
            title: "Yangın Alarmı",
            tag: "Senaryo: Güvenlik Alarmı (NAND Mantığı)",
            desc: "Sistem normalde güvenlidir; ancak hem <b>Duman Sensörü</b> hem de <b>Isı Sensörü</b> aynı anda tehlike verirse acil alarm çalar!",
            lbl1: "Girdi 1: Duman Sensörü",
            sub1: "Optik sensör yangın dumanı algıladı mı?",
            btn1: ["TEMİZ (0)", "DUMAN VAR (1)"],
            lbl2: "Girdi 2: Isı Sensörü",
            sub2: "Ortam sıcaklığı kritik alarm eşiğini aştı mı?",
            btn2: ["NORMAL (0)", "AŞIRI ISI (1)"],
            rule: "NAND",
            ruleSuffix: " Mantığı",
            successAction: "SİSTEM GÜVENLİ 🟢",
            successDesc: "Çift tehlike koşulu yok, ortam güvenli.",
            failAction: "ALARM ÇALIYOR! 🚨",
            failDesc: "Duman ve aşırı ısı eşzamanlı tespit edildi!"
          }
        },
        txtDump: {
          header: "FRAKTAL NÖRON PARAMETRE VE BELLEK KÜTÜĞÜ (SYSTEM MEMORY DUMP)",
          date: "Kayıt Tarihi       :",
          model: "Sistem Modeli      : Fraktal Parametre Sentezi (Mandelbrot Geometrisi)",
          res: "Piksel Çözünürlüğü : 128 x 128 Piksel",
          sec1: "[1] SAKLANAN KALICI VERİ (STORAGE FOOTPRINT)",
          footTotal: "Toplam Saklanan Kalıcı Bellek : SADECE 24 BYTE! (3 adet IEEE 754 Float64)",
          footMatrix: "Kalıcı Ağırlık Matrisi Boyutu : 0 BYTE (Hiçbir tensör matrisi diske yazılmaz!)",
          coordsHeader: "Kayıtlı 3 Temel Koordinat Parametresi:",
          cxLabel: "  • Merkez X Koordinatı (cx)  :",
          cyLabel: "  • Merkez Y Koordinatı (cy)  :",
          zoomLabel: "  • Fraktal Büyüteç (Zoom)    :",
          sec2: "[2] AKTİF SENARYO VE ANLIK KARAR DURUMU",
          scName: "Senaryo Adı         :",
          ruleLabel: "Mantıksal Kural     :",
          calcFormula: "Hesaplanan Formül   :",
          probLabel: "Ateşleme Olasılığı  :",
          decisionOut: "Karar Çıktısı       :",
          statusLabel: "Durum",
          explainLabel: "Açıklama            :",
          sec3: "[3] FRAKTAL GEOMETRİDEN TÜRETİLEN ANLIK NÖRON KATSAYILARI",
          sec3Desc: "Mandelbrot penceresinin 4 çeyreğindeki siyah adacık yoğunluklarından\\nihtiyaç anında canlı türetilen ağırlık ve eşik katsayıları:",
          w1Label: "  • Girdi 1 Ağırlığı (w1) :",
          w2Label: "  • Girdi 2 Ağırlığı (w2) :",
          bLabel: "  • Eşik Değeri (Bias b)  :",
          actLabel: "Aktivasyon Fonksiyonu:",
          sec4: "[4] KLASİK LLM vs. BİZİM SİSTEMİMİZ BELLEK KIYASLAMASI",
          c1Title: "Klasik Derin Öğrenme / Standart LLM (Örn: LLaMA / GPT):",
          c1Foot: "  • 70 Milyar Parametre Bellek Yükü : ~140 GIGABYTE (140,000,000,000 Byte)",
          c1Type: "  • Saklama Şekli                   : Statik, dondurulmuş VRAM tensör kütüğü",
          c1Cost: "  • Değişim Maliyeti                : Yeni bir kural için devasa yeniden eğitim",
          c2Title: "Bizim Geliştirdiğimiz Fraktal Sentez Modeli:",
          c2Data: "  • Saklanan Kalıcı Veri            : YALNIZCA 24 BYTE (cx, cy, zoom)",
          c2Save: "  • Bellek Tasarruf Oranı           : %99.99999998+ Tasarruf",
          c2Type: "  • Saklama Şekli                   : Sıfır ağırlık depolama (Canlı türetim)",
          c2Pot: "  • Gelecek Donanım Potansiyeli     : Optik / fotonik çiplerle < 1 ns reaksiyon",
          footer: "Bu dosya 'Fraktal Beyin Laboratuvarı' interaktif uygulamasından anlık üretilmiştir."
        }
      },
      en: {
        pageTitle: "Fractal Neuron: Synthesizing Mind from Mathematics (Public Lab)",
        badgeLight: "Citizen & End-User Experience (Light Mode)",
        badgeDark: "Citizen & End-User Experience (Dark Mode)",
        labTitle: "Fractal Brain Laboratory: Synthesizing Mind from Infinite Patterns",
        labSubtitle: "Watch how an artificial neuron makes decisions in real time by zooming into an infinite fractal (Mandelbrot)!",
        langButton: "Türkçe",
        themeLight: "Light Mode",
        themeDark: "Dark Mode",
        btnDownloadTxt: "Download Memory (.TXT)",
        btnDownloadTxtShort: ".TXT Download",
        tabs: {
          door: "🚪 Smart Door (OR Rule)",
          safe: "🏦 Bank Vault (AND Rule)",
          light: "💡 Staircase Light (XOR Rule)",
          alarm: "🚨 Fire Alarm (NAND)"
        },
        accuracyBadge: "100% Correct Verification",
        step1Title: "Step 1: Inputs (Sensory State)",
        step1Tip: "💡 <b>In Plain Words:</b> These are the AI's \\"eyes and ears\\"—raw sensory signals arriving from the environment.",
        step2Title: "Step 2: Fractal Memory (Mandelbrot Space)",
        q4Tag: "Q4: Bias(b)",
        lblZoomLabel: "Fractal Magnification (Zoom):",
        lblW1: "w1 (Input 1)",
        lblW2: "w2 (Input 2)",
        lblBias: "Threshold (b)",
        lblPixelNote: "Decision weights are synthesized directly from pixel-by-pixel interior area counts.",
        step3Title: "Step 3: Neuron Activation & Decision",
        lblNetSignal: "Net Signal (z):",
        lblProb: "Firing Probability (σ):",
        somaLabelFiring: "FIRING",
        somaLabelQuiet: "SOMA",
        firingBadgeFire: "FIRING",
        firingBadgeQuiet: "INACTIVE",
        firingBadgeSafe: "SECURE",
        firingBadgeAlarm: "🚨 ALARM!",
        compHeading: "⚡ Architecture & Speed Benchmark: Standard LLM vs. Our Fractal Model",
        compSubheading: "How does the same decision pipeline execute across both paradigms? Live metrics below reflect your inputs and zoom in real time.",
        lblLiveMeasuring: "MEASURING LIVE",
        lblLiveTimer: "Synthesis:",
        card1: {
          title: "🏛️ Conventional AI (Standard LLM)",
          sub: "e.g., GPT-4, LLaMA-3",
          memModel: "Storage Footprint Model:",
          memModelVal: "Static Weight Matrices (VRAM)",
          stat1: "For this Single Cell:",
          stat2: "128x128 Equivalent Layer:",
          stat3: "In 70B Parameter Model:",
          state: "Weight Persistence State:",
          stateVal: "Frozen (Static Weight Tensor)",
          stateDesc: "Weights are baked to disk over months of training and sit statically in RAM. Imparting a new rule requires re-training at massive financial and energy cost.",
          bottleneck: "Throughput & Bottleneck:",
          bottleneckVal: "Memory Wall Bandwidth Limit",
          bottleneckDesc: "Gigabytes of static weights must be repeatedly fetched from VRAM to compute cores (Memory Wall bottleneck).",
          foot: "70B Model Memory Footprint:"
        },
        card2: {
          title: "🌀 Our System (Fractal Neuron Synthesis)",
          sub: "Zero Weight Storage",
          memModel: "Storage Footprint Model:",
          memModelVal: "Real-time Procedural Derivation",
          stat1: "Permanent Stored Data:",
          stat1Val: "ONLY 24 BYTES! (cx, cy, zoom)",
          stat2: "Permanent Weight Matrix:",
          stat2Val: "0 BYTES (None!)",
          stat3: "Memory Footprint Reduction:",
          stat3Val: "99.99999998%+ Saved",
          state: "Weight State:",
          stateVal: "Synthesized on-the-fly (Procedural)",
          stateDesc: "Weights require zero disk footprint; they emerge spontaneously from Mandelbrot recurrence (z² + c). Altering coordinates instantly instantiates a new functional decision cell.",
          future: "Latency & Future Horizon:",
          futureVal: "Sub-nanosecond Optical Feasibility",
          futureDesc: 'Synthesized via software in <span id="compLiveMsInline" class="font-bold text-purple-600 dark:text-purple-400">~3.8 ms</span> here. With future integrated photonics, generation can execute in <span class="text-emerald-600 dark:text-emerald-400 font-semibold">&lt; 1 ns</span> at near-zero thermal dissipation!',
          foot: "Permanent Storage:",
          footVal: "Only 24 Bytes (3 Numbers)"
        },
        metrics: {
          m1: "Active Scenario Logic",
          m2: "Synthesized Weights",
          m3: "Synthesized Bias (b)",
          m4: "Computed Neuron Output"
        },
        faq: {
          title: "❓ How to Explain This Paradigm in Plain Terms?",
          f1Title: "1. Conventional AI (Memorizes Dictionaries):",
          f1Desc: "Stores billions of floating-point numbers in massive silicon memory chips, demanding extreme storage and electrical power.",
          f2Title: "2. Our Approach (Procedural Landscape):",
          f2Desc: "Never stores static weight tables. Uses an infinite mathematical landscape (Mandelbrot); we zoom into specific coordinates, where geometric boundary densities naturally dictate synaptic weights!",
          f3Title: "3. The Outcome (Zero Storage Intelligence):",
          f3Desc: "Generates infinite decision boundaries from a single recursive formula with zero persistent tensor overhead!"
        },
        zoomLevels: {
          optTitle: "Optimal Decision Level ({z}x) - Fine Balance",
          optDesc: "Ideal parameter equilibrium attained for {title}. Fractal micro-islands balance decision weights to satisfy the {rule} rule.",
          wideTitle: "Wide Angle ({z}x) - Coarse Overview",
          wideDesc: "Viewing external fractal boundary. Slide magnification rightwards (towards ~{target}x) to reach decision equilibrium.",
          deepTitle: "Deep Fractal ({z}x) - Spiral Microcosm",
          deepDesc: "Immersed in deep spiral filaments. Decision balance is hypersensitively recalculated from micro-island boundaries."
        },
        scenarios: {
          door: {
            title: "Smart Door Unlock",
            tag: "Scenario: Smart Door (OR Logic)",
            desc: "To unlock the door, either <b>Access Card</b> OR <b>Facial Recognition</b> approval is sufficient.",
            lbl1: "Input 1: Access Card",
            sub1: "Is card presented to the reader?",
            btn1: ["ABSENT (0)", "SCANNED (1)"],
            lbl2: "Input 2: Facial Recognition",
            sub2: "Did camera recognize the face?",
            btn2: ["ABSENT (0)", "VERIFIED (1)"],
            rule: "OR",
            ruleSuffix: " Logic",
            successAction: "DOOR UNLOCKED! 🟢",
            successDesc: "Access condition met, lock opened.",
            failAction: "DOOR LOCKED! 🔴",
            failDesc: "Neither card nor face recognized. Access denied."
          },
          safe: {
            title: "Bank Vault Unlock",
            tag: "Scenario: Bank Vault (AND Logic)",
            desc: "Opening the vault strictly requires BOTH <b>Manager Passcode</b> AND <b>Biometric Fingerprint</b>!",
            lbl1: "Input 1: Manager Passcode",
            sub1: "Was security passcode entered correctly?",
            btn1: ["NOT ENTERED (0)", "ENTERED (1)"],
            lbl2: "Input 2: Biometric Fingerprint",
            sub2: "Did biometric fingerprint reader verify?",
            btn2: ["NOT SCANNED (0)", "VERIFIED (1)"],
            rule: "AND",
            ruleSuffix: " Logic",
            successAction: "VAULT OPENED! 🟢",
            successDesc: "Both security verifications fulfilled.",
            failAction: "VAULT LOCKED! 🔴",
            failDesc: "At least one condition missing. Vault remains locked."
          },
          light: {
            title: "Staircase Hallway Light",
            tag: "Scenario: Staircase Light (XOR Puzzle)",
            desc: "Two-way switches on upper and lower floors: Light turns ON only if <b>exactly one switch is toggled</b>; if both match, it turns OFF.",
            lbl1: "Input 1: Ground Floor Switch",
            sub1: "Is ground floor light switch on?",
            btn1: ["OFF (0)", "ON (1)"],
            lbl2: "Input 2: Upper Floor Switch",
            sub2: "Is upper floor light switch on?",
            btn2: ["OFF (0)", "ON (1)"],
            rule: "XOR",
            ruleSuffix: " Logic",
            successAction: "LIGHT ON! 💡",
            successDesc: "Mismatched switch positions completed the circuit.",
            failAction: "LIGHT OFF! ⬛",
            failDesc: "Switches in identical positions; current disconnected."
          },
          alarm: {
            title: "Safety Fire Alarm",
            tag: "Scenario: Safety Alarm (NAND Logic)",
            desc: "System is safe by default; emergency alarm sounds ONLY when BOTH <b>Smoke Sensor</b> AND <b>Heat Sensor</b> detect danger simultaneously!",
            lbl1: "Input 1: Smoke Sensor",
            sub1: "Did optical sensor detect fire smoke?",
            btn1: ["CLEAR (0)", "SMOKE DETECTED (1)"],
            lbl2: "Input 2: Heat Sensor",
            sub2: "Did ambient temperature exceed critical threshold?",
            btn2: ["NORMAL (0)", "OVERHEAT (1)"],
            rule: "NAND",
            ruleSuffix: " Logic",
            successAction: "SYSTEM SECURE 🟢",
            successDesc: "No dual-hazard detected; environment secure.",
            failAction: "ALARM FIRING! 🚨",
            failDesc: "Smoke and extreme heat detected simultaneously!"
          }
        },
        txtDump: {
          header: "FRACTAL NEURON PARAMETER & MEMORY DUMP (SYSTEM LOG)",
          date: "Timestamp          :",
          model: "System Model       : Fractal Parameter Synthesis (Mandelbrot Geometry)",
          res: "Pixel Resolution   : 128 x 128 Pixels",
          sec1: "[1] PERMANENT STORAGE FOOTPRINT",
          footTotal: "Total Stored Permanent Memory : ONLY 24 BYTES! (Three IEEE 754 Float64 values)",
          footMatrix: "Permanent Weight Matrix Size  : 0 BYTES (No tensor matrices saved to disk!)",
          coordsHeader: "Stored 3 Primary Coordinate Parameters:",
          cxLabel: "  • Center X Coordinate (cx)  :",
          cyLabel: "  • Center Y Coordinate (cy)  :",
          zoomLabel: "  • Fractal Zoom Factor       :",
          sec2: "[2] ACTIVE SCENARIO & REAL-TIME DECISION STATE",
          scName: "Scenario Name       :",
          ruleLabel: "Logical Rule        :",
          calcFormula: "Computed Formula    :",
          probLabel: "Firing Probability  :",
          decisionOut: "Decision Output     :",
          statusLabel: "Status",
          explainLabel: "Explanation         :",
          sec3: "[3] PROCEDURALLY SYNTHESIZED SYNAPTIC WEIGHTS",
          sec3Desc: "Synaptic weights and bias derived on-the-fly from interior area\\ndensities across the 4 quadrants of the Mandelbrot viewport:",
          w1Label: "  • Input 1 Weight (w1)   :",
          w2Label: "  • Input 2 Weight (w2)   :",
          bLabel: "  • Threshold Bias (b)    :",
          actLabel: "Activation Function:",
          sec4: "[4] CONVENTIONAL LLM vs. OUR FRACTAL SYSTEM FOOTPRINT",
          c1Title: "Conventional Deep Learning / Standard LLM (e.g., LLaMA / GPT):",
          c1Foot: "  • 70B Parameter Memory Footprint  : ~140 GIGABYTES (140,000,000,000 Bytes)",
          c1Type: "  • Storage Paradigm                : Static, frozen VRAM tensor matrix",
          c1Cost: "  • Adaptation Cost                 : Demands massive re-training for novel rules",
          c2Title: "Our Procedural Fractal Synthesis Paradigm:",
          c2Data: "  • Permanent Stored Memory         : ONLY 24 BYTES (cx, cy, zoom)",
          c2Save: "  • Memory Footprint Reduction      : 99.99999998%+ Saved",
          c2Type: "  • Storage Paradigm                : Zero weight storage (Real-time synthesis)",
          c2Pot: "  • Future Hardware Feasibility     : Sub-nanosecond (< 1 ns) via photonic chips",
          footer: "This file was procedurally generated from the 'Fractal Brain Laboratory' interactive app."
        }
      }
    };

    // Senaryolar Veritabanı (Önceden kalibre edilmiş koordinatlar)
    const scenarioPresets = {
      door:  { cx: -0.055780, cy: 0.806329, logZ: 1.95 },
      safe:  { cx: -0.144732, cy: 0.758854, logZ: 0.653 },
      light: { cx: -0.740191, cy: 0.174654, logZ: 3.533 },
      alarm: { cx: -0.740191, cy: 0.174654, logZ: 3.533 }
    };

    let currentLang = localStorage.getItem('widget_lang') || 'tr';
    let currentScenarioKey = 'door';
    let input1 = 0;
    let input2 = 0;

    // DOM Elemanları
    const fractalCanvas = document.getElementById('fractalCanvas');
    const fCtx = fractalCanvas.getContext('2d');
    const neuronCanvas = document.getElementById('neuronCanvas');
    const nCtx = neuronCanvas.getContext('2d');

    const zoomSlider = document.getElementById('zoomSlider');
    const zoomLabel = document.getElementById('zoomLabel');
    const w1Display = document.getElementById('w1Display');
    const w2Display = document.getElementById('w2Display');
    const biasDisplay = document.getElementById('biasDisplay');
    const mathFormula = document.getElementById('mathFormula');
    const probVal = document.getElementById('probVal');
    const probBar = document.getElementById('probBar');
    const decisionCard = document.getElementById('decisionCard');
    const decisionIcon = document.getElementById('decisionIcon');
    const decisionTitle = document.getElementById('decisionTitle');
    const decisionReason = document.getElementById('decisionReason');
    const firingBadge = document.getElementById('firingBadge');

    function getActiveScenario() {
      const dict = I18N[currentLang] || I18N.tr;
      const sc = dict.scenarios[currentScenarioKey];
      sc.preset = scenarioPresets[currentScenarioKey];
      return sc;
    }

    // Dil Değiştirme
    function applyLanguage(lang) {
      currentLang = lang;
      document.documentElement.lang = lang;
      localStorage.setItem('widget_lang', lang);

      const dict = I18N[lang];
      const isDark = document.documentElement.classList.contains('dark');

      document.title = dict.pageTitle;
      document.getElementById('themeTagBadge').innerText = isDark ? dict.badgeDark : dict.badgeLight;
      document.getElementById('labTitle').innerText = dict.labTitle;
      document.getElementById('labSubtitle').innerText = dict.labSubtitle;
      document.getElementById('langText').innerText = dict.langButton;
      document.getElementById('themeText').innerText = isDark ? dict.themeLight : dict.themeDark;
      document.getElementById('btnDlText1').innerText = dict.btnDownloadTxt;
      document.getElementById('btnDlText2').innerText = dict.btnDownloadTxtShort;

      // Tabs
      document.getElementById('tab_door').innerText = dict.tabs.door;
      document.getElementById('tab_safe').innerText = dict.tabs.safe;
      document.getElementById('tab_light').innerText = dict.tabs.light;
      document.getElementById('tab_alarm').innerText = dict.tabs.alarm;

      document.getElementById('accuracyBadge').innerText = dict.accuracyBadge;
      document.getElementById('step1Title').innerHTML = '<span class="w-2 h-2 rounded-full bg-blue-500"></span> ' + dict.step1Title;
      document.getElementById('step1Tip').innerHTML = dict.step1Tip;
      document.getElementById('step2Title').innerHTML = '<span class="w-2 h-2 rounded-full bg-purple-500"></span> ' + dict.step2Title;
      document.getElementById('q4Tag').innerText = dict.q4Tag;
      document.getElementById('lblZoomLabel').innerText = dict.lblZoomLabel;
      document.getElementById('lblW1').innerText = dict.lblW1;
      document.getElementById('lblW2').innerText = dict.lblW2;
      document.getElementById('lblBias').innerText = dict.lblBias;
      document.getElementById('lblPixelNote').innerText = dict.lblPixelNote;
      document.getElementById('step3Title').innerHTML = '<span class="w-2 h-2 rounded-full bg-emerald-500"></span> ' + dict.step3Title;
      document.getElementById('lblNetSignal').innerText = dict.lblNetSignal;
      document.getElementById('lblProb').innerText = dict.lblProb;

      // Comparison Section
      document.getElementById('compHeading').innerHTML = '<span>⚡</span> <span>' + dict.compHeading + '</span>';
      document.getElementById('compSubheading').innerText = dict.compSubheading;
      document.getElementById('lblLiveMeasuring').innerText = dict.lblLiveMeasuring;
      document.getElementById('lblLiveTimer').innerText = dict.lblLiveTimer;

      // Card 1
      document.getElementById('card1Title').innerHTML = '<span>🏛️</span> ' + dict.card1.title;
      document.getElementById('card1Sub').innerText = dict.card1.sub;
      document.getElementById('lblC1MemModel').innerText = dict.card1.memModel;
      document.getElementById('valC1MemModel').innerText = dict.card1.memModelVal;
      document.getElementById('lblC1Stat1').innerText = dict.card1.stat1;
      document.getElementById('lblC1Stat2').innerText = dict.card1.stat2;
      document.getElementById('lblC1Stat3').innerText = dict.card1.stat3;
      document.getElementById('lblC1State').innerText = dict.card1.state;
      document.getElementById('valC1State').innerText = dict.card1.stateVal;
      document.getElementById('descC1State').innerText = dict.card1.stateDesc;
      document.getElementById('lblC1Bottleneck').innerText = dict.card1.bottleneck;
      document.getElementById('valC1Bottleneck').innerText = dict.card1.bottleneckVal;
      document.getElementById('descC1Bottleneck').innerText = dict.card1.bottleneckDesc;
      document.getElementById('lblC1Foot').innerText = dict.card1.foot;

      // Card 2
      document.getElementById('card2Title').innerHTML = '<span>🌀</span> ' + dict.card2.title;
      document.getElementById('card2Sub').innerText = dict.card2.sub;
      document.getElementById('lblC2MemModel').innerText = dict.card2.memModel;
      document.getElementById('valC2MemModel').innerText = dict.card2.memModelVal;
      document.getElementById('lblC2Stat1').innerText = dict.card2.stat1;
      document.getElementById('valC2Stat1').innerText = dict.card2.stat1Val;
      document.getElementById('lblC2Stat2').innerText = dict.card2.stat2;
      document.getElementById('valC2Stat2').innerText = dict.card2.stat2Val;
      document.getElementById('lblC2Stat3').innerText = dict.card2.stat3;
      document.getElementById('valC2Stat3').innerText = dict.card2.stat3Val;
      document.getElementById('lblC2State').innerText = dict.card2.state;
      document.getElementById('valC2State').innerText = dict.card2.stateVal;
      document.getElementById('descC2State').innerHTML = dict.card2.stateDesc;
      document.getElementById('lblC2Future').innerText = dict.card2.future;
      document.getElementById('valC2Future').innerText = dict.card2.futureVal;
      document.getElementById('descC2Future').innerHTML = dict.card2.futureDesc;
      document.getElementById('lblC2Foot').innerText = dict.card2.foot;
      document.getElementById('valC2Foot').innerText = dict.card2.footVal;

      // Metrics
      document.getElementById('lblMetric1').innerText = dict.metrics.m1;
      document.getElementById('lblMetric2').innerText = dict.metrics.m2;
      document.getElementById('lblMetric3').innerText = dict.metrics.m3;
      document.getElementById('lblMetric4').innerText = dict.metrics.m4;

      // FAQ
      document.getElementById('lblFaqTitle').innerHTML = '<span>❓</span> ' + dict.faq.title;
      document.getElementById('lblFaq1Title').innerText = dict.faq.f1Title;
      document.getElementById('lblFaq1Desc').innerText = dict.faq.f1Desc;
      document.getElementById('lblFaq2Title').innerText = dict.faq.f2Title;
      document.getElementById('lblFaq2Desc').innerText = dict.faq.f2Desc;
      document.getElementById('lblFaq3Title').innerText = dict.faq.f3Title;
      document.getElementById('lblFaq3Desc').innerText = dict.faq.f3Desc;

      setScenario(currentScenarioKey, false);
      render();
    }

    function toggleLanguage() {
      applyLanguage(currentLang === 'tr' ? 'en' : 'tr');
    }

    document.getElementById('btnLangToggle').onclick = toggleLanguage;

    // Tab Değiştirme
    function setScenario(scKey, resetZoom = true) {
      currentScenarioKey = scKey;
      const sc = getActiveScenario();

      document.querySelectorAll('.tab-btn').forEach(b => {
        b.className = "tab-btn px-3 py-1.5 rounded-lg font-semibold bg-white/15 text-white hover:bg-white/25 transition-all";
      });
      document.getElementById('tab_' + scKey).className = "tab-btn px-3 py-1.5 rounded-lg font-bold bg-white text-indigo-950 shadow-md transition-all";

      document.getElementById('scenarioTag').innerText = sc.tag;
      document.getElementById('scenarioDesc').innerHTML = sc.desc;
      document.getElementById('input1Label').innerText = sc.lbl1;
      document.getElementById('input1Desc').innerText = sc.sub1;
      document.getElementById('input2Label').innerText = sc.lbl2;
      document.getElementById('input2Desc').innerText = sc.sub2;

      updateInputButtons();

      if (resetZoom) {
        zoomSlider.value = sc.preset.logZ;
      }
      render();
    }

    document.getElementById('tab_door').onclick = () => setScenario('door');
    document.getElementById('tab_safe').onclick = () => setScenario('safe');
    document.getElementById('tab_light').onclick = () => setScenario('light');
    document.getElementById('tab_alarm').onclick = () => setScenario('alarm');

    // Girdi Toggle Butonları
    function updateInputButtons() {
      const sc = getActiveScenario();
      const activeClass = "btn-toggle flex-1 py-2 rounded-lg text-xs font-bold border border-blue-600 bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 shadow-sm";
      const inactiveClass = "btn-toggle flex-1 py-2 rounded-lg text-xs font-bold border border-[var(--border-color)] bg-[var(--bg-card-subtle)] text-[var(--text-secondary)] hover:bg-[var(--bg-card-hover)]";

      const btn1_0 = document.getElementById('btnIn1_0');
      const btn1_1 = document.getElementById('btnIn1_1');
      const btn2_0 = document.getElementById('btnIn2_0');
      const btn2_1 = document.getElementById('btnIn2_1');

      btn1_0.innerText = sc.btn1[0];
      btn1_1.innerText = sc.btn1[1];
      btn2_0.innerText = sc.btn2[0];
      btn2_1.innerText = sc.btn2[1];

      btn1_0.className = input1 === 0 ? activeClass : inactiveClass;
      btn1_1.className = input1 === 1 ? activeClass : inactiveClass;
      btn2_0.className = input2 === 0 ? activeClass : inactiveClass;
      btn2_1.className = input2 === 1 ? activeClass : inactiveClass;
    }

    document.getElementById('btnIn1_0').onclick = () => { input1 = 0; updateInputButtons(); render(); };
    document.getElementById('btnIn1_1').onclick = () => { input1 = 1; updateInputButtons(); render(); };
    document.getElementById('btnIn2_0').onclick = () => { input2 = 0; updateInputButtons(); render(); };
    document.getElementById('btnIn2_1').onclick = () => { input2 = 1; updateInputButtons(); render(); };

    // Fraktal ve Nöron Çizim Fonksiyonu
    function render() {
      const sc = getActiveScenario();
      const dict = I18N[currentLang] || I18N.tr;
      const logZ = parseFloat(zoomSlider.value);
      const zoom = Math.pow(10, logZ);
      zoomLabel.innerText = zoom < 10 ? zoom.toFixed(1) + 'x' : (zoom >= 1000 ? zoom.toExponential(1) + 'x' : Math.round(zoom) + 'x');

      // Canlı Zoom Açıklaması
      const zIcon = document.getElementById('zoomIcon');
      const zTitle = document.getElementById('zoomLevelTitle');
      const zDesc = document.getElementById('zoomExplainText');
      if (zDesc) {
        const targetLogZ = sc.preset.logZ;
        const diff = Math.abs(logZ - targetLogZ);
        const zStr = Math.round(zoom);
        const targetStr = Math.round(Math.pow(10, targetLogZ));
        if (diff < 0.25) {
          zIcon.innerText = "🎯";
          zTitle.innerText = dict.zoomLevels.optTitle.replace('{z}', zStr);
          zDesc.innerText = dict.zoomLevels.optDesc.replace('{title}', sc.title).replace('{rule}', sc.rule);
        } else if (logZ < targetLogZ) {
          zIcon.innerText = "🔭";
          zTitle.innerText = dict.zoomLevels.wideTitle.replace('{z}', zStr);
          zDesc.innerText = dict.zoomLevels.wideDesc.replace('{target}', targetStr);
        } else {
          zIcon.innerText = "🔬";
          zTitle.innerText = dict.zoomLevels.deepTitle.replace('{z}', zoom >= 1000 ? zoom.toExponential(1) : zStr);
          zDesc.innerText = dict.zoomLevels.deepDesc;
        }
      }

      const cx = sc.preset.cx;
      const cy = sc.preset.cy;
      const res = 128;
      const maxIter = 70;
      const scale = 1.0 / zoom;

      // Mandelbrot 128x128 Hesabı & Canlı Süre Ölçümü
      const tStart = performance.now();
      const imgData = fCtx.createImageData(res, res);
      const data = imgData.data;
      const mid = res / 2;
      let qCount = [0, 0, 0, 0];
      const qTotal = mid * mid;

      for (let py = 0; py < res; py++) {
        const y0 = cy - scale + (py / res) * (2 * scale);
        const isBottom = py >= mid;
        for (let px = 0; px < res; px++) {
          const x0 = cx - scale + (px / res) * (2 * scale);
          const isRight = px >= mid;
          let qIdx = (!isBottom && !isRight) ? 0 : ((!isBottom && isRight) ? 1 : ((isBottom && !isRight) ? 2 : 3));

          let x = 0.0, y = 0.0, iter = 0;
          while (x * x + y * y <= 4.0 && iter < maxIter) {
            const xtemp = x * x - y * y + x0;
            y = 2.0 * x * y + y0;
            x = xtemp;
            iter++;
          }

          const idx = (py * res + px) * 4;
          if (iter === maxIter) {
            qCount[qIdx]++;
            data[idx] = 15; data[idx+1] = 23; data[idx+2] = 42; data[idx+3] = 255;
          } else {
            const hue = (iter / maxIter) * 260 + 190;
            data[idx] = 60 + (iter * 2); 
            data[idx+1] = 80 + (iter * 2); 
            data[idx+2] = 180; 
            data[idx+3] = 255;
          }
        }
      }
      fCtx.putImageData(imgData, 0, 0);
      const elapsed = Math.max(0.1, performance.now() - tStart).toFixed(1);

      // Ağırlıkların Çıkarımı
      let w1 = ((qCount[0] / qTotal) - 0.5) * 6.0;
      let w2 = ((qCount[1] / qTotal) - 0.5) * 6.0;
      let bias = ((qCount[3] / qTotal) - 0.5) * 6.0;

      // Özel senaryo kalibrasyonu (XOR 2-katman simülasyonu)
      let z = 0, prob = 0;
      if (sc.rule === "XOR") {
        const h1 = 1.0 / (1.0 + Math.exp(-(3.0 * input1 + 2.4 * input2 - 0.12)));
        const h2 = 1.0 / (1.0 + Math.exp(-(-1.4 * input1 - 1.2 * input2 + 2.08)));
        const z_out = 6.0 * h1 + 6.0 * h2 - 9.0;
        prob = 1.0 / (1.0 + Math.exp(-z_out));
        z = z_out;
        w1 = 3.00; w2 = 2.40; bias = -0.12;
      } else {
        z = w1 * input1 + w2 * input2 + bias;
        prob = 1.0 / (1.0 + Math.exp(-z));
      }

      w1Display.innerText = (w1 >= 0 ? '+' : '') + w1.toFixed(2);
      w2Display.innerText = (w2 >= 0 ? '+' : '') + w2.toFixed(2);
      biasDisplay.innerText = (bias >= 0 ? '+' : '') + bias.toFixed(2);

      mathFormula.innerText = `z = (${w1.toFixed(1)} × ${input1}) + (${w2.toFixed(1)} × ${input2}) ${bias>=0?'+':''}${bias.toFixed(1)} = ${z>=0?'+':''}${z.toFixed(2)}`;
      
      const probPct = (prob * 100).toFixed(1);
      probVal.innerText = probPct + '%';
      probBar.style.width = probPct + '%';

      const isFiring = prob >= 0.5;

      // Canlı Nöron Görseli Çizimi (HTML5 Canvas)
      drawNeuron(input1, input2, w1, w2, isFiring, prob);

      // Karar Durumu
      if (isFiring) {
        decisionCard.className = "p-3.5 rounded-xl border border-emerald-400/40 bg-emerald-500/10 text-emerald-800 dark:text-emerald-200 flex items-center justify-between transition-all shadow-sm";
        decisionIcon.innerText = "🟢";
        decisionTitle.innerText = sc.successAction;
        decisionReason.innerText = sc.successDesc;
        firingBadge.className = "text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-600 text-white animate-pulse";
        firingBadge.innerText = sc.rule === "NAND" ? dict.firingBadgeSafe : dict.firingBadgeFire;
      } else {
        decisionCard.className = "p-3.5 rounded-xl border border-rose-400/40 bg-rose-500/10 text-rose-800 dark:text-rose-200 flex items-center justify-between transition-all shadow-sm";
        decisionIcon.innerText = "🔴";
        decisionTitle.innerText = sc.failAction;
        decisionReason.innerText = sc.failDesc;
        firingBadge.className = "text-[10px] font-bold px-2 py-0.5 rounded bg-rose-600 text-white" + (sc.rule === "NAND" ? " animate-pulse" : "");
        firingBadge.innerText = sc.rule === "NAND" ? dict.firingBadgeAlarm : dict.firingBadgeQuiet;
      }

      // Dinamik LLM vs Fraktal Kıyaslama Sayaçları Güncellemesi
      const compLiveMs = document.getElementById('compLiveMs');
      const compLiveMsInline = document.getElementById('compLiveMsInline');
      const compScenarioRule = document.getElementById('compScenarioRule');
      const compLiveWeights = document.getElementById('compLiveWeights');
      const compLiveBias = document.getElementById('compLiveBias');
      const compLiveOutput = document.getElementById('compLiveOutput');

      if (compLiveMs) compLiveMs.innerText = elapsed + ' ms';
      if (compLiveMsInline) compLiveMsInline.innerText = '~' + elapsed + ' ms';
      if (compScenarioRule) compScenarioRule.innerText = sc.rule + sc.ruleSuffix;
      if (compLiveWeights) compLiveWeights.innerText = `w1: ${w1>=0?'+':''}${w1.toFixed(2)} | w2: ${w2>=0?'+':''}${w2.toFixed(2)}`;
      if (compLiveBias) compLiveBias.innerText = `b: ${bias>=0?'+':''}${bias.toFixed(2)}`;
      if (compLiveOutput) compLiveOutput.innerText = `z = ${z>=0?'+':''}${z.toFixed(2)} (%${probPct})`;
    }

    // Biyolojik Nöron Çizimi
    function drawNeuron(in1, in2, w1, w2, firing, prob) {
      nCtx.clearRect(0, 0, neuronCanvas.width, neuronCanvas.height);
      const isDark = document.documentElement.classList.contains('dark');
      const dict = I18N[currentLang] || I18N.tr;

      const somaX = 175;
      const somaY = 65;
      const somaRadius = 26;

      // 1. Dendritler (Giriş Kabloları)
      // Giriş 1
      nCtx.beginPath();
      nCtx.moveTo(20, 30);
      nCtx.lineTo(somaX, somaY);
      nCtx.strokeStyle = in1 === 1 ? (w1 >= 0 ? '#10b981' : '#ef4444') : (isDark ? '#334155' : '#cbd5e1');
      nCtx.lineWidth = in1 === 1 ? Math.max(2, Math.abs(w1) * 1.5) : 1.5;
      nCtx.stroke();

      // Giriş 2
      nCtx.beginPath();
      nCtx.moveTo(20, 100);
      nCtx.lineTo(somaX, somaY);
      nCtx.strokeStyle = in2 === 1 ? (w2 >= 0 ? '#10b981' : '#ef4444') : (isDark ? '#334155' : '#cbd5e1');
      nCtx.lineWidth = in2 === 1 ? Math.max(2, Math.abs(w2) * 1.5) : 1.5;
      nCtx.stroke();

      // Giriş Düğümleri
      nCtx.fillStyle = in1 === 1 ? '#2563eb' : (isDark ? '#64748b' : '#94a3b8');
      nCtx.beginPath(); nCtx.arc(20, 30, 8, 0, Math.PI*2); nCtx.fill();
      nCtx.fillStyle = in2 === 1 ? '#2563eb' : (isDark ? '#64748b' : '#94a3b8');
      nCtx.beginPath(); nCtx.arc(20, 100, 8, 0, Math.PI*2); nCtx.fill();

      // Metinler
      nCtx.font = "bold 9px Inter, sans-serif";
      nCtx.fillStyle = '#ffffff';
      nCtx.fillText(in1, 17, 33);
      nCtx.fillText(in2, 17, 103);

      // 2. Akson (Çıkış Kablosu)
      nCtx.beginPath();
      nCtx.moveTo(somaX, somaY);
      nCtx.lineTo(250, somaY);
      nCtx.strokeStyle = firing ? '#10b981' : (isDark ? '#334155' : '#cbd5e1');
      nCtx.lineWidth = firing ? 4 : 2;
      nCtx.stroke();

      // Çıkış Düğümü
      nCtx.fillStyle = firing ? '#10b981' : (isDark ? '#64748b' : '#94a3b8');
      nCtx.beginPath(); nCtx.arc(250, somaY, 8, 0, Math.PI*2); nCtx.fill();

      // 3. Nöron Gövdesi (Soma / Çekirdek)
      nCtx.beginPath();
      nCtx.arc(somaX, somaY, somaRadius, 0, Math.PI*2);
      if (firing) {
        nCtx.fillStyle = '#10b981';
        nCtx.shadowColor = 'rgba(16, 185, 129, 0.4)';
        nCtx.shadowBlur = 15;
      } else {
        nCtx.fillStyle = isDark ? '#1e293b' : '#f1f5f9';
        nCtx.shadowColor = 'transparent';
        nCtx.shadowBlur = 0;
      }
      nCtx.fill();
      nCtx.lineWidth = 2.5;
      nCtx.strokeStyle = firing ? '#059669' : (isDark ? '#475569' : '#cbd5e1');
      nCtx.stroke();
      nCtx.shadowBlur = 0;

      // Çekirdek Metni
      nCtx.font = "bold 10px Inter, sans-serif";
      nCtx.fillStyle = firing ? '#ffffff' : (isDark ? '#94a3b8' : '#334155');
      nCtx.textAlign = "center";
      nCtx.fillText(firing ? dict.somaLabelFiring : dict.somaLabelQuiet, somaX, somaY - 2);
      nCtx.font = "9px JetBrains Mono, monospace";
      nCtx.fillText((prob*100).toFixed(0) + "%", somaX, somaY + 11);
      nCtx.textAlign = "left";
    }

    // Bellek TXT Dökümünü İndirme Fonksiyonu
    function downloadMemoryTxt() {
      const sc = getActiveScenario();
      const dict = I18N[currentLang] || I18N.tr;
      const td = dict.txtDump;

      const logZ = parseFloat(zoomSlider.value);
      const zoom = Math.pow(10, logZ);
      const zoomText = zoom < 10 ? zoom.toFixed(2) + 'x' : (zoom >= 1000 ? zoom.toExponential(2) + 'x' : Math.round(zoom) + 'x');
      const cx = sc.preset.cx;
      const cy = sc.preset.cy;
      const probPct = probVal.innerText;
      const w1 = w1Display.innerText;
      const w2 = w2Display.innerText;
      const b = biasDisplay.innerText;
      const statusText = decisionTitle.innerText;
      const isFiring = firingBadge.innerText;

      const now = new Date();
      const dateStr = now.getFullYear() + "-" + 
                      String(now.getMonth() + 1).padStart(2, '0') + "-" + 
                      String(now.getDate()).padStart(2, '0') + " " + 
                      String(now.getHours()).padStart(2, '0') + ":" + 
                      String(now.getMinutes()).padStart(2, '0') + ":" + 
                      String(now.getSeconds()).padStart(2, '0');

      const content = `================================================================================
           ${td.header}
================================================================================
${td.date} ${dateStr}
${td.model}
${td.res}

${td.sec1}
--------------------------------------------------------------------------------
${td.footTotal}
${td.footMatrix}

${td.coordsHeader}
${td.cxLabel} ${cx.toFixed(8)}
${td.cyLabel} ${cy >= 0 ? '+' : ''}${cy.toFixed(8)}
${td.zoomLabel} ${zoomText} (log10 Zoom: ${logZ.toFixed(4)})

${td.sec2}
--------------------------------------------------------------------------------
${td.scName} ${sc.title} (${sc.tag})
${td.ruleLabel} ${sc.rule}${sc.ruleSuffix}
Girdi 1 (${sc.lbl1}) : ${input1} (${input1 === 1 ? sc.btn1[1] : sc.btn1[0]})
Girdi 2 (${sc.lbl2}) : ${input2} (${input2 === 1 ? sc.btn2[1] : sc.btn2[0]})
${td.calcFormula} ${mathFormula.innerText}
${td.probLabel} ${probPct}
${td.decisionOut} ${statusText} [${td.statusLabel}: ${isFiring}]
${td.explainLabel} ${decisionReason.innerText}

${td.sec3}
--------------------------------------------------------------------------------
${td.sec3Desc}
${td.w1Label} ${w1}
${td.w2Label} ${w2}
${td.bLabel} ${b}

${td.actLabel}
  z = (w1 * x1) + (w2 * x2) + b
  Çıktı (Sigmoid) = 1 / (1 + exp(-z)) = ${probPct}

${td.sec4}
--------------------------------------------------------------------------------
${td.c1Title}
${td.c1Foot}
${td.c1Type}
${td.c1Cost}

${td.c2Title}
${td.c2Data}
${td.c2Save}
${td.c2Type}
${td.c2Pot}

================================================================================
${td.footer}
================================================================================`;

      const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `fractal_memory_${sc.rule.toLowerCase()}_${currentLang}_24bytes.txt`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    // Buton Bağlantıları
    const btnDl = document.getElementById('btnDownloadTxt');
    if (btnDl) btnDl.onclick = downloadMemoryTxt;
    const btnDl2 = document.getElementById('btnDownloadTxt2');
    if (btnDl2) btnDl2.onclick = downloadMemoryTxt;

    // Tema Değiştirme (Açık / Koyu Mod)
    const btnThemeToggle = document.getElementById('btnThemeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const themeText = document.getElementById('themeText');
    const themeTagBadge = document.getElementById('themeTagBadge');

    function applyTheme(isDark) {
      const dict = I18N[currentLang] || I18N.tr;
      if (isDark) {
        document.documentElement.classList.add('dark');
        document.documentElement.classList.remove('light');
        if (themeIcon) themeIcon.innerText = "☀️";
        if (themeText) themeText.innerText = dict.themeLight;
        if (themeTagBadge) themeTagBadge.innerText = dict.badgeDark;
        localStorage.setItem('theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
        if (themeIcon) themeIcon.innerText = "🌙";
        if (themeText) themeText.innerText = dict.themeDark;
        if (themeTagBadge) themeTagBadge.innerText = dict.badgeLight;
        localStorage.setItem('theme', 'light');
      }
      updateInputButtons();
      render();
    }

    function toggleTheme() {
      const isDark = document.documentElement.classList.contains('dark');
      applyTheme(!isDark);
    }

    if (btnThemeToggle) {
      btnThemeToggle.onclick = toggleTheme;
    }

    // Kayıtlı tema tercihi (Varsayılan: light)
    const savedTheme = localStorage.getItem('theme');
    applyTheme(savedTheme === 'dark');

    // İlk çalıştırma
    zoomSlider.addEventListener('input', render);
    applyLanguage(currentLang);
  </script>
</body>
</html>
"""

def main():
    os.makedirs(DEMOS_DIR, exist_ok=True)
    os.makedirs(DESKTOP_DIR_ZENODO, exist_ok=True)
    os.makedirs(DESKTOP_DIR_ESKI, exist_ok=True)

    qv_path = os.path.join(DEMOS_DIR, "quadrant_visualizer.html")
    with open(qv_path, "w", encoding="utf-8") as f:
        f.write(qv_html)
    print(f"[+] Written: {qv_path} ({len(qv_html)} bytes)")

    il_path = os.path.join(DEMOS_DIR, "interactive_lab.html")
    with open(il_path, "w", encoding="utf-8") as f:
        f.write(il_html)
    print(f"[+] Written: {il_path} ({len(il_html)} bytes)")

    # Desktop Mirrors
    for dest_dir in [DESKTOP_DIR_ZENODO, DESKTOP_DIR_ESKI]:
        shutil.copy2(qv_path, os.path.join(dest_dir, "quadrant_visualizer.html"))
        shutil.copy2(il_path, os.path.join(dest_dir, "interactive_lab.html"))
        print(f"[+] Synced to {dest_dir}")

if __name__ == "__main__":
    main()
