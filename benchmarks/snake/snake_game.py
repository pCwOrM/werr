"""
Deterministic Snake rules and Hamiltonian cycle logic.
Adapted from the typed-decision benchmark for standalone zero-telemetry evaluation.
"""

import random
from collections import deque
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional, Set

DIRECTIONS = ("UP", "DOWN", "LEFT", "RIGHT")
VECTORS = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}


def hamiltonian_cycle(width: int, height: int) -> List[Tuple[int, int]]:
    """Visit each square once with adjacent steps, including the closing edge."""
    if min(width, height) < 4 or (width % 2 and height % 2):
        raise ValueError("Board dimensions must be >= 4, with at least one even dimension")
    if height % 2:
        return [(y, x) for x, y in hamiltonian_cycle(height, width)]
    path = [(0, 0)]
    for y in range(height):
        xs = range(1, width) if y % 2 == 0 else range(width - 1, 0, -1)
        path.extend((x, y) for x in xs)
    path.extend((0, y) for y in range(height - 1, 0, -1))
    return path


@dataclass(frozen=True)
class MoveInfo:
    direction: str
    legal: bool
    safe: bool
    advance: int
    reason: str
    eats: bool


class SnakeGame:
    def __init__(self, width: int = 24, height: int = 16, seed: int = 7, initial_length: int = 6):
        self.width = width
        self.height = height
        self.seed = seed
        self.cycle = hamiltonian_cycle(width, height)
        self.indices = {cell: index for index, cell in enumerate(self.cycle)}
        self.capacity = width * height
        if not 2 <= initial_length < self.capacity:
            raise ValueError("Initial length must be >= 2 and smaller than the board")
        self.initial_length = initial_length
        self.rng = random.Random(seed)
        start = self.indices[(width // 2, height // 2)]
        self.body = deque(self.cycle[(start - i) % self.capacity] for i in range(initial_length))
        self.score = 0
        self.ticks = 0
        self.alive = True
        self.won = False
        self.death_reason: Optional[str] = None
        self.food = self._spawn_food()

    @property
    def head(self) -> Tuple[int, int]:
        return self.body[0]

    def _spawn_food(self) -> Optional[Tuple[int, int]]:
        occupied = set(self.body)
        empty = [cell for cell in self.cycle if cell not in occupied]
        return self.rng.choice(empty) if empty else None

    def target(self, direction: str) -> Tuple[int, int]:
        dx, dy = VECTORS[direction]
        return self.head[0] + dx, self.head[1] + dy

    def legal_reason(self, direction: str) -> str:
        cell = self.target(direction)
        x, y = cell
        if not (0 <= x < self.width and 0 <= y < self.height):
            return "wall"
        if len(self.body) > 1 and cell == self.body[1]:
            return "reverse"
        occupied = set(self.body)
        if cell != self.food and self.body:
            occupied.remove(self.body[-1])  # The tail moves on a non-growing step.
        return "body" if cell in occupied else "legal"

    def moves(self) -> List[MoveInfo]:
        if not self.alive or self.won:
            return []
        head_index = self.indices[self.head]
        tail_distance = (self.indices[self.body[-1]] - head_index) % self.capacity
        food_distance = (self.indices[self.food] - head_index) % self.capacity if self.food else 0
        moves = []
        for direction in DIRECTIONS:
            reason = self.legal_reason(direction)
            legal = (reason == "legal")
            if not legal:
                moves.append(MoveInfo(direction, legal=False, safe=False, advance=0, reason=reason, eats=False))
                continue
            target_cell = self.target(direction)
            target_index = self.indices[target_cell]
            advance = (target_index - head_index) % self.capacity
            eats = (target_cell == self.food)
            safe = True
            if advance >= tail_distance and tail_distance > 0:
                safe, reason = False, "would cross the tail"
            if safe and food_distance > 0 and (advance == 0 or advance > food_distance):
                safe, reason = False, "would skip the food on the safe route"
            moves.append(MoveInfo(direction, legal, safe, advance, reason, eats))
        return moves

    def food_reachability(self) -> Tuple[bool, int]:
        """Current empty-cell connectivity; the occupied tail is not treated as empty."""
        blocked = set(self.body) - {self.head}
        visited: Set[Tuple[int, int]] = {self.head}
        queue = deque([self.head])
        while queue:
            x, y = queue.popleft()
            for dx, dy in VECTORS.values():
                cell = (x + dx, y + dy)
                if (
                    0 <= cell[0] < self.width
                    and 0 <= cell[1] < self.height
                    and cell not in blocked
                    and cell not in visited
                ):
                    visited.add(cell)
                    queue.append(cell)
        return (self.food in visited) if self.food else False, len(visited)

    def step(self, direction: str) -> bool:
        if not self.alive or self.won:
            raise RuntimeError("Cannot step a finished game")
        if direction not in DIRECTIONS:
            raise ValueError(f"Unknown direction: {direction}")
        self.ticks += 1
        reason = self.legal_reason(direction)
        if reason != "legal":
            self.alive = False
            self.death_reason = reason
            return False
        target_cell = self.target(direction)
        self.body.appendleft(target_cell)
        if target_cell == self.food:
            self.score += 1
            if len(self.body) == self.capacity:
                self.won = True
                self.food = None
            else:
                self.food = self._spawn_food()
            return True
        self.body.pop()
        return False

    def snapshot(self) -> Dict:
        return {
            "width": self.width,
            "height": self.height,
            "seed": self.seed,
            "score": self.score,
            "length": len(self.body),
            "ticks": self.ticks,
            "alive": self.alive,
            "won": self.won,
            "death_reason": self.death_reason,
        }
