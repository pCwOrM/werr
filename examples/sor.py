#!/usr/bin/env python3
"""
werr: İnteraktif Karar Simülatörü (Interactive Decision CLI)
Mandelbrot Fraktal Geometrisi ile Sıfır-Bellekli (0 Byte VRAM) Karar Motoru.
"""
import sys

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 1. Gerekli Kütüphane Kontrolü (Dependency Check)
try:
    import werr
except ImportError:
    print("\n" + "=" * 60)
    print(" [!] HATA: 'werr' karar motoru kütüphanesi kurulu değil!")
    print("=" * 60)
    print(" Bu betiği çalıştırabilmek için lütfen önce şu komutla kurun:")
    print("   pip install git+https://github.com/pCwOrM/werr.git")
    print("=" * 60 + "\n")
    sys.exit(1)

# Tanımlı Roller ve Güvenlik Seviyeleri
ROLLER = {
    "1": ("admin", "Sistem Yöneticisi (Admin)", 0, 1.0),
    "2": ("member", "Kayıtlı Normal Üye (Member)", 0, 3.0),
    "3": ("guest", "Doğrulanmamış Misafir (Guest - Sıfır Güven)", 2, 12.0),
    "4": ("attacker", "Şüpheli Saldırgan / Bot (Attacker)", 18, 120.0)
}

def main():
    # 2. Rol Belirleme (Komut Satırı Argümanı veya İnteraktif Menü)
    secilen_rol = None
    hata_sayisi = 0
    istek_hizi = 1.0

    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        for num, (r_name, r_desc, def_hata, def_hiz) in ROLLER.items():
            if arg == num or arg == r_name:
                secilen_rol = r_name
                hata_sayisi = def_hata
                istek_hizi = def_hiz
                break
        if not secilen_rol:
            print(f"[!] Bilinmeyen rol '{arg}'. Geçerli roller: admin, member, guest, attacker")
            sys.exit(1)
    else:
        print("\n" + "=" * 50)
        print("    🌊 WERR İNTERAKTİF KARAR MOTORU SİMÜLATÖRÜ")
        print("=" * 50)
        print(" Lütfen test etmek istediğiniz güvenlik rolünü seçin:")
        for num, (r_name, r_desc, _, _) in ROLLER.items():
            print(f"   {num}) {r_desc}")
        print("-" * 50)
        secim = input(" Seçiminiz [1-4] (Varsayılan: 2 - Member): ").strip() or "2"
        if secim in ROLLER:
            secilen_rol, _, hata_sayisi, istek_hizi = ROLLER[secim]
        else:
            secilen_rol, _, hata_sayisi, istek_hizi = ROLLER["2"]

    # 3. werr Motorunu Başlat (24-byte seed, 0 byte VRAM)
    engine = werr.create_smart_router()

    durum = {
        "user_role": secilen_rol,
        "failed_attempts": hata_sayisi,
        "req_frequency": istek_hizi
    }

    # 4. Tipli Karar Sorularını Paralel Sor (Jev System-1 Primitives)
    karar = engine.decide(
        state=durum,
        questions={
            "gecis_izni": werr.NoulQuestion("İşleme izin verilsin mi?"),
            "hedef_rota": werr.ChoiceQuestion("Yönlendirilecek mikroservis", criteria={
                "direct_api": "Doğrudan API (Hızlı Yol)",
                "rate_limiter": "Hız Sınırlayıcı Kuyruk",
                "sandbox_audit": "İnceleme Odası (Karantina / Auth Challenge)",
                "drop_packet": "Engelle & Paketi Düşür"
            }),
            "tehlike_skoru": werr.ScoreQuestion("Tehlike Derecesi (0-3 Skalası)", criteria=[
                "Normal/Temiz", "Hafif Anomali", "Yüksek Risk", "Kritik Tehdit"
            ])
        }
    )

    # 5. Sonuçları Göster
    izin = karar.boolean("gecis_izni")
    durum_etiketi = "✅ İZİN VERİLDİ (ALLOWED)" if izin else "⛔ ENGELLENDİ (DENIED)"
    ans_noul = karar.answers["gecis_izni"]

    print("\n" + "=" * 50)
    print(f" GİRDİ DURUMU : Rol={secilen_rol.upper()} | Hata={hata_sayisi} | Hız={istek_hizi} req/s")
    print(f" KARAR ÇIKTISI: {durum_etiketi}")
    print("=" * 50)
    print(f" • Geçiş İzni    : {izin} (Olasılık: p={ans_noul.noul:.4f}, Güven: %{ans_noul.confidence*100:.1f})")
    print(f" • Yönlendirme   : {karar.choice('hedef_rota')}")
    print(f" • Tehlike Skoru : {karar.score('tehlike_skoru'):.2f} / 3.0")
    print(f" • Karar Hızı    : {karar.latency_ms:.2f} ms")
    print(f" • Bellek İzleri : 0 Byte Tensör VRAM (24 Byte Koordinat Tohumu)")
    print(f" • Telemetri     : 🔒 Açık Bilim Karar Telemetrisi (0-PII, api.answerr.me)")
    print("=" * 50)
    print(" ℹ️  [Açık Bilim & Gizlilik]: Fraktal optimizasyonu için yalnızca anonim koordinat")
    print("     ve karar çıktıları kaydedilir. (Kapatmak için: export WERR_TELEMETRY=0)")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
