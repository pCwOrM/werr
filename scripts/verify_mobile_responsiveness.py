import os
from playwright.sync_api import sync_playwright

WORKSPACE = r"c:\Users\maat\Documents\antigravity\wonderful-raman"

files_to_test = [
    os.path.join(WORKSPACE, "index.html"),
    os.path.join(WORKSPACE, "docs", "Halka_Sunum_ve_Teorik_Rehber.html"),
    os.path.join(WORKSPACE, "docs", "Mandelbrot_Akademik_Teknik_Raporu.html"),
    os.path.join(WORKSPACE, "docs", "Mandelbrot_Fraktal_Noron_Raporu.html"),
    os.path.join(WORKSPACE, "docs", "Halka_Anlatim_Rehberi.html"),
    os.path.join(WORKSPACE, "docs", "Halk_Icin_Kilavuz.html"),
    os.path.join(WORKSPACE, "docs", "Mandelbrot_Fractal_Neural_Synthesis_IEEE_Paper_EN.html"),
    os.path.join(WORKSPACE, "demos", "interactive_lab.html"),
    os.path.join(WORKSPACE, "demos", "quadrant_visualizer.html"),
]

viewports = [
    {"name": "iPhone (390px)", "width": 390, "height": 844},
    {"name": "Android (360px)", "width": 360, "height": 800},
]

print("=== AUTOMATED MOBILE RESPONSIVENESS AUDIT ===")
with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    
    all_passed = True
    for vp in viewports:
        print(f"\n--- Testing Viewport: {vp['name']} (width: {vp['width']}px) ---")
        page = browser.new_page(viewport={"width": vp["width"], "height": vp["height"]})
        
        for f in files_to_test:
            rel = os.path.relpath(f, WORKSPACE)
            if not os.path.exists(f):
                print(f"[MISSING] {rel}")
                continue
            
            page.goto(f"file:///{os.path.abspath(f)}")
            page.wait_for_timeout(300)
            
            scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
            client_w = page.evaluate("() => document.documentElement.clientWidth")
            body_scroll_w = page.evaluate("() => document.body.scrollWidth")
            
            max_scroll = max(scroll_w, body_scroll_w)
            overflow = max_scroll > client_w + 1  # 1px tolerance
            
            status = "FAIL (OVERFLOW)" if overflow else "PASS (100% OK)"
            tag = "[FAIL]" if overflow else "[PASS]"
            if overflow:
                all_passed = False
                print(f"{tag} {rel:<45}: scrollWidth={max_scroll}, clientWidth={client_w} => {status}")
            else:
                print(f"{tag} {rel:<45}: scrollWidth={max_scroll}, clientWidth={client_w} => {status}")
        
        page.close()
    browser.close()

if all_passed:
    print("\n>>> ALL DOCUMENTS PASSED MOBILE RESPONSIVENESS (ZERO OVERFLOW)! <<<")
else:
    print("\n>>> SOME DOCUMENTS STILL HAVE HORIZONTAL OVERFLOW. <<<")
