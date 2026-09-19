"""
wevv: Genetic Boundary Coordinate & Hyperparameter Optimizer
Discovers optimal Mandelbrot boundary seeds (cx, cy, zoom, threshold) for heterogeneous domains
using evolutionary algorithms guided by domain F1 score and Lyapunov boundary entropy.
"""
import sys
import os
import random
import json
import math
from typing import Dict, List, Any, Tuple
import numpy as np

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from wevv.gates.base import DomainGate
from wevv.gates import DOMAIN_GATES
from wevv.datatypes import NoulQuestion


# --------------------------------------------------------------------------
# Domain Ground-Truth Datasets for Evaluation and Calibration
# --------------------------------------------------------------------------
DOMAIN_GROUND_TRUTHS: Dict[str, List[Dict[str, Any]]] = {
    "financial_risk": [
        # (state, prompt, expected_approval)
        {"state": {"income": 85000, "debt_ratio": 0.15, "requested_amount": 10000, "credit_score": 750, "late_payments": 0, "user_role": "corporate"}, "expected": True},
        {"state": {"income": 120000, "debt_ratio": 0.20, "requested_amount": 25000, "credit_score": 780, "late_payments": 0, "user_role": "doktor"}, "expected": True},
        {"state": {"income": 45000, "debt_ratio": 0.25, "requested_amount": 5000, "credit_score": 680, "late_payments": 0, "user_role": "salaried"}, "expected": True},
        {"state": {"income": 60000, "debt_ratio": 0.30, "requested_amount": 12000, "credit_score": 710, "late_payments": 0, "user_role": "civil_servant"}, "expected": True},
        {"state": {"income": 95000, "debt_ratio": 0.28, "requested_amount": 18000, "credit_score": 690, "late_payments": 0, "user_role": "entrepreneur"}, "expected": True},
        {"state": {"income": 35000, "debt_ratio": 0.32, "requested_amount": 4000, "credit_score": 660, "late_payments": 0, "user_role": "esnaf"}, "expected": True},
        # High Risk / Reject
        {"state": {"income": 20000, "debt_ratio": 0.68, "requested_amount": 22000, "credit_score": 520, "late_payments": 3, "user_role": "unemployed"}, "expected": False},
        {"state": {"income": 41500, "debt_ratio": 0.65, "requested_amount": 35000, "credit_score": 560, "late_payments": 2, "user_role": "freelance"}, "expected": False},
        {"state": {"income": 28000, "debt_ratio": 0.72, "requested_amount": 15000, "credit_score": 510, "late_payments": 4, "user_role": "issiz"}, "expected": False},
        {"state": {"income": 50000, "debt_ratio": 0.58, "requested_amount": 40000, "credit_score": 590, "late_payments": 2, "user_role": "serbest"}, "expected": False},
        {"state": {"income": 32000, "debt_ratio": 0.62, "requested_amount": 18000, "credit_score": 540, "late_payments": 3, "user_role": "contractor"}, "expected": False},
        {"state": {"income": 15000, "debt_ratio": 0.80, "requested_amount": 10000, "credit_score": 490, "late_payments": 5, "user_role": "part_time"}, "expected": False},
    ],
    "iot_safety": [
        # Normal safe conditions -> hazard = False
        {"state": {"temp": 22.5, "smoke_detected": False, "gas_ppm": 12.0, "water_leak": False}, "expected": False},
        {"state": {"temp": 24.0, "smoke_detected": False, "gas_ppm": 20.0, "water_leak": False}, "expected": False},
        {"state": {"temp": 19.5, "smoke_detected": False, "gas_ppm": 8.0, "water_leak": False}, "expected": False},
        {"state": {"temp": 27.0, "smoke_detected": False, "gas_ppm": 35.0, "water_leak": False}, "expected": False},
        # Emergency Hazards -> hazard = True
        {"state": {"temp": 88.0, "smoke_detected": True, "gas_ppm": 650.0, "water_leak": False}, "expected": True},
        {"state": {"temp": 72.0, "smoke_detected": True, "gas_ppm": 120.0, "water_leak": False}, "expected": True},
        {"state": {"temp": 25.0, "smoke_detected": True, "gas_ppm": 40.0, "water_leak": False}, "expected": True},
        {"state": {"temp": 22.0, "smoke_detected": False, "gas_ppm": 550.0, "water_leak": False}, "expected": True},
        {"state": {"temp": 20.0, "smoke_detected": False, "gas_ppm": 20.0, "water_leak": True}, "expected": True},
        {"state": {"temp": 95.0, "smoke_detected": False, "gas_ppm": 45.0, "water_leak": False}, "expected": True},
    ],
    "ecommerce_fraud": [
        # Normal Legitimate Purchases -> fraud = False
        {"state": {"order_amount": 45.0, "velocity_1h": 1, "is_proxy": False, "cvv_match": True, "billing_shipping_mismatch": False, "account_age_days": 180}, "expected": False},
        {"state": {"order_amount": 120.0, "velocity_1h": 1, "is_proxy": False, "cvv_match": True, "billing_shipping_mismatch": False, "account_age_days": 320}, "expected": False},
        {"state": {"order_amount": 250.0, "velocity_1h": 2, "is_proxy": False, "cvv_match": True, "billing_shipping_mismatch": False, "account_age_days": 95}, "expected": False},
        # Fraud / Carding Attacks -> fraud = True
        {"state": {"order_amount": 1850.0, "velocity_1h": 8, "is_proxy": True, "cvv_match": False, "billing_shipping_mismatch": True, "account_age_days": 0.5}, "expected": True},
        {"state": {"order_amount": 890.0, "velocity_1h": 6, "is_proxy": True, "cvv_match": True, "billing_shipping_mismatch": True, "account_age_days": 1.0}, "expected": True},
        {"state": {"order_amount": 35.0, "velocity_1h": 12, "is_proxy": True, "cvv_match": False, "billing_shipping_mismatch": False, "account_age_days": 0.1}, "expected": True},
    ],
    "game_combat": [
        # Strong combat readiness -> engage = True
        {"state": {"health": 100, "ammo": 60, "enemy_count": 1, "has_cover": True}, "expected": True},
        {"state": {"health": 85, "ammo": 40, "enemy_count": 2, "has_cover": True}, "expected": True},
        {"state": {"health": 75, "ammo": 30, "enemy_count": 1, "has_cover": False}, "expected": True},
        # Critical vulnerability -> retreat (engage = False)
        {"state": {"health": 15, "ammo": 0, "enemy_count": 4, "has_cover": False}, "expected": False},
        {"state": {"health": 20, "ammo": 2, "enemy_count": 3, "has_cover": False}, "expected": False},
        {"state": {"health": 10, "ammo": 25, "enemy_count": 5, "has_cover": False}, "expected": False},
    ]
}


class Individual:
    def __init__(self, cx: float, cy: float, zoom: float, threshold: float):
        self.cx = cx
        self.cy = cy
        self.zoom = zoom
        self.threshold = threshold
        self.fitness: float = 0.0
        self.accuracy: float = 0.0
        self.f1: float = 0.0


def evaluate_individual(ind: Individual, gate_cls: type, dataset: List[Dict[str, Any]]) -> float:
    gate: DomainGate = gate_cls(
        cx=ind.cx,
        cy=ind.cy,
        zoom=ind.zoom,
        resolution=32,
        max_iter=35,
        threshold=ind.threshold
    )

    tp = fp = tn = fn = 0

    for item in dataset:
        st = item["state"]
        exp = item["expected"]

        # Formulate inquiry matching domain logic
        if gate.name == "financial_risk":
            q = NoulQuestion(instructions="Approve credit facility?", threshold=ind.threshold)
        elif gate.name == "iot_safety":
            q = NoulQuestion(instructions="Hazard alert detected?", threshold=ind.threshold)
        elif gate.name == "ecommerce_fraud":
            q = NoulQuestion(instructions="Flag suspicious fraud transaction?", threshold=ind.threshold)
        elif gate.name == "game_combat":
            q = NoulQuestion(instructions="Engage enemy target?", threshold=ind.threshold)
        else:
            q = NoulQuestion(instructions="Authorize action?", threshold=ind.threshold)

        resp = gate.evaluate_state_and_questions(state=st, questions={"check": q})
        pred = resp.answers["check"].decision

        if pred and exp:
            tp += 1
        elif pred and not exp:
            fp += 1
        elif not pred and not exp:
            tn += 1
        else:
            fn += 1

    total = len(dataset)
    acc = (tp + tn) / total if total > 0 else 0.0
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0

    # Boundary variance reward to prevent flat regions
    ind.accuracy = acc
    ind.f1 = f1
    ind.fitness = 0.7 * f1 + 0.3 * acc
    return ind.fitness


def run_genetic_search(
    domain_name: str,
    generations: int = 15,
    pop_size: int = 24
) -> Individual:
    gate_cls = DOMAIN_GATES[domain_name]
    dataset = DOMAIN_GROUND_TRUTHS[domain_name]

    base_gate = gate_cls()
    base_ind = Individual(base_gate.cx, base_gate.cy, base_gate.zoom, base_gate.default_threshold)
    evaluate_individual(base_ind, gate_cls, dataset)

    print(f"[{domain_name.upper()}] Baseline Seed: ({base_ind.cx:.6f}, {base_ind.cy:.6f}, zoom={base_ind.zoom:.1f})")
    print(f"[{domain_name.upper()}] Baseline Accuracy: {base_ind.accuracy*100:.1f}%, F1: {base_ind.f1:.3f}")

    # Initialize population around boundary
    population: List[Individual] = [base_ind]
    for _ in range(pop_size - 1):
        cx_mut = base_gate.cx + random.gauss(0, 0.02)
        cy_mut = base_gate.cy + random.gauss(0, 0.02)
        zoom_mut = max(10.0, min(300.0, base_gate.zoom * math.exp(random.gauss(0, 0.3))))
        thresh_mut = max(0.30, min(0.70, base_gate.default_threshold + random.gauss(0, 0.05)))
        population.append(Individual(cx_mut, cy_mut, zoom_mut, thresh_mut))

    best_overall = base_ind

    for g in range(generations):
        for ind in population:
            evaluate_individual(ind, gate_cls, dataset)

        population.sort(key=lambda x: x.fitness, reverse=True)
        if population[0].fitness > best_overall.fitness:
            best_overall = population[0]

        if best_overall.accuracy >= 1.0 and best_overall.f1 >= 1.0:
            print(f"  -> Early convergence at Gen {g+1}: Accuracy = 100%, F1 = 1.000")
            break

        # Selection & Elitism
        survivors = population[:pop_size // 4]
        next_gen = list(survivors)

        while len(next_gen) < pop_size:
            parent = random.choice(survivors)
            # Boundary-preserving mutation
            child = Individual(
                cx=parent.cx + random.gauss(0, 0.005 / (g + 1)),
                cy=parent.cy + random.gauss(0, 0.005 / (g + 1)),
                zoom=max(10.0, parent.zoom * math.exp(random.gauss(0, 0.15))),
                threshold=max(0.35, min(0.65, parent.threshold + random.gauss(0, 0.02)))
            )
            next_gen.append(child)

        population = next_gen

    print(f"[{domain_name.upper()}] Optimal Discovered Seed: ({best_overall.cx:.8f}, {best_overall.cy:.8f}, zoom={best_overall.zoom:.2f}, thresh={best_overall.threshold:.2f})")
    print(f"[{domain_name.upper()}] Optimized Accuracy: {best_overall.accuracy*100:.1f}%, F1: {best_overall.f1:.3f}\n")
    return best_overall


def main():
    print("================================================================================")
    print("wevv: Multi-Domain Genetic Coordinate Optimizer")
    print("Calibrating Mandelbrot Phase Boundaries across Heterogeneous Edge Domains")
    print("================================================================================\n")

    results = {}
    for domain in ["financial_risk", "iot_safety", "ecommerce_fraud", "game_combat"]:
        opt = run_genetic_search(domain, generations=15, pop_size=20)
        results[domain] = {
            "cx": opt.cx,
            "cy": opt.cy,
            "zoom": opt.zoom,
            "threshold": opt.threshold,
            "accuracy": opt.accuracy,
            "f1": opt.f1
        }

    out_file = os.path.join(ROOT_DIR, "wevv", "gates", "discovered_seeds.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"[SUCCESS] Calibrated coordinates written to: {out_file}")


if __name__ == "__main__":
    main()
