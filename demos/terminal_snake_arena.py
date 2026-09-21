#!/usr/bin/env python3
"""
Terminal AI Arena: Cloud API Simulator vs 0-Storage Fractal Reflex Engine
========================================================================
Demonstration of System-1 Decision Speeds in a Competitive Terminal Arena.

Fighters:
1. 🔴 Cloud Agent (Simulated TypeSafe Jev / Remote LLM API):
   - High latency (100-250ms HTTP ping roundtrip)
   - Accumulating API query costs ($0.0004 / tick)
   - Requires persistent internet & cloud backend
2. 🟢 Fractal Agent ('answerr' Zero-Storage Procedural Synthesis):
   - Sub-millisecond latency (< 0.3 ms local reflex)
   - $0.0000 cost, 100% offline
   - 0 Byte persistent weights (procedural Mandelbrot boundary derivation)
"""

import os
import sys
import time
import math
import random
from typing import List, Tuple, Dict, Optional

if os.name == 'nt':
    os.system('')
    import msvcrt


# ============================================================================
# ANSI Color Palette
# ============================================================================
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

C_CYAN = "\033[96m"
C_GREEN = "\033[92m"
C_RED = "\033[91m"
C_YELLOW = "\033[93m"
C_MAGENTA = "\033[95m"
C_GRAY = "\033[90m"
C_WHITE = "\033[97m"
C_ORANGE = "\033[38;5;208m"


# ============================================================================
# Decision Engines
# ============================================================================
class FractalZeroStorageBrain:
    """
    Sub-millisecond procedural Mandelbrot reflex engine.
    """
    def __init__(self):
        self.cx = -0.7436438870371587
        self.cy = 0.1318259042053119

    def decide(
        self,
        head: Tuple[int, int],
        food_list: List[Tuple[int, int]],
        my_body: List[Tuple[int, int]],
        opponent_body: List[Tuple[int, int]],
        grid_w: int,
        grid_h: int,
        current_dir: str
    ) -> Tuple[str, float]:
        t0 = time.perf_counter()
        moves = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}

        hx, hy = head
        all_obstacles = set(my_body) | set(opponent_body)

        # Find closest food
        if food_list:
            best_food = min(food_list, key=lambda f: abs(f[0] - hx) + abs(f[1] - hy))
        else:
            best_food = (grid_w // 2, grid_h // 2)

        fx, fy = best_food
        dx_target = fx - hx
        dy_target = fy - hy

        scores = {}
        for i, (m_name, (dx, dy)) in enumerate(moves.items()):
            if m_name == opposites.get(current_dir):
                scores[m_name] = -9999.0
                continue
            nx, ny = hx + dx, hy + dy
            if nx < 0 or nx >= grid_w or ny < 0 or ny >= grid_h or (nx, ny) in all_obstacles:
                scores[m_name] = -9999.0
                continue

            # Free space flood-fill
            visited = {(nx, ny)}
            queue = [(nx, ny)]
            while queue and len(visited) < 30:
                cx, cy = queue.pop(0)
                for odx, ody in moves.values():
                    nox, noy = cx + odx, cy + ody
                    if (0 <= nox < grid_w and 0 <= noy < grid_h and 
                        (nox, noy) not in all_obstacles and (nox, noy) not in visited):
                        visited.add((nox, noy))
                        queue.append((nox, noy))
            free_cells = len(visited)

            # Procedural fractal escape modulation
            zx = self.cx + (dx_target * 0.0006) + (i * 0.0002)
            zy = self.cy + (dy_target * 0.0006) + (i * 0.0002)
            iters = 0
            while zx * zx + zy * zy <= 4.0 and iters < 20:
                zx, zy = zx * zx - zy * zy + self.cx, 2.0 * zx * zy + self.cy
                iters += 1

            dist_curr = abs(dx_target) + abs(dy_target)
            dist_next = abs(fx - nx) + abs(fy - ny)
            dist_delta = dist_curr - dist_next

            score = (dist_delta * 14.0) + (free_cells * 1.5) + (iters / 20.0) * 3.0
            if free_cells < 3:
                score -= 200.0
            scores[m_name] = score

        best_move = max(scores, key=scores.get)
        lat_ms = (time.perf_counter() - t0) * 1000.0
        return best_move, lat_ms


class SimulatedCloudApiBrain:
    """
    Simulates remote cloud LLM / Jev API with realistic HTTP latency and query costs.
    """
    def __init__(self, base_cloud_ping_ms: float = 160.0):
        self.base_ping_ms = base_cloud_ping_ms
        self.total_cost = 0.0
        self.cost_per_call = 0.0004  # $0.0004 per typed question

    def decide(
        self,
        head: Tuple[int, int],
        food_list: List[Tuple[int, int]],
        my_body: List[Tuple[int, int]],
        opponent_body: List[Tuple[int, int]],
        grid_w: int,
        grid_h: int,
        current_dir: str
    ) -> Tuple[str, float]:
        t0 = time.perf_counter()

        # Simulate cloud network jitter (e.g. 130ms - 220ms)
        simulated_lag = max(0.001, (self.base_ping_ms + random.uniform(-25.0, 45.0)) / 1000.0)
        time.sleep(simulated_lag)

        self.total_cost += self.cost_per_call

        moves = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        hx, hy = head
        all_obstacles = set(my_body) | set(opponent_body)

        if food_list:
            best_food = min(food_list, key=lambda f: abs(f[0] - hx) + abs(f[1] - hy))
        else:
            best_food = (grid_w // 2, grid_h // 2)

        fx, fy = best_food
        scores = {}
        for m_name, (dx, dy) in moves.items():
            if m_name == opposites.get(current_dir):
                scores[m_name] = -9999.0
                continue
            nx, ny = hx + dx, hy + dy
            if nx < 0 or nx >= grid_w or ny < 0 or ny >= grid_h or (nx, ny) in all_obstacles:
                scores[m_name] = -9999.0
                continue

            dist_curr = abs(fx - hx) + abs(fy - hy)
            dist_next = abs(fx - nx) + abs(fy - ny)
            scores[m_name] = (dist_curr - dist_next) * 10.0 + random.uniform(-1.0, 1.0)

        best_move = max(scores, key=scores.get)
        lat_ms = (time.perf_counter() - t0) * 1000.0
        return best_move, lat_ms


# ============================================================================
# Arena Simulation
# ============================================================================
class ArenaSnakeGame:
    def __init__(self, width: int = 28, height: int = 16):
        self.width = width
        self.height = height

        self.fractal_brain = FractalZeroStorageBrain()
        self.cloud_brain = SimulatedCloudApiBrain(base_cloud_ping_ms=150.0)

        self.paused = False
        self.ticks = 0
        self.reset()

        # Telemetry Stats
        self.cloud_latencies = []
        self.fractal_latencies = []

    def reset(self):
        self.cloud_body = [(3, 3), (2, 3), (1, 3)]
        self.cloud_dir = "RIGHT"
        self.cloud_score = 0
        self.cloud_last_lat = 155.0

        self.fractal_body = [(self.width - 4, self.height - 4), (self.width - 3, self.height - 4), (self.width - 2, self.height - 4)]
        self.fractal_dir = "LEFT"
        self.fractal_score = 0
        self.fractal_last_lat = 0.22

        self.foods = []
        for _ in range(2):
            self._spawn_food()

    def _spawn_food(self):
        occupied = set(self.cloud_body) | set(self.fractal_body) | set(self.foods)
        candidates = [(x, y) for x in range(self.width) for y in range(self.height) if (x, y) not in occupied]
        if candidates:
            self.foods.append(random.choice(candidates))

    def step(self):
        if self.paused:
            return

        self.ticks += 1

        # 1. Fractal Zero-Storage Turn (Local, Instant Reflex)
        f_head = self.fractal_body[0]
        f_move, f_lat = self.fractal_brain.decide(
            head=f_head,
            food_list=self.foods,
            my_body=self.fractal_body,
            opponent_body=self.cloud_body,
            grid_w=self.width,
            grid_h=self.height,
            current_dir=self.fractal_dir
        )
        self.fractal_dir = f_move
        self.fractal_last_lat = f_lat
        self.fractal_latencies.append(f_lat)

        # 2. Cloud API Turn (Simulated Network Lag)
        c_head = self.cloud_body[0]
        c_move, c_lat = self.cloud_brain.decide(
            head=c_head,
            food_list=self.foods,
            my_body=self.cloud_body,
            opponent_body=self.fractal_body,
            grid_w=self.width,
            grid_h=self.height,
            current_dir=self.cloud_dir
        )
        self.cloud_dir = c_move
        self.cloud_last_lat = c_lat
        self.cloud_latencies.append(c_lat)

        # 3. Advance Fractal Snake
        move_map = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
        fdx, fdy = move_map[self.fractal_dir]
        new_f_head = (f_head[0] + fdx, f_head[1] + fdy)

        # Collision check Fractal
        if (new_f_head[0] < 0 or new_f_head[0] >= self.width or
            new_f_head[1] < 0 or new_f_head[1] >= self.height or
            new_f_head in self.fractal_body[:-1] or new_f_head in self.cloud_body):
            # Respawn Fractal Snake
            self.fractal_body = [(self.width - 4, self.height - 4), (self.width - 3, self.height - 4)]
            self.fractal_dir = "LEFT"
        else:
            self.fractal_body.insert(0, new_f_head)
            if new_f_head in self.foods:
                self.fractal_score += 1
                self.foods.remove(new_f_head)
                self._spawn_food()
            else:
                self.fractal_body.pop()

        # 4. Advance Cloud Snake
        cdx, cdy = move_map[self.cloud_dir]
        new_c_head = (c_head[0] + cdx, c_head[1] + cdy)

        # Collision check Cloud
        if (new_c_head[0] < 0 or new_c_head[0] >= self.width or
            new_c_head[1] < 0 or new_c_head[1] >= self.height or
            new_c_head in self.cloud_body[:-1] or new_c_head in self.fractal_body):
            # Respawn Cloud Snake
            self.cloud_body = [(3, 3), (2, 3)]
            self.cloud_dir = "RIGHT"
        else:
            self.cloud_body.insert(0, new_c_head)
            if new_c_head in self.foods:
                self.cloud_score += 1
                self.foods.remove(new_c_head)
                self._spawn_food()
            else:
                self.cloud_body.pop()

    def render(self):
        lines = []

        # Banner
        banner = (
            f"{BOLD}{C_YELLOW}╔═════════════════════════════════════════════════════════════════════════════════════════════════╗{RESET}\n"
            f"{BOLD}{C_YELLOW}║   ⚔️  TERMINAL AI ARENA: Cloud API Simulator  VS  0-Storage Fractal Reflex Engine ('answerr')    ║{RESET}\n"
            f"{BOLD}{C_YELLOW}╚═════════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}"
        )
        lines.append(banner)

        # Board rendering
        board_rows = []
        cloud_set = set(self.cloud_body[1:])
        fractal_set = set(self.fractal_body[1:])
        c_head = self.cloud_body[0]
        f_head = self.fractal_body[0]

        head_chars = {"UP": "▲", "DOWN": "▼", "LEFT": "◄", "RIGHT": "►"}

        board_rows.append(f"{BOLD}{C_WHITE}╔{'══' * self.width}╗{RESET}")
        for y in range(self.height):
            row_str = f"{BOLD}{C_WHITE}║{RESET}"
            for x in range(self.width):
                pos = (x, y)
                if pos == c_head:
                    row_str += f"{BOLD}{C_RED}{head_chars.get(self.cloud_dir, 'C')} {RESET}"
                elif pos in cloud_set:
                    row_str += f"{C_RED}■ {RESET}"
                elif pos == f_head:
                    row_str += f"{BOLD}{C_CYAN}{head_chars.get(self.fractal_dir, 'F')} {RESET}"
                elif pos in fractal_set:
                    row_str += f"{C_GREEN}■ {RESET}"
                elif pos in self.foods:
                    row_str += f"{BOLD}{C_YELLOW}★ {RESET}"
                else:
                    row_str += f"{C_GRAY}· {RESET}"
            row_str += f"{BOLD}{C_WHITE}║{RESET}"
            board_rows.append(row_str)
        board_rows.append(f"{BOLD}{C_WHITE}╚{'══' * self.width}╝{RESET}")

        # Comparative Telemetry Table
        avg_c_lat = (sum(self.cloud_latencies) / len(self.cloud_latencies)) if self.cloud_latencies else 150.0
        avg_f_lat = (sum(self.fractal_latencies) / len(self.fractal_latencies)) if self.fractal_latencies else 0.22

        speedup_ratio = (avg_c_lat / max(0.001, avg_f_lat))

        hud_rows = [
            f"{BOLD}{C_WHITE}╔════════════════════ ARENA TELEMETRY COMPARISON ════════════════════╗{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} {BOLD}METRIC{RESET}              │ {BOLD}{C_RED}🔴 CLOUD API AGENT{RESET}    │ {BOLD}{C_CYAN}🟢 FRACTAL 0-WEIGHT{RESET}   {BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}╠─────────────────────┼──────────────────────┼──────────────────────╣{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} Apples Captured     │ {BOLD}{C_RED}{self.cloud_score:<20}{RESET} │ {BOLD}{C_CYAN}{self.fractal_score:<20}{RESET} {BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} Real-Time Latency   │ {C_RED}{self.cloud_last_lat:5.1f} ms (Laggy){RESET}    │ {BOLD}{C_GREEN}{self.fractal_last_lat:5.2f} ms (Reflex) ⚡{RESET}{BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} Average Latency     │ {C_RED}{avg_c_lat:5.1f} ms{RESET}            │ {BOLD}{C_GREEN}{avg_f_lat:5.2f} ms{RESET}            {BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} Speedup Factor      │ {DIM}1.0x (Baseline){RESET}       │ {BOLD}{C_YELLOW}{speedup_ratio:4.0f}x FASTER 🚀{RESET}     {BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} Model Weights       │ {C_RED}Cloud / 4-8 GB LLM{RESET}   │ {BOLD}{C_GREEN}0.00 KB (Procedural){RESET} {BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} Total Cost (USD)    │ {BOLD}{C_RED}${self.cloud_brain.total_cost:6.4f}{RESET}             │ {BOLD}{C_GREEN}$0.0000 (100% Free){RESET}  {BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} Offline Capability  │ {C_RED}NO (Needs WiFi/API){RESET}   │ {BOLD}{C_GREEN}YES (Edge Embedded){RESET}  {BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}╠─────────────────────┴──────────────────────┴──────────────────────╣{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} ARENA TICKS: {BOLD}{self.ticks:<8}{RESET}                                           {BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}║{RESET} CONTROLS   : [SPACE] Pause | [R] Reset | [Q] Quit Match            {BOLD}{C_WHITE}║{RESET}",
            f"{BOLD}{C_WHITE}╚═══════════════════════════════════════════════════════════════════╝{RESET}"
        ]

        # Combine side-by-side
        max_rows = max(len(board_rows), len(hud_rows))
        empty_board_space = " " * (self.width * 2 + 2)

        for i in range(max_rows):
            b_part = board_rows[i] if i < len(board_rows) else empty_board_space
            h_part = hud_rows[i] if i < len(hud_rows) else ""
            lines.append(f"{b_part}   {h_part}")

        sys.stdout.write("\033[H" + "\n".join(lines) + "\n")
        sys.stdout.flush()

    def handle_input(self) -> bool:
        if os.name == 'nt':
            while msvcrt.kbhit():
                ch = msvcrt.getch().decode('utf-8', errors='ignore').lower()
                if ch == 'q':
                    return False
                elif ch == ' ':
                    self.paused = not self.paused
                elif ch == 'r':
                    self.reset()
        return True


def run():
    sys.stdout.write("\033[?25l\033[2J")
    sys.stdout.flush()

    arena = ArenaSnakeGame(width=28, height=16)

    try:
        while True:
            if not arena.handle_input():
                break

            arena.step()
            arena.render()
            time.sleep(0.04)

    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h\033[0m\n")
        sys.stdout.flush()
        print("\n[✓] Terminal AI Arena exited cleanly.")


if __name__ == "__main__":
    run()
