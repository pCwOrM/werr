import os
from playwright.sync_api import sync_playwright

WORKSPACE_DIR = r"c:\Users\maat\Documents\antigravity\wonderful-raman"
ARTIFACT_DIR = r"C:\Users\maat\.gemini\antigravity\brain\be1030f1-5b3e-4e9e-886d-2b41ab9b7de4"

# 1. MARKDOWN REHBERİ
md_path_art = os.path.join(ARTIFACT_DIR, "halka_anlatim_rehberi.md")
md_path_ws = os.path.join(WORKSPACE_DIR, "halka_anlatim_rehberi.md")

md_content = """# Fraktal Yapay Zekayı Halka ve Son Kullanıcıya Anlatım Rehberi
**Hazırlayan:** Antigravity AI & Araştırma Ekibi  
**Hedef Kitle:** Mühendis olmayanlar, öğrenciler, gazeteciler, yatırımcılar, arkadaşlar ve aile  
**Amacı:** Matematiksel karmaşaya boğulmadan; güçlü metaforlar, görsel örnekler ve akılda kalıcı hikayelerle bu buluşu herkesin anlayacağı dille sunmak.

---

## 1. 30 Saniyelik Asansör Konuşması (Elevator Pitch)

> *"Bugünkü yapay zekalar (ChatGPT gibi) trilyonlarca sayıyı devasa bilgisayarlara ezberleterek çalışır; bu yüzden dev gibi enerji ve yüzlerce ekran kartı harcar.*  
> *Biz ise sayıları ezberlemek yerine, doğada ve matematikte kendiliğinden var olan sonsuz bir tabloya — Mandelbrot fraktalına — büyüteçle bakıyoruz.*  
> *Fraktalın doğru köşesine baktığımızda oradaki karanlık adacıkların büyüklüğü, yapay nöronumuzun karar katsayısı oluyor. Hiçbir şeyi hafızada saklamadan, tek bir minik formülle çalışan bir yapay zeka beyni üretiyoruz!"*

---

## 2. Zihinde Canlandırıcı 3 Büyük Metafor

İnsanlar formülleri değil, zihinlerinde resmedebildikleri hikayeleri anlarlar. Karşınızdakine anlatırken şu 3 metaforu kullanın:

### Metafor 1: "Dev Ansiklopedi Taşımak vs. Sihirli Dürbün Kullanmak"
* **Klasik Yapay Zeka:** Sırtında 1000 ciltlik bir ansiklopedi taşır. Her bir soruya cevap vermek için sayfaları çevirir, devasa belleklere (RAM/VRAM) ihtiyaç duyar.
* **Bizim Yöntemimiz:** Sırtında hiçbir şey taşımaz. Elinde sadece sihirli bir dürbün (koordinat ve zoom) vardır. Sonsuz duvar halısına (Mandelbrot) bakar; baktığı yerdeki desenin karanlık oranından cevabı anında okur!

### Metafor 2: "DNA ve İnsan Hücresi"
* Bir insanın trilyonlarca hücresi ve 100 trilyon beyin bağlantısı vardır. Fakat insan DNA'sı bir USB belleğin küçük bir kısmı kadardır (~750 MB).
* DNA her bir hücreyi tek tek çizmez; bir **özyinelemeli tohum kural** koyar ve o kural kendi kendine büyür. Mandelbrot da tam olarak böyledir: $z = z^2 + c$ tek satırlık bir tohumdur ama sonsuz bir evren doğurur!

### Metafor 3: "Çiçek Dürbünü (Kaleidoskop)"
* Çiçek dürbününü hafifçe çevirdiğinizde içindeki cam kırıkları bambaşka muazzam simetrik şekillere bürünür. Bizim zoom seviyesini değiştirmemiz de aynen böyledir; hafifçe içeri daldığımızda nöronumuz bambaşka bir mantığı (OR, AND, XOR) öğrenmiş olur.

---

## 3. Adım Adım Çalışma Akışı (Girdi &rarr; Hesaplama &rarr; Çıktı)

Halka açık arayüzümüzü (`fraktal_noron_halk_arayuzu.html`) gösterirken izleyeceğiniz sıra:

1. **Adım 1: Girdi Gelir (Yapay Zekanın Gözleri):**
   * Örnek: Akıllı kapıda "Kart okutuldu mu? (Evet=1 / Hayır=0)" ve "Yüz tanındı mı? (Evet=1 / Hayır=0)".
2. **Adım 2: Fraktal Aynasına Bakılır (Yapay Zekanın Hafızası):**
   * Ekranda gördüğünüz rengarenk Mandelbrot penceresi açılır. 
   * Bu penceredeki **ortadaki siyah alanın büyüklüğünü (karanlık oranı)** piksel piksel sayarız.
   * Pencereyi 4'e bölüyoruz: Sol üst köşe 1. girdinin önemini, sağ üst 2. girdinin önemini, alt köşe ise eşik değerini belirler.
3. **Adım 3: Nöron Ateşlenir ve Karar Çıkar (Yapay Zekanın Kararı):**
   * Sinyaller toplanır. Eğer toplam sinyal eşiği aşarsa ortadaki nöron yeşil neon ışığıyla parlar (**ATEŞLENDİ!**) ve kapı açılır!

---

## 4. Halkın Soracağı 7 Zor Soru ve Net Yanıtları (FAQ)

### Soru 1: "Yani bilgisayar resme bakarak mı düşünüyor? Nasıl oluyor bu?"
**Cevap:** Evet, tam olarak öyle! Klasik bilgisayarlar sayıları depolarken, biz bir geometrik şeklin piksel yoğunluğunu sayıya dönüştürüyoruz. Resmin neresine ve ne kadar yakından baktığımız, nöronun ne kadar sert veya yumuşak karar vereceğini belirliyor.

### Soru 2: "Bu sistem ChatGPT'den daha mı akıllı?"
**Cevap:** Henüz değil. ChatGPT trilyonlarca kelime okumuş devasa bir kütüphanedir. Bizim yaptığımız şey ise henüz tek bir "akıllı beyin hücresi" (nöron). Fakat bizim hücremiz hafızada neredeyse hiç yer tutmuyor. Gelecekte bu hücreleri yan yana koyarak devasa ama sıfır hafıza kaplayan yeni nesil bir ChatGPT yapılabilir.

### Soru 3: "Karanlık bölge ne alaka? Neden aydınlık yerler değil?"
**Cevap:** Mandelbrot kümesinde ortadaki siyah alan, denklemin sonsuza patlamayıp kendi içinde sakin ve dengede kaldığı yerdir. Matematiksel olarak "istikrarı" temsil eder. Bu yüzden siyah piksellerin kapladığı alan, nöronumuz için en güvenilir terazi ağırlığıdır.

### Soru 4: "Bunun dünyaya gerçek faydası ne olacak?"
**Cevap:** Üç büyük devrim getirebilir:
1. **Sıfır Hafıza (Sıkıştırma):** Telefonunuza sığmayan devasa yapay zeka modelleri, küçük bir fraktal tohumla cebinize girebilir.
2. **Korsanlığa Karşı Koruma (Kriptografik Güvenlik):** Ağırlıklar açıkta saklanmadığı için kimse yapay zekanın kodunu çalamaz. Koordinatı bilmeyen modeli çalıştıramaz.
3. **Işık Hızında Hesaplama (Optik Çipler):** Gelecekte bu fraktal desenler elektrikle değil, doğrudan ışık ve merceklerle hesaplanıp nanosaniyede sıfır elektrikle çalışabilir.

### Soru 5: "Peki bilgisayar her seferinde resmi hesaplarken yorulmaz mı?"
**Cevap:** Bugünün normal bilgisayarlarında evet, resmi çizmek biraz vakit alıyor. Ancak kuantum bilgisayarlar veya ışıkla çalışan optik çipler çıktığında bu hesaplamalar ışık hızında (sıfır bekleme süresiyle) gerçekleşecek. Biz bugünden o geleceğin yazılım mimarisini test ediyoruz!

### Soru 6: "Mandelbrot'ta kaç kapı çözebildiniz?"
**Cevap:** Mantık biliminin en temel 4 kapısını (VEYA, VE, TERS-VE, TERS-VEYA) ve hatta bilgisayar bilimcilerin 1969'da 'tek nöron bunu çözemez' dediği meşhur **XOR (Özel VEYA)** bulmacasını iki fraktal nöronu birbirine bağlayarak **%100 doğrulukla** çözdük!

### Soru 7: "Bunu dünyada başka yapan var mı?"
**Cevap:** Fraktalları yapay zekaya benzetmeye çalışanlar oldu; ancak bir Mandelbrot kümesini 128x128 piksellik 4 kadrana bölüp, oradaki siyah alan oranını doğrudan nöronun ağırlık matrisine bağlayarak XOR ve mantık kapılarını %100 çözen ilk deneysel çalışma bizimkidir!

---

## 5. Sunum Yaparken Kaçınılması ve Kullanılması Gereken Kelimeler

| ❌ KESİNLİKLE KULLANMAYIN (Kafaları Karıştırır) | ✅ BUNUN YERİNE KULLANIN (Hemen Anlaşılır) |
| :--- | :--- |
| Geriye Yayılım (Backpropagation) | "Hata yaparak öğrenme / İnce ayar" |
| Stokastik Gradyan İnişi (SGD) | "En iyi noktayı arama" |
| Hiperdüzlem / Non-Linear Separability | "Karar çizgisi / İki grubu birbirinden ayırmak" |
| Tensör Matris Çarpımı ($W \cdot x + b$) | "Tartıdaki ağırlıkların dengesi" |
| Lyapunov Kaotik Hassasiyeti | "Kelebek etkisi / Küçük bir kaymanın büyük sonucu" |
| İteratif Kuadratik Polinom | "Kendi kendini tekrarlayan sihirli kural" |

---

## 6. Canlı Sunum Senaryosu (5 Dakikalık Akış)

1. **Giriş (1. Dk):** `fraktal_noron_halk_arayuzu.html` uygulamasını büyük ekranda açın. "Bugün size ekran kartlarını ısıtmadan düşünen bir nöron göstereceğim" deyin.
2. **Girdileri Gösterin (2. Dk):** Akıllı kapı senaryosunu açın. "Kart Yok, Yüz Yok" yapın. Ekranda nöronun kırmızı söndüğünü ve kapının kilitli olduğunu gösterin.
3. **Fraktalı Açıklayın (3. Dk):** Ortadaki Mandelbrot görseline işaret edin. "Bu resmi tanıdınız mı? İşte bizim yapay zekamız tüm aklını bu resmin içindeki siyah adalardan alıyor" deyin.
4. **Tetikleyin (4. Dk):** Giriş Kartı butonuna basın ("VAR"). Kablolardan yeşil elektriğin aktığını, nöronun "ATEŞLENDİ!" diye parladığını ve kapının "AÇILDI 🟢" olduğunu gösterin.
5. **Kapanış & Vurgu (5. Dk):** "Gördüğünüz gibi bellekte tek bir sayı bile saklamadık. Yapay zekanın geleceği devasa veri merkezlerinde değil, doğanın kendi matematiksel desenlerinde saklı olabilir" diyerek bitirin.
"""

with open(md_path_art, "w", encoding="utf-8") as f:
    f.write(md_content)

with open(md_path_ws, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"[+] Halka Anlatım Markdown Rehberi oluşturuldu: {md_path_ws}")

# 2. GÖRSEL VE PDF BASKIYA UYGUN HTML REHBERİ
html_guide_path_ws = os.path.join(WORKSPACE_DIR, "Halka_Anlatim_Rehberi.html")
html_guide_path_art = os.path.join(ARTIFACT_DIR, "Halka_Anlatim_Rehberi.html")
pdf_guide_path_ws = os.path.join(WORKSPACE_DIR, "Halka_Anlatim_Rehberi.pdf")

html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fraktal Yapay Zekayı Halka Anlatım Rehberi</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    :root {{
      --primary: #4f46e5;
      --primary-dark: #3730a3;
      --text: #0f172a;
      --text-muted: #475569;
      --border: #e2e8f0;
      --card-bg: #f8fafc;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      color: var(--text);
      background-color: #f1f5f9;
      line-height: 1.65;
      font-size: 13.5px;
      -webkit-font-smoothing: antialiased;
    }}

    .container {{
      max-width: 960px;
      margin: 30px auto;
      background: #ffffff;
      padding: 50px 65px;
      border-radius: 16px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
      border: 1px solid var(--border);
    }}

    @media print {{
      body {{ background: #ffffff; font-size: 11.5px; }}
      .container {{ max-width: 100% !important; margin: 0 !important; padding: 0 !important; box-shadow: none !important; border: none !important; }}
      .no-print {{ display: none !important; }}
      .page-break {{ page-break-before: always; }}
      .avoid-break {{ page-break-inside: avoid; }}
      @page {{ size: A4; margin: 15mm; }}
    }}

    .top-bar {{
      display: flex; justify-content: space-between; align-items: center;
      background: #0f172a; color: white; padding: 16px 24px; border-radius: 12px; margin-bottom: 30px;
    }}
    .btn-pdf {{
      background: var(--primary); color: white; border: none; padding: 10px 20px;
      font-size: 13px; font-weight: 600; border-radius: 8px; cursor: pointer; display: inline-flex; align-items: center; gap: 8px;
    }}

    header {{ border-bottom: 2px solid var(--border); padding-bottom: 22px; margin-bottom: 30px; }}
    .badge {{
      display: inline-block; padding: 4px 12px; font-size: 11px; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.05em; border-radius: 9999px;
      background: #eef2ff; color: var(--primary); border: 1px solid #c7d2fe; margin-bottom: 12px;
    }}
    h1 {{ font-size: 24px; font-weight: 800; color: #0f172a; margin-bottom: 8px; }}
    .subtitle {{ font-size: 14px; color: var(--text-muted); }}

    section {{ margin-bottom: 32px; }}
    h2 {{
      font-size: 17px; font-weight: 700; color: #0f172a; margin-bottom: 14px;
      border-left: 4px solid var(--primary); padding-left: 10px;
    }}
    h3 {{ font-size: 14px; font-weight: 600; color: #1e293b; margin: 16px 0 8px 0; }}
    p {{ margin-bottom: 12px; color: #334155; }}

    .pitch-card {{
      background: #eef2ff; border-left: 5px solid var(--primary);
      padding: 18px 22px; border-radius: 0 12px 12px 0; margin: 16px 0; font-size: 13.5px;
      font-style: italic; color: #1e1b4b; line-height: 1.7;
    }}

    .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 16px 0; }}
    .metafor-card {{
      background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px;
      padding: 16px; font-size: 12px;
    }}
    .metafor-title {{ font-size: 13px; font-weight: 700; color: var(--primary); margin-bottom: 6px; }}

    .faq-item {{
      background: var(--card-bg); border: 1px solid var(--border); border-radius: 10px;
      padding: 14px 18px; margin-bottom: 12px;
    }}
    .faq-q {{ font-weight: 700; color: #0f172a; font-size: 13px; margin-bottom: 4px; }}
    .faq-a {{ color: #334155; font-size: 12.5px; line-height: 1.6; }}

    table {{ width: 100%; border-collapse: collapse; margin: 14px 0 20px 0; font-size: 12px; }}
    th, td {{ padding: 9px 12px; text-align: left; border: 1px solid var(--border); }}
    th {{ background: #f1f5f9; font-weight: 600; color: #334155; }}
    tr:nth-child(even) {{ background: #fafafa; }}
  </style>
</head>
<body>

<div class="container">

  <div class="top-bar no-print">
    <div>
      <h3 style="font-size: 14px; font-weight: 700;">🗣️ Halka ve Son Kullanıcıya Anlatım Rehberi</h3>
      <p style="font-size: 11px; color: #94a3b8;">Sıradan insanlara, yatırımcılara ve basına bu projeyi nasıl sunarsınız?</p>
    </div>
    <button class="btn-pdf" onclick="window.print()">
      PDF Olarak Kaydet / Yazdır
    </button>
  </div>

  <header>
    <div class="badge">İletişim & Sunum Rehberi</div>
    <h1>Fraktal Yapay Zekayı Halka Anlatım Rehberi</h1>
    <div class="subtitle">Teknik jargondan arındırılmış asansör konuşması, zihinde canlandırıcı metaforlar ve 7 zor soruya yanıtlar.</div>
  </header>

  <!-- 1. Asansör Konuşması -->
  <section class="avoid-break">
    <h2>1. 30 Saniyelik Asansör Konuşması (Elevator Pitch)</h2>
    <div class="pitch-card">
      "Bugünkü yapay zekalar (ChatGPT gibi) trilyonlarca sayıyı devasa bilgisayarlara ezberleterek çalışır; bu yüzden dev gibi enerji ve yüzlerce ekran kartı harcar.<br><br>
      Biz ise sayıları ezberlemek yerine, doğada ve matematikte kendiliğinden var olan sonsuz bir tabloya — Mandelbrot fraktalına — büyüteçle bakıyoruz. Fraktalın doğru köşesine baktığımızda oradaki karanlık adacıkların büyüklüğü, yapay nöronumuzun karar katsayısı oluyor. Hiçbir şeyi hafızada saklamadan, tek bir minik formülle çalışan bir yapay zeka beyni üretiyoruz!"
    </div>
  </section>

  <!-- 2. Üç Büyük Metafor -->
  <section class="avoid-break">
    <h2>2. Zihinde Canlandırıcı 3 Büyük Metafor</h2>
    <div class="grid-3">
      <div class="metafor-card">
        <div class="metafor-title">📖 1. Ansiklopedi vs. Dürbün</div>
        <p><strong>Klasik AI:</strong> Sırtında 1000 ciltlik dev bir ansiklopedi taşır. Her soru için sayfaları çevirir.</p>
        <p style="margin-top: 6px;"><strong>Bizimki:</strong> Sırtında hiçbir şey taşımaz; elinde sihirli bir dürbün vardır. Sonsuz fraktal halının doğru köşesine bakar ve desenden cevabı anında okur!</p>
      </div>

      <div class="metafor-card">
        <div class="metafor-title">🧬 2. DNA ve İnsan Hücresi</div>
        <p>İnsan beyninde 100 trilyon sinaps vardır ama insan DNA'sı bir flaş belleğin minik bir kısmı kadardır (~750 MB).</p>
        <p style="margin-top: 6px;">DNA her hücreyi tek tek çizmez; bir <em>özyinelemeli tohum kural</em> koyar ve o büyür. Mandelbrot da tek satırlık bir tohumdan ($z=z^2+c$) sonsuz bir evren doğurur!</p>
      </div>

      <div class="metafor-card">
        <div class="metafor-title">🔮 3. Çiçek Dürbünü (Kaleidoskop)</div>
        <p>Çiçek dürbününü hafifçe çevirdiğinizde içindeki cam kırıkları bambaşka muazzam simetrik şekillere bürünür.</p>
        <p style="margin-top: 6px;">Bizim zoom seviyesini değiştirmemiz de böyledir; hafifçe içeri daldığımızda nöron bambaşka bir mantığı (OR, AND, XOR) öğrenmiş olur.</p>
      </div>
    </div>
  </section>

  <!-- 3. Adım Adım Akış -->
  <section class="page-break avoid-break">
    <h2>3. 3 Adımda Fraktal Düşünce Akışı</h2>
    <ol style="margin-left: 20px; line-height: 1.7; color: #334155;">
      <li><strong>1. Girdi Gelir (Yapay Zekanın Gözleri):</strong> Örneğin akıllı kapıda kart okutuldu mu (1) ya da yüz tanındı mı (1)? Dış dünyadan gelen ham sinyallerdir.</li>
      <li><strong>2. Fraktal Aynasına Bakılır (Yapay Zekanın Hafızası):</strong> Ekranda açılan 128&times;128 Mandelbrot penceresindeki karanlık alanın büyüklüğü sayılır. Sol üst köşe kartın önemini, sağ üst köşe yüzün önemini, alt köşe ise eşik değerini belirler.</li>
      <li><strong>3. Nöron Ateşlenir (Yapay Zekanın Kararı):</strong> Toplam sinyal eşiği aşarsa nöron neon yeşil ışıkla parlar (ATEŞLENDİ!) ve kapı açılır!</li>
    </ol>
  </section>

  <!-- 4. FAQ -->
  <section class="avoid-break">
    <h2>4. Halkın Soracağı 7 Zor Soru ve Yanıtları (FAQ)</h2>

    <div class="faq-item">
      <div class="faq-q">S1: "Yani bilgisayar resme bakarak mı düşünüyor?"</div>
      <div class="faq-a">Evet! Klasik bilgisayarlar sayıları hafıza çiplerinde saklarken, biz geometrik bir şeklin içindeki siyah adacıkların büyüklüğünü karar ağırlığına dönüştürüyoruz. Resmin neresine ve ne kadar derinine baktığımız, kararın karakterini belirliyor.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q">S2: "Bu ChatGPT'den daha mı zeki?"</div>
      <div class="faq-a">Henüz değil. ChatGPT trilyonlarca kelime okumuş devasa bir kütüphanedir. Bizim yaptığımız şey ise hafızada neredeyse sıfır yer tutan tek bir akıllı beyin hücresi. Ancak gelecekte bu hücreleri yan yana koyarak devasa ama cep telefonuna sığan yeni nesil modeller yapılabilir.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q">S3: "Karanlık bölge ne alaka? Neden aydınlık yerler değil?"</div>
      <div class="faq-a">Mandelbrot kümesinde ortadaki siyah alan, denklemin sonsuza patlamayıp kendi içinde sakin ve dengede kaldığı yerdir. Matematiksel olarak 'istikrarı' temsil eder; bu yüzden nöronumuz için en güvenilir terazi ağırlığıdır.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q">S4: "Bunun insanlığa gerçek faydası ne olacak?"</div>
      <div class="faq-a">Üç devrim: <strong>(1) Sıfır Hafıza:</strong> Devasa yapay zeka modelleri küçük bir koordinat defteriyle cebinize sığar. <strong>(2) Kriptografik Güvenlik:</strong> Ağırlıklar açıkta saklanmadığı için çalınamaz veya kopyalanamaz. <strong>(3) Işık Hızında Çipler:</strong> Gelecekte optik ve kuantum çiplerle sıfır elektrik ve gecikmeyle çalışabilir.</div>
    </div>

    <div class="faq-item">
      <div class="faq-q">S5: "Mandelbrot ile hangi problemleri çözebildiniz?"</div>
      <div class="faq-a">Mantık biliminin tüm temel kapılarını (VEYA, VE, TERS-VE, TERS-VEYA) ve bilgisayar biliminde 'tek nöron bunu çözemez' denilen meşhur doğrusal olmayan <strong>XOR (Özel VEYA)</strong> bulmacasını 2 katmanlı fraktal ağımızla <strong>%100 doğrulukla</strong> çözdük!</div>
    </div>
  </section>

  <!-- 5. Dil Sözlüğü -->
  <section class="avoid-break">
    <h2>5. Sunum Dili Sözlüğü: Hangi Kelimelerden Kaçınmalı?</h2>
    <table>
      <thead>
        <tr>
          <th style="width: 50%;">❌ KESİNLİKLE KULLANMAYIN (Kafaları Karıştırır)</th>
          <th style="width: 50%;">✅ BUNUN YERİNE KULLANIN (Hemen Anlaşılır)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Geriye Yayılım (Backpropagation)</td>
          <td>"Hata yaparak öğrenme / İnce ayar"</td>
        </tr>
        <tr>
          <td>Stokastik Gradyan İnişi (SGD)</td>
          <td>"En iyi noktayı arama"</td>
        </tr>
        <tr>
          <td>Hiperdüzlem / Non-Linear Separability</td>
          <td>"Karar çizgisi / İki grubu birbirinden ayırmak"</td>
        </tr>
        <tr>
          <td>Tensör Matris Çarpımı (W &times; x + b)</td>
          <td>"Tartıdaki ağırlıkların dengesi"</td>
        </tr>
        <tr>
          <td>Lyapunov Kaotik Hassasiyeti</td>
          <td>"Kelebek etkisi / Küçük bir kaymanın büyük sonucu"</td>
        </tr>
        <tr>
          <td>İteratif Kuadratik Polinom</td>
          <td>"Kendi kendini tekrarlayan sihirli kural"</td>
        </tr>
      </tbody>
    </table>
  </section>

  <footer style="border-top: 1px solid var(--border); padding-top: 16px; margin-top: 30px; font-size: 11px; color: var(--text-muted); text-align: center;">
    Fraktal Yapay Zeka Halka Anlatım Rehberi &bull; 15 Eylül 2026
  </footer>

</div>

</body>
</html>
"""

with open(html_guide_path_ws, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(html_guide_path_art, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[+] Halka Anlatım HTML Rehberi oluşturuldu: {html_guide_path_ws}")

# PDF DERLEME
print("[*] Halka Anlatım Rehberi PDF formatına derleniyor...")
with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page()
    page.goto(f'file:///{os.path.abspath(html_guide_path_ws)}')
    page.pdf(
        path=pdf_guide_path_ws,
        format='A4',
        print_background=True,
        margin={'top': '14mm', 'bottom': '14mm', 'left': '12mm', 'right': '12mm'}
    )
    browser.close()

print(f"[+] Halka Anlatım Rehberi PDF Başarıyla Oluşturuldu: {pdf_guide_path_ws}")
print(f"    Boyut: {os.path.getsize(pdf_guide_path_ws) // 1024} KB")
