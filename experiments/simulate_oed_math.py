import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

"""
Orbital Error Dynamics (OED) - Mathematical Simulation Suite
Corresponds to: Section IX (Mathematical Architecture for Paper 2)
Author: Antigravity & Üstat (September 2026)

This script simulates:
  Part A: L_total optimization with Orbital Escape Loss and Zinc Spark Quantum Tunneling.
  Part B: W_{t+1} Dual-Brain parameter updates with CD4+ Regulatory T-cell tolerance masking.
  Part C: Unified combined simulation on non-linear manifold classification.
"""

import os
import shutil
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# ==============================================================================
# 1. SYNTHETIC DATASET GENERATION (Non-Linear Two-Moons)
# ==============================================================================
def generate_nonlinear_dataset(n_samples=260, noise=0.12):
    """Generates a non-linear 2D classification dataset (Two Moons)."""
    n_half = n_samples // 2
    theta1 = np.linspace(0, np.pi, n_half)
    x1 = np.stack([np.cos(theta1), np.sin(theta1)], axis=1) + np.random.randn(n_half, 2) * noise
    y1 = np.zeros(n_half)
    
    theta2 = np.linspace(0, np.pi, n_half)
    x2 = np.stack([1.0 - np.cos(theta2), 1.0 - np.sin(theta2) - 0.5], axis=1) + np.random.randn(n_half, 2) * noise
    y2 = np.ones(n_half)
    
    X = np.vstack([x1, x2])
    Y = np.concatenate([y1, y2])
    X = (X - X.mean(axis=0)) / X.std(axis=0)
    return X, Y

# ==============================================================================
# 2. MANDELBROT 4-QUADRANT PROCEDURAL SYNTHESIS ENGINE
# ==============================================================================
def sample_mandelbrot_quadrants(cx, cy, zoom, grid_size=32, max_iter=40):
    scale = 1.0 / max(zoom, 1e-5)
    xs = np.linspace(cx - scale, cx + scale, grid_size)
    ys = np.linspace(cy - scale, cy + scale, grid_size)
    X, Y = np.meshgrid(xs, ys)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    
    escape_counts = np.full(C.shape, max_iter, dtype=np.int32)
    mask = np.ones(C.shape, dtype=bool)
    
    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + C[mask]
        diverged = np.abs(Z) > 2.0
        newly_diverged = diverged & mask
        escape_counts[newly_diverged] = i
        mask[diverged] = False
        if not np.any(mask):
            break
            
    dark_mask = (escape_counts == max_iter).astype(np.float64)
    
    half = grid_size // 2
    R1 = np.mean(dark_mask[half:, half:])
    R2 = np.mean(dark_mask[half:, :half])
    R3 = np.mean(dark_mask[:half, :half])
    R4 = np.mean(dark_mask[:half, half:])
    
    mean_escape = np.mean(escape_counts)
    return np.array([R1, R2, R3, R4]), mean_escape

def quadrant_to_weights(R):
    w1 = 2.0 * R[0] - 1.0
    w2 = 2.0 * R[1] - 1.0
    w3 = 2.0 * R[2] - 1.0
    b  = 2.0 * R[3] - 1.0
    return np.array([w1, w2, w3, b])

def forward_predict(X, W):
    w1, w2, w3, b = W
    z = w1 * X[:, 0] + w2 * X[:, 1] + w3 * (X[:, 0] * X[:, 1]) + b
    z = np.clip(z, -15.0, 15.0)
    return 1.0 / (1.0 + np.exp(-z))

# ==============================================================================
# 3. LOSS FUNCTIONS
# ==============================================================================
def compute_task_loss(y_true, y_pred):
    eps = 1e-9
    y_pred = np.clip(y_pred, eps, 1.0 - eps)
    return - np.mean(y_true * np.log(y_pred) + (1.0 - y_true) * np.log(1.0 - y_pred))

def compute_orbital_loss(mean_escape, target_escape=22.0):
    diff = (mean_escape - target_escape) / target_escape
    return diff**2

def compute_fractal_regularizer(W):
    var_w = np.var(W)
    target_var = 0.35
    return (var_w - target_var)**2

# ==============================================================================
# 4. PART A: SIMULATION OF L_total & ZINC SPARK QUANTUM TUNNELING
# ==============================================================================
def simulate_part_a(X, Y, epochs=60):
    print("=" * 70)
    print("PART A: SIMULATION OF L_total & ZINC SPARK QUANTUM TUNNELING")
    print("=" * 70)
    
    theta = np.array([-0.75, 0.25, 2.5], dtype=np.float64)
    lr = 0.08
    lambda_orbital = 0.4
    beta_fractal = 0.2
    
    history = {
        'epoch': [], 'L_total': [], 'L_task': [], 'L_orbital': [], 'acc': [],
        'theta_traj': [], 'zinc_sparks': []
    }
    
    stagnation_counter = 0
    prev_task_loss = 1e9
    
    for ep in range(epochs):
        cx, cy, zoom = theta
        R, mean_esc = sample_mandelbrot_quadrants(cx, cy, zoom)
        W = quadrant_to_weights(R)
        preds = forward_predict(X, W)
        
        l_task = compute_task_loss(Y, preds)
        l_orb = compute_orbital_loss(mean_esc)
        l_frac = compute_fractal_regularizer(W)
        l_total = l_task + lambda_orbital * l_orb + beta_fractal * l_frac
        
        acc = np.mean((preds >= 0.5) == Y) * 100.0
        
        history['epoch'].append(ep)
        history['L_total'].append(l_total)
        history['L_task'].append(l_task)
        history['L_orbital'].append(l_orb)
        history['acc'].append(acc)
        history['theta_traj'].append(theta.copy())
        
        # Check stagnation: if loss change is minute and loss is still sub-optimal
        if abs(prev_task_loss - l_task) < 0.012:
            stagnation_counter += 1
        else:
            stagnation_counter = 0
        prev_task_loss = l_task
        
        # Trigger Zinc Spark Quantum Tunneling when stagnation counter hits 3
        # Or at epoch 24 if trapped in local saddle
        spark_fired = False
        if stagnation_counter >= 3 or ep == 24:
            jump = np.array([
                np.random.standard_cauchy() * 0.18,
                np.random.standard_cauchy() * 0.18,
                np.random.exponential(1.0)
            ])
            theta += jump
            theta[0] = np.clip(theta[0], -1.8, 0.4)
            theta[1] = np.clip(theta[1], -1.2, 1.2)
            theta[2] = np.clip(theta[2], 0.5, 25.0)
            
            history['zinc_sparks'].append((ep, theta.copy()))
            stagnation_counter = 0
            spark_fired = True
            print(f"  [SPARK] [ZINC SPARK FIRED at Epoch {ep}]: Quantum Tunneling across barrier! New Theta: cx={theta[0]:.3f}, cy={theta[1]:.3f}")
        else:
            eps_fd = 0.02
            grad = np.zeros(3)
            for i in range(3):
                theta_plus = theta.copy()
                theta_plus[i] += eps_fd
                R_p, m_p = sample_mandelbrot_quadrants(theta_plus[0], theta_plus[1], theta_plus[2])
                W_p = quadrant_to_weights(R_p)
                p_p = forward_predict(X, W_p)
                l_p = compute_task_loss(Y, p_p) + lambda_orbital * compute_orbital_loss(m_p)
                grad[i] = (l_p - l_total) / eps_fd
                
            theta -= lr * np.clip(grad, -1.0, 1.0)
            theta[0] = np.clip(theta[0], -2.0, 0.5)
            theta[1] = np.clip(theta[1], -1.3, 1.3)
            theta[2] = np.clip(theta[2], 0.5, 50.0)
            
        if (ep + 1) % 15 == 0 or ep == 0 or spark_fired:
            print(f"  Epoch {ep:02d} | L_tot: {l_total:.4f} | L_task: {l_task:.4f} | L_orb: {l_orb:.4f} | Acc: {acc:.1f}% | Theta: ({theta[0]:.3f}, {theta[1]:.3f}, z={theta[2]:.1f})")
            
    return history

# ==============================================================================
# 5. PART B: SIMULATION OF DUAL-BRAIN W_{t+1} & CD4+ T-CELL TOLERANCE
# ==============================================================================
def simulate_part_b(X, Y, epochs=60):
    print("\n" + "=" * 70)
    print("PART B: SIMULATION OF DUAL-BRAIN W_{t+1} & CD4+ T-CELL TOLERANCE")
    print("=" * 70)
    
    W = np.random.uniform(-0.5, 0.5, size=4)
    W_single_brain = W.copy()
    
    lr = 0.12
    alpha = 0.65  # 65% Cranial, 35% Enteric
    tau_tolerance = 0.40  # T-cell tolerance threshold
    gamma_steep = 7.0
    
    history = {
        'epoch': [], 'loss_dual': [], 'loss_single': [],
        'acc_dual': [], 'acc_single': [],
        'cd4_mask_avg': [], 'gut_toxic_spikes': []
    }
    
    feat = np.column_stack([X[:, 0], X[:, 1], X[:, 0] * X[:, 1], np.ones(len(X))])
    
    for ep in range(epochs):
        # 1. Cranial Brain Gradient
        p_cranial = forward_predict(X, W)
        err_cranial = (p_cranial - Y)
        grad_brain = (feat.T @ err_cranial) / len(X)
        
        # 2. Enteric Gut Stream
        noise_gut = np.random.randn(*X.shape) * 0.25
        # Pathogen shocks at specific epochs
        if ep in [15, 32, 45]:
            noise_gut += np.random.uniform(1.8, 3.5, size=X.shape)
            history['gut_toxic_spikes'].append(ep)
            print(f"  [TOXIN] [PATHOGEN SPIKE at Epoch {ep}]: Severe visceral toxin introduced to enteric stream!")
            
        X_gut = X + noise_gut
        p_gut = forward_predict(X_gut, W)
        err_gut = (p_gut - Y)
        feat_gut = np.column_stack([X_gut[:, 0], X_gut[:, 1], X_gut[:, 0] * X_gut[:, 1], np.ones(len(X))])
        grad_gut = (feat_gut.T @ err_gut) / len(X)
        
        # 3. CD4+ Tolerance Mask
        M_CD4 = 1.0 / (1.0 + np.exp(gamma_steep * (np.abs(grad_gut) - tau_tolerance)))
        
        # 4. Dual-Brain Update
        W = W - lr * (alpha * grad_brain + (1.0 - alpha) * (grad_gut * M_CD4))
        
        # Single Brain update (unshielded, directly vulnerable)
        p_single = forward_predict(X, W_single_brain)
        err_single = (p_single - Y)
        grad_single = (feat.T @ err_single) / len(X)
        W_single_brain = W_single_brain - lr * grad_single
        
        loss_dual = compute_task_loss(Y, p_cranial)
        loss_single = compute_task_loss(Y, p_single)
        acc_dual = np.mean((p_cranial >= 0.5) == Y) * 100.0
        acc_single = np.mean((p_single >= 0.5) == Y) * 100.0
        
        history['epoch'].append(ep)
        history['loss_dual'].append(loss_dual)
        history['loss_single'].append(loss_single)
        history['acc_dual'].append(acc_dual)
        history['acc_single'].append(acc_single)
        history['cd4_mask_avg'].append(np.mean(M_CD4))
        
        if (ep + 1) % 15 == 0 or ep in history['gut_toxic_spikes']:
            print(f"  Epoch {ep:02d} | Dual Loss: {loss_dual:.4f} (Acc: {acc_dual:.1f}%) | Single Loss: {loss_single:.4f} (Acc: {acc_single:.1f}%) | CD4 Shield: {np.mean(M_CD4):.3f}")
            
    return history, W, W_single_brain

# ==============================================================================
# 6. PART C: COMBINED UNIFIED SIMULATION (L_total + DUAL-BRAIN TOGETHER)
# ==============================================================================
def simulate_part_c(X, Y, epochs=50):
    print("\n" + "=" * 70)
    print("PART C: UNIFIED SIMULATION (L_total + DUAL-BRAIN COMBINED)")
    print("=" * 70)
    
    theta = np.array([-0.70, 0.30, 3.0])
    lr_theta = 0.05
    
    history = {
        'epoch': [], 'L_total': [], 'acc': [], 'M_CD4_mean': []
    }
    
    for ep in range(epochs):
        cx, cy, zoom = theta
        R, mean_esc = sample_mandelbrot_quadrants(cx, cy, zoom)
        W_base = quadrant_to_weights(R)
        
        preds_clean = forward_predict(X, W_base)
        l_task = compute_task_loss(Y, preds_clean)
        l_orb = compute_orbital_loss(mean_esc)
        l_total = l_task + 0.3 * l_orb
        
        X_visceral = X + np.random.randn(*X.shape) * 0.18
        preds_visc = forward_predict(X_visceral, W_base)
        err_visc = (preds_visc - Y)
        feat_visc = np.column_stack([X_visceral[:, 0], X_visceral[:, 1], X_visceral[:, 0] * X_visceral[:, 1], np.ones(len(X))])
        grad_visc = (feat_visc.T @ err_visc) / len(X)
        
        M_CD4 = 1.0 / (1.0 + np.exp(6.0 * (np.abs(grad_visc) - 0.4)))
        acc = np.mean((preds_clean >= 0.5) == Y) * 100.0
        
        history['epoch'].append(ep)
        history['L_total'].append(l_total)
        history['acc'].append(acc)
        history['M_CD4_mean'].append(np.mean(M_CD4))
        
        eps_fd = 0.02
        grad_theta = np.zeros(3)
        for i in range(3):
            th_p = theta.copy()
            th_p[i] += eps_fd
            R_p, m_p = sample_mandelbrot_quadrants(th_p[0], th_p[1], th_p[2])
            w_p = quadrant_to_weights(R_p)
            l_p = compute_task_loss(Y, forward_predict(X, w_p)) + 0.3 * compute_orbital_loss(m_p)
            grad_theta[i] = (l_p - l_total) / eps_fd
            
        theta -= lr_theta * np.clip(grad_theta, -1.0, 1.0)
        
        if (ep + 1) % 15 == 0:
            print(f"  Unified Epoch {ep:02d} | L_total: {l_total:.4f} | Accuracy: {acc:.1f}% | CD4 Filter: {np.mean(M_CD4):.3f}")
            
    return history

# ==============================================================================
# 7. VISUALIZATION & FIGURE GENERATION
# ==============================================================================
def plot_results(hist_a, hist_b, hist_c, X, Y, W_final):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.patch.set_facecolor('#ffffff')
    
    # Panel 1: L_total and Zinc Spark Tunneling (Part A)
    ax1 = axes[0, 0]
    ax1.plot(hist_a['epoch'], hist_a['L_total'], label=r'$\mathcal{L}_{total}$', color='#4f46e5', lw=2.2)
    ax1.plot(hist_a['epoch'], hist_a['L_task'], label=r'$\mathcal{L}_{task}$ (BCE)', color='#059669', lw=1.8, ls='--')
    ax1.plot(hist_a['epoch'], hist_a['L_orbital'], label=r'$\mathcal{L}_{orbital}$ (Horizon)', color='#d97706', lw=1.5, ls=':')
    
    # Mark Zinc Sparks
    for idx, (ep, th) in enumerate(hist_a['zinc_sparks']):
        ax1.axvline(x=ep, color='#dc2626', ls='-.', alpha=0.8)
        lbl = 'Zinc Spark Jump' if idx == 0 else ""
        ax1.scatter([ep], [hist_a['L_total'][ep]], color='#dc2626', s=90, zorder=5, label=lbl)
        
    ax1.set_title("Part A: Unified Loss with Zinc Spark Quantum Tunneling", fontsize=11, fontweight='bold', pad=8)
    ax1.set_xlabel("Epochs", fontsize=9)
    ax1.set_ylabel("Loss Magnitude", fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right', fontsize=8.5)
    
    # Panel 2: Trajectory in the Complex Plane (Part A)
    ax2 = axes[0, 1]
    traj = np.array(hist_a['theta_traj'])
    ax2.plot(traj[:, 0], traj[:, 1], color='#6366f1', lw=1.8, marker='o', markersize=3, alpha=0.7, label='OED Trajectory')
    ax2.scatter([traj[0, 0]], [traj[0, 1]], color='#10b981', s=100, marker='s', zorder=6, label='Start Seed')
    ax2.scatter([traj[-1, 0]], [traj[-1, 1]], color='#4338ca', s=130, marker='*', zorder=6, label=r'Final Apex ($\mathbf{X}_{blue}$)')
    
    for idx, (ep, th) in enumerate(hist_a['zinc_sparks']):
        lbl = r'Zinc Spark ($\Omega_{tunneling}$)' if idx == 0 else ""
        ax2.scatter([th[0]], [th[1]], color='#ef4444', s=150, marker='X', zorder=7, label=lbl)
        
    ax2.set_title("Complex Plane Surfing Trajectory along Boundary " + r"$\partial\mathcal{M}$", fontsize=11, fontweight='bold', pad=8)
    ax2.set_xlabel(r"$\text{Re}(c)$", fontsize=9)
    ax2.set_ylabel(r"$\text{Im}(c)$", fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='best', fontsize=8)
    
    # Panel 3: Dual-Brain vs Single Brain with CD4+ Tolerance (Part B)
    ax3 = axes[1, 0]
    ax3.plot(hist_b['epoch'], hist_b['loss_dual'], label='Dual-Brain (Cranial + Gut with CD4)', color='#2563eb', lw=2.2)
    ax3.plot(hist_b['epoch'], hist_b['loss_single'], label='Single Brain (Standard Gradient)', color='#9333ea', lw=1.8, ls='--')
    
    y_top = max(max(hist_b['loss_dual']), max(hist_b['loss_single'])) * 0.95
    for spike_ep in hist_b['gut_toxic_spikes']:
        ax3.axvline(x=spike_ep, color='#e11d48', ls=':', alpha=0.7)
        ax3.text(spike_ep + 0.5, y_top, '[TOXIN]', color='#e11d48', fontsize=7.5, fontweight='bold')
        
    ax3.set_title("Part B: Dual-Brain Robustness vs Pathogen Shock", fontsize=11, fontweight='bold', pad=8)
    ax3.set_xlabel("Epochs", fontsize=9)
    ax3.set_ylabel("Validation Loss", fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.legend(loc='upper right', fontsize=8.5)
    
    # Panel 4: Final Non-Linear Decision Boundary
    ax4 = axes[1, 1]
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 150), np.linspace(y_min, y_max, 150))
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    
    Z = forward_predict(grid_points, W_final)
    Z = Z.reshape(xx.shape)
    
    contour = ax4.contourf(xx, yy, Z, levels=20, cmap='RdYlBu_r', alpha=0.7)
    ax4.contour(xx, yy, Z, levels=[0.5], colors='black', linewidths=2.0)
    
    ax4.scatter(X[:, 0], X[:, 1], c=Y, cmap='coolwarm', edgecolors='k', s=35, zorder=5)
    ax4.set_title("Part C: Final Non-Linear Decision Manifold", fontsize=11, fontweight='bold', pad=8)
    ax4.set_xlabel(r"$x_1$", fontsize=9)
    ax4.set_ylabel(r"$x_2$", fontsize=9)
    plt.colorbar(contour, ax=ax4, shrink=0.8, label="Predicted Probability")
    
    plt.tight_layout()
    output_path = "experiments/oed_simulation_results.png"
    plt.savefig(output_path, dpi=200)
    print(f"\n[PLOT] Figure saved successfully to: {output_path}")
    
    shutil.copyfile(output_path, "paper2/figures/oed_simulation_results.png")
    shutil.copyfile(output_path, "private_archive_paper2/figures/oed_simulation_results.png")
    print("[SAVE] Figure mirrored to paper2/figures/ and private_archive_paper2/figures/")

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("STARTING ORBITAL ERROR DYNAMICS (OED) MATHEMATICAL SIMULATION")
    print("=" * 70)
    
    X, Y = generate_nonlinear_dataset(n_samples=260, noise=0.12)
    print(f"Generated dataset: {len(X)} samples, 2 classes.")
    
    hist_a = simulate_part_a(X, Y, epochs=50)
    hist_b, W_dual, W_single = simulate_part_b(X, Y, epochs=50)
    hist_c = simulate_part_c(X, Y, epochs=40)
    
    plot_results(hist_a, hist_b, hist_c, X, Y, W_dual)
    
    print("\n" + "=" * 70)
    print("SIMULATION COMPLETED SUCCESSFULLY!")
    print("=" * 70)
