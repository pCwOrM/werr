#!/usr/bin/env python3
"""
Terminal Snake Arena Video Generator: Produces High-Resolution MP4 & Animated GIF
================================================================================
Generates a 14-second cinematic recording showing:
- 1v1 AI Battle: 🔴 Simulated Cloud API Agent vs 🟢 WERR 0-Weight Fractal Reflex
- Live Comparative Telemetry HUD:
  * Latency: ~160ms (Cloud Lag) vs 0.08ms (WERR Reflex ⚡ 1800x faster)
  * Memory: Cloud Server vs 0.00 KB Local Procedural
  * Cost: $0.0004/step accumulating vs $0.0000 Free
"""

import os
import sys
import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from demos.terminal_snake_arena import ArenaSnakeGame


def create_arena_video(
    output_mp4: str = "demos/terminal_snake_arena_showcase.mp4",
    output_gif: str = "demos/terminal_snake_arena_showcase.gif",
    total_frames: int = 140,
    fps: int = 10
):
    print(f"[*] Starting Snake Arena Video generation ({total_frames} frames @ {fps} FPS)...")

    # Dimensions
    width = 1180
    height = 640

    # Fonts
    try:
        font_title = ImageFont.truetype("consola.ttf", 16)
        font_hud_title = ImageFont.truetype("consola.ttf", 15)
        font_hud_bold = ImageFont.truetype("consolab.ttf", 14)
        font_hud = ImageFont.truetype("consola.ttf", 13)
        font_board = ImageFont.truetype("consola.ttf", 20)
        font_banner = ImageFont.truetype("consola.ttf", 14)
    except Exception:
        font_title = ImageFont.load_default()
        font_hud_title = font_title
        font_hud_bold = font_title
        font_hud = font_title
        font_board = font_title
        font_banner = font_title

    # Initialize Arena
    game = ArenaSnakeGame(width=26, height=16)

    frames = []

    for f_idx in range(total_frames):
        # Step the arena match
        game.step()

        # Render Frame
        img = Image.new("RGB", (width, height), (10, 14, 23))  # Dark sleek terminal canvas
        draw = ImageDraw.Draw(img)

        # 1. Terminal Window Header Bar
        draw.rectangle([(0, 0), (width, 36)], fill=(22, 27, 34))
        draw.line([(0, 36), (width, 36)], fill=(48, 54, 61), width=1)

        # Window Dots
        draw.ellipse([(14, 12), (24, 22)], fill=(248, 81, 73))    # Red
        draw.ellipse([(32, 12), (42, 22)], fill=(210, 153, 34))   # Yellow
        draw.ellipse([(50, 12), (60, 22)], fill=(46, 160, 67))    # Green

        header_text = "pCwOrM@edge-node: ~/mandelbrot-neural-synthesis (demos/terminal_snake_arena.py — 1v1 Arena Match)"
        draw.text((75, 10), header_text, fill=(139, 148, 158), font=font_title)

        # 2. Dramatic Arena Top Banner
        draw.rectangle([(20, 50), (width - 20, 92)], fill=(244, 63, 94, 30), outline=(244, 63, 94))
        banner_text = "⚔️  TERMINAL AI ARENA: 🔴 Cloud API Simulator vs 🟢 WERR 0-Storage Fractal Reflex Engine"
        draw.text((36, 62), banner_text, fill=(255, 255, 255), font=font_banner)

        # 3. Game Board (Left Canvas)
        board_x = 24
        board_y = 106
        cell_size = 22
        board_w = game.width * cell_size
        board_h = game.height * cell_size

        draw.rectangle([(board_x - 3, board_y - 3), (board_x + board_w + 3, board_y + board_h + 3)],
                       fill=(9, 13, 22), outline=(48, 54, 61), width=2)

        # Grid dots
        for gx in range(game.width):
            for gy in range(game.height):
                dot_x = board_x + gx * cell_size + cell_size // 2
                dot_y = board_y + gy * cell_size + cell_size // 2
                draw.rectangle([(dot_x - 1, dot_y - 1), (dot_x + 1, dot_y + 1)], fill=(27, 33, 46))

        # Draw Foods
        for fx, fy in game.foods:
            px = board_x + fx * cell_size
            py = board_y + fy * cell_size
            draw.ellipse([(px + 3, py + 3), (px + cell_size - 3, py + cell_size - 3)], fill=(245, 158, 11))
            draw.ellipse([(px + 7, py + 7), (px + cell_size - 7, py + cell_size - 7)], fill=(254, 240, 138))

        # Draw Cloud Snake (Red)
        c_head = game.cloud_body[0]
        for idx, (sx, sy) in enumerate(game.cloud_body):
            px = board_x + sx * cell_size
            py = board_y + sy * cell_size
            color = (244, 63, 94) if idx == 0 else (190, 18, 60)
            draw.rectangle([(px + 2, py + 2), (px + cell_size - 2, py + cell_size - 2)], fill=color)

        # Draw Fractal/WERR Snake (Cyan & Emerald)
        f_head = game.fractal_body[0]
        for idx, (sx, sy) in enumerate(game.fractal_body):
            px = board_x + sx * cell_size
            py = board_y + sy * cell_size
            color = (56, 189, 248) if idx == 0 else (16, 185, 129)
            draw.rectangle([(px + 2, py + 2), (px + cell_size - 2, py + cell_size - 2)], fill=color)

        # 4. Right: Comparative Telemetry HUD Box
        hud_x = board_x + board_w + 24
        hud_y = 106
        hud_w = width - hud_x - 24
        hud_h = board_h + 6

        draw.rectangle([(hud_x, hud_y), (hud_x + hud_w, hud_y + hud_h)], fill=(15, 20, 31), outline=(48, 54, 61), width=1)

        # HUD Header
        draw.rectangle([(hud_x, hud_y), (hud_x + hud_w, hud_y + 36)], fill=(22, 29, 44))
        draw.text((hud_x + 14, hud_y + 10), "📊 ARENA TELEMETRY & SPEEDUP STATS", fill=(56, 189, 248), font=font_hud_title)

        cur_y = hud_y + 48
        line_h = 24

        def draw_hud_row(label, cloud_val, werr_val, highlight_werr=False):
            nonlocal cur_y
            draw.text((hud_x + 14, cur_y), label, fill=(148, 163, 184), font=font_hud)
            draw.text((hud_x + 160, cur_y), str(cloud_val), fill=(248, 81, 73), font=font_hud)
            w_color = (52, 211, 153) if highlight_werr else (240, 246, 252)
            draw.text((hud_x + 320, cur_y), str(werr_val), fill=w_color, font=font_hud_bold if highlight_werr else font_hud)
            cur_y += line_h

        # Column Labels
        draw.text((hud_x + 160, cur_y), "🔴 CLOUD API", fill=(244, 63, 94), font=font_hud_bold)
        draw.text((hud_x + 320, cur_y), "🟢 WERR REFLEKS", fill=(56, 189, 248), font=font_hud_bold)
        cur_y += line_h + 4
        draw.line([(hud_x + 10, cur_y - 2), (hud_x + hud_w - 10, cur_y - 2)], fill=(48, 54, 61), width=1)

        # Metric Rows
        draw_hud_row("Toplanan Elma:", f"{game.cloud_score} elma", f"{game.fractal_score} elma", highlight_werr=True)
        draw_hud_row("Son Gecikme:", f"{game.cloud_last_lat:5.1f} ms", f"{game.fractal_last_lat:5.2f} ms", highlight_werr=True)

        avg_c = (sum(game.cloud_latencies) / len(game.cloud_latencies)) if game.cloud_latencies else 150.0
        avg_f = (sum(game.fractal_latencies) / len(game.fractal_latencies)) if game.fractal_latencies else 0.08
        draw_hud_row("Ortalama Gecikme:", f"{avg_c:5.1f} ms (Lag)", f"{avg_f:5.2f} ms (Refleks)", highlight_werr=True)

        ratio = avg_c / max(0.01, avg_f)
        draw_hud_row("Hız Çarpanı:", "1.0x (Taban)", f"{ratio:4.0f}x DAHA HIZLI 🚀", highlight_werr=True)

        draw_hud_row("Kalıcı Ağırlık:", "Sunucu / 4-8 GB", "0.00 KB (24 Bayt Tohum)", highlight_werr=True)
        draw_hud_row("GPU / VRAM:", "0 MB (Uzak API)", "0 MB (%100 Çevrimdışı)", highlight_werr=True)
        draw_hud_row("Kümülatif Maliyet:", f"${game.cloud_brain.total_cost:.4f}", "$0.0000 (Ücretsiz)", highlight_werr=True)

        cur_y += 6
        draw.line([(hud_x + 10, cur_y), (hud_x + hud_w - 10, cur_y)], fill=(48, 54, 61), width=1)
        cur_y += 10

        draw.text((hud_x + 14, cur_y), f"ARENA ADIMI : {game.ticks} ticks", fill=(203, 213, 225), font=font_hud_bold)
        cur_y += line_h - 4
        draw.text((hud_x + 14, cur_y), "MİMARİ     : Sıfır-Bellek Mandelbrot Kaotik Sınır Rezonansı", fill=(100, 116, 139), font=font_hud)
        cur_y += line_h - 4
        draw.text((hud_x + 14, cur_y), "CANLI TEST : https://pcworm.github.io/mandelbrot-fractal-neural-synthesis/demos/snake.html", fill=(56, 189, 248), font=font_hud)

        # Footer Watermark
        draw.text((width - 440, height - 24), "GitHub: pCwOrM/mandelbrot-fractal-neural-synthesis", fill=(88, 96, 105), font=font_hud)

        frames.append(img)

    # -----------------------------------------------------------------
    # Save MP4 & GIF
    # -----------------------------------------------------------------
    os.makedirs(os.path.dirname(output_mp4), exist_ok=True)
    os.makedirs(os.path.dirname(output_gif), exist_ok=True)

    print(f"[*] Encoding MP4 video to {output_mp4}...")
    np_frames = [np.array(f) for f in frames]
    writer = imageio.get_writer(output_mp4, fps=fps, codec='libx264', quality=8)
    for n_frame in np_frames:
        writer.append_data(n_frame)
    writer.close()
    mp4_size_kb = os.path.getsize(output_mp4) / 1024.0
    print(f"[+] MP4 saved successfully: {output_mp4} ({mp4_size_kb:.1f} KB)")

    print(f"[*] Encoding Animated GIF to {output_gif}...")
    frames[0].save(
        output_gif,
        save_all=True,
        append_images=frames[1:],
        duration=int(1000 / fps),
        loop=0,
        optimize=True
    )
    gif_size_kb = os.path.getsize(output_gif) / 1024.0
    print(f"[+] GIF saved successfully: {output_gif} ({gif_size_kb:.1f} KB)")

    return output_mp4, output_gif


if __name__ == "__main__":
    create_arena_video()
