import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

"""
TÜRKPATENT Resmi Başvuru Paketi Üretici
Resmi Standartlarda 4 PDF Dokümanı ve 1 Bülten JPG'si üretir:
  1. TARIFNAME.pdf (Açıklama, referanslar, teknik detaylar)
  2. ISTEMLER.pdf (Koruma talep edilen bağımsız ve bağımlı teknik istemler)
  3. OZET.pdf (Resmi özet)
  4. RESIMLER.pdf (Şekil 1 - 7 resmi çizim sayfaları)
  5. bulten_resmi.jpg (Resmi Patent Bülteninde yayınlanacak Şekil 5)
"""

from playwright.sync_api import sync_playwright
from PIL import Image

OUT_DIR = os.path.abspath("turkpatent_hazirlik")
FIG_DIR = os.path.abspath("zenodo_preprint_package/figures")
os.makedirs(OUT_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. BÜLTEN RESMİ (JPG)
# -----------------------------------------------------------------------------
print("1. Bülten resmi (JPG) hazırlanıyor...")
fig5_png = os.path.join(FIG_DIR, "fig5_dual_brain_cybernetics.png")
bulten_jpg = os.path.join(OUT_DIR, "bulten_resmi.jpg")
im = Image.open(fig5_png).convert('RGB')
im.save(bulten_jpg, "JPEG", quality=95)
print(f"Bülten resmi hazır: {bulten_jpg}")

# -----------------------------------------------------------------------------
# HTML ŞABLONLARI
# -----------------------------------------------------------------------------
CSS_STYLE = """
<style>
    @page {
        size: A4 portrait;
        margin: 20mm 20mm 20mm 25mm; /* Sol 25mm, Diğerleri 20mm (TÜRKPATENT standardı) */
        @bottom-center {
            content: counter(page);
            font-family: 'Times New Roman', serif;
            font-size: 11pt;
        }
    }
    body {
        font-family: 'Times New Roman', Times, serif;
        font-size: 11pt;
        line-height: 1.5;
        color: #000000;
        margin: 0;
        padding: 0;
        text-align: justify;
    }
    h1 {
        font-size: 13pt;
        font-weight: bold;
        text-align: center;
        text-transform: uppercase;
        margin-bottom: 24px;
        line-height: 1.3;
    }
    h2 {
        font-size: 11pt;
        font-weight: bold;
        text-transform: uppercase;
        margin-top: 20px;
        margin-bottom: 8px;
        page-break-after: avoid;
    }
    p {
        margin-top: 0;
        margin-bottom: 10px;
        text-indent: 1.25cm; /* Patent paragrafları ilk satır girintili */
    }
    .no-indent {
        text-indent: 0;
    }
    .claim {
        margin-bottom: 14px;
        text-indent: 0;
        padding-left: 1.25cm;
        text-indent: -1.25cm;
    }
    .figure-container {
        page-break-after: always;
        text-align: center;
        padding-top: 40px;
    }
    .figure-container:last-child {
        page-break-after: avoid;
    }
    .figure-img {
        max-width: 90%;
        max-height: 650px;
        object-fit: contain;
    }
    .figure-title {
        font-size: 12pt;
        font-weight: bold;
        margin-top: 25px;
        text-transform: uppercase;
    }
</style>
"""

# =============================================================================
# DOKÜMAN 1: TARİFNAME
# =============================================================================
tarifname_html = f"""<!DOCTYPE html>
<html lang="tr">
<head><meta charset="UTF-8">{CSS_STYLE}</head>
<body>
<h1>TARİFNAME</h1>
<h1>YAPAY SİNİR AĞLARINDA SIFIR BELLEK AYAK İZİYLE YÖRÜNGE HATA DİNAMİKLERİ ÜZERİNDEN AĞIRLIK SENTEZLEYEN VE ADAPTİF BAĞIŞIKLIK KORUMALI HESAPLAMA SİSTEMİ VE YÖNTEMİ</h1>

<h2>Buluşun İlgili Olduğu Teknik Alan</h2>
<p>Bu buluş; derin yapay sinir ağları, makine öğrenmesi algoritmaları, sinirsel hesaplama işlemci mimarileri ve analog optik hesaplama alanları ile ilgilidir. Buluş özellikle; yapay sinir ağlarındaki sinaptik ağırlık matrislerinin fiziksel bellek birimlerinde (DRAM/SRAM) kalıcı olarak saklanması ihtiyacını ortadan kaldıran, ağırlıkları karmaşık düzlemdeki dinamik manifold yörüngelerinden gerçek zamanlı olarak geçici rezonanslar halinde sentezleyen, düşmanca duyusal saldırılara ve gürültüye karşı adaptif bağışıklık filtreleme maskesi kullanan bir hesaplama yöntemi ve bu yöntemi icra eden donanım sistemi ile ilgilidir.</p>

<h2>Tekniğin Bilinen Durumu (Önceki Teknik)</h2>
<p>Günümüz yapay zeka ve derin öğrenme modelleri (örneğin Transformer ve Büyük Dil Modelleri); milyarlarca veya trilyonlarca skaler ağırlık parametresinin silikon bellek çiplerinde (DRAM/HBM) statik kayan noktalı (floating-point) tensörler olarak saklanması esasına dayanmaktadır. Bu klasik mimari üç temel teknik darboğaz yaratmaktadır:</p>
<p>Birincisi; işlemci çekirdekleri (GPU/TPU) ile bellek birimleri arasında milyarlarca parametrenin sürekli taşınması sonucu ortaya çıkan Von Neumann bellek duvarı (Memory Wall) darboğazıdır. Modern yapay zeka veri merkezlerinde tüketilen elektrik enerjisinin %85'inden fazlası aritmetik işlem yapmaktan değil, statik ağırlık tensörlerinin bellek ile işlemci arasında fiziksel olarak taşınmasından kaynaklanmaktadır.</p>
<p>İkincisi; klasik optimizasyon yöntemlerinin (gradyan inişi) toplam hatayı sıfıra indirme (&Lscr; &rarr; 0) hedefidir. Dinamik sistemler ve denge-dışı termodinamik kuramına göre, bir sistemdeki tüm iç sapmaların ve gerilimlerin sıfırlanması termodinamik dengeye ve entropi ölümüne karşılık gelmektedir. Pratikte yapay sinir ağlarının kayıpları sıfıra zorlandığında aşırı düzleşme (over-smoothing), sentetik verilerle beslendiğinde geri dönülmez temsil çöküşü (model collapse) ve en ufak düşmanca gürültüde (adversarial perturbation) karar yüzeylerinin dağılması sorunları ortaya çıkmaktadır.</p>
<p>Üçüncüsü; biyolojik morfogenez ile yapay sistemler arasındaki yapısal çelişkidir. İnsan genomu yaklaşık 750 megabaytlık bir dijital bilgi içermesine rağmen 100 milyar nöron ve 100 trilyon sinapsın gelişimini yönetmektedir. Biyolojik canlılık hiçbir statik ağırlık tensörü saklamamakta; prosedürel ve özyinelemeli tohumlar üzerinden gerektiğinde fonksiyon üretmektedir.</p>

<h2>Buluşun Amacı ve Çözdüğü Teknik Problemler</h2>
<p>Buluşun temel amacı; yapay sinir ağlarında ağırlık matrislerini kalıcı olarak fiziksel bellekte saklama zorunluluğunu ortadan kaldıran, katman derinliğinden bağımsız olarak daima sabit O(1) = 24 byte bellek ayak iziyle çalışan bir ağırlık sentezleme sistemi geliştirmektir.</p>
<p>Buluşun diğer bir amacı; sistemi sıfır hata noktasına (statik dengeye) kilitlemek yerine, Mandelbrot parametre uzayı sınırında (&part;&Mscr;) homeostatik sınır sörfü yaparak modelin kaotik ıraksama ile temsil çöküşü arasında sürekli dinamik kalmasını sağlayan Yörünge Hata Dinamikleri kontrolcüsü sunmaktır.</p>
<p>Buluşun diğer bir amacı; konveks olmayan kayıp uzaylarındaki yerel gradyan tuzaklarından ve eyer noktalarından kurtulmak için memeli döllenmesindeki çinko kıvılcımı olgusundan esinlenen ağır kuyruklu Cauchy dağılımlı stokastik bir sıçrama operatörü (&Omega;<sub>tunneling</sub>) sağlamaktır.</p>
<p>Buluşun diğer bir amacı; duyusal akışlardan gelen ani dağılım dışı (OOD) gürültüleri ve düşmanca saldırı toksinlerini bastırarak merkezi koordinat tohumunu koruyan adaptif CD4+ regülatuvar T-hücresi bağışıklık filtreleme maskesi (M<sub>CD4</sub>) içeren bir Çift Beyin (kraniyal-enterik) sibernetik mimarisi sağlamaktır.</p>
<p>Buluşun nihai bir amacı ise; yöntemin dijital mikroişlemcilerin yanı sıra, uzaysal ışık modülatörleri (SLM) ve optik Fourier lensleri kullanan analog optik işlemcilerde ışık hızında (sub-nanosaniye) sıfır termal kayıpla icra edilebilmesini mümkün kılmaktır.</p>

<h2>Şekillerin Kısa Açıklaması</h2>
<p class="no-indent"><b>Şekil 1:</b> Buluş konusu parametre uzayı sınır geometrisi, kardioid cusp tekilliği, omuz dönüm locusları ve radyal kaçış akılarını gösteren şematik görünüm.</p>
<p class="no-indent"><b>Şekil 2:</b> Statik denge ölümü, korunumlu harmonik salınım ve tekillikte kırılan açık termodinamik bükük sinüs dalgasının morfofiziksel karşılaştırma grafikleri.</p>
<p class="no-indent"><b>Şekil 3:</b> Konveks olmayan potansiyel enerji bariyerini aşan ağır kuyruklu biyomimetik stokastik sıçrama operatörünün (tünelleme) prensip şeması.</p>
<p class="no-indent"><b>Şekil 4:</b> Dinamik faz uzayında iç hiperbolik çöküş, kaotik ıraksama patlaması ve aktif OED sınır sörfü limit döngüsü portresi.</p>
<p class="no-indent"><b>Şekil 5:</b> Merkezi/Kraniyal işlemci, Enterik duyusal işlemci ve aradaki adaptif CD4+ bağışıklık filtreleme maskesini içeren Çift Beyin sibernetik blok diyagramı.</p>
<p class="no-indent"><b>Şekil 6:</b> Karmaşık düzlemin 4 kadranının Adenin, Timin, Sitozin ve Guanin biyolojik bazlarına eşlenerek matris saklamaksızın ağırlık vektörü türetme geometrisi.</p>
<p class="no-indent"><b>Şekil 7:</b> 5 bağımsız tohumlu ampirik doğrulama deneyine ait kayıp yakınsaması, gürültü saldırısı dayanıklılığı ve sabit O(1) bellek ayak izi grafikleri.</p>

<h2>Şekillerdeki Referansların Listesi</h2>
<p class="no-indent"><b>(1)</b> Merkezi Koordinat Üreteci / Kraniyal İşlemci Birimi</p>
<p class="no-indent"><b>(2)</b> Yörünge Hata Dinamiği ve Homeostatik Sınır Kontrolcüsü</p>
<p class="no-indent"><b>(3)</b> Ağır Kuyruklu Biyomimetik Stokastik Sıçrama Operatörü (&Omega;<sub>tunneling</sub>)</p>
<p class="no-indent"><b>(4)</b> Enterik / Viseral Duyusal Akış İşlemcisi</p>
<p class="no-indent"><b>(5)</b> Adaptif CD4+ Regülatuvar Bağışıklık Filtreleme Maskesi (M<sub>CD4</sub>)</p>
<p class="no-indent"><b>(6)</b> 4-Kadran Genetik Ağırlık Ayrıştırıcı Birim</p>
<p class="no-indent"><b>(7)</b> Geçici Operasyonel Ağırlık Tamponu (O(1) = 24 Byte)</p>
<p class="no-indent"><b>(8)</b> Analog Optik Uzaysal Işık Modülatörü (SLM)</p>
<p class="no-indent"><b>(9)</b> 4f Optik Fourier Lensi</p>
<p class="no-indent"><b>(10)</b> Karanlık Havza CMOS Fotodedektör Dizisi</p>

<h2>Buluşun Ayrıntılı Açıklaması</h2>
<p>Buluş konusu yöntem ve sistem; bir yapay sinir ağının sinaptik ağırlıklarını fiziksel DRAM matrislerinde saklamak yerine, üç elemanlı kompakt bir parametre koordinat tohumu &Theta; = (c<sub>x</sub>, c<sub>y</sub>, &zeta;) &isin; &Ropf;<sup>3</sup> üzerinden prosedürel olarak üretir. Burada c = c<sub>x</sub> + i c<sub>y</sub> &isin; &Copf; karmaşık koordinatı, &zeta; ise yakınlaştırma (zoom) ölçeğini temsil etmektedir. Toplam kalıcı depolama ihtiyacı yalnızca 3 adet 64-bit kayan noktalı sayıdan ibaret olup tam olarak 24 byte'tır (O(1)).</p>
<p>İşlemci birimi (1), verilen &Theta; koordinatında karmaşık karesel polinom yinelemesini z<sub>n+1</sub> = z<sub>n</sub><sup>2</sup> + c (z<sub>0</sub> = 0) çalıştırır. Örnekleme alanı dört geometrik kadrana ayrılır: 1. Kadran (+Re, +Im), 2. Kadran (-Re, +Im), 3. Kadran (-Re, -Im) ve 4. Kadran (+Re, -Im). Ayrıştırıcı birim (6), kaçış yapmayan karanlık alanların kadranlara düşen kütle oranlarını R<sub>1</sub>, R<sub>2</sub>, R<sub>3</sub>, R<sub>4</sub> &isin; [0, 1] hesaplar. Bu oranlar biyolojik genetik bazlarla eşleştirilerek; w<sub>1</sub> = 2R<sub>1</sub> - 1 (Adenin / Uarıcı Ağırlık), w<sub>2</sub> = 2R<sub>2</sub> - 1 (Timin / İnhibitör Ağırlık), w<sub>3</sub> = 2R<sub>3</sub> - 1 (Sitozin / Çapraz Etkileşim) ve b = 2R<sub>4</sub> - 1 (Guanin / Sapma Değeri) olarak geçici ağırlık tamponuna (7) aktarılır.</p>
<p>Girdi vektörü üzerinde ileri yayılım hesabı yapıldıktan sonra toplam kayıp fonksiyonu hesaplanır: &Lscr;<sub>total</sub> = &Lscr;<sub>task</sub> + &lambda;<sub>orb</sub> &Lscr;<sub>orbital</sub>. Burada &Lscr;<sub>orbital</sub> = ((N<sub>esc</sub> - N*) / N*)<sup>2</sup> terimi, parametrelerin Mandelbrot kardioidinin analitik cusp noktası (c = 1/4) ve omuz locusları (0.25 &plusmn; 0.18i) etrafındaki sınır koridorunda kalmasını denetler. İleri ve geri yayılım tamamlandığı anda geçici ağırlıklar bellekten silinir; sistem daima 24 byte bellek durumuna geri döner.</p>
<p>Optimizasyon sırasında gradyan vektörünün normu belirlenen bir eşik değerin altına düştüğünde (&Vert;&nabla;<sub>&Theta;</sub> &Lscr;&Vert; &lt; &epsilon;<sub>tol</sub>) ve görev hatası sürdüğünde, gradyan durgunluğu tespit edilir. Bu anda sıçrama operatörü (3) devreye girerek parametre tohumuna ağır kuyruklu Cauchy dağılımından (&xi; ~ Cauchy(0, &gamma;)) türetilen bir tünelleme vektörü ekler (&Theta;<sub>t+1</sub> = &Theta;<sub>t</sub> + &Omega;<sub>tunneling</sub>). Bu işlem, yerel konveks olmayan potansiyel bariyerlerini aşarak global havzalara sıçramayı sağlar (Şekil 3).</p>
<p>Sistemin Çift Beyin mimarisinde (Şekil 5); merkezi işlemci (1) düşük frekanslı global parametre kararlarını üretirken, enterik duyusal işlemci (4) gerçek zamanlı yüksek frekanslı çevresel veri akışını işler. Düşmanca gürültülerin veya sensör şoklarının merkezi koordinatları bozmasını engellemek üzere adaptif CD4+ bağışıklık filtreleme maskesi (5) devreye girer: M<sub>CD4</sub> = 1 / [1 + exp(&alpha;(&verbar;&nabla;<sub>W</sub>&Lscr;<sub>visc</sub>&verbar; - &tau;))]. Filtrelenmiş gradyan (&Delta;W<sub>shielded</sub> = &nabla;&Lscr;<sub>visc</sub> &odot; M<sub>CD4</sub>), yalnızca tolere edilebilir seviyedeki adaptif düzeltmelerin merkezi modele yansımasına izin verir.</p>

<h2>Buluşun Sanayiye Uygulanma Biçimi</h2>
<p>Buluş konusu sistem ve yöntem; akıllı telefonlar, IoT uç bilişim (Edge AI) cihazları, mikrodenetleyiciler ve otonom araç içi çipler gibi bellek ve güç kısıtı bulunan her türlü dijital donanıma doğrudan uygulanabilir. Ayrıca uzaysal ışık modülatörü (8), Fourier lensi (9) ve fotodedektör dizisi (10) entegre edilerek ışık hızında çalışan ultra düşük enerjili analog optik yapay zeka işlemcilerine de entegre edilebilir.</p>
</body>
</html>
"""

# =============================================================================
# DOKÜMAN 2: İSTEMLER
# =============================================================================
istemler_html = f"""<!DOCTYPE html>
<html lang="tr">
<head><meta charset="UTF-8">{CSS_STYLE}</head>
<body>
<h1>İSTEMLER</h1>

<div class="claim">
<b>1.</b> Yapay sinir ağlarında sinaptik ağırlık matrislerini kalıcı bellekte saklamaksızın prosedürel olarak sentezleyen bir hesaplama yöntemi olup; özelliği;
<br>&bull; Bir merkezi koordinat üreteci (1) tarafından, üç boyutlu bir parametre koordinat tohumunun (&Theta; = (c<sub>x</sub>, c<sub>y</sub>, &zeta;)) belirlenmesi,
<br>&bull; Belirlenen söz konusu koordinat tohumu etrafında karmaşık karesel polinom yinelemesinin (z<sub>n+1</sub> = z<sub>n</sub><sup>2</sup> + c) çalıştırılarak karmaşık düzlem kütle dağılımının örneklenmesi,
<br>&bull; Örneklenen kütle dağılımının bir 4-kadran genetik ayrıştırıcı (6) aracılığıyla dört kadrana bölünerek her bir kadranın kaçış yapmayan kütle oranlarından (R<sub>1</sub>, R<sub>2</sub>, R<sub>3</sub>, R<sub>4</sub>) operasyonel ağırlık ve sapma vektörünün (W = [w<sub>1</sub>, w<sub>2</sub>, w<sub>3</sub>, b]<sup>T</sup>) geçici bir tamponda (7) sentezlenmesi,
<br>&bull; Sentezlenen söz konusu geçici ağırlık vektörü üzerinden yapay sinir ağı ileri yayılım işleminin icra edilmesi,
<br>&bull; İleri yayılım ve gradyan güncellemesi sonrasında söz konusu geçici ağırlık vektörünün bellekten silinerek kalıcı depolama ayak izinin daima sabit O(1) düzeyinde tutulması adımlarını içermesidir.
</div>

<div class="claim">
<b>2.</b> İstem 1'e göre bir yöntem olup, özelliği; söz konusu koordinat tohumunun (&Theta;) optimizasyonu sırasında, parametrelerin Mandelbrot kardioid sınırında (&part;&Mscr;) yer alan cusp tekilliği (c = 1/4) ve omuz dönüm locusları civarında kalmasını sağlayan ve Lyapunov üssünü sıfıra yakın tutarak homeostatik sınır sörfü yaptıran bir yörünge hata kontrolcüsü (2) içermesidir.
</div>

<div class="claim">
<b>3.</b> İstem 1'e göre bir yöntem olup, özelliği; optimizasyon sürecinde gradyan normunun belirlenen bir duraklama eşik değerinin altına düşmesi durumunda (&Vert;&nabla;<sub>&Theta;</sub> &Lscr;&Vert; &lt; &epsilon;<sub>tol</sub>), parametre tohumuna ağır kuyruklu Cauchy dağılımından (&Omega;<sub>tunneling</sub> ~ Cauchy(0, &gamma;)) türetilen bir sıçrama vektörünün eklendiği bir biyomimetik stokastik sıçrama operatörünün (3) tetiklenmesi adımıyla karakterize edilmesidir.
</div>

<div class="claim">
<b>4.</b> İstem 1'e göre bir yöntem olup, özelliği; gerçek zamanlı duyusal veri akışından (4) gelen gradyanları değerlendiren ve düşmanca gürültü veya dağılım dışı parazit durumlarında gradyan şiddetini sigmoid bir eşik fonksiyonu üzerinden sönümleyerek merkezi koordinat tohumunu koruyan bir adaptif CD4+ regülatuvar bağışıklık filtreleme maskesi (5) adımı içermesidir.
</div>

<div class="claim">
<b>5.</b> İstem 1'e göre bir yöntem olup, özelliği; söz konusu 4-kadran genetik ayrıştırıcı (6) adımında, 1. Kadranın Adenin bazına eşlenerek uyarıcı ağırlığı (w<sub>1</sub> = 2R<sub>1</sub> - 1), 2. Kadranın Timin bazına eşlenerek inhibitör ağırlığı (w<sub>2</sub> = 2R<sub>2</sub> - 1), 3. Kadranın Sitozin bazına eşlenerek çapraz etkileşim ağırlığını (w<sub>3</sub> = 2R<sub>3</sub> - 1) ve 4. Kadranın Guanin bazına eşlenerek sapma değerini (b = 2R<sub>4</sub> - 1) türetmesi adımıyla karakterize edilmesidir.
</div>

<div class="claim">
<b>6.</b> İstem 1'e göre bir yöntem olup, özelliği; söz konusu ağırlık sentezleme ve ileri yayılım işlemlerinin; koordinat tohumunu lazer dalga boyuna faz-kodlayan bir uzaysal ışık modülatörü (8), continuous 2D Fourier dönüşümü uygulayan bir 4f optik lensi (9) ve optik yoğunluğu sinaptik akıma dönüştüren bir karanlık havza fotodedektör dizisi (10) vasıtasıyla analog optik ortamda icra edilmesidir.
</div>

<div class="claim">
<b>7.</b> İstem 1 ila 6'daki yöntem adımlarını icra etmek üzere yapılandırılmış bir yapay sinir ağı hesaplama sistemi olup, özelliği;
<br>&bull; Üç elemanlı parametre koordinat tohumunu (&Theta;) saklayan bir merkezi işlemci birimi (1),
<br>&bull; Parametrelerin kardioid sınırında kalmasını sağlayan bir yörünge hata kontrolcüsü (2),
<br>&bull; Gradyan duraklamalarında devreye giren bir ağır kuyruklu stokastik sıçrama operatörü (3),
<br>&bull; Yüksek frekanslı duyusal akışları işleyen bir enterik işlemci (4),
<br>&bull; Duyusal gradyan şoklarını sönümleyen bir adaptif CD4+ bağışıklık filtreleme devresi (5),
<br>&bull; Karmaşık düzlem kütle oranlarını ağırlıklara dönüştüren bir 4-kadran ayrıştırıcı (6), ve
<br>&bull; İleri yayılım süresince ağırlıkları barındırıp işlem bittiğinde boşalan bir geçici ağırlık tamponu (7) ihtiva etmesidir.
</div>

<div class="claim">
<b>8.</b> Bir bilgisayar veya mikroişlemci tarafından çalıştırıldığında İstem 1 ila 5'teki yöntem adımlarının gerçekleştirilmesini sağlayan komutları içeren bilgisayar programı ürünüdür.
</div>

</body>
</html>
"""

# =============================================================================
# DOKÜMAN 3: ÖZET
# =============================================================================
ozet_html = f"""<!DOCTYPE html>
<html lang="tr">
<head><meta charset="UTF-8">{CSS_STYLE}</head>
<body>
<h1>ÖZET</h1>
<h1>YAPAY SİNİR AĞLARINDA SIFIR BELLEK AYAK İZİYLE YÖRÜNGE HATA DİNAMİKLERİ ÜZERİNDEN AĞIRLIK SENTEZLEYEN VE ADAPTİF BAĞIŞIKLIK KORUMALI HESAPLAMA SİSTEMİ VE YÖNTEMİ</h1>

<p>Bu buluş; derin yapay sinir ağlarında trilyonlarca parametrenin fiziksel bellekte (DRAM) statik olarak saklanmasından kaynaklanan Von Neumann bellek darboğazını, aşırı enerji tüketimini ve sıfır kayba zorlama neticesinde oluşan temsil çöküşünü ortadan kaldıran bir yapay sinir ağı ağırlık sentezleme yöntemi ve sistemidir. Buluş konusu sistem; sinaptik ağırlıkları kalıcı bellek matrisleri olarak saklamak yerine, karmaşık sayı düzlemindeki ikinci dereceden polinom yörüngesinden (z<sub>n+1</sub> = z<sub>n</sub><sup>2</sup> + c) türetilen geçici rezonanslar olarak gerçek zamanlı sentezlemektedir. Sistem; kardioid sınırında homeostatik sınır sörfü yaparak aşırı uyum çöküşünü engelleyen bir yörünge hata dinamiği kontrolcüsü, yerel gradyan tuzaklarını aşan ağır kuyruklu stokastik sıçrama operatörü, duyusal akışlardaki gürültü ve saldırıları süzerek merkezi koordinatları koruyan adaptif CD4+ regülatuvar bağışıklık filtreleme maskesi ve karmaşık düzlemin dört kadranını genetik bazlara eşleyen sıfır-depolamalı (O(1) = 24 byte) ağırlık projeksiyon mimarisini içermektedir.</p>
</body>
</html>
"""

# =============================================================================
# DOKÜMAN 4: RESİMLER (7 SAYFA)
# =============================================================================
def get_b64(path):
    import base64
    with open(path, 'rb') as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

resimler_html = f"""<!DOCTYPE html>
<html lang="tr">
<head><meta charset="UTF-8">{CSS_STYLE}</head>
<body>
<div class="figure-container">
    <img class="figure-img" src="{get_b64(os.path.join(FIG_DIR, 'fig1_observer_horizon.png'))}" />
    <div class="figure-title">ŞEKİL 1</div>
</div>
<div class="figure-container">
    <img class="figure-img" src="{get_b64(os.path.join(FIG_DIR, 'fig2_bent_sine_and_cusp.png'))}" />
    <div class="figure-title">ŞEKİL 2</div>
</div>
<div class="figure-container">
    <img class="figure-img" src="{get_b64(os.path.join(FIG_DIR, 'fig3_quantum_tunneling_operator.png'))}" />
    <div class="figure-title">ŞEKİL 3</div>
</div>
<div class="figure-container">
    <img class="figure-img" src="{get_b64(os.path.join(FIG_DIR, 'fig4_nonequilibrium_phase_surfing.png'))}" />
    <div class="figure-title">ŞEKİL 4</div>
</div>
<div class="figure-container">
    <img class="figure-img" src="{get_b64(os.path.join(FIG_DIR, 'fig5_dual_brain_cybernetics.png'))}" />
    <div class="figure-title">ŞEKİL 5</div>
</div>
<div class="figure-container">
    <img class="figure-img" src="{get_b64(os.path.join(FIG_DIR, 'fig6_complex_4quadrant_genetics.png'))}" />
    <div class="figure-title">ŞEKİL 6</div>
</div>
<div class="figure-container">
    <img class="figure-img" src="{get_b64(os.path.join(FIG_DIR, 'fig7_empirical_benchmark.png'))}" />
    <div class="figure-title">ŞEKİL 7</div>
</div>
</body>
</html>
"""

# =============================================================================
# PLAYWRIGHT İLE PDF'LERİ DERLEME
# =============================================================================
print("2. Playwright ile TÜRKPATENT PDF belgeleri derleniyor...")
docs = [
    ("TARIFNAME.pdf", tarifname_html),
    ("ISTEMLER.pdf", istemler_html),
    ("OZET.pdf", ozet_html),
    ("RESIMLER.pdf", resimler_html)
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for fname, html in docs:
        temp_html = os.path.join(OUT_DIR, f"temp_{fname}.html")
        pdf_path = os.path.join(OUT_DIR, fname)
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(html)
        
        page = browser.new_page()
        page.goto(f"file:///{temp_html.replace(chr(92), '/')}", wait_until="networkidle")
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
        )
        page.close()
        os.remove(temp_html)
        print(f"  Üretildi: {fname}")
    browser.close()

# Sayfa sayılarını kontrol et
import pypdf
print("\n--- TÜRKPATENT EPATS FORMU İÇİN RESMİ SAYFA VE İSTEM SAYILARI ---")
for fname in ["TARIFNAME.pdf", "ISTEMLER.pdf", "OZET.pdf", "RESIMLER.pdf"]:
    pdf_path = os.path.join(OUT_DIR, fname)
    reader = pypdf.PdfReader(pdf_path)
    print(f"  {fname}: {len(reader.pages)} Sayfa")

print("  Toplam İstem Sayısı: 8")
print("  Bülten Resmi Sırası: 5 (Şekil 5)")
print("------------------------------------------------------------------")
print("TÜRKPATENT PAKETİ HAZIR: " + OUT_DIR)
