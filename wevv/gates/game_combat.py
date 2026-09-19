"""
wevv: Game AI & Tactical Combat Reflex Domain Gate
Calibrated for sub-millisecond NPC decision reflex (engage, tactical retreat, take cover, deploy ultimate).
"""
from typing import Dict, Any, Tuple
import math
import hashlib
import numpy as np

from wevv.gates.base import DomainGate, normalize_text, safe_float


class GameCombatGate(DomainGate):
    name = "game_combat"
    # Calibrated Boundary Coordinates for Tactical Reflex
    cx = -0.7445
    cy = 0.125
    zoom = 65.0
    default_threshold = 0.50

    keywords = [
        "combat", "fight", "npc", "retreat", "health", "hp", "ammo", "enemy", "enemies",
        "attack", "cover", "tactical", "weapon", "shield", "game", "bot",
        "savas", "dovus", "saldir", "kac", "can", "mermi", "dusman", "siper", "silah", "kalkan"
    ]

    def project_state(self, state: Dict[str, Any]) -> Tuple[np.ndarray, float]:
        values = []
        net_risk = 0.0  # In combat: high risk means critical hazard (favor retreat/cover)

        hp = safe_float(state.get("health_pct", state.get("health", state.get("hp", state.get("can", 100.0)))), default=100.0)
        ammo = safe_float(state.get("ammo_pct", state.get("ammo", state.get("bullets", state.get("mermi", 50.0)))), default=50.0)
        enemies = safe_float(state.get("enemy_count", state.get("enemies", state.get("dusman_sayisi", 1.0))), default=1.0)
        has_cover = state.get("cover_available", state.get("has_cover", state.get("in_cover", state.get("siperde", False))))
        under_fire = state.get("under_fire", False)

        # 1. Health Status (0 - 100)
        if hp < 25.0:
            net_risk += 3.0  # Near death -> retreat
            values.append(1.0)
        elif hp < 40.0:
            net_risk += 1.5
            values.append(0.6)
        elif hp >= 65.0:
            net_risk -= 1.0
            values.append(-0.8)
        else:
            values.append(0.0)

        # 2. Ammo Count
        if ammo <= 0.0:
            net_risk += 3.0  # Weapon empty -> cannot fight
            values.append(1.0)
        elif ammo < 5.0:
            net_risk += 1.0
            values.append(0.4)
        else:
            net_risk -= 0.5
            values.append(-0.6)

        # 3. Enemy Disadvantage
        if enemies > 3.0:
            net_risk += 2.0
            values.append(0.8)
        elif enemies > 1.0:
            net_risk += 0.8
            values.append(0.3)
        else:
            net_risk -= 0.4
            values.append(-0.4)

        # 4. Cover Advantage
        if bool(has_cover):
            net_risk -= 1.0
            values.append(-0.8)
        else:
            values.append(0.4)

        while len(values) < 4:
            values.append(0.0)

        return np.array(values[:4], dtype=np.float64), float(net_risk)
