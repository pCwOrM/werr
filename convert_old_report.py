import os
import base64

ESKI_RAPOR_DIR = r"C:\Users\maat\Desktop\eski_rapor"

def get_base64(filename):
    path = os.path.join(ESKI_RAPOR_DIR, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

img_patches = get_base64("mandelbrot_patches.png")
img_zoom_curve = get_base64("zoom_weight_curve.png")

html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mandelbrot Fraktal Tabanlı Ağırlık/Bias Türetim Deneyi - Rapor</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

    :root {{
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --text: #0f172a;
      --text-muted: #475569;
      --border: #e2e8f0;
      --card-bg: #f8fafc;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      color: var(--text);
      background-color: #f1f5f9;
      line-height: 1.6;
      font-size: 14px;
      -webkit-font-smoothing: antialiased;
    }}

    .page-container {{
      max-width: 950px;
      margin: 30px auto;
      background: #ffffff;
      padding: 50px 60px;
      border-radius: 16px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
      border: 1px solid var(--border);
    }}

    @media print {{
      body {{
        background: #ffffff;
        font-size: 12px;
      }}
      .page-container {{
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        box-shadow: none !important;
        border: none !important;
        border-radius: 0 !important;
      }}
      .no-print {{
        display: none !important;
      }}
      .avoid-break {{
        page-break-inside: avoid;
      }}
      .page-break {{
        page-break-before: always;
      }}
      @page {{
        size: A4;
        margin: 15mm 15mm 15mm 15mm;
      }}
    }}

    /* Action Bar */
    .action-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #0f172a;
      color: white;
      padding: 16px 24px;
      border-radius: 12px;
      margin-bottom: 30px;
    }}
    .action-bar h3 {{
      font-size: 15px;
      font-weight: 600;
    }}
    .action-bar p {{
      font-size: 12px;
      color: #94a3b8;
    }}
    .btn-print {{
      background: var(--primary);
      color: white;
      border: none;
      padding: 10px 20px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }}
    .btn-print:hover {{
      background: var(--primary-dark);
    }}

    /* Header */
    .report-header {{
      border-bottom: 2px solid var(--border);
      padding-bottom: 22px;
      margin-bottom: 30px;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 12px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-radius: 9999px;
      background: #eff6ff;
      color: var(--primary);
      border: 1px solid #dbeafe;
      margin-bottom: 12px;
    }}
    h1 {{
      font-size: 24px;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 10px;
    }}
    .lead {{
      font-size: 14px;
      color: #334155;
      line-height: 1.6;
    }}

    /* Content */
    section {{
      margin-bottom: 32px;
    }}
    h2 {{
      font-size: 17px;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 14px;
      border-left: 4px solid var(--primary);
      padding-left: 10px;
    }}
    h3 {{
      font-size: 14px;
      font-weight: 600;
      color: #1e293b;
      margin: 16px 0 8px 0;
    }}
    p {{
      margin-bottom: 12px;
      color: #334155;
      line-height: 1.65;
    }}

    /* Math Formula Blocks */
    .math-block {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 16px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: #0f172a;
      margin: 12px 0;
      text-align: center;
    }}

    /* Tables */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0 20px 0;
      font-size: 12px;
    }}
    th, td {{
      padding: 9px 12px;
      text-align: left;
      border: 1px solid var(--border);
    }}
    th {{
      background: #f1f5f9;
      font-weight: 600;
      color: #334155;
    }}
    tr:nth-child(even) {{
      background: #fafafa;
    }}
    .text-center {{
      text-align: center;
    }}
    .badge-success {{
      background: #ecfdf5;
      color: #059669;
      font-weight: 600;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 11px;
    }}

    /* Images */
    .img-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px;
      margin: 16px 0;
      text-align: center;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .img-card img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      display: block;
      margin: 0 auto;
    }}
    .img-caption {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 8px;
      font-weight: 500;
    }}

    /* Callouts */
    .callout {{
      padding: 14px 18px;
      border-radius: 10px;
      margin: 16px 0;
      font-size: 13px;
      border-left: 4px solid;
    }}
    .callout-info {{
      background: #eff6ff;
      border-color: #3b82f6;
      color: #1e40af;
    }}
    .callout-warning {{
      background: #fffbeb;
      border-color: #f59e0b;
      color: #92400e;
    }}
    .callout-title {{
      font-weight: 700;
      margin-bottom: 4px;
    }}
  </style>
</head>
<body>

<div class="page-container">

  <!-- Print Button Bar -->
  <div class="action-bar no-print">
    <div>
      <h3>📄 Mandelbrot Fraktal Deney Raporu (Arşiv)</h3>
      <p>Bu belgeyi doğrudan tarayıcınızdan PDF olarak kaydedebilirsiniz.</p>
    </div>
    <button class="btn-print" onclick="window.print()">
      <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
        <path d="M2.5 8a.5.5 0 1 0 0-1 .5.5 0 0 0 0 1z"/>
        <path d="M5 1a2 2 0 0 0-2 2v2H2a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h1v1a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-1h1a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-1V3a2 2 0 0 0-2-2H5zM4 3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2H4V3zm1 5a2 2 0 0 0-2 2v1H2a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v-1a2 2 0 0 0-2-2H5zm7 2v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1z"/>
      </svg>
      PDF Olarak Kaydet / Yazdır
    </button>
  </div>

  <!-- Header -->
  <header class="report-header">
    <div class="badge">Deney Raporu</div>
    <h1>Mandelbrot Fraktal Tabanlı Ağırlık/Bias Türetim Deneyi</h1>
    <p class="lead">
      Bu çalışma; Mandelbrot kümesi pencerelerinden görüntü işleme ve piksel analizi yoluyla <strong>karanlık alan (ıraksamayan noktalar kümesi)</strong> oranını okuyup, bunu yapay bir nöronun karar eşiğine (bias) ve ağırlıklarına bağlayan deneysel prototipin sonuçlarını içerir.
    </p>
  </header>

  <!-- 1. Deney Düzeneği -->
  <section class="avoid-break">
    <h2>1. Deney Düzeneği ve Matematiksel Eşleme</h2>
    <h3>Koordinat ve Zoom Uzayından Ağırlık Türetimi</h3>
    <p>
      Geleneksel sinir ağlarında her ağırlık bağımsız bir sayı olarak tensör matrislerinde tutulur. Bu prototipte ise parametreler şu üçlü ile ifade edilir:
    </p>
    <div class="math-block">&theta; = (c<sub>x</sub>, c<sub>y</sub>, zoom)</div>

    <ol style="margin-left: 20px; margin-bottom: 16px; color: #334155; line-height: 1.7;">
      <li><strong>Fraktal Pencere:</strong> Verilen (c<sub>x</sub>, c<sub>y</sub>) merkezli ve scale = 1 / zoom genişliğindeki karmaşık düzlem penceresinde z<sub>n+1</sub> = z<sub>n</sub><sup>2</sup> + c iterasyonu uygulanır.</li>
      <li><strong>Karanlık Bölge Tespiti (Black Ratio):</strong> Maksimum iterasyona (N<sub>max</sub> = 80) kadar kaçış yarıçapını (|z| &le; 2.0) aşmayan pikseller (kümenin içi) sayılır:
        <div class="math-block">R<sub>black</sub> = &sum; [|z<sub>N<sub>max</sub></sub>| &le; 2] / N<sub>piksel</sub></div>
      </li>
      <li><strong>Bias Eşlemesi:</strong> Elde edilen oran [0, 1] aralığından nöron için uygun bir çalışma aralığına normalize edilir:
        <div class="math-block">b = (R<sub>black</sub> - 0.5) &times; 4.0 &isin; [-2.0, +2.0]</div>
      </li>
      <li><strong>Nöron Kararı:</strong>
        <div class="math-block">&ycirc; = &sigma;(w<sub>1</sub> x<sub>1</sub> + w<sub>2</sub> x<sub>2</sub> + b)</div>
      </li>
    </ol>
  </section>

  <!-- 2. Deney Sonuçları ve Görseller -->
  <section class="avoid-break">
    <h2>2. Deney Sonuçları ve Görseller</h2>
    <p>Kod doğrudan Python ortamında çalıştırılmış ve aşağıdaki 3 referans bölge test edilmiştir:</p>

    <table>
      <thead>
        <tr>
          <th>Durum</th>
          <th>Merkez (c<sub>x</sub>, c<sub>y</sub>)</th>
          <th class="text-center">Zoom</th>
          <th class="text-center">Siyah Alan Oranı</th>
          <th class="text-center">Kaçış Ort.</th>
          <th class="text-center">Türetilen Bias (b)</th>
          <th class="text-center">Nöron Çıktısı &ycirc;</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Ana Gövde (Merkez)</strong></td>
          <td>(-0.5, 0.0)</td>
          <td class="text-center">1.0&times;</td>
          <td class="text-center"><strong>%38.3</strong></td>
          <td class="text-center">0.4386</td>
          <td class="text-center"><strong>-0.467</strong></td>
          <td class="text-center"><strong>0.630</strong></td>
        </tr>
        <tr>
          <td><strong>Seahorse Valley (Sınır)</strong></td>
          <td>(-0.7436, 0.1318)</td>
          <td class="text-center">100.0&times;</td>
          <td class="text-center"><strong>%50.3</strong></td>
          <td class="text-center">0.7108</td>
          <td class="text-center"><strong>+0.012</strong></td>
          <td class="text-center"><strong>0.733</strong></td>
        </tr>
        <tr>
          <td><strong>Dış Bölge (Kaçış)</strong></td>
          <td>(2.0, 2.0)</td>
          <td class="text-center">1.0&times;</td>
          <td class="text-center"><strong>%0.0</strong></td>
          <td class="text-center">0.0010</td>
          <td class="text-center"><strong>-2.000</strong></td>
          <td class="text-center"><strong>0.269</strong></td>
        </tr>
      </tbody>
    </table>

    <p style="font-size: 11px; color: var(--text-muted); margin-bottom: 16px;">
      <em>*(Girdi vektörü: x<sub>1</sub> = 0.5, x<sub>2</sub> = 0.5, w<sub>1</sub> = 1.0, w<sub>2</sub> = 1.0)*</em>
    </p>

    <h3>Referans Pencereler ve Siyah Alan Maskeleri</h3>
    <div class="img-card">
      <img src="{img_patches}" alt="Mandelbrot Pencereleri ve Karanlık Alan Maskeleri">
      <div class="img-caption">Şekil 1: Test edilen referans Mandelbrot bölgeleri ve siyah alan (ıraksamayan) maskeleri.</div>
    </div>
  </section>

  <!-- 3. Zoom Katsayısı -->
  <section class="page-break avoid-break">
    <h2>3. Zoom Katsayısının Ağırlık Üzerindeki Fraktal Etkisi</h2>
    <p>Seahorse Valley sınırında zoom katsayısı 1.0&times; ile 50,000&times; arasında logaritmik olarak taranmıştır:</p>

    <div class="img-card">
      <img src="{img_zoom_curve}" alt="Zoom Katsayısına Göre Bias ve Siyah Alan Eğrisi">
      <div class="img-caption">Şekil 2: Zoom katsayısına bağlı olarak üretilen siyah alan oranı, ortalama kaçış süresi ve bias (b) eğrisi.</div>
    </div>

    <h3>Temel Gözlemler:</h3>
    <ol style="margin-left: 20px; color: #334155; line-height: 1.7;">
      <li><strong>Fraktal Salınım:</strong> Zoom arttıkça siyah alan oranı tekdüze (monoton) artıp azalmaz; fraktalın kendi kendine benzer (self-similar) mini kopyalarına girip çıktıkça sürekli yerel tepeler ve vadiler oluşturur.</li>
      <li><strong>Hassasiyet (Sensitivity):</strong> Çok küçük bir zoom değişimi, siyah alan oranında sıçramalara sebep olabilir. Bu durum deterministik kaosun doğrudan sonucudur.</li>
      <li><strong>Kaçış Ortalaması Avantajı:</strong> Kırmızı kesikli çizgiyle gösterilen <em>Ortalama Kaçış Süresi</em>, siyah alan oranına göre daha yumuşak ve sürekli bir eğri üretmektedir.</li>
    </ol>
  </section>

  <!-- 4. Pratik Görev: OR Kapısı -->
  <section class="avoid-break">
    <h2>4. Pratik Görev Testi: Mantıksal OR Kapısı Optimizasyonu</h2>
    <p>
      Deney kapsamında sabit ağırlıklı (w<sub>1</sub>=2.0, w<sub>2</sub>=2.0) bir nöronda OR kapısını çözmek için gereken bias değeri fraktal zoom araması ile test edilmiştir:
    </p>

    <ul style="margin-left: 20px; margin-bottom: 14px; color: #334155;">
      <li><strong>Gereken Teorik Bias:</strong> Yaklaşık -1.00 (R<sub>black</sub> = 0.25)</li>
      <li><strong>Bulunan Optimal Zoom:</strong> <strong>884.73&times;</strong></li>
      <li><strong>Elde Edilen Siyah Alan:</strong> <strong>0.2422</strong> (%24.22)</li>
      <li><strong>Oluşan Bias:</strong> <strong>-1.0312</strong></li>
    </ul>

    <h3>Doğruluk Tablosu:</h3>
    <table>
      <thead>
        <tr>
          <th class="text-center">Girdi (x<sub>1</sub>, x<sub>2</sub>)</th>
          <th class="text-center">Hedef</th>
          <th class="text-center">z = 2x<sub>1</sub> + 2x<sub>2</sub> + b</th>
          <th class="text-center">&sigma;(z)</th>
          <th class="text-center">Tahmin</th>
          <th class="text-center">Durum</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="text-center font-mono">(0, 0)</td>
          <td class="text-center">0</td>
          <td class="text-center font-mono">-1.03</td>
          <td class="text-center">0.263</td>
          <td class="text-center">0</td>
          <td class="text-center"><span class="badge-success">BAŞARILI ✅</span></td>
        </tr>
        <tr>
          <td class="text-center font-mono">(0, 1)</td>
          <td class="text-center">1</td>
          <td class="text-center font-mono">+0.97</td>
          <td class="text-center">0.725</td>
          <td class="text-center">1</td>
          <td class="text-center"><span class="badge-success">BAŞARILI ✅</span></td>
        </tr>
        <tr>
          <td class="text-center font-mono">(1, 0)</td>
          <td class="text-center">1</td>
          <td class="text-center font-mono">+0.97</td>
          <td class="text-center">0.725</td>
          <td class="text-center">1</td>
          <td class="text-center"><span class="badge-success">BAŞARILI ✅</span></td>
        </tr>
        <tr>
          <td class="text-center font-mono">(1, 1)</td>
          <td class="text-center">1</td>
          <td class="text-center font-mono">+2.97</td>
          <td class="text-center">0.951</td>
          <td class="text-center">1</td>
          <td class="text-center"><span class="badge-success">BAŞARILI ✅</span></td>
        </tr>
      </tbody>
    </table>

    <p>
      <strong>Doğruluk: %100!</strong> Model, Mandelbrot kümesinde doğru derinliğe dalarak mantıksal bir kapıyı doğru çözecek parametreyi görsel alandan yakalamıştır.
    </p>
  </section>

  <!-- 5. Çıkarımlar -->
  <section class="avoid-break">
    <h2>5. Çıkarımlar ve Gelecek Adımlar</h2>

    <div class="callout callout-info">
      <div class="callout-title">HyperNEAT Paralelliği</div>
      Bu yöntem, HyperNEAT'in uzamsal koordinatlardan ağırlık türeten CPPN ağlarına benzer şekilde, son derece kompakt parametrelerle (sadece 3 skaler: c<sub>x</sub>, c<sub>y</sub>, zoom) sonsuz çeşitlilikte ağırlık türetme potansiyeline sahiptir.
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">Kuantum ve Donanım Perspektifi</div>
      Piksel bazlı simülasyon günümüz GPU'larında iteratif döngü maliyeti getirse de; gelecekte optik/fotonik işlemciler veya kuantum girişim haritaları ile fraktal veya dalga fonksiyonlarının anlık fiziksel projeksiyonlarından ağırlık okunması fikri teorik olarak bu prototipin donanım eşleniği olabilir.
    </div>
  </section>

  <footer style="border-top: 1px solid var(--border); padding-top: 16px; margin-top: 30px; font-size: 11px; color: var(--text-muted); text-align: center;">
    Mandelbrot Fraktal Tabanlı Nöral Ağırlık/Bias Türetim Deneyi &bull; Standalone HTML Raporu
  </footer>

</div>

</body>
</html>
"""

output_path = os.path.join(ESKI_RAPOR_DIR, "mandelbrot_fractal_neuron_report.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[+] Eski rapor HTML olarak başarıyla kaydedildi: {output_path}")
print(f"[+] Boyut: {len(html_content) // 1024} KB")
