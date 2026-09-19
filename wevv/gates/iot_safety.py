"""
wevv: IoT Life Safety & Industrial Hazard Domain Gate
Calibrated for sub-millisecond environmental hazard triage (smoke, fire, gas leaks, extreme temperature).
"""
from typing import Dict, Any, Tuple
import math
import hashlib
import numpy as np

from wevv.gates.base import DomainGate, normalize_text, safe_float


class IoTSafetyGate(DomainGate):
    name = "iot_safety"
    # Calibrated Boundary Coordinates for Critical Hazard Transition
    cx = -0.745
    cy = 0.112
    zoom = 85.0
    default_threshold = 0.50

    keywords = [
        "iot", "sensor", "temperature", "temp", "smoke", "gas", "co2", "fire", "leak",
        "hazard", "evacuate", "alarm", "thermostat", "hvac", "smart_home", "furnace",
        "sicaklik", "duman", "gaz", "yangin", "kacak", "tehlike", "alarm", "tahliye", "sensor"
    ]

    def project_state(self, state: Dict[str, Any]) -> Tuple[np.ndarray, float]:
        values = []
        net_risk = 0.0

        temp = safe_float(state.get("temp", state.get("temperature", state.get("temp_c", state.get("sicaklik", 22.0)))))
        smoke = state.get("smoke_detected", state.get("smoke", state.get("duman", False)))
        gas_ppm = safe_float(state.get("gas_ppm", state.get("co_ppm", state.get("gaz", 0.0))))
        water_leak = state.get("water_leak", state.get("leak", state.get("su_kacagi", False)))
        flame = state.get("flame_detected", state.get("fire", state.get("alev", False)))

        # 1. Temperature Anomaly
        if temp > 65.0 or temp < -15.0:
            net_risk += 3.0  # Acute fire or freezing emergency
            values.append(1.0)
        elif temp > 45.0:
            net_risk += 1.5  # Severe overheat
            values.append(0.6)
        elif temp > 35.0:
            net_risk += 0.5
            values.append(0.2)
        else:
            net_risk -= 0.5
            values.append(-0.5)

        # 2. Smoke & Flame Detection (Immediate life safety priority)
        if bool(smoke) or bool(flame):
            net_risk += 3.5
            values.append(1.0)
        else:
            values.append(-0.8)

        # 3. Toxic Gas / CO Concentration
        if gas_ppm > 400.0:
            net_risk += 3.0
            values.append(1.0)
        elif gas_ppm > 150.0:
            net_risk += 1.5
            values.append(0.5)
        elif gas_ppm > 50.0:
            net_risk += 0.5
            values.append(0.0)
        else:
            values.append(-0.8)

        # 4. Water Leak / Structural
        if bool(water_leak):
            net_risk += 2.0
            values.append(0.8)
        else:
            values.append(-0.5)

        while len(values) < 4:
            values.append(0.0)

        return np.array(values[:4], dtype=np.float64), float(net_risk)
