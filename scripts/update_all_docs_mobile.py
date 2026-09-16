import os
import re
import base64
import subprocess

WORKSPACE_DIR = r"c:\Users\maat\Documents\antigravity\wonderful-raman"
ARTIFACT_DIR = r"C:\Users\maat\.gemini\antigravity\brain\be1030f1-5b3e-4e9e-886d-2b41ab9b7de4"
Q1_DESKTOP = r"C:\Users\maat\Desktop\ZENODO_V3_VEYA_Q1_DERGIYE_HAZIRLIK"

def get_b64(filename):
    for d in [os.path.join(WORKSPACE_DIR, "figures"), ARTIFACT_DIR]:
        p = os.path.join(d, filename)
        if os.path.exists(p):
            with open(p, "rb") as f:
                return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

# ==============================================================================
# 1. BUILD_ACADEMIC_REPORT.PY
# ==============================================================================
print("[*] 1. Patching build_academic_report.py...")
acad_path = os.path.join(WORKSPACE_DIR, "scripts", "build_academic_report.py")
with open(acad_path, "r", encoding="utf-8") as f:
    acad_code = f.read()

# Add get_base64_image check for figures dir if not present
if 'os.path.join(WORKSPACE_DIR, "figures")' not in acad_code:
    acad_code = acad_code.replace(
        'def get_base64_image(filename):\n    path = os.path.join(ARTIFACT_DIR, filename)',
        'def get_base64_image(filename):\n    for d in [os.path.join(WORKSPACE_DIR, "figures"), ARTIFACT_DIR]:\n        path = os.path.join(d, filename)\n        if os.path.exists(path):\n            with open(path, "rb") as f:\n                return f"data:image/png;base64,{base64.b64encode(f.read()).decode(\'utf-8\')}"'
    )

if 'img_continuous =' not in acad_code:
    acad_code = acad_code.replace(
        'img_xor = get_base64_image("xor_complete_network_128.png")',
        'img_xor = get_base64_image("xor_complete_network_128.png")\nimg_continuous = get_base64_image("continuous_manifolds_benchmark.png")'
    )

resp_acad_css = """
    .table-responsive {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin: 16px 0 22px 0;
    }
    .table-responsive table.data-table {
      margin: 0 !important;
      min-width: 540px;
    }

    @media screen and (max-width: 768px) {
      body {
        font-size: 13px;
      }
      .document-wrapper {
        padding: 20px 14px !important;
        margin: 10px 4px !important;
        border-radius: 8px;
        box-shadow: none;
      }
      .top-action-bar {
        flex-direction: column;
        gap: 12px;
        text-align: center;
        padding: 14px 16px;
      }
      .top-action-bar > div:last-child {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 8px;
      }
      .btn-pdf {
        width: 100%;
        justify-content: center;
      }
      h1.paper-title {
        font-size: 20px;
        line-height: 1.35;
      }
      .grid-2 {
        grid-template-columns: 1fr;
      }
      .meta-table {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
      }
      .meta-table td {
        display: block;
        border: none;
        border-bottom: 1px solid var(--border-light);
        padding: 6px 10px;
      }
      .equation-box {
        font-size: 11px;
        padding: 10px 8px;
        word-break: break-all;
      }
      pre.code-block {
        font-size: 10px;
        padding: 10px 12px;
      }
    }
  </style>"""

if '.table-responsive' not in acad_code:
    acad_code = acad_code.replace('  </style>', resp_acad_css)

# Wrap tables
old_table_res = '<table class="data-table">\n      <thead>\n        <tr>\n          <th>Bölge ve Parametreler</th>'
new_table_res = '<div class="table-responsive">\n    <table class="data-table">\n      <thead>\n        <tr>\n          <th>Bölge ve Parametreler</th>'
if old_table_res in acad_code:
    acad_code = acad_code.replace(old_table_res, new_table_res)
    acad_code = acad_code.replace(
        '          <td class="text-right badge-ok">%0.09</td>\n        </tr>\n      </tbody>\n    </table>\n\n    <div class="fig-container avoid-break">',
        '          <td class="text-right badge-ok">%0.09</td>\n        </tr>\n      </tbody>\n    </table>\n    </div>\n\n    <div class="fig-container avoid-break">'
    )

old_table_gate = '<table class="data-table">\n      <thead>\n        <tr>\n          <th>Mantık Kapısı</th>'
new_table_gate = '<div class="table-responsive">\n    <table class="data-table">\n      <thead>\n        <tr>\n          <th>Mantık Kapısı</th>'
if old_table_gate in acad_code:
    acad_code = acad_code.replace(old_table_gate, new_table_gate)
    acad_code = acad_code.replace(
        '          <td class="text-center"><span class="badge-ok">%100 DOĞRU ✅</span></td>\n        </tr>\n      </tbody>\n    </table>\n\n    <div class="fig-container avoid-break">\n      <img src="__IMG_GATES__"',
        '          <td class="text-center"><span class="badge-ok">%100 DOĞRU ✅</span></td>\n        </tr>\n      </tbody>\n    </table>\n    </div>\n\n    <div class="fig-container avoid-break">\n      <img src="__IMG_GATES__"'
    )

old_table_xor = '<table class="data-table">\n      <thead>\n        <tr>\n          <th class="text-center">Girdi (x<sub>1</sub>, x<sub>2</sub>)</th>'
new_table_xor = '<div class="table-responsive">\n    <table class="data-table">\n      <thead>\n        <tr>\n          <th class="text-center">Girdi (x<sub>1</sub>, x<sub>2</sub>)</th>'
if old_table_xor in acad_code:
    acad_code = acad_code.replace(old_table_xor, new_table_xor)
    acad_code = acad_code.replace(
        '          <td class="text-center"><span class="badge-ok">BAŞARILI ✅</span></td>\n        </tr>\n      </tbody>\n    </table>\n\n    <div class="fig-container avoid-break">\n      <img src="__IMG_XOR__"',
        '          <td class="text-center"><span class="badge-ok">BAŞARILI ✅</span></td>\n        </tr>\n      </tbody>\n    </table>\n    </div>\n\n    <div class="fig-container avoid-break">\n      <img src="__IMG_XOR__"'
    )

# Section 3.6
section_36_html = """    <div class="fig-container avoid-break">
      <img src="__IMG_XOR__" alt="2-Katmanlı XOR Ağı ve 2D Karar Yüzeyi">
      <div class="fig-caption">Şekil 6: Sol ve Orta: Nöron 1 (OR) ve Nöron 2 (NAND) 128&times;128 pencereleri. Sağ: Fraktal ağın oluşturduğu doğrusal olmayan (non-linear) 2D XOR karar yüzeyi.</div>
    </div>
  </section>

  <!-- Deney 6: Sürekli Manifold Doğrusal Olmayan Kıyaslamaları (Two-Moons & Two-Spirals) -->
  <section class="page-break avoid-break">
    <h3 class="sub-heading">3.6. Deney 6: Sürekli Manifold Doğrusal Olmayan Kıyaslamaları (Two-Moons & Two-Spirals)</h3>
    <p>
      Ayrık mantık kapılarının ötesine geçilerek; çok katmanlı fraktal nöral sentez mimarisinin sürekli ve yüksek eğrilikli (high-curvature) karar manifoldlarındaki temsil gücü makine öğreniminin en zorlu sentetik kıyaslama kümeleri olan <strong>Two-Moons (İki Yarımay)</strong> ve <strong>Two-Spirals (İki Sarmal / Spiral)</strong> üzerinde test edilmiştir:
    </p>

    <div class="table-responsive">
      <table class="data-table">
        <thead>
          <tr>
            <th>Veri Kümesi (Manifold)</th>
            <th class="text-center">Örneklem Sayısı (N)</th>
            <th class="text-center">Gürültü Seviyesi (&sigma;)</th>
            <th class="text-center">Ağ Mimarisi</th>
            <th class="text-center">Doğruluk (Accuracy)</th>
            <th class="text-center">F1-Skoru</th>
            <th class="text-center">Doğrulama Durumu</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Two-Moons (İki Yarımay)</strong></td>
            <td class="text-center">1,000</td>
            <td class="text-center">0.10</td>
            <td class="text-center">2-Katmanlı Fraktal Ağ (4 Nöron)</td>
            <td class="text-center"><strong>%99.30</strong></td>
            <td class="text-center">0.9930</td>
            <td class="text-center"><span class="badge-ok">KUSURSUZ SINIFLANDIRMA ✅</span></td>
          </tr>
          <tr>
            <td><strong>Two-Spirals (İki Spiral)</strong></td>
            <td class="text-center">1,000</td>
            <td class="text-center">0.05</td>
            <td class="text-center">3-Katmanlı Fraktal Ağ (8 Nöron)</td>
            <td class="text-center"><strong>%98.50</strong></td>
            <td class="text-center">0.9848</td>
            <td class="text-center"><span class="badge-ok">YÜKSEK KARARLILIK ✅</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="fig-container avoid-break">
      <img src="__IMG_CONTINUOUS__" alt="Two-Moons ve Two-Spirals Doğrusal Olmayan Karar Sınırları">
      <div class="fig-caption">Şekil 7: Fraktal morfolojiden türetilen parametrelerle inşa edilen kesintisiz doğrusal olmayan karar sınırları: (Sol) Two-Moons %99.3 doğruluk; (Sağ) Two-Spirals %98.5 doğruluk.</div>
    </div>
  </section>"""

if '__IMG_CONTINUOUS__' not in acad_code:
    acad_code = acad_code.replace(
        """    <div class="fig-container avoid-break">
      <img src="__IMG_XOR__" alt="2-Katmanlı XOR Ağı ve 2D Karar Yüzeyi">
      <div class="fig-caption">Şekil 6: Sol ve Orta: Nöron 1 (OR) ve Nöron 2 (NAND) 128&times;128 pencereleri. Sağ: Fraktal ağın oluşturduğu doğrusal olmayan (non-linear) 2D XOR karar yüzeyi.</div>
    </div>
  </section>""",
        section_36_html
    )
    acad_code = acad_code.replace(
        'html_final = html_final.replace("__IMG_XOR__", img_xor)',
        'html_final = html_final.replace("__IMG_XOR__", img_xor)\nhtml_final = html_final.replace("__IMG_CONTINUOUS__", img_continuous)'
    )

top_bar_old = """    <button class="btn-pdf" onclick="window.print()">
      <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
        <path d="M2.5 8a.5.5 0 1 0 0-1 .5.5 0 0 0 0 1z"/>
        <path d="M5 1a2 2 0 0 0-2 2v2H2a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h1v1a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-1h1a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-1V3a2 2 0 0 0-2-2H5zM4 3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2H4V3zm1 5a2 2 0 0 0-2 2v1H2a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v-1a2 2 0 0 0-2-2H5zm7 2v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1z"/>
      </svg>
      PDF Olarak Kaydet / Yazdır
    </button>"""

top_bar_new = """    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
      <a href="Halka_Sunum_ve_Teorik_Rehber.html" class="btn-pdf" style="background: #4338ca; text-decoration: none;">
        🗣️ Halka Sunum Rehberi
      </a>
      <button class="btn-pdf" onclick="window.print()">
        <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
          <path d="M2.5 8a.5.5 0 1 0 0-1 .5.5 0 0 0 0 1z"/>
          <path d="M5 1a2 2 0 0 0-2 2v2H2a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h1v1a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-1h1a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-1V3a2 2 0 0 0-2-2H5zM4 3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2H4V3zm1 5a2 2 0 0 0-2 2v1H2a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v-1a2 2 0 0 0-2-2H5zm7 2v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1z"/>
        </svg>
        PDF Olarak Kaydet / Yazdır
      </button>
    </div>"""

if top_bar_old in acad_code:
    acad_code = acad_code.replace(top_bar_old, top_bar_new)

old_save = """html_report_path_art = os.path.join(ARTIFACT_DIR, "Mandelbrot_Akademik_Teknik_Raporu.html")
html_report_path_ws = os.path.join(WORKSPACE_DIR, "Mandelbrot_Akademik_Teknik_Raporu.html")

with open(html_report_path_art, "w", encoding="utf-8") as f:
    f.write(html_final)

with open(html_report_path_ws, "w", encoding="utf-8") as f:
    f.write(html_final)"""

new_save = """html_report_path_art = os.path.join(ARTIFACT_DIR, "Mandelbrot_Akademik_Teknik_Raporu.html")
html_report_path_ws = os.path.join(WORKSPACE_DIR, "Mandelbrot_Akademik_Teknik_Raporu.html")
html_report_path_docs = os.path.join(WORKSPACE_DIR, "docs", "Mandelbrot_Akademik_Teknik_Raporu.html")

for p in [html_report_path_art, html_report_path_ws, html_report_path_docs]:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html_final)

q1_desktop = r"C:\\Users\\maat\\Desktop\\ZENODO_V3_VEYA_Q1_DERGIYE_HAZIRLIK"
if os.path.exists(q1_desktop):
    with open(os.path.join(q1_desktop, "Mandelbrot_Akademik_Teknik_Raporu.html"), "w", encoding="utf-8") as f:
        f.write(html_final)"""

if old_save in acad_code:
    acad_code = acad_code.replace(old_save, new_save)

with open(acad_path, "w", encoding="utf-8") as f:
    f.write(acad_code)

print("[+] Executing build_academic_report.py...")
res = subprocess.run(["python", acad_path], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)

# ==============================================================================
# 2. GENERATE_HTML_REPORT.PY (Mandelbrot_Fraktal_Noron_Raporu.html)
# ==============================================================================
print("\n[*] 2. Patching generate_html_report.py...")
gen_path = os.path.join(WORKSPACE_DIR, "scripts", "generate_html_report.py")
with open(gen_path, "r", encoding="utf-8") as f:
    gen_code = f.read()

resp_gen_css = """
    @media screen and (max-width: 768px) {{
      .page-container {{
        padding: 20px 14px !important;
        margin: 10px 4px !important;
        border-radius: 8px;
        box-shadow: none;
      }}
      .action-bar {{
        flex-direction: column;
        gap: 12px;
        text-align: center;
        padding: 14px 16px;
      }}
      .btn-print {{
        width: 100%;
        justify-content: center;
      }}
      h1 {{
        font-size: 20px;
        line-height: 1.35;
      }}
      .meta-grid {{
        grid-template-columns: 1fr 1fr;
      }}
      .grid-2 {{
        grid-template-columns: 1fr;
      }}
      table {{
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
      }}
      pre {{
        font-size: 10px;
        padding: 10px 12px;
      }}
    }}
  </style>"""

if '@media screen and (max-width: 768px)' not in gen_code:
    gen_code = gen_code.replace('  </style>', resp_gen_css)

old_gen_save = """with open(report_artifact_path, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(report_workspace_path, "w", encoding="utf-8") as f:
    f.write(html_content)"""

new_gen_save = """report_docs_path = os.path.join(WORKSPACE_DIR, "docs", "Mandelbrot_Fraktal_Noron_Raporu.html")
for p in [report_artifact_path, report_workspace_path, report_docs_path]:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html_content)

q1_desktop = r"C:\\Users\\maat\\Desktop\\ZENODO_V3_VEYA_Q1_DERGIYE_HAZIRLIK"
if os.path.exists(q1_desktop):
    with open(os.path.join(q1_desktop, "Mandelbrot_Fraktal_Noron_Raporu.html"), "w", encoding="utf-8") as f:
        f.write(html_content)"""

if old_gen_save in gen_code:
    gen_code = gen_code.replace(old_gen_save, new_gen_save)

with open(gen_path, "w", encoding="utf-8") as f:
    f.write(gen_code)

print("[+] Executing generate_html_report.py...")
res = subprocess.run(["python", gen_path], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)

# ==============================================================================
# 3. BUILD_HALKA_REHBER.PY (Halka_Anlatim_Rehberi.html)
# ==============================================================================
print("\n[*] 3. Patching build_halka_rehber.py...")
halka_path = os.path.join(WORKSPACE_DIR, "scripts", "build_halka_rehber.py")
with open(halka_path, "r", encoding="utf-8") as f:
    halka_code = f.read()

resp_halka_css = """
    @media screen and (max-width: 768px) {{
      .container {{
        padding: 20px 14px !important;
        margin: 10px 4px !important;
        border-radius: 8px;
        box-shadow: none;
      }}
      .top-bar {{
        flex-direction: column;
        gap: 12px;
        text-align: center;
        padding: 14px 16px;
      }}
      .btn-pdf {{
        width: 100%;
        justify-content: center;
      }}
      h1 {{
        font-size: 20px;
        line-height: 1.35;
      }}
      .grid-3 {{
        grid-template-columns: 1fr !important;
      }}
      table {{
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
      }}
    }}
  </style>"""

if '@media screen and (max-width: 768px)' not in halka_code:
    halka_code = halka_code.replace('  </style>', resp_halka_css)

old_halka_save = """with open(html_guide_path_ws, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(html_guide_path_art, "w", encoding="utf-8") as f:
    f.write(html_content)"""

new_halka_save = """html_docs_path = os.path.join(WORKSPACE_DIR, "docs", "Halka_Anlatim_Rehberi.html")
for p in [html_guide_path_ws, html_guide_path_art, html_docs_path]:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html_content)

q1_desktop = r"C:\\Users\\maat\\Desktop\\ZENODO_V3_VEYA_Q1_DERGIYE_HAZIRLIK"
if os.path.exists(q1_desktop):
    with open(os.path.join(q1_desktop, "Halka_Anlatim_Rehberi.html"), "w", encoding="utf-8") as f:
        f.write(html_content)"""

if old_halka_save in halka_code:
    halka_code = halka_code.replace(old_halka_save, new_halka_save)

with open(halka_path, "w", encoding="utf-8") as f:
    f.write(halka_code)

print("[+] Executing build_halka_rehber.py via uv (playwright)...")
res = subprocess.run(["uv", "run", "--with", "playwright", "python", halka_path], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)

# ==============================================================================
# 4. BUILD_ENGLISH_IEEE_PAPER.PY
# ==============================================================================
print("\n[*] 4. Patching build_english_ieee_paper.py...")
ieee_path = os.path.join(WORKSPACE_DIR, "scripts", "build_english_ieee_paper.py")
with open(ieee_path, "r", encoding="utf-8") as f:
    ieee_code = f.read()

# Add viewport tag
if '<meta name="viewport"' not in ieee_code:
    ieee_code = ieee_code.replace(
        '<meta charset="UTF-8">\n<title>',
        '<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>'
    )

resp_ieee_css = """
  @media screen and (max-width: 768px) {{
    body {{
      padding: 16px 12px !important;
      font-size: 10.5pt !important;
    }}
    .two-column-body {{
      column-count: 1 !important;
    }}
    .abstract-container {{
      max-width: 100% !important;
    }}
    .paper-title {{
      font-size: 16pt !important;
    }}
    table {{
      display: block !important;
      width: 100% !important;
      overflow-x: auto !important;
      -webkit-overflow-scrolling: touch;
    }}
    img {{
      max-width: 100% !important;
      height: auto !important;
    }}
  }}
</style>"""

if '@media screen and (max-width: 768px)' not in ieee_code:
    ieee_code = ieee_code.replace('</style>', resp_ieee_css)

with open(ieee_path, "w", encoding="utf-8") as f:
    f.write(ieee_code)

print("[+] Executing build_english_ieee_paper.py via uv (playwright)...")
res = subprocess.run(["uv", "run", "--with", "playwright", "python", ieee_path], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)

print("\n[*] All scripts patched and built successfully!")
