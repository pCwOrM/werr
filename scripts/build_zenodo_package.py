import os
import zipfile

def build_zenodo_zip():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paper_dir = os.path.join(base_dir, 'paper')
    zip_path = os.path.join(paper_dir, 'werr_zenodo_v2_code_and_benchmarks.zip')

    included_dirs = ['werr', 'benchmarks/jevbench', 'benchmarks/sealed']
    included_files = ['README.md', 'README_TR.md', 'LICENSE', 'pyproject.toml', 'docs/PAPER_V2_BLUEPRINT.md']

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for f in included_files:
            fp = os.path.join(base_dir, f)
            if os.path.exists(fp):
                zipf.write(fp, arcname=f)

        for d in included_dirs:
            dp = os.path.join(base_dir, d)
            if os.path.exists(dp):
                for root, _, files in os.walk(dp):
                    for file in files:
                        if file.endswith(('.pyc', '.pyo')) or '__pycache__' in root:
                            continue
                        full_p = os.path.join(root, file)
                        rel_p = os.path.relpath(full_p, base_dir)
                        zipf.write(full_p, arcname=rel_p)

    print(f"[+] Zenodo Research Archive successfully packaged: {zip_path}")
    print(f"[+] Size: {os.path.getsize(zip_path)} bytes")

if __name__ == '__main__':
    build_zenodo_zip()
