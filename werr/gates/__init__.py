"""
wevv.gates: Domain-specific System-One decision gates.
"""
from typing import Dict, Type
from werr.gates.base import DomainGate, normalize_text
from werr.gates.api_security import APISecurityGate
from werr.gates.financial import FinancialRiskGate
from werr.gates.iot_safety import IoTSafetyGate
from werr.gates.ecommerce_fraud import EcommerceFraudGate
from werr.gates.game_combat import GameCombatGate

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
