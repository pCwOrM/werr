import os
import shutil
import zipfile

WORKSPACE_DIR = r"c:\Users\maat\Documents\antigravity\wonderful-raman"
ARTIFACT_DIR = r"C:\Users\maat\.gemini\antigravity\brain\be1030f1-5b3e-4e9e-886d-2b41ab9b7de4"
ARXIV_DIR = os.path.join(WORKSPACE_DIR, "arxiv")
FIGURES_DIR = os.path.join(ARXIV_DIR, "figures")

DESKTOP_DIRS = [
    r"C:\Users\maat\Desktop\ZENODO_V2_YUKLENECEKLER",
    r"C:\Users\maat\Desktop\ZENODO_GUNCEL_DOSYALAR"
]

def create_arxiv_bundle():
    print("=" * 70)
    print("PACKAGING CAMERA-READY ARXIV / OVERLEAF LATEX BUNDLE")
    print("=" * 70)

    zip_filename = "Mandelbrot_Fractal_Paper_arXiv_Bundle.zip"
    zip_path_arxiv = os.path.join(ARXIV_DIR, zip_filename)
    zip_path_root = os.path.join(WORKSPACE_DIR, zip_filename)
    zip_path_artifact = os.path.join(ARTIFACT_DIR, zip_filename)

    # Temporary or clean packaging: only main.tex, references.bib, and figures/
    with zipfile.ZipFile(zip_path_arxiv, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 1. main.tex
        tex_path = os.path.join(ARXIV_DIR, "main.tex")
        zipf.write(tex_path, "main.tex")
        print("  [+] Added: main.tex")

        # 2. references.bib
        bib_path = os.path.join(ARXIV_DIR, "references.bib")
        zipf.write(bib_path, "references.bib")
        print("  [+] Added: references.bib")

        # 3. figures
        for f in sorted(os.listdir(FIGURES_DIR)):
            if f.endswith(".png") or f.endswith(".jpg") or f.endswith(".pdf"):
                fp = os.path.join(FIGURES_DIR, f)
                zipf.write(fp, os.path.join("figures", f))
                print(f"  [+] Added figure: figures/{f}")

    # Copy to root and artifacts
    shutil.copy2(zip_path_arxiv, zip_path_root)
    shutil.copy2(zip_path_arxiv, zip_path_artifact)

    # Copy to desktop folders if they exist
    for d in DESKTOP_DIRS:
        if os.path.exists(d):
            shutil.copy2(zip_path_arxiv, os.path.join(d, zip_filename))
            print(f"  [+] Mirrored to Desktop: {d}")

    size_kb = os.path.getsize(zip_path_arxiv) // 1024
    print(f"\n[SUCCESS] arXiv Bundle successfully created: {zip_path_arxiv} ({size_kb} KB)")

if __name__ == "__main__":
    create_arxiv_bundle()
