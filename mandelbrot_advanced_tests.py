import os
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Artifact çıkış dizini
ARTIFACT_DIR = r"C:\Users\maat\.gemini\antigravity\brain\be1030f1-5b3e-4e9e-886d-2b41ab9b7de4"
os.makedirs(ARTIFACT_DIR, exist_ok=True)

def compute_mandelbrot_patch(cx, cy, zoom, res=128, max_iter=100):
    """
    Belirli bir merkez (cx, cy) ve zoom seviyesinde vectorized Mandelbrot penceresi üretir.
    Döndürdüğü değerler:
    - black_ratio: Ortadaki ıraksamayan siyah bölgenin alan oranı [0, 1]
    - avg_escape: Ortalama kaçış süresi oranı [0, 1]
    - escape_iters: (res, res) boyutunda 2D tam sayı matrisi
    """
    scale = 1.0 / zoom
    x = np.linspace(cx - scale, cx + scale, res)
    y = np.linspace(cy - scale, cy + scale, res)
    C = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    Z = np.zeros_like(C)
    escape_iters = np.full(C.shape, max_iter, dtype=int)
    mask = np.ones(C.shape, dtype=bool)

    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + C[mask]
        escaped = np.abs(Z) > 2.0
        newly_escaped = escaped & mask
        escape_iters[newly_escaped] = i
        mask = mask & (~escaped)

    black_pixels = np.sum(escape_iters == max_iter)
    black_ratio = black_pixels / (res * res)
    avg_escape = np.mean(escape_iters) / max_iter
    return black_ratio, avg_escape, escape_iters

def extract_quadrant_weights(escape_iters, max_iter=100):
    """
    128x128 boyutundaki tek bir Mandelbrot penceresini 4 çeyreğe (quadrant) böler:
    - Q1 (Sol Üst)  -> w1 (Ağırlık 1)
    - Q2 (Sağ Üst)  -> w2 (Ağırlık 2)
    - Q3 (Sol Alt)  -> w3 (Opsiyonel / Ek bağlantı)
    - Q4 (Sağ Alt)  -> bias (Eşik Değeri)
    Her çeyrekteki siyah piksel oranı [-3.0, +3.0] aralığında ağırlık/bias'a dönüştürülür.
    """
    h, w = escape_iters.shape
    mid_h, mid_w = h // 2, w // 2

    q1 = escape_iters[:mid_h, :mid_w]
    q2 = escape_iters[:mid_h, mid_w:]
    q3 = escape_iters[mid_h:, :mid_w]
    q4 = escape_iters[mid_h:, mid_w:]

    quads = [q1, q2, q3, q4]
    weights = []
    ratios = []

    for q in quads:
        ratio = np.sum(q == max_iter) / q.size
        ratios.append(ratio)
        # Oranı [-3.0, +3.0] aralığına ölçekle
        w_val = (ratio - 0.5) * 6.0
        weights.append(w_val)

    # w1, w2, w3, bias
    return weights[0], weights[1], weights[2], weights[3], ratios

# ==========================================================
# TEST 1: ÇÖZÜNÜRLÜK KARŞILAŞTIRMASI (32x32 vs 64x64 vs 128x128)
# ==========================================================
def test_resolution_impact():
    print("\n" + "="*70)
    print("TEST 1: ÇÖZÜNÜRLÜK DUYARLILIK VE KARARLILIK TESTİ (32x32 vs 64x64 vs 128x128)")
    print("="*70)

    regions = [
        ("Ana Gövde", -0.5, 0.0, 1.0),
        ("Seahorse Valley (Derin Zoom)", -0.7436438870371587, 0.13182590420531197, 500.0),
        ("Mini-Mandelbrot Uydusu", -1.75, 0.0, 25.0),
        ("Elephant Valley", 0.27, 0.005, 50.0)
    ]

    resolutions = [32, 64, 128, 256]
    results = {}

    for name, cx, cy, zoom in regions:
        print(f"\nBölge: {name} (Zoom: {zoom}x)")
        results[name] = {"res": resolutions, "black_ratios": [], "times": []}
        for r in resolutions:
            t0 = time.perf_counter()
            br, ae, _ = compute_mandelbrot_patch(cx, cy, zoom, res=r, max_iter=100)
            elapsed_ms = (time.perf_counter() - t0) * 1000.0
            results[name]["black_ratios"].append(br)
            results[name]["times"].append(elapsed_ms)
            print(f"  [{r}x{r}] -> Siyah Oran: {br*100:6.2f}% | Hesaplama Süresi: {elapsed_ms:5.2f} ms")

    # Görselleştirme
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    for name in results:
        axes[0].plot(resolutions, [r*100 for r in results[name]["black_ratios"]], marker='o', label=name)
    axes[0].set_title("Çözünürlüğe Göre Siyah Alan Oranı Kararlılığı (%)")
    axes[0].set_xlabel("Piksel Çözünürlüğü (N x N)")
    axes[0].set_ylabel("Siyah Alan Oranı (%)")
    axes[0].set_xticks(resolutions)
    axes[0].grid(True, linestyle="--", alpha=0.5)
    axes[0].legend()

    for name in results:
        axes[1].plot(resolutions, results[name]["times"], marker='s', label=name)
    axes[1].set_title("Çözünürlüğe Göre Hesaplama Maliyeti (ms)")
    axes[1].set_xlabel("Piksel Çözünürlüğü (N x N)")
    axes[1].set_ylabel("Süre (milisaniye)")
    axes[1].set_xticks(resolutions)
    axes[1].grid(True, linestyle="--", alpha=0.5)
    axes[1].legend()

    plt.tight_layout()
    out_path = os.path.join(ARTIFACT_DIR, "resolution_comparison_128.png")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"\n[+] Çözünürlük karşılaştırma grafiği kaydedildi: {out_path}")

# ==========================================================
# TEST 2: 128x128 TEK BİR PENCEREDEN TÜM AĞIRLIKLARI TÜRETME (4-Quadrant)
# ==========================================================
def test_quadrant_weights():
    print("\n" + "="*70)
    print("TEST 2: 128x128 TEK PENCEREDEN ÇOKLU AĞIRLIK TÜRETİMİ (w1, w2, w3, bias)")
    print("="*70)

    cx, cy, zoom = -0.7436438870371587, 0.13182590420531197, 250.0
    br, ae, patch = compute_mandelbrot_patch(cx, cy, zoom, res=128, max_iter=100)
    w1, w2, w3, bias, ratios = extract_quadrant_weights(patch, max_iter=100)

    print(f"Referans Pencere: Seahorse Valley (Zoom: {zoom}x, Çözünürlük: 128x128)")
    print(f"  Toplam Siyah Alan Oranı: {br*100:.2f}%")
    print(f"  -> Q1 (Sol Üst)  -> w1   : {w1:+.4f} (Siyah: {ratios[0]*100:.1f}%)")
    print(f"  -> Q2 (Sağ Üst)  -> w2   : {w2:+.4f} (Siyah: {ratios[1]*100:.1f}%)")
    print(f"  -> Q3 (Sol Alt)  -> w3   : {w3:+.4f} (Siyah: {ratios[2]*100:.1f}%)")
    print(f"  -> Q4 (Sağ Alt)  -> Bias : {bias:+.4f} (Siyah: {ratios[3]*100:.1f}%)")

    # Görselleştirme: 128x128 pencere ve 4 çeyrek çizgileri
    fig, ax = plt.subplots(figsize=(7, 7))
    im = ax.imshow(patch, cmap='twilight_shifted', origin='lower')
    ax.axhline(64, color='white', linestyle='--', linewidth=2)
    ax.axvline(64, color='white', linestyle='--', linewidth=2)
    
    ax.text(32, 96, f"Q1 (w1)\n{w1:+.2f}", color='white', fontsize=12, fontweight='bold', ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="black", alpha=0.6))
    ax.text(96, 96, f"Q2 (w2)\n{w2:+.2f}", color='white', fontsize=12, fontweight='bold', ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="black", alpha=0.6))
    ax.text(32, 32, f"Q3 (w3)\n{w3:+.2f}", color='white', fontsize=12, fontweight='bold', ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="black", alpha=0.6))
    ax.text(96, 32, f"Q4 (Bias)\n{bias:+.2f}", color='white', fontsize=12, fontweight='bold', ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", fc="black", alpha=0.6))

    ax.set_title(f"128x128 Mandelbrot Penceresinden 4 Çeyrek Ağırlık/Bias Ayrıştırması", fontsize=11)
    ax.axis('off')
    plt.tight_layout()
    out_path = os.path.join(ARTIFACT_DIR, "quadrant_weights_128.png")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"[+] 4-Quadrant ağırlık ayrıştırma görseli kaydedildi: {out_path}")

# ==========================================================
# TEST 3: TÜM MANTIKSAL KAPILAR İÇİN 128x128 FRAKTAL EVRİMSEL ARAMA (AND, OR, NAND, NOR)
# ==========================================================
def test_all_logic_gates():
    print("\n" + "="*70)
    print("TEST 3: 128x128 ÇÖZÜNÜRLÜKTE TÜM MANTIKSAL KAPILARIN OPTİMİZASYONU (AND, OR, NAND, NOR)")
    print("="*70)

    gates = {
        "OR":   [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 1)],
        "AND":  [((0, 0), 0), ((0, 1), 0), ((1, 0), 0), ((1, 1), 1)],
        "NAND": [((0, 0), 1), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)],
        "NOR":  [((0, 0), 1), ((0, 1), 0), ((1, 0), 0), ((1, 1), 0)]
    }

    # Arama uzayı: Farklı merkez noktaları ve zoom seviyeleri
    # Seahorse Valley, Elephant Valley, Main Body, Cusp
    anchor_points = [
        (-0.7436438870371587, 0.13182590420531197),  # Seahorse Valley
        (0.27, 0.005),                                # Elephant Valley
        (-1.25, 0.02),                                # West Filaments
        (-0.1, 0.8),                                  # North Antenna
        (-1.75, 0.0),                                 # Mini Mandelbrot
    ]

    gate_solutions = {}

    for gate_name, data in gates.items():
        print(f"\n--- {gate_name} Kapısı Çözümü Aranıyor (128x128 Fraktal Penceresi) ---")
        best_acc = -1
        best_loss = float('inf')
        best_params = None
        best_weights = None

        np.random.seed(42)
        # Evrimsel / Rasgele Tepe Tırmanma (Random-Walk Search)
        for trial in range(300):
            # Merkez seçimi veya perturbasyonu
            anchor = anchor_points[np.random.randint(len(anchor_points))]
            cx = anchor[0] + np.random.uniform(-0.05, 0.05)
            cy = anchor[1] + np.random.uniform(-0.05, 0.05)
            zoom = 10.0 ** np.random.uniform(0.5, 4.5)  # 3x ile 30000x arası zoom

            _, _, patch = compute_mandelbrot_patch(cx, cy, zoom, res=128, max_iter=80)
            w1, w2, _, bias, _ = extract_quadrant_weights(patch, max_iter=80)

            # Doğruluk ve Kayıp (MSE) hesapla
            correct = 0
            loss = 0.0
            for (x1, x2), target in data:
                z = w1 * x1 + w2 * x2 + bias
                pred = 1.0 / (1.0 + np.exp(-np.clip(z, -15, 15)))
                loss += (pred - target)**2
                pred_label = 1 if pred >= 0.5 else 0
                if pred_label == target:
                    correct += 1

            acc = correct / len(data)
            if acc > best_acc or (acc == best_acc and loss < best_loss):
                best_acc = acc
                best_loss = loss
                best_params = (cx, cy, zoom)
                best_weights = (w1, w2, bias)

            if best_acc == 1.0 and best_loss < 0.15:
                break

        gate_solutions[gate_name] = {
            "params": best_params,
            "weights": best_weights,
            "acc": best_acc,
            "loss": best_loss,
            "data": data
        }

        w1, w2, bias = best_weights
        cx, cy, zoom = best_params
        print(f"  [SONUÇ] Doğruluk: %{best_acc*100:.0f} (MSE Kaybı: {best_loss:.4f})")
        print(f"  Parametreler: cx={cx:.6f}, cy={cy:.6f}, zoom={zoom:.1f}x")
        print(f"  Türetilen Katsayılar (128x128'den): w1={w1:+.3f}, w2={w2:+.3f}, bias={bias:+.3f}")
        for (x1, x2), target in data:
            z = w1 * x1 + w2 * x2 + bias
            p = 1.0 / (1.0 + np.exp(-np.clip(z, -15, 15)))
            lbl = 1 if p >= 0.5 else 0
            print(f"    Girdi ({x1}, {x2}) -> Hedef {target} | z={z:+.2f} | Sigmoid={p:.3f} | Tahmin: {lbl} [{'OK' if lbl==target else 'HATA'}]")

    # Tüm kapıların görselleştirilmesi
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    for idx, (gate_name, info) in enumerate(gate_solutions.items()):
        cx, cy, zoom = info["params"]
        w1, w2, bias = info["weights"]
        _, _, patch = compute_mandelbrot_patch(cx, cy, zoom, res=128, max_iter=80)
        
        ax = axes[idx]
        im = ax.imshow(patch, cmap='magma', origin='lower')
        ax.set_title(f"{gate_name} Kapısı (%{info['acc']*100:.0f} Başarı)\nZoom: {zoom:.1f}x | w1={w1:+.2f}, w2={w2:+.2f}, b={bias:+.2f}", fontsize=10)
        ax.axis('off')
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    plt.tight_layout()
    out_path = os.path.join(ARTIFACT_DIR, "gate_solutions_128.png")
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"\n[+] Mantıksal kapılar görseli kaydedildi: {out_path}")

# ==========================================================
# TEST 4: NON-LINEAR XOR PROBLEMİ (2 Nöronlu Fraktal Ağ)
# ==========================================================
def test_xor_with_two_fractal_patches():
    print("\n" + "="*70)
    print("TEST 4: DOĞRUSAL OLMAYAN (NON-LINEAR) XOR PROBLEMİ (2 Nöronlu 128x128 Fraktal Ağ)")
    print("="*70)
    print("XOR problemi tek bir düz çizgiyle ayrılamaz (Minsky-Papert).")
    print("İki ayrı 128x128 Mandelbrot penceresi ile Nöron 1 (NAND benzeri) ve Nöron 2 (OR benzeri) türetilecek.")

    xor_data = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1, 1), 0)]

    # Nöron 1 (NAND / Üst Sınır) ve Nöron 2 (OR / Alt Sınır)
    # Çıktı Nöronu: H1 AND H2
    np.random.seed(99)
    best_acc = -1
    best_loss = float('inf')
    best_patches = None

    for step in range(400):
        # 1. Nöron için fraktal pencere
        cx1 = -0.7436 + np.random.uniform(-0.08, 0.08)
        cy1 = 0.1318 + np.random.uniform(-0.08, 0.08)
        z1 = 10.0 ** np.random.uniform(1.0, 3.5)

        # 2. Nöron için fraktal pencere
        cx2 = 0.27 + np.random.uniform(-0.08, 0.08)
        cy2 = 0.005 + np.random.uniform(-0.08, 0.08)
        z2 = 10.0 ** np.random.uniform(1.0, 3.5)

        _, _, p1 = compute_mandelbrot_patch(cx1, cy1, z1, res=128, max_iter=70)
        _, _, p2 = compute_mandelbrot_patch(cx2, cy2, z2, res=128, max_iter=70)

        w1_1, w1_2, _, b1, _ = extract_quadrant_weights(p1, max_iter=70)
        w2_1, w2_2, _, b2, _ = extract_quadrant_weights(p2, max_iter=70)

        # Çıkış katmanı sabit weights: 3.0*h1 + 3.0*h2 - 4.5 (AND birleşimi)
        correct = 0
        loss = 0.0
        for (x1, x2), target in xor_data:
            # Gizli katman nöronları
            h1 = 1.0 / (1.0 + np.exp(-np.clip(w1_1 * x1 + w1_2 * x2 + b1, -15, 15)))
            h2 = 1.0 / (1.0 + np.exp(-np.clip(w2_1 * x1 + w2_2 * x2 + b2, -15, 15)))
            
            # Çıktı nöronu (h1 ve h2'nin mantıksal birleşimi)
            z_out = 3.5 * h1 + 3.5 * h2 - 5.0
            out = 1.0 / (1.0 + np.exp(-np.clip(z_out, -15, 15)))
            
            loss += (out - target)**2
            pred = 1 if out >= 0.5 else 0
            if pred == target:
                correct += 1

        acc = correct / len(xor_data)
        if acc > best_acc or (acc == best_acc and loss < best_loss):
            best_acc = acc
            best_loss = loss
            best_patches = (cx1, cy1, z1, w1_1, w1_2, b1, cx2, cy2, z2, w2_1, w2_2, b2)

        if best_acc == 1.0 and best_loss < 0.2:
            break

    print(f"\n[XOR SONUCU] Doğruluk: %{best_acc*100:.0f} (MSE: {best_loss:.4f})")
    cx1, cy1, z1, w1_1, w1_2, b1, cx2, cy2, z2, w2_1, w2_2, b2 = best_patches
    print(f"  Nöron 1 (128x128 Mandelbrot 1): w1={w1_1:+.2f}, w2={w1_2:+.2f}, bias={b1:+.2f} (Zoom: {z1:.1f}x)")
    print(f"  Nöron 2 (128x128 Mandelbrot 2): w1={w2_1:+.2f}, w2={w2_2:+.2f}, bias={b2:+.2f} (Zoom: {z2:.1f}x)")

    for (x1, x2), target in xor_data:
        h1 = 1.0 / (1.0 + np.exp(-np.clip(w1_1 * x1 + w1_2 * x2 + b1, -15, 15)))
        h2 = 1.0 / (1.0 + np.exp(-np.clip(w2_1 * x1 + w2_2 * x2 + b2, -15, 15)))
        z_out = 3.5 * h1 + 3.5 * h2 - 5.0
        out = 1.0 / (1.0 + np.exp(-np.clip(z_out, -15, 15)))
        lbl = 1 if out >= 0.5 else 0
        print(f"  Girdi ({x1}, {x2}) -> Hedef {target} | h1={h1:.2f}, h2={h2:.2f} | Çıktı Sigmoid={out:.3f} | Tahmin: {lbl} [{'OK' if lbl==target else 'HATA'}]")

if __name__ == "__main__":
    test_resolution_impact()
    test_quadrant_weights()
    test_all_logic_gates()
    test_xor_with_two_fractal_patches()
    print("\n" + "="*70)
    print("TÜM 128x128 TESTLER BAŞARIYLA TAMAMLANDI!")
    print("="*70)
