import os
import base64
import shutil
from playwright.sync_api import sync_playwright

PACKAGE_DIR = r"c:\Users\maat\Documents\antigravity\wonderful-raman\zenodo_preprint_package"
TEMPLATE_HTML = os.path.join(PACKAGE_DIR, "preprint_template.html")
OUTPUT_HTML = os.path.join(PACKAGE_DIR, "preprint_presentation.html")
OUTPUT_PDF = os.path.join(PACKAGE_DIR, "Orbital_Error_Dynamics_Preprint.pdf")
DOCS_PDF = r"c:\Users\maat\Documents\antigravity\wonderful-raman\docs\Orbital_Error_Dynamics_Preprint.pdf"
PRIVATE_PDF = r"c:\Users\maat\Documents\antigravity\wonderful-raman\private_archive_paper2\docs\Orbital_Error_Dynamics_Preprint.pdf"
BRAIN_PDF = r"C:\Users\maat\.gemini\antigravity\brain\be1030f1-5b3e-4e9e-886d-2b41ab9b7de4\Orbital_Error_Dynamics_Preprint.pdf"

def get_b64(rel_path):
    path = os.path.join(PACKAGE_DIR, rel_path)
    if not os.path.exists(path):
        print(f"Warning: {rel_path} not found!")
        return ""
    ext = os.path.splitext(rel_path)[1].lower().replace('.', '')
    if ext == 'jpg': ext = 'jpeg'
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:image/{ext};base64,{data}"

print("Encoding clean scientific figures to base64...")
images = {
    "__FIG1_OBSERVER__": get_b64("figures/fig1_observer_horizon.png"),
    "__FIG2_BENT_SINE__": get_b64("figures/fig2_bent_sine_and_cusp.png"),
    "__FIG3_TUNNELING__": get_b64("figures/fig3_quantum_tunneling_operator.png"),
    "__FIG4_PHASE_SURFING__": get_b64("figures/fig4_nonequilibrium_phase_surfing.png"),
    "__FIG5_DUAL_BRAIN__": get_b64("figures/fig5_dual_brain_cybernetics.png"),
    "__FIG6_GENETICS__": get_b64("figures/fig6_complex_4quadrant_genetics.png"),
    "__FIG7_BENCHMARK__": get_b64("figures/fig7_empirical_benchmark.png")
}

print("Reading HTML template...")
with open(TEMPLATE_HTML, 'r', encoding='utf-8') as f:
    html_content = f.read()

print("Replacing image placeholders...")
for placeholder, b64_val in images.items():
    html_content = html_content.replace(placeholder, b64_val)

print(f"Writing compiled HTML to {OUTPUT_HTML}...")
with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Compiling Zenodo Preprint PDF with Playwright Chromium...")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file:///{OUTPUT_HTML.replace(chr(92), '/')}", wait_until="networkidle")
    page.pdf(
        path=OUTPUT_PDF,
        format="A4",
        print_background=True,
        margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
    )
    browser.close()

print(f"Preprint PDF generated successfully at: {OUTPUT_PDF}")
print(f"Preprint File Size: {os.path.getsize(OUTPUT_PDF) / (1024*1024):.2f} MB")

# Mirror to docs, private archive, and brain
shutil.copyfile(OUTPUT_PDF, DOCS_PDF)
shutil.copyfile(OUTPUT_PDF, PRIVATE_PDF)
shutil.copyfile(OUTPUT_PDF, BRAIN_PDF)
print("Mirrored to docs, private archive, and brain archive successfully!")
