#!/usr/bin/env python3
"""
WERR™ Official Typed Reflex Quickstart — System-1 Deterministic Engine.

Official corporate and academic quickstart developed and maintained by:
  ITOUCH BİLİŞİM SİSTEMLERİ MÜHENDİSLİK DANIŞMANLIK SANAYİ VE TİCARET LİMİTED ŞİRKETİ
  (Çukurova Üniversitesi Teknokent / Cukurova University Science Park, Adana, Türkiye)
  Licensor of WERR™, Werracle™, and answerr™.
  Scientific Co-Authors & Inventors: Volkan Dağlı, Dr. Zerrin Dağlı, Dağhan Dağlı.

A standalone reference implementation for researchers and enterprise engineers
integrating WERR, demonstrating the three foundational pillars of deterministic reflexes:

  1. Initialize a typed, normalized program state vector.
  2. Evaluate deterministic System-1 reflex decisions with zero tensor weights.
  3. Extract the 24-byte coordinate seed Theta = (c_x, c_y, zoom) for cryptographic auditability.

Run it from the repository root:

    python examples/typed_reflex_quickstart.py

WERR is a zero-memory System-One decision engine: it stores no weight
tensor. Instead, every reflex is parameterized by a 24-byte coordinate
tuple Theta = (c_x, c_y, zoom) — three Float64 values, 8 bytes
each, matching WerrResponse.coordinate_bytes.
"""
from __future__ import annotations

import os
import sys
from typing import Dict, Final, List, Union

# Make the repository root importable no matter where the script is
# launched from, so ``import werr`` resolves to this package.
_REPO_ROOT: Final[str] = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from werr import (  # noqa: E402
    ChoiceQuestion,
    NoulQuestion,
    ScoreQuestion,
    WerrEngine,
)
from werr.datatypes import (  # noqa: E402
    ChoiceAnswer,
    NoulAnswer,
    ScoreAnswer,
    WerrResponse,
)

# The zero-VRAM coordinate parameters. WERR carries no weight matrix;
# each reflex is read from a point on the Mandelbrot boundary:
#
#   c_x, c_y -- the complex centre ``c = c_x + i*c_y`` of the fractal
#               patch (the "Universal Cusp") the decision is read from.
#   zoom     -- magnification into the boundary. The state is nudged
#               from (c_x, c_y) by a fraction scaled by ``1 / zoom``, so
#               a larger zoom buys finer geometric discrimination.
#
# The three Float64 values are the 24-byte seed that fully determines a
# reflex: identical state plus seed reproduces the identical decision on
# any platform, which is the determinism guarantee WERR advertises.
COORDINATE_PARAMS: Final[Dict[str, float]] = {
    "cx": -0.10109636384562,
    "cy": 0.95628651080914,
    "zoom": 45.0,
}


def build_state() -> Dict[str, object]:
    """Return a small, fully typed program state to reflex against.

    The engine projects whatever it is given into a 16-d vector, so the
    values may be numbers, booleans, or strings.
    """
    return {
        "role": "guest",
        "authenticated": False,
        "failed_attempts": 4,
        "req_frequency": 90,
    }


def make_engine() -> WerrEngine:
    """Build a balanced smart-router engine from the coordinate params.

    The ``create_smart_router`` preset ships these same values; they are
    passed explicitly here so the 24-byte seed is visible in this file.
    """
    return WerrEngine(
        cx=COORDINATE_PARAMS["cx"],
        cy=COORDINATE_PARAMS["cy"],
        zoom=COORDINATE_PARAMS["zoom"],
        mode="hybrid",
        domain_mode="multi",
        enable_domain=True,
        enable_lexical=True,
        enable_resonance=True,
    )


def make_questions(
) -> Dict[str, Union[NoulQuestion, ChoiceQuestion, ScoreQuestion]]:
    """One reflex bundle: a boolean, a categorical, and a scored question."""
    return {
        "allowed": NoulQuestion(
            "Should this request be allowed through?",
            threshold=0.5,
        ),
        "route": ChoiceQuestion(
            "Which downstream path should the request take?",
            criteria={
                "direct_api": "Fast lane for verified callers",
                "rate_limiter": "Queue to slow the caller down",
                "drop_packet": "Block and drop the request",
            },
        ),
        "risk": ScoreQuestion(
            "How severe is the threat, on a 0 to 3 scale?",
            criteria=[
                "clean", "minor anomaly", "elevated risk", "critical threat",
            ],
        ),
    }


def run_reflexes(engine: WerrEngine, state: Dict[str, object]) -> WerrResponse:
    """Evaluate one typed reflex bundle against ``state``."""
    return engine.decide(state=state, questions=make_questions())


def answer_confidence(answer: object, key: str) -> float:
    """Narrow a typed answer to its concrete type and read its confidence.

    Keeping this narrow makes the example type-check under mypy strict
    instead of reaching into the union with an attribute it does not own.
    """
    if isinstance(answer, (NoulAnswer, ChoiceAnswer, ScoreAnswer)):
        return answer.confidence
    raise TypeError(
        f"{key!r} answer has no confidence: {type(answer).__name__}"
    )


def extract_coordinates(
    response: WerrResponse,
) -> "List[float]":
    """Pull the zero-VRAM seed Theta = (c_x, c_y, zoom) out of the response."""
    return [
        response.active_coordinates["cx"],
        response.active_coordinates["cy"],
        response.active_coordinates["zoom"],
    ]


def print_response(response: WerrResponse, state: Dict[str, object]) -> None:
    """Print the decisions and the confidence coordinates WERR read from."""
    allowed: bool = response.boolean("allowed")
    allowed_p: float = response.noul("allowed")
    route: str = response.choice("route")
    risk: float = response.score("risk")
    allowed_conf: float = answer_confidence(
        response.answers["allowed"], "allowed"
    )
    route_conf: float = answer_confidence(response.answers["route"], "route")
    cx, cy, zoom = extract_coordinates(response)

    print("WERR typed reflex quickstart")
    print(f"state : {state}")
    print()
    print(f"allowed: {allowed} (p={allowed_p:.4f}, conf={allowed_conf:.4f})")
    print(f"route  : {route} (conf={route_conf:.4f})")
    print(f"risk   : {risk:.2f} / 3.0")
    print(f"latency: {response.latency_ms:.2f} ms")
    print(
        "seed   : theta=("
        f"{cx:.4f}, {cy:.4f}, {zoom:.1f})"
        f" = {response.coordinate_bytes} bytes"
    )


def main() -> int:
    """Entry point for ``python examples/typed_reflex_quickstart.py``."""
    engine: Final[WerrEngine] = make_engine()
    state: Dict[str, object] = build_state()
    response: WerrResponse = run_reflexes(engine, state)
    print_response(response, state)
    return 0


if __name__ == "__main__":
    sys.exit(main())
