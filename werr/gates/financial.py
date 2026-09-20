"""
werr: Financial Underwriting & Credit Risk Domain Gate
Calibrated for sub-10ms credit approvals, loan underwriting, and default probability estimation.
"""
from typing import Dict, Any, Tuple
import math
import hashlib
import numpy as np

from werr.gates.base import DomainGate, normalize_text, safe_float


class FinancialRiskGate(DomainGate):
    name = "financial_risk"
    # Calibrated Boundary Coordinates for Financial Phase Transitions
    cx = -0.748
    cy = 0.065
    zoom = 60.0
    default_threshold = 0.50

    keywords = [
        "credit", "loan", "debt", "income", "borrower", "underwriting", "finance", "financial",
        "mortgage", "lender", "repayment", "default", "interest", "facility", "liquidity",
        "kredi", "borc", "gelir", "finans", "taksit", "odeme", "risk", "teminat", "limit",
        "findeks", "kredi_notu", "maas", "aylik_gelir", "ihtiyac_kredisi", "konut_kredisi",
        "tasit_kredisi", "kefil", "ipotek", "borclanma", "faiz", "subprime", "prime",
        "annual_income", "monthly_income", "debt_ratio", "collateral", "delinquency"
    ]

    def project_state(self, state: Dict[str, Any]) -> Tuple[np.ndarray, float]:
        employment_risks = {
            "civil_servant": -1.2, "government": -1.2, "kamu": -1.2, "memur": -1.2, "devlet": -1.2,
            "corporate": -0.8, "salaried": -0.7, "maasli": -0.7, "calisan": -0.7, "ozel_sektor": -0.7,
            "professional": -0.9, "doktor": -1.0, "doctor": -1.0, "muhendis": -0.8, "engineer": -0.8,
            "avukat": -0.8, "lawyer": -0.8, "ogretmen": -0.8, "teacher": -0.8,
            "executive": -1.0, "manager": -0.8, "consultant": -0.7,
            "pensioner": -0.6, "retired": -0.6, "emekli": -0.6,
            "entrepreneur": 0.2, "girisimci": 0.2, "freelance": 0.4, "serbest": 0.3, "serbest_meslek": 0.3,
            "contractor": 0.3, "esnaf": 0.2, "sozlesmeli": 0.2,
            "unemployed": 2.5, "issiz": 2.5, "part_time": 1.2, "ogrenci": 1.5, "student": 1.5, "stajyer": 1.0, "intern": 1.0
        }

        values = []
        net_risk = 0.0

        # Income extraction (supports annual income or monthly income normalized to annual)
        income = safe_float(state.get("annual_income_usd", state.get("annual_income", state.get("yillik_gelir", 0.0))))
        if income == 0.0:
            monthly_income = safe_float(state.get("income", state.get("gelir", state.get("aylik_gelir", state.get("maas", 0.0)))))
            if monthly_income > 0:
                income = monthly_income * 12.0 if monthly_income < 300000 else monthly_income

        debt_ratio = safe_float(state.get("debt_to_income_ratio", state.get("debt_ratio", state.get("borc_gelir_orani", state.get("borc_orani", state.get("dti", 0.0))))))
        requested = safe_float(state.get("loan_amount_requested", state.get("requested_amount", state.get("amount", state.get("talep_edilen_kredi", state.get("kredi_tutari", state.get("facility_amount", 0.0)))))))
        late_payments = safe_float(state.get("late_payments_last_2yrs", state.get("late_payments", state.get("gecikmis_odeme_sayisi", state.get("gecikme_adedi", state.get("gecikme", state.get("delinquencies", 0.0)))))))
        credit_score = safe_float(state.get("credit_score", state.get("findeks", state.get("findeks_notu", state.get("kredi_notu", state.get("fico", 0.0))))))
        homeowner = state.get("homeowner", state.get("ev_sahibi", state.get("mulk_durumu", False)))

        # 1. Debt-to-Income (DTI) evaluation (CFPB 36% rule)
        if debt_ratio > 0.0:
            if debt_ratio > 0.60:
                net_risk += 2.5
            elif debt_ratio > 0.45:
                net_risk += 1.2
            elif debt_ratio > 0.36:
                net_risk += 0.3
            else:
                net_risk -= 0.8
            values.append(min(1.0, max(-1.0, (debt_ratio - 0.35) * 2.5)))

        # 2. Leverage: Requested Amount / Annual Income
        if income > 0 and requested > 0:
            leverage = requested / income
            if leverage > 0.60:
                net_risk += 1.5
            elif leverage > 0.40:
                net_risk += 0.7
            elif leverage < 0.20:
                net_risk -= 0.6
            values.append(min(1.0, max(-1.0, (leverage - 0.3) * 2.0)))

        # 3. Delinquencies / Late Payments
        if late_payments > 0:
            net_risk += late_payments * 1.5
            values.append(min(1.0, late_payments * 0.5))
        else:
            net_risk -= 0.3
            values.append(-0.5)

        # 4. Credit Score (Dual Scale: Turkish Findeks 0-1900 vs Standard FICO 300-850)
        if credit_score > 0:
            if credit_score > 900.0:  # Findeks Scale (0 - 1900)
                if credit_score >= 1700:
                    net_risk -= 1.8  # Çok İyidir (Super Prime)
                elif credit_score >= 1500:
                    net_risk -= 1.2  # İyidir (Prime)
                elif credit_score >= 1200:
                    net_risk -= 0.3  # Az Riskli
                elif credit_score >= 950:
                    net_risk += 0.8  # Orta Riskli
                else:
                    net_risk += 2.2  # Yüksek Riskli
                values.append(min(1.0, max(-1.0, (credit_score - 1350.0) / 400.0)))
            else:  # Standard FICO Scale (300 - 850)
                if credit_score >= 740:
                    net_risk -= 1.5
                elif credit_score >= 670:
                    net_risk -= 0.6
                elif credit_score >= 620:
                    net_risk += 0.1
                elif credit_score >= 550:
                    net_risk += 1.2
                else:
                    net_risk += 2.5
                values.append(min(1.0, max(-1.0, (credit_score - 650.0) / 150.0)))

        # 5. Employment / Role
        role_val = normalize_text(str(state.get("user_role", state.get("employment", state.get("meslek", state.get("rol", ""))))))
        for r_key, r_risk in employment_risks.items():
            if r_key in role_val:
                net_risk += r_risk
                values.append(math.tanh(r_risk))
                break

        # 6. Asset / Homeownership collateral
        if bool(homeowner):
            net_risk -= 0.4
            values.append(-0.3)

        # Fallback padding
        while len(values) < 4:
            values.append(0.0)

        return np.array(values[:4], dtype=np.float64), float(net_risk)
