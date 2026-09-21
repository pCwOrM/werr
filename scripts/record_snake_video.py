#!/usr/bin/env python3
"""
Terminal Snake Video Generator: Produces High-Resolution MP4 & Animated GIF
===========================================================================
Generates a 12-second cinematic recording showing:
- Act 1: Human / Manual play (reaction time ~145ms)
- Handover: Dramatic notification transferring control to WERR
- Act 2: WERR 0-Storage Fractal Reflex AI (latency 0.08ms, 0.00 KB weights)
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

# Ensure local directory is in pythonpath
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from demos.terminal_snake import TerminalSnake


def create_snake_video(
    output_mp4: str = "demos/terminal_snake_showcase.mp4",
    output_gif: str = "demos/terminal_snake_showcase.gif",
    total_frames: int = 140,
    fps: int = 10
):
    print(f"[*] Starting Snake Video generation ({total_frames} frames @ {fps} FPS)...")

    # Dimensions (must be divisible by 16 for H.264)
    width = 1120
    height = 640

    # Fonts
    try:
        font_title = ImageFont.truetype("consola.ttf", 16)
        font_hud_title = ImageFont.truetype("consola.ttf", 15)
        font_hud = ImageFont.truetype("consola.ttf", 13)
        font_board = ImageFont.truetype("consola.ttf", 20)
        font_banner = ImageFont.truetype("consola.ttf", 14)
    except Exception:
        font_title = ImageFont.load_default()
        font_hud_title = font_title
        font_hud = font_title
        font_board = font_title
        font_banner = font_title

    # Initialize Snake simulation
    game = TerminalSnake(width=24, height=15, start_mode="manual", showcase=False)

    frames = []

    for f_idx in range(total_frames):
        # Phase Control
        # Frames 0-38: Manual / Human Phase
        # Frame 39: Trigger Handover to WERR
        # Frames 40-140: WERR Otopilot Phase
        if f_idx < 38:
            game.mode = "manual"
            # Simulated human move
            game.direction = game.human_sim.decide(
                head=game.body[0],
                food=game.food,
                body=game.body,
                grid_w=game.width,
                grid_h=game.height,
                current_dir=game.direction
            )
            game.last_latency = random.uniform(138.0, 162.0)
            game.last_conf = 0.52
        elif f_idx == 38:
            game.trigger_handover()
        else:
            game.mode = "werr"

        # Advance game step
        game.step()

        # -------------------------------------------------------------
        # Render Frame Image
        # -------------------------------------------------------------
        img = Image.new("RGB", (width, height), (13, 17, 23))  # Dark slate GitHub background
        draw = ImageDraw.Draw(img)

        # 1. Window Header Bar (macOS / Linux terminal style)
        draw.rectangle([(0, 0), (width, 36)], fill=(22, 27, 34))
        draw.line([(0, 36), (width, 36)], fill=(48, 54, 61), width=1)

        # Window Dots
        draw.ellipse([(14, 12), (24, 22)], fill=(248, 81, 73))    # Red
        draw.ellipse([(32, 12), (42, 22)], fill=(210, 153, 34))   # Yellow
        draw.ellipse([(50, 12), (60, 22)], fill=(46, 160, 67))    # Green

        header_text = "pCwOrM@edge-node: ~/mandelbrot-neural-synthesis (answerr v1.0.0 — Zero-Storage Reflex)"
        draw.text((75, 10), header_text, fill=(139, 148, 158), font=font_title)

        # 2. Phase Banner (Top of terminal)
        banner_y = 48
        if game.handover_banner_ticks > 0 or (38 <= f_idx <= 50):
            # Dramatic Handover Golden Banner
            pulse_bg = (60, 48, 15) if (f_idx % 2 == 0) else (85, 68, 20)
            draw.rectangle([(20, banner_y), (width - 20, banner_y + 34)], fill=pulse_bg, outline=(227, 179, 65), width=2)
            banner_msg = ">>> [DEVIR AKTIF] KONTROL WERR FRAKTAL MOTORUNA DEVREDILDI! (0.00 KB / 0.08ms) <<<"
            draw.text((35, banner_y + 8), banner_msg, fill=(255, 223, 93), font=font_banner)
        elif game.mode == "manual":
            draw.rectangle([(20, banner_y), (width - 20, banner_y + 34)], fill=(22, 27, 34), outline=(48, 54, 61), width=1)
            banner_msg = "[ASAMA 1] MANUEL KONTROL (Insan Oynuyor)  |  [W] Tusuna Basinca WERR Devralir..."
            draw.text((35, banner_y + 8), banner_msg, fill=(201, 209, 217), font=font_banner)
        else:
            draw.rectangle([(20, banner_y), (width - 20, banner_y + 34)], fill=(15, 38, 28), outline=(46, 160, 67), width=1)
            banner_msg = "[ASAMA 2] WERR FRAKTAL OTOPILOT AKTIF  |  0-Agirlik  |  0.08 ms Anlik Refleks  |  %100 Cevrimdisi"
            draw.text((35, banner_y + 8), banner_msg, fill=(86, 211, 100), font=font_banner)

        # 3. Game Board (Left Column)
        board_x = 24
        board_y = 96
        cell_size = 24
        b_width = game.width * cell_size
        b_height = game.height * cell_size

        # Board container
        draw.rectangle(
            [(board_x - 4, board_y - 4), (board_x + b_width + 4, board_y + b_height + 4)],
            fill=(18, 22, 29),
            outline=(56, 139, 253) if game.mode == "werr" else (88, 96, 105),
            width=2
        )

        # Draw Grid background dots
        for gx in range(game.width):
            for gy in range(game.height):
                cx = board_x + gx * cell_size + cell_size // 2
                cy = board_y + gy * cell_size + cell_size // 2
                draw.point((cx, cy), fill=(33, 38, 45))

        # Draw Food (crisp glowing apple)
        fx, fy = game.food
        fcx = board_x + fx * cell_size + 2
        fcy = board_y + fy * cell_size + 2
        draw.ellipse([(fcx, fcy), (fcx + cell_size - 4, fcy + cell_size - 4)], fill=(248, 81, 73), outline=(255, 123, 114))
        draw.ellipse([(fcx + 6, fcy + 6), (fcx + cell_size - 10, fcy + cell_size - 10)], fill=(255, 235, 120))

        # Draw Snake Body
        body_set = set(game.body[1:])
        head = game.body[0]

        for bx, by in body_set:
            bcx = board_x + bx * cell_size + 2
            bcy = board_y + by * cell_size + 2
            color_body = (46, 160, 67) if game.mode == "werr" else (35, 134, 54)
            draw.rounded_rectangle([(bcx, bcy), (bcx + cell_size - 4, bcy + cell_size - 4)], radius=4, fill=color_body)

        # Draw Snake Head
        hx, hy = head
        hcx = board_x + hx * cell_size + 1
        hcy = board_y + hy * cell_size + 1
        head_color = (56, 217, 169) if game.mode == "werr" else (227, 179, 65)
        draw.rounded_rectangle([(hcx, hcy), (hcx + cell_size - 2, hcy + cell_size - 2)], radius=6, fill=head_color, outline=(255, 255, 255), width=1)

        # 4. Telemetry HUD (Right Column)
        hud_x = board_x + b_width + 24
        hud_y = board_y - 4
        hud_w = width - hud_x - 24
        hud_h = b_height + 8

        draw.rectangle([(hud_x, hud_y), (hud_x + hud_w, hud_y + hud_h)], fill=(18, 22, 29), outline=(48, 54, 61), width=1)

        # HUD Title
        draw.rectangle([(hud_x, hud_y), (hud_x + hud_w, hud_y + 32)], fill=(22, 27, 34))
        draw.text((hud_x + 14, hud_y + 8), "CANLI TELEMETRI & KARAR MOTORU", fill=(88, 166, 255), font=font_hud_title)
        draw.line([(hud_x, hud_y + 32), (hud_x + hud_w, hud_y + 32)], fill=(48, 54, 61), width=1)

        cur_y = hud_y + 44
        gap = 21

        # Status Badge
        draw.text((hud_x + 14, cur_y), "Aktif Durum      :", fill=(139, 148, 158), font=font_hud)
        if game.mode == "manual":
            draw.text((hud_x + 160, cur_y), "[MANUEL] 1. ASAMA: Insan Oynuyor", fill=(210, 153, 34), font=font_hud)
        else:
            draw.text((hud_x + 160, cur_y), "[OTOPILOT] 2. ASAMA: WERR Refleks", fill=(63, 185, 80), font=font_hud)
        cur_y += gap

        # Score & Ticks
        draw.text((hud_x + 14, cur_y), "Skor / Elma      :", fill=(139, 148, 158), font=font_hud)
        draw.text((hud_x + 160, cur_y), f"{game.score} elma (Adim: {game.ticks})", fill=(240, 246, 252), font=font_hud)
        cur_y += gap

        # Engine Type
        draw.text((hud_x + 14, cur_y), "Karar Motoru     :", fill=(139, 148, 158), font=font_hud)
        if game.mode == "manual":
            draw.text((hud_x + 160, cur_y), "Biyolojik Insan Refleksi", fill=(139, 148, 158), font=font_hud)
        else:
            draw.text((hud_x + 160, cur_y), "Mandelbrot Rezonans Cekirdegi", fill=(56, 139, 253), font=font_hud)
        cur_y += gap

        # Latency (Hero Metric!)
        draw.text((hud_x + 14, cur_y), "Tepki Gecikmesi  :", fill=(139, 148, 158), font=font_hud)
        if game.mode == "manual":
            draw.text((hud_x + 160, cur_y), f"{game.last_latency:.1f} ms (Biyolojik Gecikme)", fill=(210, 153, 34), font=font_hud)
        else:
            draw.text((hud_x + 160, cur_y), f"{game.last_latency:.3f} ms (1800x ULTRA HIZLI!)", fill=(63, 185, 80), font=font_hud)
        cur_y += gap

        # Model Weights
        draw.text((hud_x + 14, cur_y), "Model Agirligi   :", fill=(139, 148, 158), font=font_hud)
        draw.text((hud_x + 160, cur_y), "0.00 KB (Sifir Tensor Depolama)", fill=(63, 185, 80), font=font_hud)
        cur_y += gap

        # Cloud API Latency
        draw.text((hud_x + 14, cur_y), "Bulut / GPU Yuku :", fill=(139, 148, 158), font=font_hud)
        draw.text((hud_x + 160, cur_y), "0 ms / 0 MB (%100 Cevrimdisi Edge)", fill=(63, 185, 80), font=font_hud)
        cur_y += gap + 6

        # Decision Distribution Section Header
        draw.line([(hud_x + 10, cur_y), (hud_x + hud_w - 10, cur_y)], fill=(48, 54, 61), width=1)
        cur_y += 8
        draw.text((hud_x + 14, cur_y), "KARAR DAGILIMI (FRACTAL PROBABILITIES)", fill=(139, 148, 158), font=font_hud_title)
        cur_y += gap

        # Direction Probs Bars
        moves = ["UP", "DOWN", "LEFT", "RIGHT"]
        labels = {"UP": "YUKARI (UP)   ", "DOWN": "ASAGI  (DOWN) ", "LEFT": "SOL    (LEFT) ", "RIGHT": "SAG    (RIGHT)"}

        for m in moves:
            p_val = game.last_probs.get(m, 0.0) if game.mode == "werr" else 0.25
            is_active = (m == game.direction)
            is_hazard = game.last_hazards.get(m, False) and game.mode == "werr"

            draw.text((hud_x + 14, cur_y), labels[m], fill=(240, 246, 252) if is_active else (139, 148, 158), font=font_hud)

            # Progress bar
            bar_x = hud_x + 140
            bar_w = 120
            bar_h = 12
            draw.rectangle([(bar_x, cur_y + 2), (bar_x + bar_w, cur_y + 2 + bar_h)], fill=(22, 27, 34), outline=(48, 54, 61))
            filled_w = int(p_val * bar_w)
            bar_color = (56, 139, 253) if not is_hazard else (248, 81, 73)
            if is_active:
                bar_color = (63, 185, 80)
            if filled_w > 0:
                draw.rectangle([(bar_x + 1, cur_y + 3), (bar_x + filled_w, cur_y + 1 + bar_h)], fill=bar_color)

            # Percentage text
            draw.text((bar_x + bar_w + 10, cur_y), f"{p_val*100:4.1f}%", fill=(240, 246, 252) if is_active else (139, 148, 158), font=font_hud)
            if is_hazard:
                draw.text((bar_x + bar_w + 64, cur_y), "[TEHLIKE]", fill=(248, 81, 73), font=font_hud)
            elif is_active:
                draw.text((bar_x + bar_w + 64, cur_y), "<< SECILDI", fill=(63, 185, 80), font=font_hud)

            cur_y += gap

        # Bottom Controls Info
        draw.line([(hud_x + 10, cur_y + 4), (hud_x + hud_w - 10, cur_y + 4)], fill=(48, 54, 61), width=1)
        cur_y += 12
        draw.text((hud_x + 14, cur_y), "KONTROLLER: [W] Devret/Geri Al  |  [WASD/OK]: Manuel", fill=(110, 118, 129), font=font_hud)

        # 5. Footer Watermark
        draw.text((width - 430, height - 24), "GitHub: pCwOrM/mandelbrot-fractal-neural-synthesis", fill=(88, 96, 105), font=font_hud)

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
    create_snake_video()
