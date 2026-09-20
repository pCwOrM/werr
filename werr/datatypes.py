"""
werr: Type-safe System-One Fractal Decision Data Types
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
    criteria: Union[Dict[str, str], List[str]]
    temperature: float = 0.0


@dataclass
class ScoreQuestion:
    """
    Continuous or ordinal score judgment question.
    Projects state into a continuous scalar [0.0, max_level].
    """
    instructions: str
    criteria: Optional[List[str]] = None
    min_val: float = 0.0
    max_val: float = 3.0


@dataclass
class NoulAnswer:
    """Answer for a Boolean judgment question."""
    type: str = "noul"
    decision: bool = False
    noul: float = 0.0
    confidence: float = 0.0


@dataclass
class ChoiceAnswer:
    """Answer for a categorical decision question."""
    type: str = "choice"
    choice: str = ""
    probabilities: Dict[str, float] = field(default_factory=dict)
    confidence: float = 0.0


@dataclass
class ScoreAnswer:
    """Answer for a continuous or ordinal score judgment question."""
    type: str = "score"
    score: float = 0.0
    level: str = ""
    probabilities: Dict[Union[int, str], float] = field(default_factory=dict)
    confidence: float = 0.0


@dataclass
class WerrResponse:
    """
    Standardized response returned by WerrEngine.
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


# Backward compatibility alias
WevvResponse = WerrResponse
