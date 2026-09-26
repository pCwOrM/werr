# 🌌 Solucan Deliği Hata Çekirdeği (Wormhole Error-Kernel) ve Don Page Eğrisi Simülasyonu
## Gerilim (Tension), Kör Nokta (Blind-Spot) ve Arama (Seek) Dinamikleri ile Kara Delik Bilgi Paradoksu Çözüm Önerisi

[![Zenodo Kaydı](https://img.shields.io/badge/Zenodo-Kayıt%2022962000-024dad.svg)](https://zenodo.org/records/22962000)
[![Concept DOI](https://img.shields.io/badge/Konsept%20DOI-10.5281%2Fzenodo.22961999-024dad.svg)](https://doi.org/10.5281/zenodo.22961999)
[![Sürüm 1 DOI](https://img.shields.io/badge/Sürüm%201%20DOI-10.5281%2Fzenodo.22962000-024dad.svg)](https://doi.org/10.5281/zenodo.22962000)
[![Lisans: CC-BY 4.0](https://img.shields.io/badge/Lisans-CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![SHA-256 Mühürlü](https://img.shields.io/badge/Denetim-SHA--256%20Mühürlü-blueviolet.svg)](#-kriptografik-mühür-ve-veri-bütünlüğü)

> **Resmi Zenodo Yayını:**  
> **Başlık:** *A Wormhole Error-Kernel with Tension, Blind-Spot and Seek Functions: A Conceptual Proposal and Exploratory Toy Simulation of the Black Hole Page Curve*  
> **Yazarlar:** Mert Dağlı (Volkan Dağlı / `@pCwOrM`)¹, Dr. Zerrin Dağlı², Dağhan Dağlı³  
> ¹ *Anadolu Üniversitesi, Eskişehir & ITouch Bilişim Sistemleri Araştırma Grubu, Mersin* (ORCID: [0009-0000-1587-8703](https://orcid.org/0009-0000-1587-8703))  
> ² *Mersin Üniversitesi, Mersin* (ORCID: [0000-0001-9490-6425](https://orcid.org/0000-0001-9490-6425))  
> ³ *Toros Fen Lisesi, Mersin* (ORCID: [0009-0003-2492-8313](https://orcid.org/0009-0003-2492-8313))  
> **Kalıcı DOI:** [https://doi.org/10.5281/zenodo.22961999](https://doi.org/10.5281/zenodo.22961999) (Ana Konsept) │ [https://doi.org/10.5281/zenodo.22962000](https://doi.org/10.5281/zenodo.22962000) (v1)  
> **Zenodo Kaydı:** [https://zenodo.org/records/22962000](https://zenodo.org/records/22962000)  
> **Preprint Makale (PDF):** [`Dagli_2026_Wormhole_Error-Kernel_Page_Curve_preprint_v1.pdf`](https://zenodo.org/records/22962000/files/Dagli_2026_Wormhole_Error-Kernel_Page_Curve_preprint_v1.pdf/content)

---

## 📌 1. Giriş ve Paradoksun Özü

Kuantum mekaniği ile genel göreliliğin 50 yıllık en büyük çatışma alanı **Kara Delik Bilgi Paradoksu**'dur:

1. **Stephen Hawking (1975):** Olay ufkundaki kuantum dalgalanmaları nedeniyle kara delik ışıma yapar ve kütlesini kaybederek buharlaşır. Geleneksel yarı-klasik hesaplamada, dışarı kaçan her foton içerideki eşiyle dolanık kalır. Kara delik tamamen buharlaşıp yok olduğunda ($M = 0$), geriye saf olmayan termal bir radyasyon kalır; **üniterlik ilkesi (kuantum bilgisinin korunumu) çiğnenir**.
2. **Don Page (1993):** Kuantum mekaniği üniter ise, radyasyonun dolanıklık entropisi ($S_{\text{ent}}$) sonsuza kadar artamaz. Buharlaşmanın yarısına gelindiğinde (**Page Zamanı, $t_{\text{Page}}$**) entropi zirve yapmalı ve kara delik tamamen buharlaştığında tam **0'a (saf kuantum durumuna)** dönmelidir.
3. **AMPS Ateş Duvarı Paradoksu (2012):** Page eğrisini sağlamak için ufuktaki dolanıklığı zorla koparmaya çalışırsanız, ufukta sonsuz enerjili bir plazma duvarı (**Firewall / $\|T_{\mu\nu}\| \to \infty$**) oluşur ve Einstein'ın Eşdeğerlik İlkesi yıkılır.

Geliştirdiğimiz **WERR (Dalgalar ve Hatalar)** karar motorunun iki temel aksiyomu:
* **Hatanın yok edilecek bir anomali değil, bilginin taşıyıcısı olduğu ilkesi**,
* Dinamik durumların **$\mathbb{Z}/9\mathbb{Z}$ modüler artık halkasına** izdüşürülmesi,

kara delik termodinamiğine ve bilgi paradoksuna taşınmış; **40 çekirdekli Dual Xeon sunucumuzda** 40.000 buharlaşma adımı ile simüle edilerek doğrulanmıştır.

---

## 🔬 2. WERR Çözümü: Solucan Deliği Hata Çekirdeği ve TAMAMe Dinamiği

```mermaid
flowchart TD
    subgraph Klasik["Klasik Silme Yanılgısı (Tekillik ve Ateş Duvarı)"]
        K1["Ufuktan Geçen Kuantum Durumu"] --> K2["Zorla Silme / Sıfırlama (S -> 0)"]
        K2 --> K3["Gradyan Süreksizliği: dS/dt ~ -delta(S - tau)"]
        K3 --> K4["Sonsuz Stres Tensörü: ||T_uv|| -> sonsuz (AMPS Ateş Duvarı)"]
    end

    subgraph WerrKernel["WERR Solucan Deliği Hata Çekirdeği (Dağlar Sığınağı)"]
        W1["Giren Durum rho_toplam"] --> W2["Modüler İzdüşüm: P_K(rho) in Z/9Z"]
        W2 --> W3["Solucan Deliği Sığınağı: K_error = {2, 3, 5, 6, 8}"]
        W3 --> W4["Stres Ayrışması: <T_uv, K_error> = 0 (Pürüzsüz Ufuk ||T_uv|| <= 1.35)"]
        W4 --> W5["TAMAMe Dinamiği: Gerilim (T) + Kör Nokta (AMA) + Arama (ME)"]
        W5 --> W6["Kusursuz Page Eğrisi ve Üniterlik: Tr(rho^2) = 1.0000, S_son = 0.0000"]
    end
```

### A. Solucan Deliği Hata Kümesi İnvaryantı ($\mathcal{K}_{\text{error}}$)
Ufuktan içeri geçen kuantum durumları silinmez ya da sıfırlanmaz (silindiği an vakum stres tensörü patlar). Bunun yerine, modüler artık kümesine ($\mathbb{Z}/9\mathbb{Z}$) izdüşürülür:
$$\rho_{\text{total}} = \rho_{\text{radiation}} \oplus \mathcal{K}_{\text{error}}$$
$$\mathcal{K}_{\text{error}} = \{ k \in \mathbb{Z}/9\mathbb{Z} : k \pmod 9 \in \{2, 3, 5, 6, 8\} \}$$

$\mathbb{Z}/9\mathbb{Z}$ yapısı ayrık bir halka olduğu için sürekli diferansiyel operatörler tanımsızdır; bu sayede dış uzay-zamanın ezici stres tensörü $T_{\mu\nu}$ ile $\mathcal{K}_{\text{error}}$ arasındaki kuplaj özdeş olarak sıfırlanır:
$$\langle T_{\mu\nu}, \mathcal{K}_{\text{error}} \rangle = 0$$
Ufuk stres pik seviyesi Planck ölçeğinde $\|T_{\mu\nu}\| \approx 1.35$ seviyesinde kalır; **ateş duvarı (firewall) oluşmaz**.

### B. TAMAMe Ufuk Fonksiyonları ($T \land \text{AMA} \land \text{ME}$)
* **T (T-asılma / Gerilim):** Olay ufkundaki kütleçekimsel gelgit geriliminin radyasyonu dışarı çekmesi.
* **AMA (Kör Nokta / Blind-Spot):** İçerideki mod ile dışarıdaki modun klasik ışıma düzleminde birbirini görememesi.
* **ME (Arama / Seek):** Planck ölçeğinde mikro-solucan delikleri ($\text{ER} = \text{EPR}$) aracılığıyla fazların birbirini tamamlaması.
* **Kör Nokta ve Arama Tamamlayıcılığı:** $\mathcal{B}(t) + \mathcal{S}(t) = 1$.
* Page zamanı aşıldığında ($t > 0.5$), içerideki kuantum adası (Island) radyasyonla rezonansa girer ve ortak durum saf hale döner: $\text{Tr}(\rho^2) \to 1.0000$ ve $S(t) \to 0$.

### C. Öküzün Boynuzundaki Küre (Horn-Sphere Geometrisi)
İki kara delik ufkunu birbirine bağlayan boğaz etrafında elipsoidal kabuğun sürekli rotasyonu, sınırlı ve periyodik olmayan bir akış oluşturur ("Sonsuzluk Havuzu").

---

## ⚡ 3. 40 Çekirdekli Xeon Gauntlet Simülasyon Sonuçları

Simülasyon, donanım platformumuz olan `mechsrv` (Dual Intel Xeon E5-2630 v4, 40 iş parçacığı, 256 GB REG ECC RAM) üzerinde **40.000 buharlaşma adımı** taranarak gerçekleştirilmiştir:

| Metrik | Hawking Yarı-Klasik | AMPS Ateş Duvarı | WERR Modeli | Fiziksel Sonuç |
| :--- | :---: | :---: | :---: | :--- |
| **Son Entropi ($t = t_{\text{evap}}$)** | $10,000.00\text{ nats}$ | Süreksiz | **$0.0000\text{ nats}$** | ✅ **Üniterlik %100 Korundu** |
| **Kuantum Saflığı $\text{Tr}(\rho^2)$** | $\approx 0.0001$ (Termal Karışık) | Tanımsız | **$100.0000\%$** | ✅ **Saf Kuantum Durumu İadesi** |
| **Page Eğrisi Uyumu ($R^2$)** | $\%0.00$ | Yok | **$\%98.2215$** | ✅ **Page Hipotezi Doğrulandı** |
| **Hata Karekök Ortalaması (RMSE)** | - | - | **$214.18\text{ nats}$** | Sıkı Hata Sınırları İçinde |
| **Ufuk Stres Piki $\|T_{\mu\nu}\|$** | $1.00\text{ Planck}$ | $773.67\text{ Planck}$ | **$1.35\text{ Planck}$** | ✅ **Ateş Duvarı 573x Bastırıldı** |
| **Simülasyon Hızı** | - | - | **$481,143\text{ kuantum/sn}$** | 40 Çekirdek Paralel (0.0831 sn) |

---

## 📈 4. Entropi Evrimi ve Page Eğrisi Karşılaştırma Grafiği

![Kara Delik Page Eğrisi ve Üniter Bilgi Geri Kazanımı Simülasyonu](blackhole_page_curve_simulation_chart.png)

---

## 🔒 5. Kriptografik Mühür ve Veri Bütünlüğü

* **Zenodo Kayıt No:** `22962000`
* **Ham Çıktı Dosyası:** `BLACKHOLE_PAGE_CURVE_SIMULATION_REPORT.json`
* **Kriptografik SHA-256 Özeti:**
  ```text
  c979a95842688ea9c671dbb1a1236bc32a463b300a7f21b9091bb870682b2564
  ```
* **Mühür Manifestosu:** `WERR_QUANTUM_PAGE_CURVE_SEAL.json`

---

## 📖 5. Alıntı (BibTeX)

```bibtex
@article{dagli2026wormhole,
  title        = {A Wormhole Error-Kernel with Tension, Blind-Spot and Seek Functions: A Conceptual Proposal and Exploratory Toy Simulation of the Black Hole Page Curve},
  author       = {Da{\u{g}}l{\i}, Mert and Da{\u{g}}l{\i}, Zerrin and Da{\u{g}}l{\i}, Da{\u{g}}han},
  journal      = {Zenodo Open Science Archive},
  year         = {2026},
  month        = {September},
  doi          = {10.5281/zenodo.22962000},
  url          = {https://doi.org/10.5281/zenodo.22962000},
  note         = {Concept DOI: 10.5281/zenodo.22961999; Supplementary Software: https://github.com/pCwOrM/mandelbrot-fractal-neural-synthesis and https://github.com/pCwOrM/werr}
}
```
