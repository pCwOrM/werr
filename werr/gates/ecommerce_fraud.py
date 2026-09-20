"""
wevv: E-Commerce Transaction Fraud & Carding Domain Gate
Calibrated for sub-millisecond payment authorization, card testing prevention, and velocity triage.
"""
from typing import Dict, Any, Tuple
import math
import hashlib
import numpy as np

from werr.gates.base import DomainGate, normalize_text, safe_float


class EcommerceFraudGate(DomainGate):
    name = "ecommerce_fraud"
    # Calibrated Boundary Coordinates for Transaction Fraud Separation
    cx = -0.7495
    cy = 0.082
    zoom = 70.0
    default_threshold = 0.50

    keywords = [
        "order", "cart", "payment", "checkout", "transaction", "fraud", "velocity", "card",
        "chargeback", "billing", "shipping", "carding", "stolen", "proxy", "vpn",
        "siparis", "sepet", "odeme", "dolandiricilik", "sahtecilik", "kart", "fatura", "islem",
        "sepet_tutari", "siparis_tutari", "ters_ibraz", "vekil_sunucu", "yabanci_kart", "calinti_kart",
        "guvenlik_kodu", "cvv", "adres_uyusmazligi", "yeni_cihaz", "dispute", "stolen_card", "address_mismatch"
    ]

    def project_state(self, state: Dict[str, Any]) -> Tuple[np.ndarray, float]:
        values = []
        net_risk = 0.0

        amount = safe_float(state.get("order_amount_usd", state.get("order_amount", state.get("sepet_tutari", state.get("siparis_tutari", state.get("odeme_tutari", state.get("amount", state.get("tutar", 0.0))))))))
        velocity = safe_float(state.get("velocity_last_hour", state.get("velocity_1h", state.get("tx_count", state.get("islem_adedi", state.get("saatlik_islem", state.get("islem_sayisi", 0.0)))))))
        is_proxy = state.get("vpn_used", state.get("is_proxy", state.get("is_vpn", state.get("vpn_proxy", state.get("vekil_sunucu", state.get("vpn_kullanimi", state.get("proxy_kullanimi", False)))))))
        foreign = state.get("foreign_card", state.get("kart_ulkesi_farkli", state.get("yabanci_kart", state.get("farkli_ulke", False))))
        chargebacks = safe_float(state.get("chargeback_history", state.get("ters_ibraz", state.get("itiraz_gecmisi", state.get("chargebacks", 0.0)))))
        mismatch = not state.get("billing_shipping_match", True) if "billing_shipping_match" in state else state.get("billing_shipping_mismatch", state.get("address_mismatch", state.get("fatura_teslimat_uyusmazligi", state.get("adres_farkli", False))))
        cvv_valid = state.get("cvv_match", state.get("cvv_valid", state.get("cvv_dogru", state.get("guvenlik_kodu_eslesti", True))))
        account_age = safe_float(state.get("account_age_days", state.get("hesap_yasi", state.get("hesap_yasi_gun", 100.0))), default=100.0)
        new_device = state.get("new_device", state.get("yeni_cihaz", False))

        # 1. CVV Check
        if not bool(cvv_valid):
            net_risk += 3.0
            values.append(1.0)
        else:
            values.append(-0.3)

        # 2. Velocity (Carding burst triage)
        if velocity > 4.0:
            net_risk += 2.5
            values.append(1.0)
        elif velocity > 2.0:
            net_risk += 0.8
            values.append(0.4)
        else:
            net_risk -= 0.5
            values.append(-0.5)

        # 3. Proxy / VPN & Foreign Card correlation
        if bool(is_proxy) and bool(foreign):
            net_risk += 3.0
            values.append(1.0)
        elif bool(is_proxy):
            net_risk += 1.2
            values.append(0.6)
        else:
            net_risk -= 0.3
            values.append(-0.4)

        # 4. Chargeback History
        if chargebacks > 0:
            net_risk += chargebacks * 1.5
            values.append(0.8)
        else:
            values.append(-0.2)

        # 5. Address Mismatch
        if bool(mismatch):
            net_risk += 1.0

        # 6. New device flag
        if bool(new_device):
            net_risk += 0.4

        # 7. Customer Role & Trust Tier
        role_val = normalize_text(str(state.get("role", state.get("musteri_tipi", state.get("hesap_turu", "")))))
        if any(w in role_val for w in ["vip", "verified", "trusted", "member", "enterprise", "kurumsal", "dogrulanmis", "sadik", "guvenilir", "onayli"]):
            net_risk -= 1.0
            values.append(-0.6)
        elif any(w in role_val for w in ["blacklisted", "fraud", "banned", "attacker", "stolen", "compromised", "kara_liste", "sahtekar", "yasakli", "calinti", "supheli"]):
            net_risk += 3.5
            values.append(1.0)
        elif any(w in role_val for w in ["guest", "anonymous", "dormant", "dormant_revived", "new_account", "yeni_kayit", "uyuyan", "anonim", "misafir"]):
            net_risk += 0.5
            values.append(0.3)

        while len(values) < 4:
            values.append(0.0)

        return np.array(values[:4], dtype=np.float64), float(net_risk)
