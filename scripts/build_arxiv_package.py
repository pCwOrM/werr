import os
import zipfile

def build_zip():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paper_dir = os.path.join(base_dir, 'paper')
    zip_path = os.path.join(paper_dir, 'werr_arxiv_package.zip')
    legacy_zip_path = os.path.join(paper_dir, 'wevv_arxiv_package.zip')
    
    for zpath in [zip_path, legacy_zip_path]:
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # add main.tex
            tex_file = os.path.join(paper_dir, 'main.tex')
            zipf.write(tex_file, arcname='main.tex')
            
            # add references.bib
            bib_file = os.path.join(paper_dir, 'references.bib')
            zipf.write(bib_file, arcname='references.bib')
            
            # add figures
            fig_dir = os.path.join(paper_dir, 'figures')
            for root, _, files in os.walk(fig_dir):
                for file in files:
                    full_p = os.path.join(root, file)
                    rel_p = os.path.relpath(full_p, paper_dir)
                    zipf.write(full_p, arcname=rel_p)
                
    print(f"Successfully packaged arXiv bundle: {zip_path}")
    print(f"Size: {os.path.getsize(zip_path)} bytes")

if __name__ == '__main__':
    build_zip()
