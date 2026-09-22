import os

html_path = r"zenodo_preprint_package\preprint_template.html"
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove manual page-breaks
text = text.replace('<div class="page-break"></div>\n\n', '')
text = text.replace('<div class="page-break"></div>\n', '')
text = text.replace('<div class="page-break"></div>', '')

# Normalize figure heights
for h in [220, 200, 195, 190, 185, 180]:
    text = text.replace(f'max-height: {h}px;', 'max-height: 165px;')

# Ensure sections and figures have page-break rules
text = text.replace('h2 {', 'h2 {\n        page-break-after: avoid;\n        break-after: avoid;')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("HTML optimized successfully.")
