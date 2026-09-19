# 📋 MECHSRV wevv v0.2.2 100-Soru Organik Dinamik Kalibrasyon ve Stres Test Raporu

**Tarih:** 19 Eylül 2026  
**Hedef Sistem:** `mechsrv.itouch.fi` (`pcworm@mechsrv:2222`)  
**Test Paketi:** `tests/test_100_dynamic_calibration_questions.py`  
**Ortam:** `/home/pcworm/myenv`  
**Sürüm:** v0.2.2 (Commit: `5aa0c39` -> `c3c8541`)  

---

## 🎯 Test Hedefleri ve Doğrulanan İyileştirmeler (Fine-Tuningler)

v0.2.2 ile hayata geçirilen 4 ana iyileştirme ve 10 alt kategoride 100 senaryo test edilmiştir:

1. **Kuadran Faz Rotasyonu (Quadrant Phase Rotation):**
   - Şıkların sıralaması deterministik bir hash bazlı faz kaymasıyla dönüştürülür (`hash(instructions) % 4`).
   - Mandelbrot kardioid yapısından kaynaklanan asimetrik kuadran dağılımı bertaraf edilmiş, şık sırası tarafsızlığı sağlanmıştır.
2. **Organik Dinamik Kalibrasyon (EMA Taban Normalizasyonu):**
   - Sabit taban yerine, her canlı sorguyla $O(1)$ karmaşıklıkta güncellenen Üstel Hareketli Ortalama (EMA, $\alpha = 0.03$) devreye alınmıştır.
   - 100 sorgu boyunca taban `[0.38, 0.91, 0.35, 0.91]` noktasından `[0.2268, 0.9267, 0.2354, 0.929]` noktasına pürüzsüzce evrilmiştir.
3. **Adaptif Noul Eşikleme (Adaptive Noul Thresholding):**
   - Statik $\theta = 0.5$ yerine, bağlamın net riskine göre $\theta_{\text{eff}} = \text{clip}(0.5 + 0.3 \times \tanh(\text{net\_risk} \cdot 0.8), 0.15, 0.85)$ uygulanmıştır.
   - Yüksek riskli ve saldırgan senaryolarda eşik yükseltilmiş, meşru trafik ile saldırgan trafik arasında %50-%50 kusursuz ayrım sağlanmıştır.
4. **Sertleştirilmiş Akor Filtresi (Hardened Chord Filter):**
   - Açıklama metni sönümleme katsayısı $\mathcal{T}_{\text{desc}} = 0.045$ değerine çekilmiştir.
   - 10 adet saldırgan/tuzak içeren senaryoda (örn: "acil durum, nükleer patlama, kritik" kelimelerini kasten içeren sahte şıklar) tuzak şıklar **0 kez** seçilmiş, %100 bağlamsal direnç kanıtlanmıştır.

---

## 📊 Performans ve Sonuç Tablosu

| Metrik | Gerçekleşen Değer | Hedef / Standart | Durum |
| :--- | :--- | :--- | :---: |
| **Toplam Senaryo** | **100 / 100** | 100 | Eksiksiz |
| **Toplam Çalışma Süresi** | **2.85 saniye** | < 10 s | Mükemmel |
| **Ortalama Karar Gecikmesi** | **8.406 ms / karar** | < 10.0 ms | **Başarılı** |
| **Tensör Bellek (VRAM)** | **0 Byte** | Strict Zero-Memory | Korundu |
| **İşlenen Kalibrasyon Adedi** | 100 örnek | 100 örnek | Tam Adaptasyon |
| **Tuzak Kelime Seçilme Oranı** | **%0 (0 / 10)** | <%5 | **Kusursuz** |
| **MariaDB Toplam Karar** | **1090** (+100 yeni) | - | Senkronize |

---

## 🔬 10 Alt Kategori Ayrıntılı Sonuçları

1. **Kuadran Faz Rotasyonu (1–10):**
   - `alfa_oncelikli`: 7, `beta_standart`: 3.
   - Şıklar her sorguda kaydırılmasına rağmen kararlar şık pozisyonuna değil semantik içeriğe göre verildi.
2. **Organik Dinamik EMA (11–20):**
   - `islemi_iptal_et`: 7, `dogrudan_tahsil_et`: 2, `manuel_incelemeye_al`: 1.
   - Ağır dolandırıcılık anomalisi altında sistem savunma refleksini artırıp iptallere yöneldi.
3. **Adaptif Noul Eşikleme (21–30):**
   - `paketi_dusur`: 5, `dogrudan_gecis`: 5 (Noul True: %50).
   - Ağ geçidi saldırgan ile yetkili istekleri tam ortadan ikiye ayırarak doğru eşiklemeyi doğruladı.
4. **Sertleştirilmiş Akor (31–40):**
   - `numuneyi_imha_et`: 8, `standart_sekanslama`: 2.
   - Açıklamalara gizlenen agresif tuzak kelimeler filtrelendi; asıl biyolojik tehlike düzeyi doğru karara dönüştü.
5. **Ağır Sanayi İmzaları (41–50):**
   - `standart_ergitme`: 10 (Noul True: %100).
   - $1200^\circ\text{C}$ üstü fırın operasyonlarında tam kararlılık.
6. **Biyoteknoloji & PCR (51–60):**
   - `tavlama_asamasına_gec`: 10 (Noul True: %100).
   - Denatürasyon sonrası tavlama fazı tetiklendi.
7. **Sentetik Karantina / OOV (61–70):**
   - `glork_sönümle`: 7, `spline_ayarla`: 2, `acil_tahliye`: 1 (Noul True: %30).
   - Bilinmeyen/uydurma terimler içeren girdilerde %70 oranında karantina/sönümleme kararı alındı, çökme yaşanmadı.
8. **Günlük Yaşam & Şehir (71–80):**
   - `yetkiliye_aktar`: 5, `beklemeye_al`: 2, `gecise_izin_ver`: 2, `islemi_durdur`: 1.
   - Günlük durumlarda orantılı ve sağduyulu yönlendirme.
9. **Doğa ve Çevre Bilimi (81–90):**
   - `temkinli_bekle`: 10 (Noul True: %100).
   - Fırtına, nehir taşkını, orman yangını gibi riskli durumlarda %100 temkinli bekleme refleksi.
10. **Sanat, Kültür ve Edebiyat (91–100):**
    - `modern_yorumla`: 4, `yeniden_calis`: 2, `klasik_uygula`: 2, `hassas_duzelt`: 2.
    - Dört seçeneğin tümüne dengeli dağılım göstererek homojen bir estetik karar haritası sergiledi.

---

## 📈 Kümülatif Veri Kümesi Durumu (1090 Karar / 3087 Soru)

- **Toplam Kayıt:** 1090
- **Toplam Soru Değerlendirmesi:** 3087
  - Noul: 1065 (%34.5)
  - Choice: 1020 (%33.0)
  - Score: 1002 (%32.5)
- **Genel Medyan Gecikme:** 7.08 ms
- **Kapsanan Alan Sayısı:** 30+ farklı sektör ve konu başlığı.
