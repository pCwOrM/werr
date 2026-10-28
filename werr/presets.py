"""
werr: Pre-calibrated Fractal Gate Presets
Resonant coordinates discovered on the Mandelbrot boundary (dM) for specific System-One decision tasks.
"""
from werr.engine import WerrEngine, WevvEngine


def create_security_guard(resolution: int = 36, max_iter: int = 36) -> WerrEngine:
    """
    Creates an engine calibrated for high-sensitivity security, access-control,
    and fraud detection (sharp boundary transitions).
    """
    return WerrEngine(
        base_cx=-0.7436438870371587,
        base_cy=0.1318259042053119,
        base_zoom=120.0,
        resolution=resolution,
        max_iter=max_iter,
        mode="hybrid",
        domain_mode="multi",
        enable_domain=True,
        enable_lexical=True,
        enable_resonance=True,
        tripod=True
    )


def create_smart_router(resolution: int = 36, max_iter: int = 36) -> WerrEngine:
    """
    Creates an engine calibrated with balanced 4-Quadrant entropy
    and multi-domain semantic intent routing for production dispatch.
    """
    return WerrEngine(
        base_cx=-0.10109636384562,
        base_cy=0.95628651080914,
        base_zoom=45.0,
        resolution=resolution,
        max_iter=max_iter,
        mode="hybrid",
        domain_mode="multi",
        enable_domain=True,
        enable_lexical=True,
        enable_resonance=True,
        tripod=True
    )


def create_risk_evaluator(resolution: int = 36, max_iter: int = 36) -> WerrEngine:
    """
    Creates an engine calibrated for smooth gradient escape times,
    ideal for continuous score and priority rankings.
    """
    return WerrEngine(
        base_cx=-0.75,
        base_cy=0.1,
        base_zoom=25.0,
        resolution=resolution,
        max_iter=max_iter,
        mode="hybrid",
        domain_mode="multi",
        enable_domain=True,
        enable_lexical=True,
        enable_resonance=True,
        tripod=True
    )



def create_fast_reflex(resolution: int = 24, max_iter: int = 24) -> WerrEngine:
    """
    Creates an ultra-low latency engine (< 2.5 ms) calibrated for high-throughput
    real-time reflex robotics, aeronautical envelope checks, and neuromorphic motor triggers.
    """
    return WerrEngine(
        base_cx=-0.10109636384562,
        base_cy=0.95628651080914,
        base_zoom=45.0,
        resolution=resolution,
        max_iter=max_iter,
        mode="hybrid",
        domain_mode="multi",
        enable_domain=True,
        enable_lexical=True,
        enable_resonance=True,
        tripod=True
    )


def create_bioneural_reflex(resolution: int = 24, max_iter: int = 24) -> WerrEngine:
    """
    Creates an engine calibrated for Drosophila connectome neuromuscular interfacing
    (FlyWire 158K neurons, sub-3ms saccade and flight velocity reflex actuation).
    """
    return create_fast_reflex(resolution=resolution, max_iter=max_iter)
