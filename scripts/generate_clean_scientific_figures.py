import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

"""
Scientific Figure Generator for Orbital Error Dynamics (OED)
Generates 7 publication-ready, 100% original academic figures:
  1. fig1_observer_horizon.png: Mandelbrot boundary, cusp at c=1/4, inflection loci, escape vector field.
  2. fig2_bent_sine_and_cusp.png: Flatline vs harmonic sine vs bent sine dissipative cardioid cusp.
  3. fig3_quantum_tunneling_operator.png: Non-convex barrier, local trap, perturbed jump operator (zinc spark).
  4. fig4_nonequilibrium_phase_surfing.png: Phase portrait, attractor sink vs divergence vs limit surfing.
  5. fig5_dual_brain_cybernetics.png: Cranial-Enteric cybernetic loop with adaptive CD4+ immune gating mask.
  6. fig6_complex_4quadrant_genetics.png: 4-quadrant complex mapping (A, T, C, G) and zero-storage projection.
  7. fig7_empirical_benchmark.png: 5-seed rigorous benchmark (loss curves, noise resilience, memory scaling).
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import os

# Output directories
OUT_DIRS = [
    os.path.abspath("zenodo_preprint_package/figures"),
    os.path.abspath("private_archive_paper2/figures")
]

for d in OUT_DIRS:
    os.makedirs(d, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#2c3e50'
plt.rcParams['axes.linewidth'] = 1.2

def save_fig(fig, filename):
    for d in OUT_DIRS:
        path = os.path.join(d, filename)
        fig.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Saved: {filename}")
    plt.close(fig)

# ==============================================================================
# FIGURE 1: OBSERVER HORIZON & BOUNDARY GEOMETRY
# ==============================================================================
def generate_fig1():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    
    # Generate Mandelbrot boundary slice
    res = 400
    xmin, xmax, ymin, ymax = -1.6, 0.6, -1.1, 1.1
    xs = np.linspace(xmin, xmax, res)
    ys = np.linspace(ymin, ymax, res)
    X, Y = np.meshgrid(xs, ys)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    escape = np.full(C.shape, 60, dtype=float)
    mask = np.ones(C.shape, dtype=bool)
    
    for i in range(60):
        Z[mask] = Z[mask]**2 + C[mask]
        div = np.abs(Z) > 2.0
        newly_div = div & mask
        escape[newly_div] = i
        mask[div] = False
        if not np.any(mask):
            break
            
    im = ax.imshow(escape, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap='Blues_r', alpha=0.85)
    
    # Theoretical Main Cardioid Boundary
    t = np.linspace(0, 2*np.pi, 500)
    cardioid_x = 0.5 * np.cos(t) - 0.25 * np.cos(2*t)
    cardioid_y = 0.5 * np.sin(t) - 0.25 * np.sin(2*t)
    ax.plot(cardioid_x, cardioid_y, color='#c0392b', lw=2.0, linestyle='--', label=r'Cardioid Boundary $\partial\mathcal{M}$')
    
    # Mark the unique analytic cusp at c = 1/4
    ax.scatter([0.25], [0.0], color='#e74c3c', s=120, zorder=5, edgecolors='black', lw=1.5)
    ax.annotate(r'Analytic Cusp ($c = 1/4$)' + '\n' + r'Tangency Singularity',
                xy=(0.25, 0.0), xytext=(0.35, 0.45),
                arrowprops=dict(arrowstyle="->", color='#c0392b', lw=1.5),
                fontsize=10, fontweight='bold', color='#962d22',
                bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2e9", ec="#e08272", lw=1))
                
    # Mark Shoulder Inflection Loci X_upper and X_lower
    ax.scatter([0.25, 0.25], [0.18, -0.18], color='#2980b9', s=90, zorder=5, edgecolors='black', lw=1.2)
    ax.annotate(r'$\mathbf{X}_{upper} = (0.25, +0.18)$' + '\n' + r'Inflection Horizon Locus',
                xy=(0.25, 0.18), xytext=(-0.55, 0.75),
                arrowprops=dict(arrowstyle="->", color='#2980b9', lw=1.5),
                fontsize=9.5, color='#1b4f72',
                bbox=dict(boxstyle="round,pad=0.3", fc="#ebf5fb", ec="#85c1e9", lw=1))
                
    ax.annotate(r'$\mathbf{X}_{lower} = (0.25, -0.18)$' + '\n' + r'Inflection Horizon Locus',
                xy=(0.25, -0.18), xytext=(-0.55, -0.85),
                arrowprops=dict(arrowstyle="->", color='#2980b9', lw=1.5),
                fontsize=9.5, color='#1b4f72',
                bbox=dict(boxstyle="round,pad=0.3", fc="#ebf5fb", ec="#85c1e9", lw=1))

    # Surfing Corridor Annotation
    ax.annotate(r'Homeostatic Surfing Corridor' + '\n' + r'($\lambda \approx 0$, Non-Equilibrium Steady State)',
                xy=(-0.75, 0.25), xytext=(-1.45, 0.05),
                arrowprops=dict(arrowstyle="->", color='#27ae60', lw=2),
                fontsize=10, fontweight='bold', color='#1e8449',
                bbox=dict(boxstyle="round,pad=0.4", fc="#eafaf1", ec="#82e0aa", lw=1.2))

    # Escape Vector Arrows
    ax.quiver([0.45, 0.45], [0.3, -0.3], [0.15, 0.15], [0.15, -0.15], 
              color='#e67e22', scale=3.0, width=0.008, label=r'Radial Escape Flux $\mathbf{v}_{escape}$')

    ax.set_title("Figure 1: Parameter Space Geometry & Critical Boundary Loci\n$(\\partial\\mathcal{M}, \\text{Cardioid Cusp } c=1/4, \\text{ and Horizon Surfing Band})$",
                 fontsize=12, fontweight='bold', pad=12, color='#1a252f')
    ax.set_xlabel(r"$\mathrm{Re}(c)$ (Real Parameter Axis)", fontsize=11)
    ax.set_ylabel(r"$\mathrm{Im}(c)$ (Imaginary Parameter Axis)", fontsize=11)
    ax.legend(loc='lower left', framealpha=0.9, fontsize=9)
    ax.grid(True, linestyle=':', alpha=0.4, color='#7f8c8d')
    
    save_fig(fig, "fig1_observer_horizon.png")

# ==============================================================================
# FIGURE 2: BENT SINE WAVE & DISSIPATIVE CUSP
# ==============================================================================
def generate_fig2():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 4.2), dpi=300)
    
    t = np.linspace(0, 4*np.pi, 500)
    
    # 1. Equilibrium Flatline
    ax1.plot(t, np.zeros_like(t), color='#7f8c8d', lw=2.5)
    ax1.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_title("(a) Thermodynamic Death\n(Static Equilibrium)", fontsize=11, fontweight='bold', color='#34495e')
    ax1.set_xlabel("Time (t)", fontsize=10)
    ax1.set_ylabel("State Variable x(t)", fontsize=10)
    ax1.text(2*np.pi, 0.4, r"$\frac{dx}{dt} = 0, \quad \Delta S = 0$" + "\nZero Adaptive Capacity\nStatic Gradient Minimum", 
             ha='center', fontsize=9.5, color='#7f8c8d', bbox=dict(boxstyle="round", fc="#f8f9f9", ec="#d5dbdb"))
    ax1.grid(True, linestyle=':', alpha=0.4)
    
    # 2. Linear Harmonic Sine Wave
    y_harm = np.sin(t)
    ax2.plot(t, y_harm, color='#2980b9', lw=2.2)
    ax2.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_title("(b) Conservative Oscillation\n(Linear Reversible)", fontsize=11, fontweight='bold', color='#1b4f72')
    ax2.set_xlabel("Time (t)", fontsize=10)
    ax2.text(2*np.pi, 0.5, r"$x(t) = A\sin(\omega t)$" + "\nConservative Hamiltonian\nNo Information Dissipation", 
             ha='center', fontsize=9.5, color='#1b4f72', bbox=dict(boxstyle="round", fc="#ebf5fb", ec="#aed6f1"))
    ax2.grid(True, linestyle=':', alpha=0.4)
    
    # 3. Bent Sine Wave with Cusp Singularity
    # Non-linear folding: sin(t) with quadratic feedback and asymmetric cusp pinch
    y_bent = np.sin(t) - 0.45 * np.cos(2*t) * np.sign(np.sin(t))
    # Normalize and introduce sharp cusp pinch
    y_bent = 0.85 * np.sin(t) - 0.35 * (np.sin(t)**2) * np.sign(np.cos(t))
    ax3.plot(t, y_bent, color='#c0392b', lw=2.4)
    ax3.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax3.set_ylim(-1.5, 1.5)
    ax3.set_title("(c) Non-Equilibrium Bent Cycle\n(Dissipative Cardioid Cusp)", fontsize=11, fontweight='bold', color='#922b21')
    ax3.set_xlabel("Time (t)", fontsize=10)
    
    # Annotate cusp and non-equilibrium dissipation
    ax3.scatter([np.pi/2, 5*np.pi/2], [y_bent[int(500/8)], y_bent[int(500*5/8)]], color='#e74c3c', s=70, zorder=4)
    ax3.text(2*np.pi, 0.7, r"$\partial_t x = f(x) + \nabla \Phi$" + "\nNonlinear Cusp Dissipation\nContinuous Information Generation", 
             ha='center', fontsize=9.5, color='#922b21', bbox=dict(boxstyle="round", fc="#fdf2e9", ec="#f5b7b1"))
    ax3.grid(True, linestyle=':', alpha=0.4)
    
    fig.suptitle("Figure 2: Morphological Comparison of Cybernetic Dynamics Across Regimes", fontsize=13, fontweight='bold', y=1.03, color='#1a252f')
    plt.tight_layout()
    save_fig(fig, "fig2_bent_sine_and_cusp.png")

# ==============================================================================
# FIGURE 3: BIOMIMETIC PERTURBED JUMP OPERATOR (QUANTUM TUNNELING / ZINC SPARK)
# ==============================================================================
def generate_fig3():
    fig, ax = plt.subplots(figsize=(8.5, 5.2), dpi=300)
    
    x = np.linspace(-2.2, 2.5, 500)
    # Double-well potential with high barrier
    V = 0.5 * (x**4 - 3.2 * x**2 - 0.8 * x) + 2.0
    
    ax.plot(x, V, color='#2c3e50', lw=2.8, label=r'Non-Convex Energy Landscape $V(\Theta)$')
    
    # Fill potential
    ax.fill_between(x, V, 10, color='#eaeded', alpha=0.35)
    ax.set_ylim(-0.5, 6.0)
    
    # Local trapped minimum
    x_local = -1.35
    v_local = 0.5 * (x_local**4 - 3.2 * x_local**2 - 0.8 * x_local) + 2.0
    ax.scatter([x_local], [v_local], color='#e67e22', s=130, zorder=5, edgecolors='black', lw=1.5)
    
    ax.annotate("Suboptimal Local Minimum\n($\\nabla_\\Theta \\mathcal{L} \\to 0$, Gradient Stagnation)",
                xy=(x_local, v_local), xytext=(-2.1, 4.5),
                arrowprops=dict(arrowstyle="->", color='#d35400', lw=1.8),
                fontsize=9.5, fontweight='bold', color='#a04000',
                bbox=dict(boxstyle="round,pad=0.3", fc="#fef5e7", ec="#f8c471", lw=1.2))
                
    # Global optimal minimum
    x_glob = 1.48
    v_glob = 0.5 * (x_glob**4 - 3.2 * x_glob**2 - 0.8 * x_glob) + 2.0
    ax.scatter([x_glob], [v_glob], color='#27ae60', s=140, zorder=5, edgecolors='black', lw=1.5)
    ax.annotate("Global Functional Basin\n(Target Dynamic Attractor)",
                xy=(x_glob, v_glob), xytext=(1.0, 4.8),
                arrowprops=dict(arrowstyle="->", color='#27ae60', lw=1.8),
                fontsize=9.5, fontweight='bold', color='#196f3d',
                bbox=dict(boxstyle="round,pad=0.3", fc="#eafaf1", ec="#82e0aa", lw=1.2))
                
    # Barrier height arrow
    x_bar = -0.15
    v_bar = 0.5 * (x_bar**4 - 3.2 * x_bar**2 - 0.8 * x_bar) + 2.0
    ax.plot([x_bar, x_bar], [v_local, v_bar], color='#c0392b', linestyle='--', lw=1.8)
    ax.text(x_bar - 0.08, (v_local + v_bar)/2, r"$\Delta V_{barrier}$", color='#922b21', fontsize=11, fontweight='bold', ha='right')

    # Perturbed Jump Operator Trajectory (Cauchy / Zinc Spark)
    # Arc over/through barrier
    jump_x = np.linspace(x_local, x_glob, 100)
    jump_y = v_local + 0.8 * np.sin(np.pi * (jump_x - x_local) / (x_glob - x_local))
    ax.plot(jump_x, jump_y, color='#8e44ad', linestyle='-.', lw=2.4, 
            label=r'Biomimetic Jump $\Omega_{\mathrm{tunneling}} \sim \mathrm{Cauchy}(0, \gamma)$')
            
    # Wave packet decay through barrier
    bar_slice = np.linspace(-0.6, 0.4, 60)
    psi = 1.5 + 0.3 * np.exp(-3.5 * np.abs(bar_slice + 0.1)) * np.cos(25 * bar_slice)
    ax.plot(bar_slice, psi, color='#9b59b6', lw=1.8, label=r'Tunneling Amplitude $|\psi(x)|^2 \propto e^{-2\kappa d}$')
    
    ax.annotate(r"Biomimetic Zinc Spark Trigger" + "\n" + r"(\|\nabla \mathcal{L}\| < \epsilon_{tol} \rightarrow \Delta\Theta \sim \Omega)",
                xy=(0.0, 2.0), xytext=(-0.85, 0.4),
                arrowprops=dict(arrowstyle="->", color='#8e44ad', lw=1.8),
                fontsize=9.5, fontweight='bold', color='#5b2c6f',
                bbox=dict(boxstyle="round,pad=0.3", fc="#f4ecf7", ec="#bb8fce", lw=1.2))

    ax.set_title("Figure 3: Biomimetic Perturbed Jump Operator Escaping Non-Convex Gradient Traps\n" + 
                 r"(Formalizing Stochastic Quantum Tunneling Analogs in Neural Parameter Evolution)",
                 fontsize=11.5, fontweight='bold', pad=12, color='#1a252f')
    ax.set_xlabel(r"Parameter Coordinate Manifold $\Theta \in \mathbb{C} \times \mathbb{R}^+$", fontsize=10.5)
    ax.set_ylabel(r"Effective Energy / Loss Functional $\mathcal{L}(\Theta)$", fontsize=10.5)
    ax.legend(loc='upper right', framealpha=0.9, fontsize=9.2)
    ax.grid(True, linestyle=':', alpha=0.4)
    
    save_fig(fig, "fig3_quantum_tunneling_operator.png")

# ==============================================================================
# FIGURE 4: NON-EQUILIBRIUM PHASE SPACE SURFING
# ==============================================================================
def generate_fig4():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    
    theta = np.linspace(0, 10*np.pi, 1200)
    
    # 1. Hyperbolic Sink Collapse (Overfitting)
    r_sink = np.exp(-0.25 * theta)
    x_sink = r_sink * np.cos(theta) - 1.2
    y_sink = r_sink * np.sin(theta)
    ax.plot(x_sink, y_sink, color='#c0392b', lw=1.8, linestyle=':', label=r'Dead Attractor Collapse (Trivial Sink, $\lambda < 0$)')
    ax.scatter([-1.2], [0], color='#c0392b', s=80, marker='x', lw=2)
    
    # 2. Explosive Divergent Orbit (Gradient Explosion / Runaway)
    theta_div = np.linspace(0, 2.5*np.pi, 300)
    r_div = 0.2 * np.exp(0.4 * theta_div)
    x_div = r_div * np.cos(theta_div) + 1.2
    y_div = r_div * np.sin(theta_div)
    ax.plot(x_div, y_div, color='#e67e22', lw=1.8, linestyle='--', label=r'Unbounded Divergence (Runaway Chaos, $\lambda > 0$)')
    
    # 3. Homeostatic Surfing Limit Cycle (Active OED Regulation)
    theta_surf = np.linspace(0, 12*np.pi, 1500)
    # Perturbed quasi-periodic limit cycle
    r_surf = 0.95 + 0.12 * np.sin(3.5 * theta_surf) + 0.04 * np.cos(7.0 * theta_surf)
    x_surf = r_surf * np.cos(theta_surf)
    y_surf = r_surf * np.sin(theta_surf)
    ax.plot(x_surf, y_surf, color='#27ae60', lw=2.4, label=r'OED Horizon Surfing Orbit ($\lambda \approx 0$, Critical Edge)')
    
    # Flow quiver on the limit cycle
    idx_arrows = [100, 350, 600, 850, 1100]
    ax.quiver(x_surf[idx_arrows], y_surf[idx_arrows], 
              -y_surf[idx_arrows], x_surf[idx_arrows],
              color='#1e8449', scale=15.0, width=0.007)
              
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-1.8, 1.8)
    
    ax.annotate("Balance of Radial Acceleration & Damping:\n" + r"$\mathbf{a}_{net} = \nabla N_{esc} - \gamma_{visc} \mathbf{v}$",
                xy=(0.0, 1.05), xytext=(-0.9, 1.45),
                arrowprops=dict(arrowstyle="->", color='#27ae60', lw=1.5),
                fontsize=9.5, fontweight='bold', color='#145a32',
                bbox=dict(boxstyle="round,pad=0.3", fc="#eafaf1", ec="#82e0aa", lw=1.2))

    ax.set_title("Figure 4: Dynamic Phase Space $(z_n, z_{n+1})$ Portrait Under Orbital Regulation\n" + 
                 r"(Active Homeostatic Boundary Surfing vs. Catastrophic Sink & Chaotic Divergence)",
                 fontsize=11.5, fontweight='bold', pad=12, color='#1a252f')
    ax.set_xlabel(r"State Dimension $z_n$", fontsize=11)
    ax.set_ylabel(r"Evolving State Dimension $z_{n+1}$", fontsize=11)
    ax.legend(loc='lower left', framealpha=0.9, fontsize=9.2)
    ax.grid(True, linestyle=':', alpha=0.4)
    
    save_fig(fig, "fig4_nonequilibrium_phase_surfing.png")

# ==============================================================================
# FIGURE 5: DUAL-BRAIN CYBERNETICS & ADAPTIVE CD4+ IMMUNE GATING
# ==============================================================================
def generate_fig5():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # 1. Central / Cranial Brain Block
    cranial_box = patches.FancyBboxPatch((0.6, 3.2), 3.2, 2.2, boxstyle="round,pad=0.2", 
                                        fc="#ebf5fb", ec="#2980b9", lw=2)
    ax.add_patch(cranial_box)
    ax.text(2.2, 5.0, "CENTRAL / CRANIAL BRAIN", ha='center', fontsize=11, fontweight='bold', color='#1b4f72')
    ax.text(2.2, 4.4, "Seed Parameter: $\\Theta = (c_x, c_y, \\zeta)$\n" +
                      "Memory Footprint: $O(1) = 24$ Bytes\n" +
                      "Dynamics: Mandelbrot Sampler", ha='center', fontsize=9.2, color='#2c3e50')
    ax.text(2.2, 3.6, "Perturbed Jump: $\\Omega_{\\mathrm{tunneling}}$", ha='center', fontsize=9, fontweight='bold', color='#8e44ad')

    # 2. Enteric / Visceral Brain Block
    enteric_box = patches.FancyBboxPatch((6.2, 3.2), 3.2, 2.2, boxstyle="round,pad=0.2", 
                                        fc="#fef9e7", ec="#f39c12", lw=2)
    ax.add_patch(enteric_box)
    ax.text(7.8, 5.0, "ENTERIC / VISCERAL BRAIN", ha='center', fontsize=11, fontweight='bold', color='#7d6608')
    ax.text(7.8, 4.4, "Real-Time Sensory Input $X_{visc}$\n" +
                      "Local Fast Adaptation: $\\nabla_W \\mathcal{L}_{task}$\n" +
                      "High-Frequency Environmental Stream", ha='center', fontsize=9.2, color='#2c3e50')
    ax.text(7.8, 3.6, "Dynamic Error Flow: $\\mathcal{L}_{task}$", ha='center', fontsize=9, fontweight='bold', color='#d35400')

    # 3. Operational Weight Synthesis Arrow
    ax.annotate("", xy=(6.2, 4.5), xytext=(3.8, 4.5),
                arrowprops=dict(arrowstyle="->", color='#2980b9', lw=2.5))
    ax.text(5.0, 4.75, "Operational Weight Projection\n" + r"$W_t = \Phi(\Theta_t) \in \mathbb{R}^4$", 
            ha='center', fontsize=9.5, fontweight='bold', color='#1b4f72')

    # 4. CD4+ Adaptive Immune Gating Filter Block (Bottom Middle)
    cd4_box = patches.FancyBboxPatch((3.4, 0.6), 3.2, 1.8, boxstyle="round,pad=0.2", 
                                    fc="#fdf2e9", ec="#c0392b", lw=2)
    ax.add_patch(cd4_box)
    ax.text(5.0, 2.05, "ADAPTIVE CD4+ IMMUNE GATING", ha='center', fontsize=10.5, fontweight='bold', color='#922b21')
    ax.text(5.0, 1.4, r"Mask: $M_{CD4} = \sigma(-\alpha(\|\nabla\| - \tau))$" + "\n" +
                      "Adversarial / Toxin Attenuation\n" +
                      "Biological Vagus Filter", ha='center', fontsize=9, color='#641e16')

    # 5. Feedback Paths (Vagus Nerve Loop)
    # Down from Enteric to CD4+
    ax.annotate("", xy=(6.6, 1.5), xytext=(7.8, 3.2),
                arrowprops=dict(arrowstyle="->", color='#c0392b', lw=2, linestyle='--'))
    ax.text(7.7, 2.2, "Raw Visceral\nGradient $\\nabla_{visc}$", ha='center', fontsize=8.5, color='#922b21')

    # From CD4+ back to Cranial Brain
    ax.annotate("", xy=(2.2, 3.2), xytext=(3.4, 1.5),
                arrowprops=dict(arrowstyle="->", color='#27ae60', lw=2.5))
    ax.text(2.3, 2.1, "Shielded Homeostatic\nModulation $\\Delta\\Theta$", ha='center', fontsize=8.8, fontweight='bold', color='#196f3d')

    ax.set_title("Figure 5: Cybernetic Dual-Brain Architecture & Adaptive Immune Filter Flow\n" + 
                 "(Coupling O(1) Central Parameter Manifolds with High-Frequency Shielded Visceral Adaptation)",
                 fontsize=12, fontweight='bold', pad=14, color='#1a252f')
                 
    save_fig(fig, "fig5_dual_brain_cybernetics.png")

# ==============================================================================
# FIGURE 6: COMPLEX 4-QUADRANT GENETIC MAPPING
# ==============================================================================
def generate_fig6():
    fig, ax = plt.subplots(figsize=(7.5, 7.5), dpi=300)
    
    # Generate Mandelbrot patch
    grid_size = 200
    cx, cy, scale = -0.75, 0.1, 0.8
    xs = np.linspace(cx - scale, cx + scale, grid_size)
    ys = np.linspace(cy - scale, cy + scale, grid_size)
    X, Y = np.meshgrid(xs, ys)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    escape = np.full(C.shape, 40, dtype=float)
    mask = np.ones(C.shape, dtype=bool)
    
    for i in range(40):
        Z[mask] = Z[mask]**2 + C[mask]
        div = np.abs(Z) > 2.0
        escape[div & mask] = i
        mask[div] = False
        if not np.any(mask):
            break
            
    ax.imshow(escape, extent=[cx - scale, cx + scale, cy - scale, cy + scale], 
              origin='lower', cmap='cividis', alpha=0.88)
              
    # Quadrant dividing axes centered at (cx, cy)
    ax.axvline(cx, color='white', linestyle='--', lw=1.8)
    ax.axhline(cy, color='white', linestyle='--', lw=1.8)
    
    # Quadrant Labels & Biological Genetic Bases
    # Q1: (+Re, +Im)
    ax.text(cx + 0.45*scale, cy + 0.65*scale, 
            "QUADRANT I: ADENINE (A)\n" + r"Mass Ratio $R_1 \in [0,1]$" + "\n" + r"Weight: $w_1 = 2R_1 - 1$",
            ha='center', fontsize=10, fontweight='bold', color='#f9e79f',
            bbox=dict(boxstyle="round,pad=0.3", fc="#1c2833", ec="#f39c12", lw=1.5, alpha=0.9))
            
    # Q2: (-Re, +Im)
    ax.text(cx - 0.45*scale, cy + 0.65*scale, 
            "QUADRANT II: THYMINE (T)\n" + r"Mass Ratio $R_2 \in [0,1]$" + "\n" + r"Weight: $w_2 = 2R_2 - 1$",
            ha='center', fontsize=10, fontweight='bold', color='#aed6f1',
            bbox=dict(boxstyle="round,pad=0.3", fc="#1c2833", ec="#3498db", lw=1.5, alpha=0.9))

    # Q3: (-Re, -Im)
    ax.text(cx - 0.45*scale, cy - 0.65*scale, 
            "QUADRANT III: CYTOSINE (C)\n" + r"Mass Ratio $R_3 \in [0,1]$" + "\n" + r"Weight: $w_3 = 2R_3 - 1$",
            ha='center', fontsize=10, fontweight='bold', color='#f5b7b1',
            bbox=dict(boxstyle="round,pad=0.3", fc="#1c2833", ec="#e74c3c", lw=1.5, alpha=0.9))

    # Q4: (+Re, -Im)
    ax.text(cx + 0.45*scale, cy - 0.65*scale, 
            "QUADRANT IV: GUANINE (G)\n" + r"Mass Ratio $R_4 \in [0,1]$" + "\n" + r"Bias Offset: $b = 2R_4 - 1$",
            ha='center', fontsize=10, fontweight='bold', color='#a9dfbf',
            bbox=dict(boxstyle="round,pad=0.3", fc="#1c2833", ec="#2ecc71", lw=1.5, alpha=0.9))

    # Center Seed Coordinate
    ax.scatter([cx], [cy], color='red', s=140, edgecolors='white', lw=2, zorder=6)
    ax.annotate(r"Observer Seed $\Theta = (c_x, c_y)$" + "\nDynamic Sampling Origin",
                xy=(cx, cy), xytext=(cx + 0.12, cy - 0.25),
                arrowprops=dict(arrowstyle="->", color='white', lw=1.5),
                fontsize=9.5, fontweight='bold', color='white',
                bbox=dict(boxstyle="round,pad=0.2", fc="#922b21", ec="white", lw=1))

    ax.set_title("Figure 6: Complex 4-Quadrant Genetic Base Decomposition\n" + 
                 r"(Mapping Fractal Mass Ratios to Neural Weights Without Persistent Matrix Storage)",
                 fontsize=11.5, fontweight='bold', pad=12, color='#1a252f')
    ax.set_xlabel(r"$\mathrm{Re}(c)$ Real Axis", fontsize=11)
    ax.set_ylabel(r"$\mathrm{Im}(c)$ Imaginary Axis", fontsize=11)
    
    save_fig(fig, "fig6_complex_4quadrant_genetics.png")

# ==============================================================================
# FIGURE 7: EMPIRICAL BENCHMARK & MULTI-SEED RIGOROUS RESULTS
# ==============================================================================
def generate_fig7():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4.6), dpi=300)
    
    # Run a quick 5-seed benchmark extraction for authentic plotting
    sys.path.append(os.path.abspath('experiments'))
    from simulate_oed_rigorous import run_multi_seed_evaluation
    bench = run_multi_seed_evaluation(n_seeds=5, epochs=50)
    
    # 1. Panel A: Training Loss Convergence Curve (Mean +/- Std)
    epochs = np.arange(1, 51)
    base_mean = np.mean(bench['base_hist'][:, :50], axis=0)
    base_std = np.std(bench['base_hist'][:, :50], axis=0)
    oed_mean = np.mean(bench['oed_hist'][:, :50], axis=0)
    oed_std = np.std(bench['oed_hist'][:, :50], axis=0)
    
    ax1.plot(epochs, base_mean, color='#2980b9', lw=2.2, label='Standard GLM Baseline')
    ax1.fill_between(epochs, base_mean - base_std, base_mean + base_std, color='#2980b9', alpha=0.18)
    
    ax1.plot(epochs, oed_mean, color='#27ae60', lw=2.2, label='OED (Zero-Storage)')
    ax1.fill_between(epochs, oed_mean - oed_std, oed_mean + oed_std, color='#27ae60', alpha=0.18)
    
    ax1.set_title("(a) Training Loss Convergence\n(5-Seed Mean $\\pm$ 1 Std Dev, T=50)", fontsize=11, fontweight='bold', color='#1a252f')
    ax1.set_xlabel("Optimization Epoch", fontsize=10)
    ax1.set_ylabel("Binary Cross-Entropy Loss", fontsize=10)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.grid(True, linestyle=':', alpha=0.4)
    
    # 2. Panel B: Clean vs Distribution Shift (Noise) Test Accuracy
    labels = ['Clean Test', 'Distribution Shift\n(Noise Perturbation)']
    base_scores = [bench['baseline_test'][0], bench['baseline_noisy'][0]]
    base_errs = [bench['baseline_test'][1], bench['baseline_noisy'][1]]
    oed_scores = [bench['oed_test'][0], bench['oed_noisy'][0]]
    oed_errs = [bench['oed_test'][1], bench['oed_noisy'][1]]
    
    x = np.arange(len(labels))
    width = 0.32
    
    rects1 = ax2.bar(x - width/2, base_scores, width, yerr=base_errs, capsize=4, 
                     label='Standard GLM Baseline', color='#3498db', edgecolor='#2471a3', lw=1.2)
    rects2 = ax2.bar(x + width/2, oed_scores, width, yerr=oed_errs, capsize=4, 
                     label='OED (Zero-Storage)', color='#2ecc71', edgecolor='#1e8449', lw=1.2)
                     
    ax2.set_ylabel("Generalization Accuracy (%)", fontsize=10)
    ax2.set_title("(b) Clean vs Distribution Shift Generalization\n(80/20 Train/Test Split, Zero Leakage)", fontsize=11, fontweight='bold', color='#1a252f')
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels, fontsize=10, fontweight='bold')
    ax2.set_ylim(0, 105)
    ax2.legend(loc='lower left', fontsize=9)
    ax2.grid(True, linestyle=':', alpha=0.4, axis='y')
    
    # Bar value labels
    for r in rects1:
        ax2.text(r.get_x() + r.get_width()/2, r.get_height() + 2, f"{r.get_height():.1f}%", 
                 ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#1b4f72')
    for r in rects2:
        ax2.text(r.get_x() + r.get_width()/2, r.get_height() + 2, f"{r.get_height():.1f}%", 
                 ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#145a32')

    # 3. Panel C: Memory Footprint vs Scale
    layers = np.array([1, 4, 16, 64, 256])
    std_memory = layers * 4 * 4  # 4 weights per layer * 4 bytes per float32
    oed_memory = np.full_like(layers, 24) # Constant 3 coords * 8 bytes (float64) = 24 bytes
    
    ax3.plot(layers, std_memory, color='#e74c3c', marker='s', lw=2.2, label='Standard Tensor Storage ($O(N)$)')
    ax3.plot(layers, oed_memory, color='#27ae60', marker='o', lw=2.4, label='OED Parameterization ($O(1) = 24$ B)')
    
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    ax3.set_title("(c) Persistent Memory Scaling\n($O(1)$ Constant Seed vs $O(N)$ Tensors)", fontsize=11, fontweight='bold', color='#1a252f')
    ax3.set_xlabel("Network Layer Complexity (N)", fontsize=10)
    ax3.set_ylabel("Persistent Storage Footprint (Bytes)", fontsize=10)
    ax3.legend(loc='center left', fontsize=9)
    ax3.grid(True, linestyle=':', alpha=0.4)
    
    fig.suptitle("Figure 7: Empirical Multi-Seed Benchmark Evaluation Across 5 Independent Runs", 
                 fontsize=13, fontweight='bold', y=1.03, color='#1a252f')
    plt.tight_layout()
    save_fig(fig, "fig7_empirical_benchmark.png")

if __name__ == '__main__':
    print("Generating Figure 1...")
    generate_fig1()
    print("Generating Figure 2...")
    generate_fig2()
    print("Generating Figure 3...")
    generate_fig3()
    print("Generating Figure 4...")
    generate_fig4()
    print("Generating Figure 5...")
    generate_fig5()
    print("Generating Figure 6...")
    generate_fig6()
    print("Generating Figure 7 (Multi-seed benchmark)...")
    generate_fig7()
    print("ALL 7 FIGURES SUCCESSFULLY GENERATED!")
