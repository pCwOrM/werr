import os
import numpy as np
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mandelbrot_core import compute_mandelbrot_patch, extract_quadrant_weights, FIGURES_DIR as ARTIFACT_DIR, sigmoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def solve_all_gates_100_percent():
    print("="*70)
    print("HEDEF: TÜM KAPILARI (NAND, NOR ve XOR) %100 DOĞRULUKLA ÇÖZEN FRAKTAL PARAMETRELER")
    print("="*70)

    gates = {
        "NAND": [((0, 0), 1), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)],
        "NOR":  [((0, 0), 1), ((0, 1), 0), ((1, 0), 0), ((1, 1), 0)]
    }

    # Çeşitli fraktal merkez adayları
    search_centers = [
        (-0.743643887, 0.131825904),
        (-0.15, 1.03),
        (-1.25, 0.05),
        (-0.75, 0.05),
        (0.27, 0.005),
        (-0.5, 0.5)
    ]

    gate_results = {}

    for name, data in gates.items():
        print(f"\n{name} Kapısı için 128x128 fraktal araması başlatılıyor...")
        np.random.seed(123)
        found = False
        
        for step in range(800):
            center = search_centers[np.random.randint(len(search_centers))]
            cx = center[0] + np.random.uniform(-0.06, 0.06)
            cy = center[1] + np.random.uniform(-0.06, 0.06)
            zoom = 10.0 ** np.random.uniform(0.5, 4.0)

            _, _, patch = compute_mandelbrot_patch(cx, cy, zoom, res=128, max_iter=70)
            w1, w2, _, bias, _ = extract_quadrant_weights(patch, max_iter=70)

            correct = 0
            loss = 0.0
            for (x1, x2), target in data:
                z = w1 * x1 + w2 * x2 + bias
                p = 1.0 / (1.0 + np.exp(-np.clip(z, -15, 15)))
                loss += (p - target)**2
                lbl = 1 if p >= 0.5 else 0
                if lbl == target:
                    correct += 1

            if correct == 4:
                print(f"  [BAŞARILI] {name} Kapısı %100 Doğrulukla Çözüldü! (Adım {step+1})")
                print(f"  Parametreler: cx={cx:.6f}, cy={cy:.6f}, zoom={zoom:.1f}x")
                print(f"  Ağırlıklar: w1={w1:+.3f}, w2={w2:+.3f}, bias={bias:+.3f} (MSE: {loss:.4f})")
                gate_results[name] = (cx, cy, zoom, w1, w2, bias, patch, loss)
                found = True
                break
        
        if not found:
            print(f"  [BİLGİ] {name} için 800 adımda %100 bulunamadı.")

    # --- XOR 2-KATMANLI OPTİMİZASYON (%100 ÇÖZÜMÜ) ---
    print("\n" + "-"*50)
    print("XOR Kapısı için 128x128 Çift Fraktal Penceresi Aranıyor...")
    xor_data = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)]
    np.random.seed(777)
    xor_found = False

    for step in range(1200):
        # 1. Pencere (N1)
        c1 = search_centers[np.random.randint(len(search_centers))]
        cx1 = c1[0] + np.random.uniform(-0.06, 0.06)
        cy1 = c1[1] + np.random.uniform(-0.06, 0.06)
        z1 = 10.0 ** np.random.uniform(0.8, 3.5)

        # 2. Pencere (N2)
        c2 = search_centers[np.random.randint(len(search_centers))]
        cx2 = c2[0] + np.random.uniform(-0.06, 0.06)
        cy2 = c2[1] + np.random.uniform(-0.06, 0.06)
        z2 = 10.0 ** np.random.uniform(0.8, 3.5)

        _, _, p1 = compute_mandelbrot_patch(cx1, cy1, z1, res=128, max_iter=60)
        _, _, p2 = compute_mandelbrot_patch(cx2, cy2, z2, res=128, max_iter=60)

        w1_1, w1_2, _, b1, _ = extract_quadrant_weights(p1, max_iter=60)
        w2_1, w2_2, _, b2, _ = extract_quadrant_weights(p2, max_iter=60)

        # Çıkış katmanı: H1 - H2 ayrımı
        correct = 0
        loss = 0.0
        for (x1, x2), target in xor_data:
            h1 = 1.0 / (1.0 + np.exp(-np.clip(w1_1 * x1 + w1_2 * x2 + b1, -12, 12)))
            h2 = 1.0 / (1.0 + np.exp(-np.clip(w2_1 * x1 + w2_2 * x2 + b2, -12, 12)))
            
            # h1 (OR gibi) ve h2 (NAND gibi)
            z_out = 3.5 * h1 + 3.5 * h2 - 5.0
            out = 1.0 / (1.0 + np.exp(-np.clip(z_out, -12, 12)))
            loss += (out - target)**2
            lbl = 1 if out >= 0.5 else 0
            if lbl == target:
                correct += 1

        if correct == 4:
            print(f"  [BAŞARILI] XOR Kapısı %100 Doğrulukla Çözüldü! (Adım {step+1})")
            print(f"  N1 (128x128): cx={cx1:.4f}, cy={cy1:.4f}, zoom={z1:.1f}x -> w1={w1_1:+.2f}, w2={w1_2:+.2f}, b={b1:+.2f}")
            print(f"  N2 (128x128): cx={cx2:.4f}, cy={cy2:.4f}, zoom={z2:.1f}x -> w1={w2_1:+.2f}, w2={w2_2:+.2f}, b={b2:+.2f}")
            print(f"  MSE Kaybı: {loss:.4f}")
            
            print("\nXOR Doğrulama Tablosu:")
            for (x1, x2), target in xor_data:
                h1 = 1.0 / (1.0 + np.exp(-np.clip(w1_1 * x1 + w1_2 * x2 + b1, -12, 12)))
                h2 = 1.0 / (1.0 + np.exp(-np.clip(w2_1 * x1 + w2_2 * x2 + b2, -12, 12)))
                z_out = 3.5 * h1 + 3.5 * h2 - 5.0
                out = 1.0 / (1.0 + np.exp(-np.clip(z_out, -12, 12)))
                lbl = 1 if out >= 0.5 else 0
                print(f"  Girdi ({x1}, {x2}) -> Hedef {target} | h1={h1:.2f}, h2={h2:.2f} | Çıktı={out:.3f} | Tahmin={lbl} [BAŞARILI]")
            
            # XOR Görselleştirmesini kaydet
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
            ax1.imshow(p1, cmap='plasma', origin='lower')
            ax1.set_title(f"XOR Nöron 1 (OR Ajanı)\nw1={w1_1:+.2f}, w2={w1_2:+.2f}, b={b1:+.2f}")
            ax1.axis('off')
            
            ax2.imshow(p2, cmap='viridis', origin='lower')
            ax2.set_title(f"XOR Nöron 2 (NAND Ajanı)\nw1={w2_1:+.2f}, w2={w2_2:+.2f}, b={b2:+.2f}")
            ax2.axis('off')
            
            plt.suptitle("128x128 Çift Mandelbrot Penceresi ile %100 Çözülen XOR Ağı", fontsize=13, fontweight='bold')
            plt.tight_layout()
            out_xor = os.path.join(ARTIFACT_DIR, "xor_solution_128.png")
            plt.savefig(out_xor, dpi=150)
            plt.close()
            print(f"\n[+] XOR çözüm grafiği kaydedildi: {out_xor}")
            xor_found = True
            break

if __name__ == "__main__":
    solve_all_gates_100_percent()
