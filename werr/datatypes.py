"""
wevv: Type-safe System-One Fractal Decision Data Types
Zero-Memory Fractal Decision Engine inspired by System-1 intuition.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union, Any


@dataclass
class NoulQuestion:
    """
    Boolean judgment question ('noul' = null/one, binary decision).
    Evaluates whether a condition holds in the given state.
    """
    instructions: str
    threshold: float = 0.5
    weight_bias: float = 0.0


@dataclass
class ChoiceQuestion:
    """
    Categorical decision question.
    Selects one option among defined criteria with full probability distribution.
    """
    instructions: str
    criteria: Dict[str, str]  # e.g. {"allow": "Safe request", "block": "Harmful request"}


@dataclass
class ScoreQuestion:
    """
    Scalar ranking/scoring question along a defined ordinal scale.
    """
    instructions: str
    criteria: List[str]  # e.g. ["Low risk", "Moderate risk", "Critical risk"]


@dataclass
class NoulAnswer:
    """
    Boolean answer with probability and confidence.
    """
    type: str = "noul"
    noul: float = 0.0  # Probability in [0.0, 1.0]
    decision: bool = False
    confidence: float = 0.0


@dataclass
class ChoiceAnswer:
    """
    Choice answer with selected option, probability breakdown, and confidence.
    """
    type: str = "choice"
    choice: str = ""
    probabilities: Dict[str, float] = field(default_factory=dict)
    confidence: float = 0.0


@dataclass
class ScoreAnswer:
    """
    Score answer with scalar score, bucket probabilities, and confidence.
    """
    type: str = "score"
    score: float = 0.0
    level: str = ""
    probabilities: Dict[Union[int, str], float] = field(default_factory=dict)
    confidence: float = 0.0


@dataclass
class WevvResponse:
    """
    Standardized response returned by WevvEngine.
    """
    model: str = "werr-0.3.0-fractal"
    domain: str = "api_security"
    answers: Dict[str, Union[NoulAnswer, ChoiceAnswer, ScoreAnswer]] = field(default_factory=dict)
    latency_ms: float = 0.0
    memory_tensor_bytes: int = 0  # True Zero-Memory: 0 bytes!
    coordinate_bytes: int = 24     # (cx, cy, zoom) in Float64
    escape_entropy: float = 0.0
    quadrant_entropy: float = 0.0
    active_coordinates: Dict[str, float] = field(default_factory=dict)

    def noul(self, key: str) -> float:
        ans = self.answers.get(key)
        if isinstance(ans, NoulAnswer) or getattr(ans, "type", None) == "noul":
            return ans.noul
        raise KeyError(f"Question '{key}' is not a NoulAnswer")

    def boolean(self, key: str) -> bool:
        ans = self.answers.get(key)
        if isinstance(ans, NoulAnswer) or getattr(ans, "type", None) == "noul":
            return ans.decision
        raise KeyError(f"Question '{key}' is not a NoulAnswer")

    def choice(self, key: str) -> str:
        ans = self.answers.get(key)
        if isinstance(ans, ChoiceAnswer) or getattr(ans, "type", None) == "choice":
            return ans.choice
        raise KeyError(f"Question '{key}' is not a ChoiceAnswer")

    def score(self, key: str) -> float:
        ans = self.answers.get(key)
        if isinstance(ans, ScoreAnswer) or getattr(ans, "type", None) == "score":
            return ans.score
        raise KeyError(f"Question '{key}' is not a ScoreAnswer")
