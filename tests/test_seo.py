"""Automated SEO, structured-data, robots.txt, sitemap.xml, and llms.txt checks for werr.io."""
from html.parser import HTMLParser
import json
import os
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://werr.io"


class _SeoHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self._in_title = False
        self.metas = []
        self.links = []
        self.h1s = []
        self._in_h1 = False
        self._cur_h1 = ""
        self.imgs = []
        self.jsonld = []
        self._in_jsonld = False
        self._cur_jsonld = ""
        self.has_main = False

    def handle_starttag(self, tag, attrs):
        t = tag.lower()
        d = dict(attrs)
        if t == "title":
            self._in_title = True
        elif t == "meta":
            self.metas.append(d)
        elif t == "link":
            self.links.append(d)
        elif t == "h1":
            self._in_h1 = True
            self._cur_h1 = ""
        elif t == "img":
            self.imgs.append(d)
        elif t == "main":
            self.has_main = True
        elif t == "script" and (d.get("type") or "").lower() == "application/ld+json":
            self._in_jsonld = True
            self._cur_jsonld = ""

    def handle_endtag(self, tag):
        t = tag.lower()
        if t == "title":
            self._in_title = False
        elif t == "h1" and self._in_h1:
            self._in_h1 = False
            self.h1s.append(re.sub(r"\s+", " ", self._cur_h1).strip())
        elif t == "script" and self._in_jsonld:
            self._in_jsonld = False
            self.jsonld.append(self._cur_jsonld.strip())

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1:
            self._cur_h1 += data
        if self._in_jsonld:
            self._cur_jsonld += data


def _url_to_rel(url: str) -> str:
    assert url.startswith(BASE_URL), f"Unexpected URL outside {BASE_URL}: {url}"
    path = url[len(BASE_URL):].lstrip("/")
    return path if path else "index.html"


def _robots_allows(robots_txt: str, path: str) -> bool:
    rules = []
    in_star = False
    for raw in robots_txt.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if line.lower().startswith("user-agent:"):
            ua = line.split(":", 1)[1].strip()
            in_star = ua == "*"
        elif in_star and line.lower().startswith(("allow:", "disallow:")):
            k, v = line.split(":", 1)
            rules.append((k.strip().lower(), v.strip()))
    best = None
    for directive, pattern in rules:
        if pattern and path.startswith(pattern):
            cand = (len(pattern), directive == "allow")
            if best is None or cand > best:
                best = cand
    return True if best is None else best[1]


class TestWerrSEO(unittest.TestCase):
    def test_robots_and_sitemap_parity(self):
        robots_path = os.path.join(ROOT, "robots.txt")
        sitemap_path = os.path.join(ROOT, "sitemap.xml")
        self.assertTrue(os.path.exists(robots_path))
        self.assertTrue(os.path.exists(sitemap_path))
        with open(robots_path, encoding="utf-8") as f:
            robots = f.read()
        self.assertIn(f"Sitemap: {BASE_URL}/sitemap.xml", robots)

        tree = ET.parse(sitemap_path)
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [el.text.strip() for el in tree.getroot().findall(".//sm:url/sm:loc", ns)]
        self.assertGreaterEqual(len(locs), 4)
        self.assertEqual(len(locs), len(set(locs)), "Duplicate URLs in sitemap.xml")

        for loc in locs:
            rel = _url_to_rel(loc)
            self.assertTrue(os.path.exists(os.path.join(ROOT, rel)), f"Missing file for {loc}")
            url_path = "/" + ("" if rel == "index.html" else rel.replace("\\", "/"))
            self.assertTrue(_robots_allows(robots, url_path), f"robots.txt blocks sitemap URL {url_path}")

    def test_llms_txt_and_404_noindex(self):
        llms_path = os.path.join(ROOT, "llms.txt")
        self.assertTrue(os.path.exists(llms_path))
        with open(llms_path, encoding="utf-8") as f:
            llms = f.read()
        self.assertIn("https://werr.io/", llms)
        self.assertGreater(len(llms), 200)

        with open(os.path.join(ROOT, "404.html"), encoding="utf-8") as f:
            err_page = f.read()
        self.assertRegex(err_page, r'<meta\s+name=["\']robots["\'][^>]*noindex')

    def test_all_sitemap_pages_metadata_headings_and_jsonld(self):
        tree = ET.parse(os.path.join(ROOT, "sitemap.xml"))
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [el.text.strip() for el in tree.getroot().findall(".//sm:url/sm:loc", ns)]
        seen_titles = set()

        for loc in locs:
            rel = _url_to_rel(loc)
            fp = os.path.join(ROOT, rel)
            with open(fp, encoding="utf-8") as f:
                html = f.read()
            p = _SeoHTMLParser()
            p.feed(html)

            title = p.title.strip()
            self.assertTrue(25 <= len(title) <= 75, f"{rel} title length {len(title)}: {title!r}")
            self.assertNotIn(title, seen_titles, f"Duplicate title {title!r}")
            seen_titles.add(title)

            descs = [m.get("content", "") for m in p.metas if (m.get("name") or "").lower() == "description"]
            self.assertEqual(len(descs), 1, f"{rel} missing description")
            self.assertTrue(90 <= len(descs[0]) <= 165, f"{rel} desc length {len(descs[0])}")

            robots_metas = [m.get("content", "") for m in p.metas if (m.get("name") or "").lower() == "robots"]
            self.assertTrue(robots_metas and "noindex" not in robots_metas[0].lower(), f"{rel} invalid robots meta")
            self.assertIn("max-image-preview:large", robots_metas[0])

            canon = [l.get("href") for l in p.links if "canonical" in (l.get("rel") or "").lower().split()]
            self.assertEqual(canon, [loc], f"{rel} canonical mismatch: {canon}")

            self.assertEqual(len(p.h1s), 1, f"{rel} must have exactly 1 <h1>, got {p.h1s}")
            self.assertGreater(len(p.h1s[0]), 1, f"{rel} empty <h1>")
            self.assertTrue(p.has_main, f"{rel} missing <main> landmark")

            ogs = {m.get("property"): m.get("content") for m in p.metas if (m.get("property") or "").startswith("og:")}
            for k in ("og:title", "og:description", "og:url", "og:image", "og:type", "og:site_name"):
                self.assertIn(k, ogs, f"{rel} missing {k}")
            self.assertEqual(ogs["og:url"], loc)

            tws = {m.get("name"): m.get("content") for m in p.metas if (m.get("name") or "").startswith("twitter:")}
            for k in ("twitter:card", "twitter:title", "twitter:description", "twitter:image"):
                self.assertIn(k, tws, f"{rel} missing {k}")

            self.assertGreaterEqual(len(p.jsonld), 1, f"{rel} missing JSON-LD")
            for raw_ld in p.jsonld:
                obj = json.loads(raw_ld)
                self.assertIn("@context", obj)

            for im in p.imgs:
                self.assertIn("alt", im, f"{rel} <img> missing alt attribute: {im}")
                src = im.get("src", "")
                if src and not src.startswith(("http://", "https://", "data:")):
                    target = os.path.normpath(os.path.join(os.path.dirname(fp), src))
                    self.assertTrue(os.path.exists(target), f"{rel} broken local image {src}")


if __name__ == "__main__":
    unittest.main()
