"""
WERR Snake Terminal Visualizer & Automatic GIF Recorder.
Visualizes WERR System-One agent playing Snake live in terminal with ANSI colors,
and optionally renders the terminal frames directly into an animated GIF.
"""

import sys
import os
import time
import argparse
from pathlib import Path
from typing import List, Tuple, Optional

from PIL import Image, ImageDraw, ImageFont

# Set WERR telemetry off for pure high-speed decision loop
os.environ["WERR_TELEMETRY"] = "0"

current_dir = Path(__file__).resolve().parent
repo_root = current_dir.parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from benchmarks.snake.snake_game import SnakeGame
from benchmarks.snake.werr_snake_policy import WerrSnakePolicy


def render_ascii_board(game: SnakeGame, decision_str: str, latency_ms: float, step: int) -> Tuple[str, List[str]]:
    """Returns ANSI formatted string for terminal and raw lines for image rendering."""
    w, h = game.width, game.height
    head = game.head
    body_set = set(game.body)
    food = game.food

    raw_lines = []
    # Title / HUD
    raw_lines.append("=" * (w * 2 + 4))
    raw_lines.append("  WERR SYSTEM-ONE SNAKE | 0-BYTE VRAM FRACTAL KERNEL")
    raw_lines.append(f"  Step: {step:04d} | Score: {game.score:02d} | Latency: {latency_ms:.2f} ms | Move: {decision_str}")
    raw_lines.append("=" * (w * 2 + 4))

    # Top border
    raw_lines.append("+" + "-" * (w * 2 + 2) + "+")
    
    for y in range(h):
        row_chars = []
        for x in range(w):
            cell = (x, y)
            if cell == head:
                row_chars.append("@ ")
            elif cell == food:
                row_chars.append("$ ")
            elif cell in body_set:
                row_chars.append("# ")
            else:
                row_chars.append(". ")
        raw_lines.append("| " + "".join(row_chars) + "|")

    # Bottom border
    raw_lines.append("+" + "-" * (w * 2 + 2) + "+")
    raw_lines.append(f"  Coordinates: cx=-0.7445, cy=0.1250 | Zoom: 65x | RAM: 0B")
    raw_lines.append("=" * (w * 2 + 4))

    # ANSI version for live stdout
    ansi_lines = []
    ansi_lines.append("\033[1;36m" + raw_lines[0] + "\033[0m")
    ansi_lines.append("\033[1;32m" + raw_lines[1] + "\033[0m")
    ansi_lines.append("\033[1;33m" + raw_lines[2] + "\033[0m")
    ansi_lines.append("\033[1;36m" + raw_lines[3] + "\033[0m")
    ansi_lines.append("\033[1;34m" + raw_lines[4] + "\033[0m")

    for line in raw_lines[5:5+h]:
        colored = line.replace("@ ", "\033[1;32m@ \033[0m") \
                      .replace("$ ", "\033[1;31m$ \033[0m") \
                      .replace("# ", "\033[0;32m# \033[0m") \
                      .replace(". ", "\033[1;30m. \033[0m")
        ansi_lines.append(colored)

    ansi_lines.append("\033[1;34m" + raw_lines[5+h] + "\033[0m")
    ansi_lines.append("\033[0;37m" + raw_lines[6+h] + "\033[0m")
    ansi_lines.append("\033[1;36m" + raw_lines[7+h] + "\033[0m")

    return "\n".join(ansi_lines), raw_lines


def get_monospace_font(size: int = 15):
    font_paths = [
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cascadiamono.ttf",
        "C:/Windows/Fonts/lucon.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/System/Library/Fonts/Menlo.ttc"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def render_frame_to_image(lines: List[str]) -> Image.Image:
    """Renders monospace lines onto a dark terminal canvas with macOS window buttons."""
    font = get_monospace_font(15)
    
    # Exact monospace advance and line height
    char_w = int(round(font.getlength("M"))) if hasattr(font, 'getlength') else 8
    ascent, descent = font.getmetrics() if hasattr(font, 'getmetrics') else (12, 4)
    char_h = ascent + descent + 2

    pad_x = 24
    pad_y = 52
    max_len = max(len(l) for l in lines)
    img_w = max_len * char_w + pad_x * 2
    img_h = len(lines) * char_h + pad_y + 24
    # Ensure even dimensions for H.264 / MP4 compatibility
    if img_w % 2 != 0:
        img_w += 1
    if img_h % 2 != 0:
        img_h += 1

    # Background
    bg_color = (20, 22, 34)  # Dark navy/slate
    img = Image.new("RGB", (img_w, img_h), bg_color)
    draw = ImageDraw.Draw(img)

    # Window header bar
    draw.rectangle([(0, 0), (img_w, 40)], fill=(28, 31, 48))

    # Window buttons (macOS style)
    draw.ellipse([(pad_x, 14), (pad_x + 12, 26)], fill=(255, 95, 86))     # Red
    draw.ellipse([(pad_x + 20, 14), (pad_x + 32, 26)], fill=(255, 189, 46)) # Yellow
    draw.ellipse([(pad_x + 40, 14), (pad_x + 52, 26)], fill=(39, 201, 63))  # Green

    # Window title
    draw.text((pad_x + 70, 12), "werr@terminal: ~/benchmarks/snake", fill=(140, 150, 180), font=font)

    # Monospace text lines
    y = pad_y
    for line in lines:
        if line.startswith("=") or line.startswith("+"):
            draw.text((pad_x, y), line, fill=(99, 102, 241), font=font)
        elif "WERR SYSTEM-ONE" in line:
            draw.text((pad_x, y), line, fill=(0, 255, 170), font=font)
        elif "Step:" in line:
            draw.text((pad_x, y), line, fill=(255, 215, 0), font=font)
        elif "Coordinates:" in line:
            draw.text((pad_x, y), line, fill=(148, 163, 184), font=font)
        elif line.startswith("|"):
            x = pad_x
            for char in line:
                if char == "@":
                    c_fill = (50, 255, 120)  # Bright green head
                elif char == "$":
                    c_fill = (255, 75, 75)   # Bright red food
                elif char == "#":
                    c_fill = (34, 197, 94)   # Emerald green body
                elif char == ".":
                    c_fill = (60, 70, 95)    # Dim grid dots
                elif char == "|":
                    c_fill = (99, 102, 241)  # Purple border
                else:
                    c_fill = (200, 210, 230)
                draw.text((x, y), char, fill=c_fill, font=font)
                x += char_w
        else:
            draw.text((pad_x, y), line, fill=(160, 175, 200), font=font)
        y += char_h

    return img


def main():
    parser = argparse.ArgumentParser(description="WERR Snake Live Visualizer & Automatic GIF/MP4 Recorder")
    parser.add_argument("--steps", type=int, default=80, help="Number of game steps to run (default: 80)")
    parser.add_argument("--width", type=int, default=18, help="Board width (default: 18)")
    parser.add_argument("--height", type=int, default=12, help="Board height (default: 12)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
    parser.add_argument("--fps", type=int, default=10, help="Playback & Video FPS (default: 10)")
    parser.add_argument("--record", type=str, default=None, help="Output media filename (.gif or .mp4)")
    parser.add_argument("--tape", type=str, default=None, help="Export Charmbracelet VHS .tape script")
    args = parser.parse_args()

    policy = WerrSnakePolicy(guarded=True, prompt="compact", resolution=32, max_iter=30)
    game = SnakeGame(width=args.width, height=args.height, seed=args.seed)

    frames: List[Image.Image] = []
    delay = 1.0 / args.fps

    print("\033[2J\033[H", end="")  # Clear screen

    for step in range(args.steps):
        decision = policy.decide(game)
        game.step(decision.executed)

        ansi_frame, raw_lines = render_ascii_board(game, decision.executed, decision.inference_ms, step)

        # Print to terminal
        sys.stdout.write("\033[H" + ansi_frame + "\n")
        sys.stdout.flush()

        if args.record:
            img = render_frame_to_image(raw_lines)
            frames.append(img)

        if not game.alive:
            break

        time.sleep(delay)

    if args.record and frames:
        out_path = Path(args.record)
        is_mp4 = out_path.suffix.lower() == ".mp4"
        
        if is_mp4:
            print(f"\n[INFO] Encoding MP4 video (H.264) with {len(frames)} frames to {args.record}...")
            try:
                import numpy as np
                import imageio.v3 as iio
                np_frames = np.array([np.array(f) for f in frames])
                iio.imwrite(str(out_path), np_frames, fps=args.fps, codec="libx264")
                print(f"[SUCCESS] MP4 video generated: {args.record} ({os.path.getsize(args.record) // 1024} KB)")
            except Exception as e:
                print(f"[ERROR] Failed to write MP4 with imageio: {e}")
        else:
            print(f"\n[INFO] Saving animated GIF with {len(frames)} frames to {args.record}...")
            duration_ms = int(1000 / args.fps)
            frames[0].save(
                args.record,
                save_all=True,
                append_images=frames[1:],
                duration=duration_ms,
                loop=0,
                optimize=True
            )
            print(f"[SUCCESS] GIF generated successfully: {args.record} ({os.path.getsize(args.record) // 1024} KB)")

    if args.tape:
        tape_content = f"""# VHS tape for Werr Snake Benchmark
Output {Path(args.tape).with_suffix('.gif')}
Set FontSize 16
Set Width 800
Set Height 600
Set Padding 20
Set Theme "Catppuccin Mocha"

Type "python benchmarks/snake/visualize_snake.py --steps {args.steps} --fps {args.fps}"
Enter
Sleep {int(args.steps / args.fps) + 2}s
"""
        with open(args.tape, "w", encoding="utf-8") as f:
            f.write(tape_content)
        print(f"[SUCCESS] VHS tape script saved to: {args.tape}")


if __name__ == "__main__":
    main()
