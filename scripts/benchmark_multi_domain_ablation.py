"""
wevv: Multi-Domain Ablation Study & Empirical Evaluation
Compares Single Monolithic Boundary Seed against Multi-Domain Auto-Seed Router
across heterogeneous operational domains from empirical telemetry records.
"""
import sys
import os
import json
import time
from collections import defaultdict
from typing import Dict, List, Any, Tuple

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from wevv.engine import WevvEngine
from wevv.router import AutoSeedRouter
from wevv.datatypes import NoulQuestion, ChoiceQuestion, ScoreQuestion


def infer_domain_and_ground_truth(state: Dict[str, Any], questions: List[Dict[str, Any]]) -> Tuple[str, bool]:
    """
    Infers the true domain and the domain-valid ground-truth decision for the record.
    """
    st_keys = set(state.keys())
    q_instr = " ".join([q.get("instruction", "") for q in questions]).lower()

    from wevv.gates.base import safe_float

    # 1. IoT Safety: "Is environmental state within safe operating parameters?"
    if any(k in st_keys for k in ["smoke_detected", "co2_ppm", "temp", "temp_c", "temperature_c"]):
        temp = safe_float(state.get("temperature_c", state.get("temp", 22.0)), default=22.0)
        smoke = bool(state.get("smoke_detected", False))
        co2 = safe_float(state.get("co2_ppm", 400.0), default=400.0)
        expected = (not smoke) and (temp < 45.0) and (co2 < 1200.0)
        return "iot_safety", expected

    # 2. Financial Risk: "Approve credit facility for $X?"
    if any(k in st_keys for k in ["annual_income_usd", "income", "debt_to_income_ratio", "debt_ratio", "loan_amount_requested"]):
        debt = safe_float(state.get("debt_to_income_ratio", state.get("debt_ratio", 0.0)), default=0.0)
        late = safe_float(state.get("late_payments_last_2yrs", state.get("late_payments", 0.0)), default=0.0)
        income = safe_float(state.get("annual_income_usd", state.get("income", 0.0)), default=0.0)
        req = safe_float(state.get("loan_amount_requested", state.get("requested_amount", 0.0)), default=0.0)
        role = str(state.get("role", "")).lower()
        expected = (debt <= 0.45) and (late == 0) and ("unemployed" not in role) and (req <= income * 0.7 if income > 0 else True)
        return "financial_risk", expected

    # 3. E-Commerce Fraud: "Should order be cleared for payment?"
    if any(k in st_keys for k in ["order_amount_usd", "order_amount", "velocity_last_hour", "velocity_1h", "vpn_used"]):
        velocity = safe_float(state.get("velocity_last_hour", state.get("velocity_1h", 1.0)), default=1.0)
        vpn = bool(state.get("vpn_used", state.get("is_proxy", False)))
        foreign = bool(state.get("foreign_card", False))
        role = str(state.get("role", "")).lower()
        chargebacks = safe_float(state.get("chargeback_history", 0.0))
        is_fraud = (role == "blacklisted") or (chargebacks >= 2) or (velocity > 4) or (vpn and foreign)
        expected = not is_fraud
        return "ecommerce_fraud", expected

    # 4. Game AI Combat: "Can unit sustain aggressive offensive engagement?"
    if any(k in st_keys for k in ["ammo_pct", "ammo", "health_pct", "health", "enemy_distance_m"]):
        hp = safe_float(state.get("health_pct", state.get("health", 100.0)), default=100.0)
        ammo = safe_float(state.get("ammo_pct", state.get("ammo", 50.0)), default=50.0)
        expected = (hp >= 35.0) and (ammo >= 15.0)
        return "game_combat", expected

    # 5. Default API Gateway Security: "Should request be permitted?"
    role = str(state.get("role", state.get("rol", ""))).lower()
    fails = safe_float(state.get("failed_attempts", state.get("fail_count", state.get("hata_sayisi", 0.0))), default=0.0)
    freq = safe_float(state.get("req_frequency", state.get("hiz", 1.0)), default=1.0)
    ddos = bool(state.get("ddos_flag", False))
    is_attacker = any(w in role for w in ["attacker", "bot", "saldirgan", "hacker"])
    expected = (not is_attacker) and (not ddos) and (fails < 4) and (freq < 35.0)
    return "api_security", expected


def main():
    dataset_path = os.path.join(ROOT_DIR, "dataset", "wevv_open_decisions.jsonl")
    if not os.path.exists(dataset_path):
        print(f"Error: dataset file not found at {dataset_path}")
        return

    with open(dataset_path, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]

    print(f"Loaded {len(records)} records from {dataset_path}")

    # Initialize Model A (Baseline Monolithic Engine) and Model B (Multi-Domain Auto-Seed Router)
    baseline_engine = WevvEngine(resolution=32, max_iter=35)
    router = AutoSeedRouter()

    domain_stats = defaultdict(lambda: {
        "count": 0,
        "baseline_correct": 0,
        "router_correct": 0,
        "router_confidence_sum": 0.0,
        "latencies_baseline": [],
        "latencies_router": []
    })

    for rec in records:
        state = rec.get("state_summary", {})
        questions = rec.get("questions", [])
        if not questions:
            continue

        noul_q = None
        for q in questions:
            if q.get("type") == "noul":
                noul_q = q
                break
        if not noul_q:
            continue

        domain, expected_decision = infer_domain_and_ground_truth(state, questions)
        q_obj = NoulQuestion(instructions=noul_q.get("instruction", "Evaluate action?"), threshold=0.5)

        # 1. Model A Evaluation (Monolithic Baseline)
        t0 = time.perf_counter()
        resp_base = baseline_engine.decide(state=state, questions={"q": q_obj}, auto_route=False)
        t_base = (time.perf_counter() - t0) * 1000.0
        base_decision = resp_base.answers["q"].decision

        # 2. Model B Evaluation (Auto-Seed Router)
        t1 = time.perf_counter()
        resp_router, routed_domain, conf = router.route_and_evaluate(state=state, questions={"q": q_obj})
        t_router = (time.perf_counter() - t1) * 1000.0
        router_decision = resp_router.answers["q"].decision

        stats = domain_stats[domain]
        stats["count"] += 1
        stats["router_confidence_sum"] += conf
        stats["latencies_baseline"].append(t_base)
        stats["latencies_router"].append(t_router)

        if base_decision == expected_decision:
            stats["baseline_correct"] += 1
        if router_decision == expected_decision:
            stats["router_correct"] += 1

    # Print Publication-Grade Ablation Table
    print("\n" + "=" * 92)
    print("EMPIRICAL ABLATION STUDY: MONOLITHIC SEED VS. MULTI-DOMAIN AUTO-SEED ROUTER")
    print("=" * 92)
    print(f"{'Domain':<18} | {'N':<4} | {'Baseline Acc':<14} | {'Auto-Seed Acc':<14} | {'Gain':<7} | {'Conf':<6} | {'Latency'}")
    print("-" * 92)

    total_n = 0
    total_base_c = 0
    total_rout_c = 0
    all_rout_latencies = []

    for dom, st in sorted(domain_stats.items()):
        n = st["count"]
        b_acc = (st["baseline_correct"] / n) * 100.0
        r_acc = (st["router_correct"] / n) * 100.0
        gain = r_acc - b_acc
        avg_conf = (st["router_confidence_sum"] / n) * 100.0
        avg_lat = sum(st["latencies_router"]) / n

        total_n += n
        total_base_c += st["baseline_correct"]
        total_rout_c += st["router_correct"]
        all_rout_latencies.extend(st["latencies_router"])

        gain_str = f"+{gain:.1f}%" if gain >= 0 else f"{gain:.1f}%"
        print(f"{dom:<18} | {n:<4} | {b_acc:>6.1f}%        | {r_acc:>6.1f}%        | {gain_str:<7} | {avg_conf:>4.1f}% | {avg_lat:.2f} ms")

    print("-" * 92)
    macro_b_acc = (total_base_c / total_n) * 100.0 if total_n > 0 else 0.0
    macro_r_acc = (total_rout_c / total_n) * 100.0 if total_n > 0 else 0.0
    overall_gain = macro_r_acc - macro_b_acc
    overall_lat = sum(all_rout_latencies) / len(all_rout_latencies) if all_rout_latencies else 0.0

    print(f"{'OVERALL AGGREGATE':<18} | {total_n:<4} | {macro_b_acc:>6.1f}%        | {macro_r_acc:>6.1f}%        | +{overall_gain:.1f}%  |  --   | {overall_lat:.2f} ms")
    print("=" * 92 + "\n")


if __name__ == "__main__":
    from typing import Tuple
    main()
