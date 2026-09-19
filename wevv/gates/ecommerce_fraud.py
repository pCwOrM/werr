"""
wevv: E-Commerce Transaction Fraud & Carding Domain Gate
Calibrated for sub-millisecond payment authorization, card testing prevention, and velocity triage.
"""
from typing import Dict, Any, Tuple
import math
import hashlib
import numpy as np

from wevv.gates.base import DomainGate, normalize_text, safe_float


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
        "siparis", "sepet", "odeme", "dolandiricilik", "sahtecilik", "kart", "fatura", "islem"
    ]

    def project_state(self, state: Dict[str, Any]) -> Tuple[np.ndarray, float]:
        values = []
        net_risk = 0.0

        amount = safe_float(state.get("order_amount_usd", state.get("order_amount", state.get("amount", state.get("tutar", 0.0)))))
        velocity = safe_float(state.get("velocity_last_hour", state.get("velocity_1h", state.get("tx_count", state.get("islem_adedi", 0.0)))))
        is_proxy = state.get("vpn_used", state.get("is_proxy", state.get("is_vpn", state.get("vpn_proxy", False))))
        foreign = state.get("foreign_card", False)
        chargebacks = safe_float(state.get("chargeback_history", 0.0))
        mismatch = not state.get("billing_shipping_match", True) if "billing_shipping_match" in state else state.get("billing_shipping_mismatch", state.get("address_mismatch", False))
        cvv_valid = state.get("cvv_match", state.get("cvv_valid", True))
        account_age = safe_float(state.get("account_age_days", state.get("hesap_yasi", 100.0)), default=100.0)

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

        # 6. Customer Role & Trust Tier
        role_val = normalize_text(str(state.get("role", "")))
        if any(w in role_val for w in ["vip", "verified", "trusted", "member"]):
            net_risk -= 1.0
            values.append(-0.6)
        elif any(w in role_val for w in ["blacklisted", "fraud", "banned"]):
            net_risk += 3.5
            values.append(1.0)
        elif any(w in role_val for w in ["guest", "anonymous"]):
            net_risk += 0.5
            values.append(0.3)

        while len(values) < 4:
            values.append(0.0)

        return np.array(values[:4], dtype=np.float64), float(net_risk)
