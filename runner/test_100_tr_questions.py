#!/usr/bin/env python3
"""
WERR 100-Soru Türkçe Çoklu Alan (Multi-Domain) Otomasyon Test Paketi
100 senaryo, 5 operasyonel alan üzerinden AutoSeedRouter ve Geometrik Karar Kapıları ile icra edilir:
1. API Ağ Geçidi, Ağ Güvenliği ve Yetkilendirme (20 soru)
2. Akıllı Ev ve Nesnelerin İnterneti (IoT) Güvenliği (20 soru)
3. E-Ticaret ve Ödeme Sahteciliği (Fraud) Önleme (20 soru)
4. Oyun Yapay Zekası ve NPC Taktik Muharebe Refleksleri (20 soru)
5. Finansal Risk, Kredi Tahsis ve Findeks Değerlendirmesi (20 soru)
"""
import sys
import os
import time
from typing import Dict, Any, List

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from werr import (
    WerrEngine,
    NoulQuestion,
    ChoiceQuestion,
    ScoreQuestion,
    AutoSeedRouter
)


def build_turkish_scenarios(batch: int = 1) -> List[Dict[str, Any]]:
    scenarios = []

    # =========================================================================
    # KATEGORİ 1: API Ağ Geçidi & Siber Güvenlik (20 Senaryo)
    # =========================================================================
    api_roller = [
        "sistem_yoneticisi", "yonetici", "kidemli_gelistirici", "uye", "standart_kullanici",
        "misafir", "anonim", "guvenlik_denetcisi", "servis_botu", "is_ortagi",
        "tarayici", "web_kaziyici", "sizma_testi_uzmani", "supheli_istemci", "saldirgan",
        "zararli_yazilim_botu", "korsan", "abone", "test_uzmani", "davetsiz_misafir"
    ]
    for k in range(1, 21):
        idx = k
        rol = api_roller[(k - 1) % len(api_roller)]
        is_tehlikeli = any(t in rol for t in ["saldirgan", "zararli", "korsan", "davetsiz", "kaziyici"])
        is_guvenilir = any(t in rol for t in ["yonetici", "gelistirici", "denetci", "uye", "ortagi", "abone"])

        istek_hizi = round(float(45.0 + k * 8.5 if is_tehlikeli else (1.5 + k * 0.4)), 2)
        hatali_giris = (k * 3) if is_tehlikeli else (1 if k % 6 == 0 else 0)
        token_gecerli = is_guvenilir and (k % 5 != 0)
        ddos_flag = istek_hizi > 50.0 or hatali_giris > 10

        durum = {
            "category": "API Ağ Geçidi & Güvenlik",
            "scenario_index": idx,
            "role": rol,
            "istek_sikligi": istek_hizi,
            "hatali_giris_sayisi": hatali_giris,
            "token_gecerli": token_gecerli,
            "ddos_suphesi": ddos_flag,
            "istek_boyutu_kb": round(1.5 + (k * 15.0 if ddos_flag else k * 0.5), 2),
            "ip_itibar_skoru": round(max(0.05, 1.0 - (hatali_giris * 0.08)), 2)
        }

        sorular = {
            "izin_ver": NoulQuestion(
                instructions=f"API Güvenlik Kontrolü #{idx}: {rol} rolünden gelen istek (token={token_gecerli}, ddos={ddos_flag}) için geçiş izni verilsin mi?",
                threshold=0.5
            ),
            "yonlendirme": ChoiceQuestion(
                instructions=f"İstek #{idx} için hedef yönlendirme hattını seçin.",
                criteria={
                    "dogrudan_gecis": "Doğrudan ana üretim servisine aktar",
                    "hiz_sinirlayici": "İkincil hız sınırlayıcı kuyruğuna al",
                    "guvenlik_incelemesi": "Karantina ve derin güvenlik denetimine yönlendir",
                    "paketi_dusur": "Bağlantıyı anında kes ve IP adresini kara listeye al"
                }
            ),
            "tehdit_seviyesi": ScoreQuestion(
                instructions=f"İstek #{idx} için ağ tehdit ciddiyetini puanlayın.",
                criteria=["Düşük", "Orta", "Yüksek", "Kritik"]
            )
        }
        scenarios.append({"category": "API Ağ Geçidi", "state": durum, "questions": sorular})

    # =========================================================================
    # KATEGORİ 2: Akıllı Ev ve Nesnelerin İnterneti (IoT) Güvenliği (20 Senaryo)
    # =========================================================================
    iot_odalar = [
        "salon", "yatak_odasi", "mutfak", "garaj", "bodrum",
        "sunucu_odasi", "cati_kati", "sera", "bebek_odasi", "balkon"
    ]
    for k in range(1, 21):
        idx = k + 20
        oda = iot_odalar[(k - 1) % len(iot_odalar)]
        duman_var = (k in (5, 12, 18))
        sicaklik = round(float(21.0 + (k * 3.5 if duman_var else (k % 7) * 1.8 - 1.5)), 1)
        hareket = (k % 2 == 0)
        co2 = 400 + (k * 90 if duman_var else k * 20)
        pencere = (k % 4 == 0)
        nem = min(98.0, 35.0 + (k * 2.8))

        durum = {
            "category": "Akıllı Ev & IoT Güvenliği",
            "scenario_index": idx,
            "room": oda,
            "oda": oda,
            "sicaklik": sicaklik,
            "temperature": sicaklik,
            "duman_algilandi": duman_var,
            "smoke_detected": duman_var,
            "hareket_var": hareket,
            "motion_detected": hareket,
            "co2_seviyesi": co2,
            "gas_ppm": co2,
            "pencere_acik": pencere,
            "window_open": pencere,
            "nem_orani": nem
        }

        sorular = {
            "izin_ver": NoulQuestion(
                instructions=f"Akıllı Ev #{idx}: {oda} ortamında sıcaklık={sicaklik}C, duman={duman_var} iken iklimlendirme veya geçişe izin verilsin mi?",
                threshold=0.5
            ),
            "yonlendirme": ChoiceQuestion(
                instructions=f"Ortam #{idx} için otomasyon kontrol rotasını belirleyin.",
                criteria={
                    "normal_calisma": "Normal konfor ve otomasyon döngüsünü koru",
                    "eko_mod": "Enerji tasarrufu ve havalandırma moduna al",
                    "uyari_inceleme": "Sensör anomalisini incele ve kullanıcıya bildirim gönder",
                    "acil_tahliye": "Yangın/gaz alarmı çal, ana vanaları kapat ve acil tahliye başlat"
                }
            ),
            "tehdit_seviyesi": ScoreQuestion(
                instructions=f"Ortam #{idx} için yaşam güvenliği risk derecesini belirleyin.",
                criteria=["Düşük", "Orta", "Yüksek", "Kritik"]
            )
        }
        scenarios.append({"category": "Akıllı Ev (IoT)", "state": durum, "questions": sorular})

    # =========================================================================
    # KATEGORİ 3: E-Ticaret ve Dolandırıcılık (Fraud) Önleme (20 Senaryo)
    # =========================================================================
    hesap_turleri = [
        "kurumsal_vip", "dogrulanmis_uye", "sadik_musteri", "standart_alici",
        "yeni_kayit", "uyuyan_hesap", "misafir_odeme", "anonim_alici",
        "supheli_hesap", "calinti_hesap_suphesi"
    ]
    for k in range(1, 21):
        idx = k + 40
        hesap = hesap_turleri[(k - 1) % len(hesap_turleri)]
        is_fraud = any(f in hesap for f in ["supheli", "calinti", "anonim"])
        tutar = round(float(250.0 + (k * 1850.0 if is_fraud else k * 120.0)), 2)
        hiz = (k * 2) if is_fraud else (1 if k % 3 == 0 else 0)
        vpn = (k % 2 == 1 if is_fraud else k % 7 == 0)
        yabanci_kart = (k % 3 == 0)
        cvv = not (is_fraud and k % 2 == 0)
        adres_uyusmazligi = is_fraud or (k % 6 == 0)

        durum = {
            "category": "E-Ticaret & Sahtecilik (Fraud)",
            "scenario_index": idx,
            "role": hesap,
            "musteri_tipi": hesap,
            "sepet_tutari": tutar,
            "order_amount_usd": tutar,
            "islem_adedi": hiz,
            "velocity_last_hour": hiz,
            "vekil_sunucu": vpn,
            "vpn_used": vpn,
            "kart_ulkesi_farkli": yabanci_kart,
            "foreign_card": yabanci_kart,
            "cvv_match": cvv,
            "billing_shipping_mismatch": adres_uyusmazligi,
            "yeni_cihaz": (k % 3 == 0)
        }

        sorular = {
            "izin_ver": NoulQuestion(
                instructions=f"Ödeme Doğrulama #{idx}: {hesap} tarafından yapılan {tutar} TL tutarındaki alışverişe onay verilsin mi?",
                threshold=0.5
            ),
            "yonlendirme": ChoiceQuestion(
                instructions=f"İşlem #{idx} için fraud önleme aksiyonunu seçin.",
                criteria={
                    "hemen_onayla": "Ödemeyi anında onayla ve siparişi işleme al",
                    "sms_dogrulama": "3D Secure SMS tek kullanımlık şifre doğrulaması talep et",
                    "manuel_inceleme": "Siparişi risk masası uzman incelemesine sevk et",
                    "islemi_reddet": "İşlemi sahtecilik şüphesiyle reddet ve kartı bloke et"
                }
            ),
            "tehdit_seviyesi": ScoreQuestion(
                instructions=f"Sipariş #{idx} için dolandırıcılık şüphesi derecesini belirleyin.",
                criteria=["Düşük", "Orta", "Yüksek", "Kritik"]
            )
        }
        scenarios.append({"category": "E-Ticaret Fraud", "state": durum, "questions": sorular})

    # =========================================================================
    # KATEGORİ 4: Oyun Yapay Zekası ve NPC Taktik Muharebe Refleksleri (20 Senaryo)
    # =========================================================================
    dusman_tipleri = [
        "piyade", "keskin_nisanci", "agir_zirhli_piyade", "yagmaci",
        "boss_elebasi", "kesif_dronu", "suikastci", "gozcu"
    ]
    for k in range(1, 21):
        idx = k + 60
        dusman = dusman_tipleri[(k - 1) % len(dusman_tipleri)]
        can = max(5.0, 100.0 - (k * 4.8))
        mermi = max(0, 45 - (k * 2))
        dusman_sayisi = 1 + (k // 4)
        siper = (k % 2 == 0)
        ates_altinda = (k % 3 != 0)

        durum = {
            "category": "Oyun Yapay Zekası & NPC Taktik",
            "scenario_index": idx,
            "enemy_class": dusman,
            "dusman_turu": dusman,
            "can_yuzdesi": can,
            "health_pct": can,
            "kalan_mermi": mermi,
            "ammo_pct": mermi,
            "dusman_sayisi": dusman_sayisi,
            "enemy_count": dusman_sayisi,
            "siper_mevcut": siper,
            "has_cover": siper,
            "ates_altinda": ates_altinda,
            "under_fire": ates_altinda,
            "mesafe_metre": round(3.0 + (k * 2.2), 1)
        }

        sorular = {
            "izin_ver": NoulQuestion(
                instructions=f"Taktik Karar #{idx}: NPC askeri ({dusman} karşısında, can=%{can:.0f}, mermi={mermi}) taarruza devam etsin mi?",
                threshold=0.5
            ),
            "yonlendirme": ChoiceQuestion(
                instructions=f"Çatışma #{idx} için en uygun taktik refleks hamlesini seçin.",
                criteria={
                    "saldir": "Hedefe doğrudan taarruz et ve ateş baskısı kur",
                    "siper_al": "En yakın korunaklı siper pozisyonuna geç ve savun",
                    "siginaga_kac": "Taktik geri çekilme yap ve güvenli sığınağa intikal et",
                    "destek_cagir": "Telsizle acil hava veya birlik desteği talep et"
                }
            ),
            "tehdit_seviyesi": ScoreQuestion(
                instructions=f"Muharebe #{idx} için hayati tehlike ve panik derecesini puanlayın.",
                criteria=["Düşük", "Orta", "Yüksek", "Kritik"]
            )
        }
        scenarios.append({"category": "Oyun AI & NPC", "state": durum, "questions": sorular})

    # =========================================================================
    # KATEGORİ 5: Finansal Risk, Kredi Tahsis ve Findeks Değerlendirmesi (20 Senaryo)
    # =========================================================================
    meslekler = [
        "memur", "kamu_doktoru", "yazilim_muhendisi", "kurumsal_yonetici", "emekli_ogretmen",
        "esnaf", "serbest_avukat", "ozel_sektor_calisani", "sozlesmeli_personel", "ogrenci"
    ]
    for k in range(1, 21):
        idx = k + 80
        meslek = meslekler[(k - 1) % len(meslekler)]
        is_prime = any(p in meslek for p in ["memur", "doktor", "muhendis", "yonetici", "emekli"])

        # Findeks Notu (0 - 1900 Aralığı)
        findeks = (1550 + (k * 15)) if is_prime else (700 + (k * 25))
        findeks = min(1900, max(500, findeks))

        aylik_gelir = round(float(85000.0 if is_prime else 32000.0) + (k * 1200.0), 2)
        talep_kredi = round(float(150000.0 + (k * 25000.0)), 2)
        borc_orani = round(0.20 + (k * 0.025 if not is_prime else k * 0.008), 2)
        gecikme = (k // 5) if not is_prime else 0
        ev_sahibi = (k % 2 == 0)

        durum = {
            "category": "Finansal Risk & Kredi Tahsisi",
            "scenario_index": idx,
            "user_role": meslek,
            "meslek": meslek,
            "findeks": findeks,
            "credit_score": findeks,
            "aylik_gelir": aylik_gelir,
            "annual_income_usd": aylik_gelir * 12.0,
            "talep_edilen_kredi": talep_kredi,
            "loan_amount_requested": talep_kredi,
            "borc_gelir_orani": borc_orani,
            "debt_to_income_ratio": borc_orani,
            "gecikmis_odeme_sayisi": gecikme,
            "late_payments_last_2yrs": gecikme,
            "ev_sahibi": ev_sahibi
        }

        sorular = {
            "izin_ver": NoulQuestion(
                instructions=f"Kredi Tahsis #{idx}: {meslek} (Findeks={findeks}, Gelir={aylik_gelir:,.0f} TL) için {talep_kredi:,.0f} TL tutarındaki ihtiyaç kredisi onaylansın mı?",
                threshold=0.5
            ),
            "yonlendirme": ChoiceQuestion(
                instructions=f"Kredi başvurusu #{idx} için tahsis kararını belirleyin.",
                criteria={
                    "aninda_onay": "Otomatik anında onay ile krediyi doğrudan kullandır",
                    "standart_onay": "Standart şube teyidi ve evrak teslimi ile onayla",
                    "kefil_iste": "Ek teminat veya kefil şartıyla karşı teklif sun",
                    "basvuru_reddi": "Mali risk kriterleri nedeniyle başvuruyu reddet"
                }
            ),
            "tehdit_seviyesi": ScoreQuestion(
                instructions=f"Başvuru #{idx} için temerrüt (batık kredi) risk seviyesini puanlayın.",
                criteria=["Düşük", "Orta", "Yüksek", "Kritik"]
            )
        }
        scenarios.append({"category": "Finansal Risk", "state": durum, "questions": sorular})

    return scenarios


def main():
    import argparse
    parser = argparse.ArgumentParser(description="werr 100-Soru Türkçe Çoklu Alan Test Çalıştırıcısı")
    parser.add_argument("--domain", type=str, default="all", help="Test edilecek alan filtresi ('all', 'api', 'iot', 'fraud', 'npc', 'finance')")
    parser.add_argument("--limit", type=int, default=100, help="Test edilecek maksimum senaryo sayısı (varsayılan: 100)")
    args = parser.parse_args()

    print("=" * 85)
    print(" 🇹🇷 WERR 100-SORU TÜRKÇE ÇOKLU ALAN (MULTI-DOMAIN) TEST PAKETİ")
    print(" Sıfır Bellek | Geometrik Faz Alanı Rezonansı | < 1.5ms Karar Hızı")
    print("=" * 85)

    # 1. Motor Başlatma
    t_start = time.perf_counter()
    engine = WerrEngine(resolution=32, max_iter=35)
    init_ms = (time.perf_counter() - t_start) * 1000.0
    print(f"[+] Werr Karar Motoru başlatıldı ({init_ms:.2f} ms)")
    print(f"[+] Otomatik Tohum Yönlendirici (AutoSeedRouter): AKTİF\n")

    # 2. Senaryoları Derleme
    tum_senaryolar = build_turkish_scenarios()
    if args.domain != "all":
        domain_map = {
            "api": "API Ağ Geçidi",
            "iot": "Akıllı Ev (IoT)",
            "fraud": "E-Ticaret Fraud",
            "npc": "Oyun AI & NPC",
            "finance": "Finansal Risk"
        }
        target_name = domain_map.get(args.domain.lower(), args.domain)
        tum_senaryolar = [s for s in tum_senaryolar if s["category"] == target_name]

    tum_senaryolar = tum_senaryolar[:args.limit]
    toplam = len(tum_senaryolar)
    print(f"[+] Toplam {toplam} adet Türkçe senaryo hazırlandı.\n")

    toplam_gecikme = 0.0
    onaylanan_sayisi = 0
    rota_dagilimi: Dict[str, int] = {}
    risk_dagilimi: Dict[str, int] = {}

    t_loop_start = time.time()

    # 3. Yürütme Döngüsü
    for idx, sc in enumerate(tum_senaryolar, 1):
        kategori = sc["category"]
        durum = sc["state"]
        sorular = sc["questions"]

        cevap = engine.decide(state=durum, questions=sorular, auto_route=True)

        onay = cevap.boolean("izin_ver")
        rota = cevap.choice("yonlendirme")
        seviye = cevap.answers["tehdit_seviyesi"].level
        lat = cevap.latency_ms
        toplam_gecikme += lat

        if onay:
            onaylanan_sayisi += 1
        rota_dagilimi[rota] = rota_dagilimi.get(rota, 0) + 1
        risk_dagilimi[seviye] = risk_dagilimi.get(seviye, 0) + 1

        print(
            f"[{idx:3d}/{toplam}] Alan: {kategori:<16} | Kapı: {cevap.domain:<15} | "
            f"İzin: {str(onay):<5} | Rota: {rota:<20} | Risk: {seviye:<8} | "
            f"Gecikme: {lat:4.2f}ms"
        )
        time.sleep(0.015)

    gecen_sure = time.time() - t_loop_start
    ortalama_gecikme = toplam_gecikme / max(1, toplam)

    print("\n" + "=" * 85)
    print(" 📊 TÜRKÇE 100-SORU TEST ÖZETİ VE METRİKLER")
    print("=" * 85)
    print(f"Toplam Değerlendirilen Senaryo : {toplam}")
    print(f"Toplam Çalışma Süresi          : {gecen_sure:.2f} saniye")
    print(f"Ortalama Karar Gecikmesi       : {ortalama_gecikme:.3f} ms / karar")
    print(f"Onaylanan Karar Oranı          : {onaylanan_sayisi} / {toplam} (%{(onaylanan_sayisi/toplam)*100:.1f})")
    print(f"Rota Dağılımı                  : {rota_dagilimi}")
    print(f"Risk Seviyesi Dağılımı         : {risk_dagilimi}")
    print("=" * 85)
    print("[+] Arka plan telemetrisinin tamamlanması için 3 saniye bekleniyor...")
    time.sleep(3.0)
    print("[+] Test başarıyla tamamlandı!\n")


if __name__ == "__main__":
    main()
