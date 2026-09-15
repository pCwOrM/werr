import os
import shutil
import zipfile
from playwright.sync_api import sync_playwright

WORKSPACE_DIR = r"c:\Users\maat\Documents\antigravity\wonderful-raman"
ARTIFACT_DIR = r"C:\Users\maat\.gemini\antigravity\brain\be1030f1-5b3e-4e9e-886d-2b41ab9b7de4"
SUBMISSION_DIR = os.path.join(WORKSPACE_DIR, "arxiv_submission")
FIGURES_DIR = os.path.join(SUBMISSION_DIR, "figures")

os.makedirs(FIGURES_DIR, exist_ok=True)

# 1. Şekilleri figures klasörüne kopyala
fig_names = [
    "mandelbrot_patches.png",
    "zoom_weight_curve.png",
    "resolution_comparison_128.png",
    "quadrant_weights_128.png",
    "gate_solutions_128.png",
    "xor_complete_network_128.png"
]

for fname in fig_names:
    src = os.path.join(ARTIFACT_DIR, fname)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(FIGURES_DIR, fname))
        print(f"[+] Kopyalandı: {fname} -> {FIGURES_DIR}")

# 2. arXiv / Overleaf için tam zip arşivi oluştur
zip_path = os.path.join(WORKSPACE_DIR, "Mandelbrot_Fractal_Paper_arXiv_Bundle.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(SUBMISSION_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, SUBMISSION_DIR)
            zipf.write(file_path, arcname)

print(f"[+] arXiv Yükleme Paketi (ZIP) Hazırlandı: {zip_path}")
print(f"    Boyut: {os.path.getsize(zip_path) // 1024} KB")

# 3. İki sütunlu IEEE akademik PDF'ini derle
pdf_output_path = os.path.join(WORKSPACE_DIR, "Mandelbrot_Fractal_Neural_Synthesis_IEEE_Paper.pdf")
pdf_artifact_path = os.path.join(ARTIFACT_DIR, "Mandelbrot_Fractal_Neural_Synthesis_IEEE_Paper.pdf")
html_source = os.path.join(WORKSPACE_DIR, "Mandelbrot_Akademik_Teknik_Raporu.html")

print("[*] Playwright / Edge ile nihai akademik PDF derleniyor...")
with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page()
    page.goto(f'file:///{os.path.abspath(html_source)}')
    page.pdf(
        path=pdf_output_path,
        format='A4',
        print_background=True,
        margin={'top': '14mm', 'bottom': '14mm', 'left': '12mm', 'right': '12mm'}
    )
    browser.close()

shutil.copy2(pdf_output_path, pdf_artifact_path)
print(f"[+] Nihai Akademik PDF Başarıyla Oluşturuldu:")
print(f"    - Workspace: {pdf_output_path}")
print(f"    - Artifact : {pdf_artifact_path}")
print(f"    - Boyut    : {os.path.getsize(pdf_output_path) // 1024} KB")
