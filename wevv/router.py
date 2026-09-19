"""
wevv: Semantic Intent Classifier & Auto-Seed Router
Routes incoming natural language prompts and environment states to the optimal
fractal boundary coordinate gate in < 0.1 ms with zero GPU tensors (O(1) memory).
"""
import time
from typing import Dict, List, Any, Optional, Union, Tuple
from wevv.gates import (
    DomainGate,
    DOMAIN_GATES,
    APISecurityGate,
    FinancialRiskGate,
    IoTSafetyGate,
    EcommerceFraudGate,
    GameCombatGate,
    normalize_text
)
from wevv.datatypes import NoulQuestion, ChoiceQuestion, ScoreQuestion


class AutoSeedRouter:
    """
    Sub-millisecond intent router that dynamically binds queries to domain coordinates.
    Employs an inverted semantic index over domain keywords and state variable signatures.
    """
    def __init__(self, default_domain: str = "api_security"):
        self.default_domain = default_domain
        self._gate_instances: Dict[str, DomainGate] = {
            name: cls() for name, cls in DOMAIN_GATES.items()
        }

        # Build reverse index for fast O(1) keyword lookup
        self._keyword_index: Dict[str, List[str]] = {}
        for d_name, gate in self._gate_instances.items():
            for kw in gate.keywords:
                n_kw = normalize_text(kw)
                if n_kw not in self._keyword_index:
                    self._keyword_index[n_kw] = []
                self._keyword_index[n_kw].append(d_name)

        # State key signatures that strongly suggest specific domains
        self._state_signatures: Dict[str, str] = {
            # Financial
            "debt_ratio": "financial_risk", "borc_orani": "financial_risk",
            "debt_to_income_ratio": "financial_risk", "annual_income_usd": "financial_risk",
            "loan_amount_requested": "financial_risk", "late_payments_last_2yrs": "financial_risk",
            "income": "financial_risk", "gelir": "financial_risk",
            "credit_score": "financial_risk", "kredi_notu": "financial_risk",
            "requested_amount": "financial_risk", "kredi_tutari": "financial_risk",
            "delinquencies": "financial_risk", "late_payments": "financial_risk",
            # IoT Safety
            "smoke_detected": "iot_safety", "duman": "iot_safety",
            "gas_ppm": "iot_safety", "co_ppm": "iot_safety", "co2_ppm": "iot_safety", "gaz": "iot_safety",
            "water_leak": "iot_safety", "su_kacagi": "iot_safety",
            "temp_c": "iot_safety", "temperature_c": "iot_safety", "temperature": "iot_safety",
            "humidity_pct": "iot_safety",
            # E-Commerce Fraud
            "order_amount": "ecommerce_fraud", "order_amount_usd": "ecommerce_fraud", "sepet_tutari": "ecommerce_fraud",
            "velocity_1h": "ecommerce_fraud", "velocity_last_hour": "ecommerce_fraud",
            "cvv_match": "ecommerce_fraud", "vpn_used": "ecommerce_fraud", "foreign_card": "ecommerce_fraud",
            "billing_shipping_match": "ecommerce_fraud", "billing_shipping_mismatch": "ecommerce_fraud", "is_proxy": "ecommerce_fraud",
            # Game Combat
            "ammo": "game_combat", "ammo_pct": "game_combat", "bullets": "game_combat", "mermi": "game_combat",
            "health_pct": "game_combat", "enemy_distance_m": "game_combat", "cover_available": "game_combat",
            "enemy_count": "game_combat", "dusman_sayisi": "game_combat",
            "has_cover": "game_combat", "siperde": "game_combat",
            # API Security
            "client_ip": "api_security", "req_frequency": "api_security",
            "failed_attempts": "api_security", "ddos_flag": "api_security", "ip_reputation_score": "api_security",
            "auth_token": "api_security", "endpoint": "api_security"
        }

    def detect_domain(
        self,
        query: Union[str, Dict[str, Any], None] = None,
        state: Optional[Dict[str, Any]] = None
    ) -> Tuple[str, float, List[str]]:
        """
        Determines the target domain with confidence and matched signal tokens.
        Latency: < 0.05 ms.
        """
        scores: Dict[str, float] = {d: 0.0 for d in self._gate_instances}
        matched_tokens: List[str] = []

        # 1. Explicit domain / category metadata (weight: 5.0)
        if state and isinstance(state, dict) and "category" in state:
            c_norm = normalize_text(str(state["category"]))
            if "iot" in c_norm or "smart" in c_norm:
                scores["iot_safety"] += 5.0
                matched_tokens.append(f"cat:{state['category']}")
            elif "finan" in c_norm or "credit" in c_norm or "loan" in c_norm:
                scores["financial_risk"] += 5.0
                matched_tokens.append(f"cat:{state['category']}")
            elif "fraud" in c_norm or "commerce" in c_norm:
                scores["ecommerce_fraud"] += 5.0
                matched_tokens.append(f"cat:{state['category']}")
            elif "game" in c_norm or "combat" in c_norm:
                scores["game_combat"] += 5.0
                matched_tokens.append(f"cat:{state['category']}")
            elif "api" in c_norm or "sec" in c_norm or "gateway" in c_norm:
                scores["api_security"] += 5.0
                matched_tokens.append(f"cat:{state['category']}")

        # 2. State variable signature inspection (weight: 2.5 per match)
        if state and isinstance(state, dict):
            for k in state.keys():
                kl = normalize_text(k)
                if kl in self._state_signatures:
                    target = self._state_signatures[kl]
                    scores[target] += 2.5
                    matched_tokens.append(f"state:{k}")
                # check partial match
                for sig, target in self._state_signatures.items():
                    if sig in kl:
                        scores[target] += 1.5
                        matched_tokens.append(f"state_partial:{k}")
                        break

        # 2. Text query / instructions tokenization
        text_content = ""
        if isinstance(query, str):
            text_content = query
        elif isinstance(query, dict):
            for v in query.values():
                if isinstance(v, (NoulQuestion, ChoiceQuestion, ScoreQuestion)):
                    text_content += " " + str(v.instructions)
                elif isinstance(v, str):
                    text_content += " " + v

        if text_content:
            norm_text = normalize_text(text_content)
            tokens = [t.strip('?,.!;:') for t in norm_text.split() if len(t) > 2]
            for tok in tokens:
                if tok in self._keyword_index:
                    for d_name in self._keyword_index[tok]:
                        scores[d_name] += 1.0
                        matched_tokens.append(f"kw:{tok}")

        # Find domain with highest score
        best_domain = self.default_domain
        max_score = 0.0
        for d_name, sc in scores.items():
            if sc > max_score:
                max_score = sc
                best_domain = d_name

        total_score = sum(scores.values())
        confidence = float(max_score / total_score) if total_score > 0 else 0.5

        return best_domain, round(confidence, 3), matched_tokens

    def get_gate(self, domain_name: str) -> DomainGate:
        """Retrieves gate instance by name (or default if unknown)."""
        return self._gate_instances.get(domain_name, self._gate_instances[self.default_domain])

    def route_and_evaluate(
        self,
        state: Dict[str, Any],
        questions: Dict[str, Union[NoulQuestion, ChoiceQuestion, ScoreQuestion]],
        preferred_domain: Optional[str] = None
    ) -> Tuple[Any, str, float]:
        """
        Routes the request to the optimal domain gate and evaluates it in a single pass.
        Returns: (WevvResponse, domain_name, routing_confidence)
        """
        if preferred_domain and preferred_domain in self._gate_instances:
            domain = preferred_domain
            confidence = 1.0
        else:
            domain, confidence, _ = self.detect_domain(query=questions, state=state)

        gate = self.get_gate(domain)
        response = gate.evaluate_state_and_questions(state=state, questions=questions)
        response.domain = domain
        return response, domain, confidence
