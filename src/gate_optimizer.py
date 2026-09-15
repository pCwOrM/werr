import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mandelbrot_core import compute_mandelbrot_patch, extract_quadrant_weights, FIGURES_DIR as ARTIFACT_DIR, sigmoid

def evaluate_network(params, res=128, max_iter=70):
    cx1, cy1, lz1, cx2, cy2, lz2, cx3, cy3, lz3 = params
    z1, z2, z3 = 10.0**lz1, 10.0**lz2, 10.0**lz3

    _, _, p1 = compute_mandelbrot_patch(cx1, cy1, z1, res=res, max_iter=max_iter)
    _, _, p2 = compute_mandelbrot_patch(cx2, cy2, z2, res=res, max_iter=max_iter)
    _, _, p3 = compute_mandelbrot_patch(cx3, cy3, z3, res=res, max_iter=max_iter)

    w1_1, w1_2, _, b1, _ = extract_quadrant_weights(p1, max_iter=max_iter)
    w2_1, w2_2, _, b2, _ = extract_quadrant_weights(p2, max_iter=max_iter)
    v1, v2, _, b3, _ = extract_quadrant_weights(p3, max_iter=max_iter)

    xor_data = [
        ((0, 0), 0),
        ((0, 1), 1),
        ((1, 0), 1),
        ((1, 1), 0)
    ]

    loss = 0.0
    correct = 0
    preds = []
    
    for (x1, x2), target in xor_data:
        h1 = 1.0 / (1.0 + np.exp(-np.clip(w1_1 * x1 + w1_2 * x2 + b1, -12, 12)))
        h2 = 1.0 / (1.0 + np.exp(-np.clip(w2_1 * x1 + w2_2 * x2 + b2, -12, 12)))
        out_z = v1 * h1 + v2 * h2 + b3
        out = 1.0 / (1.0 + np.exp(-np.clip(out_z, -12, 12)))
        
        loss += (out - target)**2
        lbl = 1 if out >= 0.5 else 0
        if lbl == target:
            correct += 1
        preds.append((x1, x2, target, h1, h2, out, lbl))

    return correct, loss, preds, (w1_1, w1_2, b1, w2_1, w2_2, b2, v1, v2, b3), (p1, p2, p3)

def run_evolution():
    print("="*75)
    print("GENETİK EVRİMSEL ARAMA: 128x128 MANDELBROT İLE %100 XOR AĞI")
    print("="*75)

    np.random.seed(42)
    pop_size = 50
    generations = 100

    # Başlangıç popülasyonu (Farklı Mandelbrot merkez bölgeleri)
    anchors = [
        (-0.7436, 0.1318),
        (-0.055, 0.806),
        (-0.144, 0.758),
        (-0.523, 0.525),
        (0.270, 0.005),
        (-1.250, 0.050)
    ]

    pop = []
    for _ in range(pop_size):
        a1 = anchors[np.random.randint(len(anchors))]
        a2 = anchors[np.random.randint(len(anchors))]
        a3 = anchors[np.random.randint(len(anchors))]
        ind = np.array([
            a1[0] + np.random.uniform(-0.05, 0.05), a1[1] + np.random.uniform(-0.05, 0.05), np.random.uniform(0.5, 3.5),
            a2[0] + np.random.uniform(-0.05, 0.05), a2[1] + np.random.uniform(-0.05, 0.05), np.random.uniform(0.5, 3.5),
            a3[0] + np.random.uniform(-0.05, 0.05), a3[1] + np.random.uniform(-0.05, 0.05), np.random.uniform(0.5, 3.5),
        ])
        pop.append(ind)

    best_overall_acc = 0
    best_overall_loss = 999.0
    best_solution = None

    for gen in range(generations):
        scores = []
        for ind in pop:
            # Hız için 64x64 ile tara, sonra 128x128 ile doğrula
            acc, loss, _, _, _ = evaluate_network(ind, res=64, max_iter=50)
            scores.append((acc, loss))

        # Sırala (Önce en yüksek doğruluk, sonra en düşük kayıp)
        sorted_indices = sorted(range(pop_size), key=lambda i: (-scores[i][0], scores[i][1]))
        top_acc, top_loss = scores[sorted_indices[0]]

        if gen % 10 == 0 or top_acc == 4:
            print(f"Jenerasyon {gen:2d} | En İyi Doğruluk: {top_acc}/4 | En Düşük MSE: {top_loss:.4f}")

        if top_acc == 4 and top_loss < 0.35:
            # 128x128 ile test et
            candidate = pop[sorted_indices[0]]
            acc128, loss128, preds, weights, patches = evaluate_network(candidate, res=128, max_iter=70)
            if acc128 == 4:
                print(f"\n[HARİKA] 128x128 Çözünürlükte %100 Başarı Yakalandı! (Jenerasyon {gen})")
                best_solution = (candidate, preds, weights, patches, loss128)
                break

        # Yeni jenerasyon (Elitizm + Mutasyon)
        elites = [pop[i] for i in sorted_indices[:10]]
        new_pop = list(elites)
        while len(new_pop) < pop_size:
            parent = elites[np.random.randint(len(elites))].copy()
            # Mutasyon: Küçük koordinat veya zoom kaymaları
            mutation_mask = np.random.rand(9) < 0.4
            mutations = np.random.normal(0, 0.04, 9)
            mutations[2::3] = np.random.normal(0, 0.2, 3) # zoom mutasyonu
            parent[mutation_mask] += mutations[mutation_mask]
            new_pop.append(parent)
        pop = new_pop

    if best_solution is None:
        # Son en iyiyi 128 ile değerlendir
        candidate = pop[sorted_indices[0]]
        acc128, loss128, preds, weights, patches = evaluate_network(candidate, res=128, max_iter=70)
        best_solution = (candidate, preds, weights, patches, loss128)

    params, preds, weights, patches, loss128 = best_solution
    w1_1, w1_2, b1, w2_1, w2_2, b2, v1, v2, b3 = weights
    p1, p2, p3 = patches

    print("\n" + "="*75)
    print(f"128x128 Nihai Ağ Doğrulama Tablosu (MSE: {loss128:.4f}):")
    print("="*75)
    print(f"Nöron 1 (128x128): w1={w1_1:+.2f}, w2={w1_2:+.2f}, b={b1:+.2f} | cx={params[0]:.4f}, cy={params[1]:.4f}, zoom={10**params[2]:.1f}x")
    print(f"Nöron 2 (128x128): w1={w2_1:+.2f}, w2={w2_2:+.2f}, b={b2:+.2f} | cx={params[3]:.4f}, cy={params[4]:.4f}, zoom={10**params[5]:.1f}x")
    print(f"Nöron 3 (128x128): v1={v1:+.2f}, v2={v2:+.2f}, b={b3:+.2f}     | cx={params[6]:.4f}, cy={params[7]:.4f}, zoom={10**params[8]:.1f}x")
    print("-" * 75)

    all_pass = True
    for x1, x2, target, h1, h2, out, lbl in preds:
        ok = (lbl == target)
        if not ok: all_pass = False
        print(f"Girdi: ({x1}, {x2}) -> Hedef: {target} | h1={h1:.3f}, h2={h2:.3f} | Çıktı={out:.3f} | Tahmin: {lbl} [{'BAŞARILI' if ok else 'HATALI'}]")

    print("-" * 75)
    print(f"Genel Sonuç: %{sum(1 for p in preds if p[2]==p[6])/4 * 100:.0f} Doğruluk!")

    # Görselleştirme
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    im1 = axes[0].imshow(p1, cmap='magma', origin='lower')
    axes[0].set_title(f"Nöron 1 (128x128)\nw1={w1_1:+.2f}, w2={w1_2:+.2f}, b={b1:+.2f}\nZoom: {10**params[2]:.1f}x", fontsize=10)
    axes[0].axis('off')
    plt.colorbar(im1, ax=axes[0], fraction=0.046, pad=0.04)

    im2 = axes[1].imshow(p2, cmap='viridis', origin='lower')
    axes[1].set_title(f"Nöron 2 (128x128)\nw1={w2_1:+.2f}, w2={w2_2:+.2f}, b={b2:+.2f}\nZoom: {10**params[5]:.1f}x", fontsize=10)
    axes[1].axis('off')
    plt.colorbar(im2, ax=axes[1], fraction=0.046, pad=0.04)

    im3 = axes[2].imshow(p3, cmap='plasma', origin='lower')
    axes[2].set_title(f"Nöron 3 (Çıkış 128x128)\nv1={v1:+.2f}, v2={v2:+.2f}, b={b3:+.2f}\nZoom: {10**params[8]:.1f}x", fontsize=10)
    axes[2].axis('off')
    plt.colorbar(im3, ax=axes[2], fraction=0.046, pad=0.04)

    plt.suptitle("128x128 Mandelbrot Pencereleri ile Evrimsel Olarak Eğitilmiş XOR Ağı", fontsize=13, fontweight='bold')
    plt.tight_layout()
    out_xor = os.path.join(ARTIFACT_DIR, "xor_evolution_solution_128.png")
    plt.savefig(out_xor, dpi=150)
    plt.close()
    print(f"[+] 128x128 XOR Nihai Görseli Kaydedildi: {out_xor}")

if __name__ == "__main__":
    run_evolution()
