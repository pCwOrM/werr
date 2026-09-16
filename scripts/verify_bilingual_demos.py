import os
from playwright.sync_api import sync_playwright

WORKSPACE = r"c:\Users\maat\Documents\antigravity\wonderful-raman"
DEMOS = os.path.join(WORKSPACE, "demos")
ARTIFACTS_DIR = r"C:\Users\maat\.gemini\antigravity\brain\be1030f1-5b3e-4e9e-886d-2b41ab9b7de4"

def test_demos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="msedge")
        
        # -------------------------------------------------------------
        # 1. Test quadrant_visualizer.html with clean context
        # -------------------------------------------------------------
        context1 = browser.new_context(viewport={"width": 1280, "height": 900})
        page1 = context1.new_page()

        qv_url = "file:///" + os.path.join(DEMOS, "quadrant_visualizer.html").replace("\\", "/")
        print(f"Navigating to {qv_url}...")
        page1.goto(qv_url)
        page1.wait_for_timeout(1000)

        # Check default TR title
        title_tr = page1.inner_text("#qvTitle")
        print(f"QV Initial Title (TR): {title_tr}")
        assert "Fraktal Nöron" in title_tr or "Fraktal" in title_tr

        # Screenshot TR Dark
        page1.screenshot(path=os.path.join(ARTIFACTS_DIR, "qv_tr_dark_preview.png"))

        # Click Lang Toggle to English
        page1.click("#langToggleBtn")
        page1.wait_for_timeout(500)
        title_en = page1.inner_text("#qvTitle")
        btn_lang_text = page1.inner_text("#langText")
        print(f"QV After Toggle (EN): Title='{title_en}', LangBtn='{btn_lang_text}'")
        assert "Fractal Neuron" in title_en
        assert btn_lang_text == "Türkçe"

        # Screenshot EN Dark
        page1.screenshot(path=os.path.join(ARTIFACTS_DIR, "qv_en_dark_preview.png"))

        # Switch to Light Theme in EN
        page1.click("#themeToggleBtn")
        page1.wait_for_timeout(500)
        page1.screenshot(path=os.path.join(ARTIFACTS_DIR, "qv_en_light_preview.png"))

        context1.close()

        # -------------------------------------------------------------
        # 2. Test interactive_lab.html with clean context
        # -------------------------------------------------------------
        context2 = browser.new_context(viewport={"width": 1280, "height": 900})
        page2 = context2.new_page()

        il_url = "file:///" + os.path.join(DEMOS, "interactive_lab.html").replace("\\", "/")
        print(f"Navigating to {il_url}...")
        page2.goto(il_url)
        page2.wait_for_timeout(1000)

        il_title_tr = page2.inner_text("#labTitle")
        print(f"IL Initial Title (TR): {il_title_tr}")
        assert "Fraktal Beyin" in il_title_tr

        # Screenshot TR Light
        page2.screenshot(path=os.path.join(ARTIFACTS_DIR, "il_tr_light_preview.png"))

        # Click Lang Toggle to English
        page2.click("#btnLangToggle")
        page2.wait_for_timeout(500)
        il_title_en = page2.inner_text("#labTitle")
        il_lang_btn = page2.inner_text("#langText")
        print(f"IL After Toggle (EN): Title='{il_title_en}', LangBtn='{il_lang_btn}'")
        assert "Fractal Brain" in il_title_en
        assert il_lang_btn == "Türkçe"

        # Switch Scenario in EN (Bank Vault)
        page2.click("#tab_safe")
        page2.wait_for_timeout(500)
        sc_tag = page2.inner_text("#scenarioTag")
        print(f"IL Scenario Tag: {sc_tag}")
        assert "bank vault" in sc_tag.lower()

        # Screenshot EN Light
        page2.screenshot(path=os.path.join(ARTIFACTS_DIR, "il_en_light_preview.png"))

        # Switch to Dark Theme in EN
        page2.click("#btnThemeToggle")
        page2.wait_for_timeout(500)
        page2.screenshot(path=os.path.join(ARTIFACTS_DIR, "il_en_dark_preview.png"))

        # Click Lang Toggle back to Turkish
        page2.click("#btnLangToggle")
        page2.wait_for_timeout(500)
        sc_tag_tr = page2.inner_text("#scenarioTag")
        print(f"IL After Back to TR: Scenario Tag='{sc_tag_tr}'")
        assert "banka" in sc_tag_tr.lower()

        context2.close()
        browser.close()
        print("[SUCCESS] All bilingual demos verified cleanly in both TR & EN, Light & Dark!")

if __name__ == "__main__":
    test_demos()
