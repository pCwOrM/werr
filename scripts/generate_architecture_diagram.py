import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up figure with high DPI and academic styling
fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 4.5)
ax.axis('off')

# Font settings
font_family = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = font_family

# Colors (Clean academic palette: deep blues, slate, amber, soft grey background)
c_bg = '#f8fafc'
c_box_bg = '#ffffff'
c_primary = '#1e3a8a'     # Deep Navy
c_accent = '#0284c7'      # Cerulean
c_amber = '#d97706'       # Amber
c_emerald = '#059669'     # Emerald Green
c_text_dark = '#0f172a'   # Slate 900
c_text_muted = '#475569'  # Slate 600
c_border = '#cbd5e1'      # Slate 300

# Background container
bg_rect = patches.FancyBboxPatch((0.1, 0.1), 11.8, 4.3, boxstyle="round,pad=0.1,rounding_size=0.15",
                                 facecolor=c_bg, edgecolor='#e2e8f0', linewidth=1.2)
ax.add_patch(bg_rect)

def draw_block(ax, x, y, w, h, title, subtitle, items, header_color, border_color):
    # Main box
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08,rounding_size=0.1",
                                 facecolor=c_box_bg, edgecolor=border_color, linewidth=1.5, zorder=2)
    ax.add_patch(box)
    
    # Header bar
    header_h = 0.65
    header = patches.FancyBboxPatch((x, y + h - header_h), w, header_h,
                                    boxstyle="round,pad=0.05,rounding_size=0.08",
                                    facecolor=header_color, edgecolor=header_color, zorder=3)
    ax.add_patch(header)
    
    # Title
    ax.text(x + w/2, y + h - 0.25, title, ha='center', va='center',
            fontsize=9.5, fontweight='bold', color='#ffffff', zorder=4)
    ax.text(x + w/2, y + h - 0.50, subtitle, ha='center', va='center',
            fontsize=7.2, fontstyle='italic', color='#e2e8f0', zorder=4)
    
    # Body items
    curr_y = y + h - 0.95
    for item in items:
        ax.text(x + 0.15, curr_y, item, ha='left', va='center',
                fontsize=7.6, color=c_text_dark, zorder=4)
        curr_y -= 0.35

# Block 1: Input Program State & Queries
b1_items = [
    r"• State Dict: $\mathbf{s} = \{x_1, x_2, \dots, x_k\}$",
    r"• Typed Questions: $Q = \{q_1, \dots, q_m\}$",
    r"• Natural Language Prompts",
    r"• Zero Tensor / 0-VRAM Wire Format",
    r"• In-Memory Dict / JSON Stream"
]
draw_block(ax, 0.4, 0.5, 2.5, 3.4, "1. INGESTION APERTURE", "State & Question Map", b1_items, c_primary, '#94a3b8')

# Block 2: Auto-Seed Router & State Projector
b2_items = [
    r"• Domain Projector: $\Phi_D: \mathbf{s} \mapsto (\mathbf{v}, \rho)$",
    r"• Semantic Token Attenuation: $\mathcal{T}_{\mathrm{desc}}$",
    r"• Inverted Keyword Index ($< 0.05$ ms)",
    r"• 5 Operational Latent Gates",
    r"• Hash-Phase Angle for OOV Terms"
]
draw_block(ax, 3.25, 0.5, 2.6, 3.4, "2. AUTO-SEED ROUTER", "Domain Coordinate Projection", b2_items, c_accent, '#7dd3fc')

# Block 3: Chaotic Mandelbrot Boundary Map
b3_items = [
    r"• Boundary Seed: $c^* = c_0 + \delta(\mathbf{s})$",
    r"• Complex Perturbation: $\delta \in \mathbb{C}$",
    r"• $\mathbb{Z}/9\mathbb{Z}$ Resonant Grid ($36 \times 36$)",
    r"• Multi-Scale Tripod ($0.60\times, 1.0\times, 1.6\times$)",
    r"• Recurrence: $z_{n+1} = z_n^2 + c^*$"
]
draw_block(ax, 6.15, 0.5, 2.6, 3.4, "3. FRACTAL REFLEX CORE", "Mandelbrot Boundary Dynamics", b3_items, c_amber, '#fcd34d')

# Block 4: Typed Decision Primitives
b4_items = [
    r"• 4-Quadrant Potential $\mathbf{Q} \in \mathbb{R}^4$",
    r"• 16-Tile Quadtree Weights $\mathbf{T} \in \mathbb{R}^{16}$",
    r"• noul: Boolean Reflex + Conf",
    r"• choice: Categorical Probability",
    r"• score: Ordinal Regression Level"
]
draw_block(ax, 9.05, 0.5, 2.5, 3.4, "4. DECISION SYNTHESIS", "Strongly-Typed Output Primitives", b4_items, c_emerald, '#6ee7b7')

# Connecting Arrows
def draw_arrow(ax, x1, y1, x2, y2, label=""):
    arrow = patches.FancyArrowPatch((x1, y1), (x2, y2),
                                    arrowstyle='-|>,head_width=3.5,head_length=5',
                                    color='#475569', linewidth=2.0, zorder=5)
    ax.add_patch(arrow)
    if label:
        ax.text((x1 + x2)/2, y1 + 0.18, label, ha='center', va='bottom',
                fontsize=7.2, fontweight='bold', color='#1e293b', zorder=6)

draw_arrow(ax, 2.9, 2.2, 3.25, 2.2, r"$\mathbf{s}, Q$")
draw_arrow(ax, 5.85, 2.2, 6.15, 2.2, r"$\Phi_D(\mathbf{s})$")
draw_arrow(ax, 8.75, 2.2, 9.05, 2.2, r"$\mathbf{Q}, \mathbf{T}$")

# Bottom Banner: Theoretical & Physical Guarantees
banner = patches.FancyBboxPatch((0.4, 0.2), 11.15, 0.26, boxstyle="round,pad=0.03,rounding_size=0.05",
                                facecolor='#e2e8f0', edgecolor='#cbd5e1', linewidth=1.0, zorder=2)
ax.add_patch(banner)
ax.text(6.0, 0.33,
        r"$\mathbf{Guarantees:}$ 0 Bytes Tensor VRAM  •  24-Byte Coordinate Seed  •  Air-Gapped Determinism  •  Sub-10ms Edge Triage Latency",
        ha='center', va='center', fontsize=7.6, fontweight='bold', color='#1e293b', zorder=4)

plt.tight_layout()
out_path = r"C:\Users\maat\Documents\antigravity\wevv\paper\figures\twin_ecosystem_architecture.png"
plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='#ffffff')
print(f"[+] Saved clean academic architecture diagram to: {out_path}")
