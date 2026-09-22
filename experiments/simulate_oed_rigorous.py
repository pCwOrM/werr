import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

"""
Rigorous Empirical Benchmark Suite for Orbital Error Dynamics (OED) - Version 3.0
- Clean train/test split (80/20)
- Zero label leakage (100% feedforward evaluation without test-time updates)
- Standard Logistic Regression (GLM) baseline
- Multi-seed evaluation (5 seeds) with Student-t 95% Confidence Intervals (t_4 = 2.776)
- Consistent 32x32 grid resolution across training and test
- Finite difference step delta = 0.02
- Epochs T = 50
- Zero gradient rate and Zinc Spark invocation tracking
"""

import numpy as np
import os

np.random.seed(42)

def generate_twomoons(n_samples=300, noise=0.12):
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
    
    # 80/20 Train/Test Split
    indices = np.random.permutation(n_samples)
    split = int(0.8 * n_samples)
    train_idx, test_idx = indices[:split], indices[split:]
    return X[train_idx], Y[train_idx], X[test_idx], Y[test_idx]

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
    return np.array([R1, R2, R3, R4]), np.mean(escape_counts)

def quadrant_to_weights(R):
    return np.array([2.0 * R[0] - 1.0, 2.0 * R[1] - 1.0, 2.0 * R[2] - 1.0, 2.0 * R[3] - 1.0])

def forward_predict(X, W):
    w1, w2, w3, b = W
    z = w1 * X[:, 0] + w2 * X[:, 1] + w3 * (X[:, 0] * X[:, 1]) + b
    z = np.clip(z, -15.0, 15.0)
    return 1.0 / (1.0 + np.exp(-z))

def compute_bce(y_true, y_pred):
    eps = 1e-9
    y_pred = np.clip(y_pred, eps, 1.0 - eps)
    return - np.mean(y_true * np.log(y_pred) + (1.0 - y_true) * np.log(1.0 - y_pred))

def train_oed(X_train, Y_train, epochs=50, seed=42):
    np.random.seed(seed)
    # Critical boundary seed
    theta = np.array([-0.72, 0.28, 2.8]) + np.random.randn(3) * 0.04
    lr_theta = 0.06
    eps_fd = 0.02
    
    losses = []
    zinc_sparks_count = 0
    zero_grad_count = 0
    
    for ep in range(epochs):
        cx, cy, zoom = theta
        R, mean_esc = sample_mandelbrot_quadrants(cx, cy, zoom, grid_size=32)
        W_oed = quadrant_to_weights(R)
        
        p_tr = forward_predict(X_train, W_oed)
        l_task = compute_bce(Y_train, p_tr)
        l_orb = ((mean_esc - 22.0) / 22.0)**2
        sigma_fractal = np.var(R)
        l_tot = l_task + 0.35 * l_orb + 0.01 * sigma_fractal
        losses.append(l_tot)
        
        # Finite difference gradient with delta = 0.02
        grad_th = np.zeros(3)
        for i in range(3):
            th_p = theta.copy()
            th_p[i] += eps_fd
            R_p, m_p = sample_mandelbrot_quadrants(th_p[0], th_p[1], th_p[2], grid_size=32)
            w_p = quadrant_to_weights(R_p)
            l_p = compute_bce(Y_train, forward_predict(X_train, w_p)) + 0.35 * (((m_p - 22.0)/22.0)**2) + 0.01 * np.var(R_p)
            grad_th[i] = (l_p - l_tot) / eps_fd
            
        grad_norm = np.linalg.norm(grad_th)
        if grad_norm == 0.0:
            zero_grad_count += 1
            
        # Zinc Spark perturbed jump operator
        if grad_norm < 0.05 and l_task > 0.38:
            zinc_sparks_count += 1
            jump = np.array([np.random.standard_cauchy() * 0.10, np.random.standard_cauchy() * 0.10, 0.4])
            theta += jump
        else:
            theta -= lr_theta * np.clip(grad_th, -1.0, 1.0)
            
        theta[0] = np.clip(theta[0], -1.8, 0.4)
        theta[1] = np.clip(theta[1], -1.2, 1.2)
        theta[2] = np.clip(theta[2], 0.5, 30.0)
        
    R_fin, _ = sample_mandelbrot_quadrants(theta[0], theta[1], theta[2], grid_size=32)
    W_fin = quadrant_to_weights(R_fin)
    return W_fin, theta, losses, zinc_sparks_count, zero_grad_count

def run_multi_seed_evaluation(n_seeds=5, epochs=50):
    print("=" * 80)
    print(f"OED EMPIRICAL BENCHMARK v3.0 (Zero Label Leakage, Consistent 32x32 Grid, N={n_seeds})")
    print("=" * 80)
    
    base_clean_accs, base_noisy_accs = [], []
    oed_clean_accs, oed_noisy_accs = [], []
    diff_clean_accs, diff_noisy_accs = [], []
    
    all_base_hist = []
    all_oed_hist = []
    
    total_sparks = 0
    total_zeros = 0
    
    for s in range(n_seeds):
        np.random.seed(100 + s)
        X_tr, Y_tr, X_te, Y_te = generate_twomoons(n_samples=300, noise=0.12)
        X_te_noisy = X_te + np.random.normal(1.2, 0.4, size=X_te.shape)
        
        # 1. Baseline Logistic Regression (Direct W optimization)
        W_base = np.random.uniform(-0.5, 0.5, size=4)
        lr_b = 0.12
        feat_tr = np.column_stack([X_tr[:, 0], X_tr[:, 1], X_tr[:, 0] * X_tr[:, 1], np.ones(len(X_tr))])
        base_losses = []
        for ep in range(epochs):
            p_tr = forward_predict(X_tr, W_base)
            base_losses.append(compute_bce(Y_tr, p_tr))
            grad = (feat_tr.T @ (p_tr - Y_tr)) / len(X_tr)
            W_base -= lr_b * grad
            
        all_base_hist.append(base_losses)
        
        acc_b_clean = np.mean((forward_predict(X_te, W_base) >= 0.5) == Y_te) * 100.0
        acc_b_noisy = np.mean((forward_predict(X_te_noisy, W_base) >= 0.5) == Y_te) * 100.0
        base_clean_accs.append(acc_b_clean)
        base_noisy_accs.append(acc_b_noisy)
        
        # 2. OED Clean Feedforward Evaluation
        w_oed, th_oed, oed_losses, sparks, zeros = train_oed(X_tr, Y_tr, epochs=epochs, seed=100+s)
        all_oed_hist.append(oed_losses)
        
        acc_o_clean = np.mean((forward_predict(X_te, w_oed) >= 0.5) == Y_te) * 100.0
        acc_o_noisy = np.mean((forward_predict(X_te_noisy, w_oed) >= 0.5) == Y_te) * 100.0
        oed_clean_accs.append(acc_o_clean)
        oed_noisy_accs.append(acc_o_noisy)
        
        diff_clean = acc_b_clean - acc_o_clean
        diff_noisy = acc_b_noisy - acc_o_noisy
        diff_clean_accs.append(diff_clean)
        diff_noisy_accs.append(diff_noisy)
        
        total_sparks += sparks
        total_zeros += zeros
        
        print(f"Seed {s+1}/{n_seeds} | Clean [GLM: {acc_b_clean:.1f}%, OED: {acc_o_clean:.1f}% (Diff: {diff_clean:+.1f}%)] | Noisy [GLM: {acc_b_noisy:.1f}%, OED: {acc_o_noisy:.1f}% (Diff: {diff_noisy:+.1f}%)]")
        
    t_crit = 2.7764 # Two-tailed 95% critical value for Student-t with df=4 (N=5)
    
    def get_stats(arr):
        m = np.mean(arr)
        s = np.std(arr, ddof=1)
        sem = s / np.sqrt(len(arr))
        ci_low = m - t_crit * sem
        ci_high = m + t_crit * sem
        return m, s, ci_low, ci_high

    print("\n" + "=" * 80)
    print(f"STATISTICAL SUMMARY (N=5, Student-t 95% Confidence Intervals, t_4 = {t_crit:.3f}):")
    print("-" * 80)
    for name, arr in [
        ("GLM Baseline (Clean)            ", base_clean_accs),
        ("OED Zero-Storage (Clean)        ", oed_clean_accs),
        ("Paired Difference Clean (GLM-OED)", diff_clean_accs),
        ("GLM Baseline (Noise Shift)      ", base_noisy_accs),
        ("OED Zero-Storage (Noise Shift)  ", oed_noisy_accs),
        ("Paired Difference Noisy (GLM-OED)", diff_noisy_accs),
    ]:
        m, s, lo, hi = get_stats(arr)
        print(f"  {name}: {m:.2f}% +/- {s:.2f}%  [95% CI: {lo:.2f}%, {hi:.2f}%]")
        
    print("-" * 80)
    print(f"Zero Gradient Epochs: {total_zeros}/{n_seeds*epochs} ({total_zeros/(n_seeds*epochs)*100:.1f}%)")
    print(f"Zinc Spark Invocations: {total_sparks}/{n_seeds*epochs} ({total_sparks/(n_seeds*epochs)*100:.1f}%)")
    print("=" * 80)
    
    return {
        'baseline_test': (np.mean(base_clean_accs), np.std(base_clean_accs, ddof=1)),
        'oed_test': (np.mean(oed_clean_accs), np.std(oed_clean_accs, ddof=1)),
        'baseline_noisy': (np.mean(base_noisy_accs), np.std(base_noisy_accs, ddof=1)),
        'oed_noisy': (np.mean(oed_noisy_accs), np.std(oed_noisy_accs, ddof=1)),
        'base_hist': np.array(all_base_hist),
        'oed_hist': np.array(all_oed_hist),
        'zero_grads': total_zeros,
        'zinc_sparks': total_sparks
    }

if __name__ == '__main__':
    run_multi_seed_evaluation(n_seeds=5, epochs=50)
