"""
wevv.gates: Domain-specific System-One decision gates.
"""
from typing import Dict, Type
from wevv.gates.base import DomainGate, normalize_text
from wevv.gates.api_security import APISecurityGate
from wevv.gates.financial import FinancialRiskGate
from wevv.gates.iot_safety import IoTSafetyGate
from wevv.gates.ecommerce_fraud import EcommerceFraudGate
from wevv.gates.game_combat import GameCombatGate

DOMAIN_GATES: Dict[str, Type[DomainGate]] = {
    "api_security": APISecurityGate,
    "financial_risk": FinancialRiskGate,
    "iot_safety": IoTSafetyGate,
    "ecommerce_fraud": EcommerceFraudGate,
    "game_combat": GameCombatGate,
}

__all__ = [
    "DomainGate",
    "normalize_text",
    "APISecurityGate",
    "FinancialRiskGate",
    "IoTSafetyGate",
    "EcommerceFraudGate",
    "GameCombatGate",
    "DOMAIN_GATES",
]
