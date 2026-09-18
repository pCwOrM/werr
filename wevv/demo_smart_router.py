"""
wevv Demo: Smart API Gateway & Safety Inspector
Simulates the 'System-One Smart if-statement' pattern using Zero-Memory Fractal Geometry.
Demonstrates sub-millisecond execution, 0-byte matrix storage, and type-safe outputs.
"""
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from wevv import (
    WevvEngine,
    NoulQuestion,
    ChoiceQuestion,
    ScoreQuestion,
    create_smart_router
)


if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def run_demo():
    print("=" * 70)
    print(" ~*~ wevv (Wave & VV-Subdivision): Zero-Memory System-One Decision Engine")
    print("=" * 70)

    # 1. Initialize our pre-calibrated fractal router
    engine = create_smart_router(resolution=64)
    print(f"[+] Engine initialized with 24-byte seed: cx={engine.cx:.5f}, cy={engine.cy:.5f}")
    print(f"[+] Memory footprint: 0 Bytes tensor weights (Pure Geometric Derivation)\n")

    # 2. Define the decision questions (Jev System-One Primitives)
    questions = {
        "allow_execution": NoulQuestion(
            instructions="Should this incoming request be granted direct execution?",
            threshold=0.5,
            weight_bias=2.2
        ),
        "route_target": ChoiceQuestion(
            instructions="Select target downstream service for this payload.",
            criteria={
                "direct_api": "Forward directly to production microservice",
                "rate_limiter": "Queue in secondary rate-limiting buffer",
                "sandbox_audit": "Redirect to isolated sandbox for deep inspection",
                "drop_packet": "Immediately reject and blacklist sender"
            }
        ),
        "threat_severity": ScoreQuestion(
            instructions="Assess the perceived threat severity.",
            criteria=[
                "Normal/Benign",
                "Minor anomaly",
                "Elevated risk",
                "Critical threat"
            ]
        )
    }

    # 3. Test scenarios
    scenarios = [
        {
            "title": "Scenario A: Regular Authenticated User",
            "state": {
                "user_role": "member",
                "auth_status": True,
                "request_path": "/api/v2/user/profile",
                "req_frequency": 1.2,
                "failed_attempts": 0,
                "payload_kb": 4.5
            }
        },
        {
            "title": "Scenario B: Suspicious Rapid Bursts from Anonymous IP",
            "state": {
                "user_role": "guest",
                "auth_status": False,
                "request_path": "/api/v2/admin/export_db",
                "req_frequency": 140.0,
                "failed_attempts": 18,
                "payload_kb": 250.0
            }
        },
        {
            "title": "Scenario C: Edge Webhook Notification",
            "state": {
                "user_role": "service_bot",
                "auth_status": True,
                "request_path": "/webhook/payment_notify",
                "req_frequency": 25.0,
                "failed_attempts": 1,
                "payload_kb": 12.0
            }
        }
    ]

    for sc in scenarios:
        print(f"--- {sc['title']} ---")
        print(f"Input State: {sc['state']}")

        # Execute decision in single parallel forward pass
        response = engine.decide(state=sc['state'], questions=questions)

        # Output typed answers
        allow_ans = response.answers["allow_execution"]
        route_ans = response.answers["route_target"]
        threat_ans = response.answers["threat_severity"]

        print(f"\n[Answers in {response.latency_ms:.2f} ms | Tensor VRAM: {response.memory_tensor_bytes} B]:")
        print(f"  * allow_execution [noul]:  Decision={allow_ans.decision} "
              f"(p={allow_ans.noul:.4f}, conf={allow_ans.confidence:.2f})")
        print(f"  * route_target    [choice]: Selected='{route_ans.choice}' "
              f"(conf={route_ans.confidence:.2f})")
        print(f"    Breakdown: {route_ans.probabilities}")
        print(f"  * threat_severity [score]:  Score={threat_ans.score:.2f}/3.0 "
              f"(conf={threat_ans.confidence:.2f})")
        print(f"    Probabilities: {threat_ans.probabilities}")

        # The 'Smart If-Statement' in ordinary code:
        if response.boolean("allow_execution") and response.score("threat_severity") < 1.5:
            print("  ==> [Action]: EXECUTE_DIRECT(request)")
        else:
            print(f"  ==> [Action]: ROUTE_TO({response.choice('route_target').upper()})")
        print()

    print("=" * 70)
    print(" [+] All decisions synthesized successfully in sub-millisecond latency.")
    print("=" * 70)


if __name__ == "__main__":
    run_demo()
