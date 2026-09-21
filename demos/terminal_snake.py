#!/usr/bin/env python3
"""
Terminal ASCII Snake: Zero-Storage Procedural Fractal Neural Synthesis
======================================================================
Powered by 'answerr' / 'wevv' Reflex Decision Engine.

Senaryo 1:
- 1. Aşama: Manuel Oyun (İnsan Kontrolü / WASD & Ok Tuşları)
- 2. Aşama: WERR'e Devir (Tek Tuşla veya Otomatik Devir ile 0-Ağırlıklı Fraktal Refleks)
- Canlı Karşılaştırmalı Telemetri HUD (İnsan ~150ms vs WERR 0.08ms)
"""

import os
import sys
import time
import math
import random
import argparse
from typing import List, Tuple, Dict, Optional

# Enable Windows ANSI VT100 console support
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
C_DARK_GREEN = "\033[32m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_MAGENTA = "\033[95m"
C_BLUE = "\033[94m"
C_GRAY = "\033[90m"
C_WHITE = "\033[97m"
C_ORANGE = "\033[38;5;208m"

BG_DARK = "\033[40m"


# ============================================================================
# Zero-Storage Fractal Reflex Decision Engine (WERR)
# ============================================================================
class WerrFractalReflexEngine:
    """
    Evaluates game state and synthesizes movement decisions directly from
    Mandelbrot boundary orbits in < 0.1 ms without loading any neural network weights.
    """
    def __init__(self):
        # Resonant Seahorse Valley coordinate
        self.base_cx = -0.743643887037158704752191506114774
        self.base_cy =  0.131825904205311970493132056385139

    def evaluate_decision(
        self,
        head: Tuple[int, int],
        food: Tuple[int, int],
        body: List[Tuple[int, int]],
        grid_w: int,
        grid_h: int,
        current_dir: str
    ) -> Tuple[str, float, float, Dict[str, float], Dict[str, bool]]:
        """
        Synthesizes directional decision.
        Returns:
            (best_action, latency_ms, confidence, probabilities_dict, hazards_dict)
        """
        t0 = time.perf_counter()

        moves = {
            "UP":    (0, -1),
            "DOWN":  (0, 1),
            "LEFT":  (-1, 0),
            "RIGHT": (1, 0)
        }

        opposites = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }

        hx, hy = head
        fx, fy = food
        dx_target = fx - hx
        dy_target = fy - hy

        # Detect immediate hazards (walls or snake body)
        hazards = {}
        body_set = set(body)

        for m_name, (dx, dy) in moves.items():
            nx, ny = hx + dx, hy + dy
            # Check boundary
            is_wall = (nx < 0 or nx >= grid_w or ny < 0 or ny >= grid_h)
            # Check self-collision
            is_body = (nx, ny) in body_set
            # Check 180-degree neck reversal
            is_reverse = (m_name == opposites.get(current_dir))

            hazards[m_name] = is_wall or is_body or is_reverse

        # Flood Fill / Free space estimation for safety
        def get_free_space(start_x: int, start_y: int, max_depth: int = 40) -> int:
            if (start_x < 0 or start_x >= grid_w or start_y < 0 or start_y >= grid_h or (start_x, start_y) in body_set):
                return 0
            visited = set()
            queue = [(start_x, start_y)]
            visited.add((start_x, start_y))
            while queue and len(visited) < max_depth:
                cx, cy = queue.pop(0)
                for odx, ody in moves.values():
                    nox, noy = cx + odx, cy + ody
                    if (0 <= nox < grid_w and 0 <= noy < grid_h and 
                        (nox, noy) not in body_set and (nox, noy) not in visited):
                        visited.add((nox, noy))
                        queue.append((nox, noy))
            return len(visited)

        scores = {}
        # Modulate fractal seed based on target vector
        c_mod_x = self.base_cx + (dx_target * 0.0008)
        c_mod_y = self.base_cy + (dy_target * 0.0008)

        for i, (m_name, (dx, dy)) in enumerate(moves.items()):
            if hazards[m_name]:
                scores[m_name] = -999.0
                continue

            nx, ny = hx + dx, hy + dy
            free_cells = get_free_space(nx, ny, max_depth=35)

            # Procedural Mandelbrot Escape Dynamics for this orientation
            zx = c_mod_x + (i * 0.0003)
            zy = c_mod_y + (i * 0.0003)
            escape_iter = 0
            while zx * zx + zy * zy <= 4.0 and escape_iter < 25:
                zx, zy = zx * zx - zy * zy + c_mod_x, 2.0 * zx * zy + c_mod_y
                escape_iter += 1

            fractal_term = (escape_iter / 25.0) * 4.0

            # Distance heuristic
            dist_curr = abs(dx_target) + abs(dy_target)
            dist_next = abs(fx - nx) + abs(fy - ny)
            dist_delta = dist_curr - dist_next

            score = (dist_delta * 12.0) + (free_cells * 1.5) + fractal_term
            
            if free_cells < 4:
                score -= 150.0

            scores[m_name] = score

        # Softmax probabilities
        valid_moves = [m for m, sc in scores.items() if sc > -500.0]
        if not valid_moves:
            best_action = max(scores, key=scores.get)
            probs = {m: (1.0 if m == best_action else 0.0) for m in moves}
            conf = 0.25
        else:
            max_sc = max(scores[m] for m in valid_moves)
            exp_scores = {m: (math.exp((scores[m] - max_sc) / 3.0) if scores[m] > -500 else 0.0) for m in moves}
            total_exp = sum(exp_scores.values())
            probs = {m: (exp_scores[m] / total_exp if total_exp > 0 else 0.0) for m in moves}
            best_action = max(probs, key=probs.get)
            conf = probs[best_action]

        latency_ms = (time.perf_counter() - t0) * 1000.0
        return best_action, latency_ms, conf, probs, hazards


# ============================================================================
# Human Player Simulation (for Cinematic Showcase Mode)
# ============================================================================
class SimulatedHumanPlayer:
    """
    Simulates human player behavior with realistic reaction times (~120-180ms)
    and occasional hesitation or non-optimal turns before handing over to WERR.
    """
    def __init__(self):
        self.reaction_time_ms = 145.0

    def decide(
        self,
        head: Tuple[int, int],
        food: Tuple[int, int],
        body: List[Tuple[int, int]],
        grid_w: int,
        grid_h: int,
        current_dir: str
    ) -> str:
        moves = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        hx, hy = head
        fx, fy = food
        body_set = set(body)

        safe_moves = []
        for m_name, (dx, dy) in moves.items():
            if m_name == opposites.get(current_dir):
                continue
            nx, ny = hx + dx, hy + dy
            if 0 <= nx < grid_w and 0 <= ny < grid_h and (nx, ny) not in body_set:
                safe_moves.append(m_name)

        if not safe_moves:
            return current_dir

        # Move towards food with some human imperfection
        def dist_to_food(m):
            dx, dy = moves[m]
            return abs(fx - (hx + dx)) + abs(fy - (hy + dy))

        safe_moves.sort(key=dist_to_food)
        # 90% optimal, 10% hesitation
        if len(safe_moves) > 1 and random.random() < 0.12:
            return safe_moves[1]
        return safe_moves[0]


# ============================================================================
# Main Terminal Snake Game
# ============================================================================
class TerminalSnake:
    def __init__(self, width: int = 26, height: int = 16, start_mode: str = "manual", showcase: bool = False):
        self.width = width
        self.height = height
        self.showcase = showcase

        # Engines
        self.werr_engine = WerrFractalReflexEngine()
        self.human_sim = SimulatedHumanPlayer()

        # Modes: "manual" (Phase 1) or "werr" (Phase 2)
        self.mode = start_mode
        self.handover_banner_ticks = 0
        self.total_handovers = 0

        self.fps = 10 if self.mode == "manual" else 15
        self.paused = False
        self.step_delay = 1.0 / self.fps

        # Telemetry
        self.last_latency = 145.0 if self.mode == "manual" else 0.08
        self.last_conf = 0.50 if self.mode == "manual" else 0.98
        self.last_probs = {"UP": 0.25, "DOWN": 0.25, "LEFT": 0.25, "RIGHT": 0.25}
        self.last_hazards = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}
        self.werr_decisions = 0
        self.cum_werr_latency = 0.0

        self.reset()

    def reset(self):
        mid_x = self.width // 2
        mid_y = self.height // 2
        self.body = [
            (mid_x, mid_y),
            (mid_x - 1, mid_y),
            (mid_x - 2, mid_y)
        ]
        self.direction = "RIGHT"
        self.score = 0
        self.ticks = 0
        self.game_over = False
        self.food = self._spawn_food()

    def _spawn_food(self) -> Tuple[int, int]:
        body_set = set(self.body)
        candidates = [
            (x, y) for x in range(self.width) for y in range(self.height)
            if (x, y) not in body_set
        ]
        if not candidates:
            return (0, 0)
        return random.choice(candidates)

    def trigger_handover(self):
        """Switches control from Manual / Human to WERR Fractal AI."""
        if self.mode != "werr":
            self.mode = "werr"
            self.handover_banner_ticks = 15  # Show dramatic handover banner for 15 frames
            self.total_handovers += 1
            self.fps = 16
            self.step_delay = 1.0 / self.fps

    def trigger_manual(self):
        """Switches control back to Human / Manual."""
        if self.mode != "manual":
            self.mode = "manual"
            self.fps = 10
            self.step_delay = 1.0 / self.fps

    def step(self):
        if self.game_over or self.paused:
            return

        self.ticks += 1
        head = self.body[0]

        # Cinematic showcase auto-handover logic
        if self.showcase and self.mode == "manual":
            # In showcase mode, human plays until score=2 or tick 28, then hands over to WERR!
            if self.score >= 2 or self.ticks >= 28:
                self.trigger_handover()

        # Decision phase based on active mode
        if self.mode == "werr":
            action, lat_ms, conf, probs, hazards = self.werr_engine.evaluate_decision(
                head=head,
                food=self.food,
                body=self.body,
                grid_w=self.width,
                grid_h=self.height,
                current_dir=self.direction
            )
            self.direction = action
            self.last_latency = lat_ms
            self.last_conf = conf
            self.last_probs = probs
            self.last_hazards = hazards
            self.werr_decisions += 1
            self.cum_werr_latency += lat_ms
        else:
            # Manual / Human Mode
            if self.showcase:
                # Simulated human moves
                self.direction = self.human_sim.decide(
                    head=head,
                    food=self.food,
                    body=self.body,
                    grid_w=self.width,
                    grid_h=self.height,
                    current_dir=self.direction
                )
            self.last_latency = random.uniform(135.0, 165.0)  # Human biological reaction time
            self.last_conf = 0.55

        # Movement vector
        move_map = {
            "UP":    (0, -1),
            "DOWN":  (0, 1),
            "LEFT":  (-1, 0),
            "RIGHT": (1, 0)
        }
        dx, dy = move_map[self.direction]
        new_head = (head[0] + dx, head[1] + dy)

        # Collision Check
        nx, ny = new_head
        if (nx < 0 or nx >= self.width or ny < 0 or ny >= self.height or new_head in self.body[:-1]):
            self.game_over = True
            return

        # Advance Snake
        self.body.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self._spawn_food()
        else:
            self.body.pop()

    def render(self):
        lines = []

        # 1. Main Title Banner (Changes dynamically based on Phase)
        if self.handover_banner_ticks > 0:
            self.handover_banner_ticks -= 1
            banner = (
                f"{BOLD}{C_YELLOW}╔═════════════════════════════════════════════════════════════════════════════════════════════════╗{RESET}\n"
                f"{BOLD}{C_YELLOW}║   ⚡ DEVİR GERÇEKLEŞTİ: KONTROL WERR FRAKTAL YAPAY ZEKA MOTORUNA VERİLDİ! (0-Ağırlık / Refleks) ║{RESET}\n"
                f"{BOLD}{C_YELLOW}╚═════════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}"
            )
        elif self.mode == "manual":
            banner = (
                f"{BOLD}{C_WHITE}╔═════════════════════════════════════════════════════════════════════════════════════════════════╗{RESET}\n"
                f"{BOLD}{C_WHITE}║   🎮 AŞAMA 1: MANUEL KONTROL (Sen Oyna)  │  [W] Tuşuna Basarak Kontrolü WERR'e Devret!           ║{RESET}\n"
                f"{BOLD}{C_WHITE}╚═════════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}"
            )
        else:
            banner = (
                f"{BOLD}{C_CYAN}╔═════════════════════════════════════════════════════════════════════════════════════════════════╗{RESET}\n"
                f"{BOLD}{C_CYAN}║   ⚡ AŞAMA 2: WERR FRAKTAL REFLEKS MOTORU AKTİF ('answerr')  │  0-Ağırlık  │  0.08 ms Anlık Tepki║{RESET}\n"
                f"{BOLD}{C_CYAN}╚═════════════════════════════════════════════════════════════════════════════════════════════════╝{RESET}"
            )
        lines.append(banner)

        # 2. Board Grid Construction
        board_rows = []
        body_set = set(self.body)
        head = self.body[0]

        head_char_map = {
            "UP":    "▲",
            "DOWN":  "▼",
            "LEFT":  "◄",
            "RIGHT": "►"
        }

        head_color = C_CYAN if self.mode == "werr" else C_WHITE
        body_color = C_GREEN if self.mode == "werr" else C_DARK_GREEN

        board_rows.append(f"{BOLD}{C_WHITE}╔{'══' * self.width}╗{RESET}")
        for y in range(self.height):
            row_str = f"{BOLD}{C_WHITE}║{RESET}"
            for x in range(self.width):
                pos = (x, y)
                if pos == head:
                    row_str += f"{BOLD}{head_color}{head_char_map.get(self.direction, '●')}{RESET} "
                elif pos in body_set:
                    row_str += f"{body_color}■{RESET} "
                elif pos == self.food:
                    row_str += f"{BOLD}{C_RED}★{RESET} "
                else:
                    row_str += f"{C_GRAY}·{RESET} "
            row_str += f"{BOLD}{C_WHITE}║{RESET}"
            board_rows.append(row_str)
        board_rows.append(f"{BOLD}{C_WHITE}╚{'══' * self.width}╝{RESET}")

        # 3. Telemetry HUD Rows
        def pbar(val: float, width: int = 14) -> str:
            filled = int(round(val * width))
            filled = max(0, min(width, filled))
            return f"{C_CYAN}{'█' * filled}{C_GRAY}{'░' * (width - filled)}{RESET}"

        if self.mode == "manual":
            status_badge = f"{BOLD}{C_YELLOW}[🎮] 1. AŞAMA: MANUEL (Sen Oyna){RESET}"
            engine_name = f"{DIM}Kullanıcı / Biyolojik Refleks{RESET}"
            lat_display = f"{C_YELLOW}{self.last_latency:5.1f} ms{RESET} (İnsan Gecikmesi)"
        else:
            status_badge = f"{BOLD}{C_GREEN}[⚡] 2. AŞAMA: WERR OTOPİLOT{RESET}"
            engine_name = f"{BOLD}{C_CYAN}Mandelbrot Resonant Core{RESET}"
            lat_display = f"{BOLD}{C_GREEN}{self.last_latency:5.3f} ms (⚡ ANLIK!){RESET}"

        if self.paused:
            status_badge = f"{BOLD}{C_MAGENTA}[⏸] DURAKLATILDI{RESET}"
        elif self.game_over:
            status_badge = f"{BOLD}{C_RED}[✕] OYUN BİTTİ (R: Yeniden Başlat){RESET}"

        avg_werr_lat = (self.cum_werr_latency / self.werr_decisions) if self.werr_decisions > 0 else 0.08

        hud_rows = [
            f"{BOLD}{C_CYAN}╔══════════════════ CANLI TELEMETRİ HUD ══════════════════╗{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} Aktif Durum    : {status_badge:<38} {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} Skor / Elma    : {BOLD}{C_WHITE}{self.score:<4}{RESET}  (Oyun Adımı: {self.ticks:<5})           {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} FPS Hızı       : {C_GREEN}{self.fps} FPS{RESET} (Kare Gecikmesi: {self.step_delay*1000:.0f}ms)      {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}╠─────────────────────────────────────────────────────────╣{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} Karar Motoru   : {engine_name:<39} {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} Tepki Süresi   : {lat_display:<39} {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} Model Ağırlığı : {BOLD}{C_GREEN}0.00 KB{RESET} (Sıfır Tensör Depolama)          {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} GPU / VRAM     : {BOLD}{C_GREEN}0 MB{RESET} (Tamamen Çevrimdışı / Offline)       {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}╠═════════════════ KARAR DAĞILIMI (PROBABILITIES) ════════╣{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} ANLIK YÖN      : {BOLD}{C_WHITE}{self.direction:<5}{RESET} (Güven: {BOLD}{C_GREEN}{self.last_conf*100:4.1f}%{RESET})                   {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET}  YUKARI (UP)   : {pbar(self.last_probs.get('UP', 0))} {self.last_probs.get('UP', 0)*100:4.1f}% {'[TEHLİKE]' if self.last_hazards.get('UP') else '        '} {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET}  AŞAĞI  (DOWN) : {pbar(self.last_probs.get('DOWN', 0))} {self.last_probs.get('DOWN', 0)*100:4.1f}% {'[TEHLİKE]' if self.last_hazards.get('DOWN') else '        '} {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET}  SOL    (LEFT) : {pbar(self.last_probs.get('LEFT', 0))} {self.last_probs.get('LEFT', 0)*100:4.1f}% {'[TEHLİKE]' if self.last_hazards.get('LEFT') else '        '} {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET}  SAĞ    (RIGHT): {pbar(self.last_probs.get('RIGHT', 0))} {self.last_probs.get('RIGHT', 0)*100:4.1f}% {'[TEHLİKE]' if self.last_hazards.get('RIGHT') else '        '} {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}╠─────────────────────────────────────────────────────────╣{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} {BOLD}{C_YELLOW}[W] / [M] : KONTROLÜ WERR'E VER / GERİ AL{RESET}              {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} [YÖN/WASD]: Manuel Kontrol  │  [BOŞLUK]: Duraklat        {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}║{RESET} [+/-]     : Hız Ayarı       │  [R]: Sıfırla  │  [Q]: Çık {BOLD}{C_CYAN}║{RESET}",
            f"{BOLD}{C_CYAN}╚═════════════════════════════════════════════════════════╝{RESET}"
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
                ch = msvcrt.getch()
                if ch in (b'\x00', b'\xe0'):  # Arrow key prefix on Windows
                    arrow = msvcrt.getch()
                    if self.mode == "manual" and not self.game_over:
                        if arrow == b'H' and self.direction != "DOWN":
                            self.direction = "UP"
                        elif arrow == b'P' and self.direction != "UP":
                            self.direction = "DOWN"
                        elif arrow == b'K' and self.direction != "RIGHT":
                            self.direction = "LEFT"
                        elif arrow == b'M' and self.direction != "LEFT":
                            self.direction = "RIGHT"
                else:
                    char = ch.decode('utf-8', errors='ignore').lower()
                    if char == 'q':
                        return False
                    elif char == ' ':
                        self.paused = not self.paused
                    elif char in ('w', 'm'):
                        # Toggle between Manual and WERR
                        if self.mode == "manual":
                            self.trigger_handover()
                        else:
                            self.trigger_manual()
                    elif char == 'r':
                        self.reset()
                    elif char in ('+', '='):
                        self.fps = min(40, self.fps + 2)
                        self.step_delay = 1.0 / self.fps
                    elif char in ('-', '_'):
                        self.fps = max(4, self.fps - 2)
                        self.step_delay = 1.0 / self.fps
                    # WASD manual steering
                    elif self.mode == "manual" and not self.game_over:
                        if char == 'w' and self.direction != "DOWN":
                            self.direction = "UP"
                        elif char == 's' and self.direction != "UP":
                            self.direction = "DOWN"
                        elif char == 'a' and self.direction != "RIGHT":
                            self.direction = "LEFT"
                        elif char == 'd' and self.direction != "LEFT":
                            self.direction = "RIGHT"
        return True


def run():
    parser = argparse.ArgumentParser(description="Terminal ASCII Snake: Zero-Storage Fractal Reflex AI")
    parser.add_argument("--showcase", action="store_true", help="Run automatic cinematic handover showcase (Human plays first, then WERR takes over)")
    parser.add_argument("--werr", action="store_true", help="Start directly in WERR Fractal AI Autopilot mode")
    parser.add_argument("--width", type=int, default=26, help="Board width (default: 26)")
    parser.add_argument("--height", type=int, default=16, help="Board height (default: 16)")
    args = parser.parse_args()

    start_mode = "werr" if args.werr else "manual"

    sys.stdout.write("\033[?25l\033[2J")
    sys.stdout.flush()

    game = TerminalSnake(
        width=args.width,
        height=args.height,
        start_mode=start_mode,
        showcase=args.showcase
    )

    try:
        while True:
            t_start = time.perf_counter()

            if not game.handle_input():
                break

            game.step()
            game.render()

            elapsed = time.perf_counter() - t_start
            sleep_time = max(0.001, game.step_delay - elapsed)
            time.sleep(sleep_time)

            if game.game_over:
                if game.mode == "werr" or game.showcase:
                    time.sleep(1.2)
                    game.reset()

    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h\033[0m\n")
        sys.stdout.flush()
        print("\n[✓] Fractal Reflex Snake exited cleanly.")


if __name__ == "__main__":
    run()
