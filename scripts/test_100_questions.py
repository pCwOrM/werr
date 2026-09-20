#!/usr/bin/env python3
"""
MECHSRV 100-Question Automation Test for werr (Multi-Domain System-One Engine)
Evaluates 100 scenarios across 5 distinct domains using dynamic Auto-Seed Routing:
1. API Gateway, Network Security & Auth (20 questions)
2. Smart Home & IoT Automation (20 questions)
3. E-Commerce & Fraud Detection (20 questions)
4. Game AI & NPC Combat Reflexes (20 questions)
5. Financial Risk & Credit Scoring (20 questions)
"""
import sys
import os
import time
from typing import Dict, Any, List

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from werr import (
    WerrEngine,
    NoulQuestion,
    ChoiceQuestion,
    ScoreQuestion,
    AutoSeedRouter
)


def build_scenarios(batch: int = 2) -> List[Dict[str, Any]]:
    scenarios = []
    start_i = (batch - 1) * 20 + 1
    end_i = start_i + 20

    # =========================================================================
    # CATEGORY 1: API Gateway, Network Security & Auth (20 Scenarios)
    # =========================================================================
    api_roles = ["admin", "root", "member", "guest", "bot", "anonymous", "attacker", "service_bot", "pentester", "crawler", "malware_agent", "auditor"]
    for i in range(start_i, end_i):
        k = (i - 1) % 20 + 1
        role = api_roles[(i - 1) % len(api_roles)]
        req_rate = float(round(1.5 * k if "bot" in role or "attacker" in role or "guest" in role else 0.8 + 0.1 * k, 2))
        failed_attempts = (k * 2) if "attacker" in role or "bot" in role or "malware" in role else (1 if k % 5 == 0 else 0)
        is_admin_flag = role in ("admin", "root")
        token_valid = (role in ("admin", "root", "member", "service_bot", "auditor")) and (k % 7 != 0)
        ddos_suspicion = req_rate > 15.0 or failed_attempts > 10

        state = {
            "category": "API Gateway & Security",
            "scenario_index": i,
            "role": role,
            "req_frequency": req_rate,
            "failed_attempts": failed_attempts,
            "is_admin": is_admin_flag,
            "token_valid": token_valid,
            "ddos_flag": ddos_suspicion,
            "payload_kb": round(2.0 + (i * 12.5 if ddos_suspicion else i * 0.8), 2),
            "ip_reputation_score": round(max(0.0, 1.0 - (failed_attempts * 0.05)), 2)
        }

        questions = {
            "allow": NoulQuestion(
                instructions=f"API Gateway Security Check #{i}: Should request from {role} (valid={token_valid}, ddos={ddos_suspicion}) be permitted?",
                threshold=0.5
            ),
            "route": ChoiceQuestion(
                instructions=f"Select downstream routing pipeline for request #{i}.",
                criteria={
                    "direct_api": "Forward directly to core production service",
                    "rate_limiter": "Queue in secondary token-bucket rate limiter",
                    "sandbox_audit": "Divert to deep security inspection sandbox",
                    "drop_packet": "Drop connection immediately and blacklist IP"
                }
            ),
            "severity": ScoreQuestion(
                instructions=f"Evaluate network threat severity for request #{i}.",
                criteria=["Low", "Medium", "High", "Critical"]
            )
        }
        scenarios.append({"category": "API Gateway", "state": state, "questions": questions})

    # =========================================================================
    # CATEGORY 2: Smart Home & IoT Automation (20 Scenarios)
    # =========================================================================
    iot_zones = ["living_room", "master_bedroom", "kitchen", "garage", "basement", "server_rack", "attic", "greenhouse", "nursery", "balcony"]
    for i in range(start_i, end_i):
        k = (i - 1) % 20 + 1
        zone = iot_zones[(i - 1) % len(iot_zones)]
        smoke = (k in (6, 13, 19))
        temp = round(21.0 + (k * 2.8 if smoke else (k % 8) * 1.5 - 2.0), 1)
        presence = (k % 2 == 0)
        co2_ppm = 420 + (k * 85 if smoke else k * 15)
        window_open = (k % 3 == 0)
        humidity = min(98.0, 40.0 + (k * 2.5))

        state = {
            "category": "Smart Home & IoT",
            "scenario_index": i,
            "role": "home_controller",
            "zone": zone,
            "temperature_c": temp,
            "smoke_detected": smoke,
            "occupancy": presence,
            "co2_ppm": co2_ppm,
            "window_open": window_open,
            "humidity_pct": humidity,
            "motion_detected": presence
        }

        questions = {
            "allow": NoulQuestion(
                instructions=f"IoT Zone [{zone}] Safety Check #{i}: Is environmental state within safe operating parameters?",
                threshold=0.5
            ),
            "route": ChoiceQuestion(
                instructions=f"Select HVAC and safety response for zone [{zone}] #{i}.",
                criteria={
                    "eco_mode": "Maintain low energy ambient stabilization",
                    "active_climate": "Engage high-power heating or cooling cycle",
                    "air_purify": "Run emergency ventilation and HEPA filtration",
                    "evacuate_alarm": "Trigger audible fire sirens and emergency evacuation"
                }
            ),
            "severity": ScoreQuestion(
                instructions=f"Classify environmental hazard level for zone [{zone}] #{i}.",
                criteria=["Low", "Medium", "High", "Critical"]
            )
        }
        scenarios.append({"category": "Smart Home IoT", "state": state, "questions": questions})

    # =========================================================================
    # CATEGORY 3: E-Commerce & Fraud Detection (20 Scenarios)
    # =========================================================================
    user_tiers = ["vip", "verified", "standard", "guest", "new_account", "blacklisted", "compromised_token", "dormant_revived", "enterprise"]
    for i in range(start_i, end_i):
        k = (i - 1) % 20 + 1
        tier = user_tiers[(i - 1) % len(user_tiers)]
        order_amount = round(25.0 + (k ** 2.4), 2)
        new_device = (k % 2 == 1)
        vpn_used = (k in (3, 7, 11, 15, 17, 20))
        foreign_card = (k % 4 == 0)
        velocity_last_hour = (k if vpn_used else max(1, k // 4))

        state = {
            "category": "E-Commerce Fraud",
            "scenario_index": i,
            "role": tier,
            "order_amount_usd": order_amount,
            "new_device": new_device,
            "vpn_used": vpn_used,
            "foreign_card": foreign_card,
            "velocity_last_hour": velocity_last_hour,
            "billing_shipping_match": not (vpn_used and foreign_card),
            "chargeback_history": 3 if tier == "blacklisted" else (1 if k % 8 == 0 else 0)
        }

        questions = {
            "allow": NoulQuestion(
                instructions=f"Fraud Assessment #{i} for tier [{tier}]: Should order of ${order_amount} be cleared for payment?",
                threshold=0.5
            ),
            "route": ChoiceQuestion(
                instructions=f"Select payment risk action for order #{i}.",
                criteria={
                    "instant_capture": "Process settlement immediately without challenge",
                    "step_up_3ds": "Request biometric 3D Secure SMS/OTP challenge",
                    "manual_review": "Escalate to human anti-fraud intelligence team",
                    "hard_decline": "Decline transaction and freeze checkout session"
                }
            ),
            "severity": ScoreQuestion(
                instructions=f"Assign fraud risk score for checkout #{i}.",
                criteria=["Low", "Medium", "High", "Critical"]
            )
        }
        scenarios.append({"category": "E-Commerce Fraud", "state": state, "questions": questions})

    # =========================================================================
    # CATEGORY 4: Game AI & NPC Combat Reflexes (20 Scenarios)
    # =========================================================================
    npc_roles = ["boss", "sniper", "heavy_infantry", "scout", "medic", "assault", "infiltrator", "drone_operator", "berserker"]
    for i in range(start_i, end_i):
        k = (i - 1) % 20 + 1
        npc = npc_roles[(i - 1) % len(npc_roles)]
        health = max(5.0, round(100.0 - (k * 4.6), 1))
        ammo_pct = max(0.0, round(100.0 - (k * 5.2), 1))
        enemy_distance = round(5.0 + (k * 3.5), 1)
        cover_available = (k % 2 == 0)
        under_fire = (k % 3 != 0)
        allies_nearby = max(0, 4 - (k // 5))

        state = {
            "category": "Game AI & Combat",
            "scenario_index": i,
            "role": npc,
            "health_pct": health,
            "ammo_pct": ammo_pct,
            "enemy_distance_m": enemy_distance,
            "cover_available": cover_available,
            "under_fire": under_fire,
            "allies_nearby": allies_nearby,
            "has_heavy_weapon": (npc in ("boss", "heavy_infantry", "berserker"))
        }

        questions = {
            "allow": NoulQuestion(
                instructions=f"NPC [{npc}] Tactical Query #{i}: Can unit sustain aggressive offensive engagement?",
                threshold=0.5
            ),
            "route": ChoiceQuestion(
                instructions=f"Select combat behavior subtree for NPC [{npc}] #{i}.",
                criteria={
                    "flank_attack": "Aggressively close distance and flank target",
                    "take_cover": "Dash into nearest defensive cover posture",
                    "suppressing_fire": "Expend ammunition to pin enemy behind cover",
                    "retreat_heal": "Tactical retreat towards squad medics or regroup point"
                }
            ),
            "severity": ScoreQuestion(
                instructions=f"Evaluate battlefield combat threat level for #{i}.",
                criteria=["Low", "Medium", "High", "Critical"]
            )
        }
        scenarios.append({"category": "Game AI", "state": state, "questions": questions})

    # =========================================================================
    # CATEGORY 5: Financial Risk & Credit Scoring (20 Scenarios)
    # =========================================================================
    applicant_roles = ["prime_borrower", "salaried_employee", "entrepreneur", "freelancer", "subprime_borrower", "student", "retiree", "gig_worker", "startup_founder"]
    for i in range(start_i, end_i):
        k = (i - 1) % 20 + 1
        applicant = applicant_roles[(i - 1) % len(applicant_roles)]
        credit_score = max(350, min(850, 450 + (k * 19 if k <= 15 else 850 - k * 15)))
        annual_income = round(22000.0 + (k * 6500.0), 2)
        debt_to_income = round(min(0.85, 0.15 + (k * 0.03)), 2)
        late_payments_2yr = max(0, (k // 4) - 1)
        loan_amount_requested = round(5000.0 + (k * 4500.0), 2)

        state = {
            "category": "Financial Risk",
            "scenario_index": i,
            "role": applicant,
            "credit_score": credit_score,
            "annual_income_usd": annual_income,
            "debt_to_income_ratio": debt_to_income,
            "late_payments_last_2yrs": late_payments_2yr,
            "loan_amount_requested": loan_amount_requested,
            "homeowner": (k % 2 == 0),
            "employment_length_years": max(1, k // 2)
        }

        questions = {
            "allow": NoulQuestion(
                instructions=f"Underwriting Decision #{i} for [{applicant}]: Approve credit facility for ${loan_amount_requested}?",
                threshold=0.5
            ),
            "route": ChoiceQuestion(
                instructions=f"Select underwriting disposition for loan request #{i}.",
                criteria={
                    "auto_approve": "Approve prime facility with automated issuance",
                    "manual_underwrite": "Forward to human credit committee for asset verification",
                    "counter_offer": "Offer reduced credit limit or demand co-signer guarantor",
                    "reject_adverse": "Issue adverse action rejection notice"
                }
            ),
            "severity": ScoreQuestion(
                instructions=f"Determine systemic default risk grade for #{i}.",
                criteria=["Low", "Medium", "High", "Critical"]
            )
        }
        scenarios.append({"category": "Financial Risk", "state": state, "questions": questions})

    return scenarios


def main():
    import argparse
    parser = argparse.ArgumentParser(description="werr 100-Question Multi-Domain Test Runner")
    parser.add_argument("--batch", type=int, default=2, help="Batch index (1: scenarios 1-20, 2: scenarios 21-40, 3: scenarios 41-60, etc.)")
    args = parser.parse_args()

    print("=" * 80)
    print(f" 🚀 WERR MULTI-DOMAIN 100-QUESTION TEST (Batch #{args.batch})")
    print(" Zero-Memory Dynamic Coordinate Hopping | Sub-2ms Edge Reflex")
    print("=" * 80)

    # 1. Initialize Engine
    t_init_start = time.perf_counter()
    engine = WerrEngine(resolution=32, max_iter=35)
    init_ms = (time.perf_counter() - t_init_start) * 1000.0
    print(f"[+] Engine loaded successfully in {init_ms:.2f}ms")
    print(f"[+] Multi-Domain Auto-Seed Router: ACTIVE\n")

    # 2. Build 100 scenarios for requested batch
    scenarios = build_scenarios(batch=args.batch)
    total_count = len(scenarios)
    start_sc_idx = (args.batch - 1) * 20 + 1
    end_sc_idx = start_sc_idx + 19
    print(f"[+] Prepared {total_count} diverse scenarios across 5 distinct domains (Scenarios #{start_sc_idx} to #{end_sc_idx}).\n")

    total_latency = 0.0
    allowed_count = 0
    route_dist: Dict[str, int] = {}
    severity_dist: Dict[int, int] = {}

    start_time = time.time()

    # 3. Execution loop with auto_route=True
    for idx, sc in enumerate(scenarios, 1):
        cat = sc["category"]
        state = sc["state"]
        questions = sc["questions"]

        # Run multi-domain auto-routed forward pass
        response = engine.decide(state=state, questions=questions, auto_route=True)

        is_allowed = response.boolean("allow")
        selected_route = response.choice("route")
        score_val = response.score("severity")
        lat = response.latency_ms
        total_latency += lat

        if is_allowed:
            allowed_count += 1
        route_dist[selected_route] = route_dist.get(selected_route, 0) + 1
        score_bucket = int(round(score_val))
        severity_dist[score_bucket] = severity_dist.get(score_bucket, 0) + 1

        role_str = str(state.get("role", "N/A"))
        print(
            f"[{idx:3d}/{total_count}] Domain: {cat:<17} | Gate: {response.domain:<15} | "
            f"Allowed: {str(is_allowed):<5} | Route: {selected_route:<17} | "
            f"Latency: {lat:5.2f}ms"
        )

        # Smooth output pacing
        time.sleep(0.02)

    duration = time.time() - start_time
    avg_latency = total_latency / total_count

    print("\n" + "=" * 80)
    print(f" 📊 TEST SUMMARY & METRICS (Batch #{args.batch})")
    print("=" * 80)
    print(f"Total Scenarios Evaluated : {total_count}")
    print(f"Total Execution Time      : {duration:.2f} seconds")
    print(f"Average Engine Latency    : {avg_latency:.3f} ms / decision")
    print(f"Allowed Decisions         : {allowed_count} / {total_count} ({(allowed_count/total_count)*100:.1f}%)")
    print(f"Routing Distribution      : {route_dist}")
    print(f"Severity Score Dist       : {severity_dist}")
    print("=" * 80)
    print("[+] Waiting 3 seconds for background telemetry catchup...")
    time.sleep(3.0)
    print("[+] Test completed successfully!\n")


if __name__ == "__main__":
    main()
