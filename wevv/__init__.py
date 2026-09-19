"""
wevv: Zero-Memory Fractal System-One Decision Engine
Open-source machine-native intuitive decision framework for software.
"""

from wevv.datatypes import (
    NoulQuestion,
    ChoiceQuestion,
    ScoreQuestion,
    NoulAnswer,
    ChoiceAnswer,
    ScoreAnswer,
    WevvResponse,
)
from wevv.engine import WevvEngine
from wevv.presets import (
    create_security_guard,
    create_smart_router,
    create_risk_evaluator,
)
from wevv.router import AutoSeedRouter
from wevv.gates import (
    DomainGate,
    DOMAIN_GATES,
    APISecurityGate,
    FinancialRiskGate,
    IoTSafetyGate,
    EcommerceFraudGate,
    GameCombatGate,
)

__version__ = "0.2.1"
__all__ = [
    "WevvEngine",
    "AutoSeedRouter",
    "DomainGate",
    "DOMAIN_GATES",
    "APISecurityGate",
    "FinancialRiskGate",
    "IoTSafetyGate",
    "EcommerceFraudGate",
    "GameCombatGate",
    "NoulQuestion",
    "ChoiceQuestion",
    "ScoreQuestion",
    "NoulAnswer",
    "ChoiceAnswer",
    "ScoreAnswer",
    "WevvResponse",
    "create_security_guard",
    "create_smart_router",
    "create_risk_evaluator",
]
