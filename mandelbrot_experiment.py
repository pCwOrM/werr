import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def compute_mandelbrot_patch(cx, cy, zoom, res=64, max_iter=80):
    """
    Belirli bir merkez (cx, cy) ve zoom seviyesinde Mandelbrot penceresi üretir.
    Döndürdüğü değer:
    - black_ratio: Ortadaki ıraksamayan siyah bölgenin alan oranı [0, 1]
    - avg_escape: Ortalama kaçış süresi oranı [0, 1]
    - escape_iters: 2D matris (görselleştirme için ham iterasyon sayıları)
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

def fractal_neuron(x1, x2, cx, cy, zoom, w1=1.0, w2=1.0, res=32):
    """
    Tek bir nöron: Bias değerini doğrudan Mandelbrot penceresinden okur.
    """
    black_ratio, _, _ = compute_mandelbrot_patch(cx, cy, zoom, res=res)
    # Siyah alan oranını [0, 1] aralığından [-2.0, 2.0] bias aralığına ölçekleyelim:
    bias = (black_ratio - 0.5) * 4.0
    # İleri besleme (Sigmoid aktivasyonu)
    z = (w1 * x1) + (w2 * x2) + bias
    y_pred = 1.0 / (1.0 + np.exp(-z))
    return y_pred, bias, black_ratio

def run_tests_and_visualize():
    print("=== 1. TEMEL DURUM TESTLERİ ===")
    test_cases = [
        ("Ana Gövde (Merkez - Yoğun Siyah Alan)", -0.5, 0.0, 1.0),
        ("Sınır Bölgesi (Seahorse Valley civarı)", -0.7436438870371587, 0.13182590420531197, 100.0),
        ("Dış Bölge (Tamamen Kaçış / Açık Alan)", 2.0, 2.0, 1.0),
    ]

    inputs = (0.5, 0.5)
    print(f"Girdi: x1={inputs[0]}, x2={inputs[1]}")
    print("-" * 70)

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    fig.suptitle("Mandelbrot Fraktal Pencereleri ve Nöron Tepkileri", fontsize=16)

    for idx, (desc, cx, cy, zoom) in enumerate(test_cases):
        pred, derived_bias, b_ratio = fractal_neuron(inputs[0], inputs[1], cx, cy, zoom, res=128)
        _, avg_esc, escape_map = compute_mandelbrot_patch(cx, cy, zoom, res=128, max_iter=80)
        
        print(f"Durum: {desc}")
        print(f"  -> Siyah Alan Oranı : {b_ratio:.4f} ({b_ratio*100:.1f}%)")
        print(f"  -> Kaçış Ortalaması : {avg_esc:.4f}")
        print(f"  -> Üretilen Bias    : {derived_bias:.4f}")
        print(f"  -> Nöron Çıktısı    : {pred:.4f}\n")

        # Üst sıra: Kaçış süresi renk haritası
        im1 = axes[0, idx].imshow(escape_map, cmap='magma', origin='lower')
        axes[0, idx].set_title(f"{desc.split('(')[0].strip()}\nZoom: {zoom}x")
        axes[0, idx].axis('off')
        plt.colorbar(im1, ax=axes[0, idx], fraction=0.046, pad=0.04)

        # Alt sıra: Siyah alan (Iraksamayan bölge maskesi)
        black_mask = (escape_map == 80).astype(int)
        axes[1, idx].imshow(black_mask, cmap='gray_r', origin='lower')
        axes[1, idx].set_title(f"Siyah Bölge (Bias: {derived_bias:.2f})\nOran: {b_ratio*100:.1f}%")
        axes[1, idx].axis('off')

    plt.tight_layout()
    
    # Grafikleri kaydet
    out_dir_artifact = r"C:\Users\maat\.gemini\antigravity\brain\be1030f1-5b3e-4e9e-886d-2b41ab9b7de4"
    os.makedirs(out_dir_artifact, exist_ok=True)
    out_path1 = os.path.join(out_dir_artifact, "mandelbrot_patches.png")
    plt.savefig(out_path1, dpi=150)
    plt.close()
    print(f"Görsel kaydedildi: {out_path1}")

    # === 2. ZOOM EĞRİSİ ANALİZİ ===
    print("=== 2. ZOOM EĞRİSİ VE AĞIRLIK DEĞİŞİM ANALİZİ ===")
    cx_sea, cy_sea = -0.7436438870371587, 0.13182590420531197
    zoom_levels = np.geomspace(1.0, 50000.0, 60)
    black_ratios = []
    avg_escapes = []
    biases = []

    for z in zoom_levels:
        br, ae, _ = compute_mandelbrot_patch(cx_sea, cy_sea, z, res=64, max_iter=80)
        black_ratios.append(br)
        avg_escapes.append(ae)
        biases.append((br - 0.5) * 4.0)

    fig2, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    ax1.plot(zoom_levels, black_ratios, label="Siyah Alan Oranı (Karanlık Bölge)", color='black', linewidth=2)
    ax1.plot(zoom_levels, avg_escapes, label="Normalize Kaçış Süresi (Sürekli Metrik)", color='crimson', linestyle='--', linewidth=2)
    ax1.set_xscale('log')
    ax1.set_ylabel("Metrik Değeri [0, 1]")
    ax1.set_title("Seahorse Valley Sınırında Zoom Katsayısına Göre Ağırlık/Bias Değişimi")
    ax1.grid(True, which="both", ls="-", alpha=0.3)
    ax1.legend()

    ax2.plot(zoom_levels, biases, label="Üretilen Bias Katsayısı (b)", color='navy', linewidth=2)
    ax2.set_xscale('log')
    ax2.set_xlabel("Zoom Katsayısı (Logaritmik Ölçek)")
    ax2.set_ylabel("Bias Değeri [-2, +2]")
    ax2.grid(True, which="both", ls="-", alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    out_path2 = os.path.join(out_dir_artifact, "zoom_weight_curve.png")
    plt.savefig(out_path2, dpi=150)
    plt.close()
    print(f"Zoom analiz görseli kaydedildi: {out_path2}")

    # === 3. BASİT BİR GÖREVDE OPTİMİZASYON DENEYİ (OR KAPISI) ===
    print("=== 3. OR KAPISI İÇİN FRAKTAL OPTİMİZASYON ===")
    # Doğruluk tablosu (OR kapısı)
    dataset = [
        ((0, 0), 0),
        ((0, 1), 1),
        ((1, 0), 1),
        ((1, 1), 1)
    ]
    # w1=2.0, w2=2.0 sabit tutulsun, doğru bias'ı verecek bir Mandelbrot penceresi (cx, cy, zoom) arayalım.
    # OR kapısında bias yaklaşık -1.0 civarında olmalıdır (z(0,0)=-1 -> sigmoid=0.26, z(0,1)=1 -> sigmoid=0.73).
    # Bizim formül: bias = (black_ratio - 0.5) * 4.0.
    # bias = -1.0 olması için black_ratio = 0.25 olmalı!
    target_bias = -1.0
    print(f"Hedef Bias: {target_bias:.2f} (Gereken Siyah Alan Oranı: {(target_bias/4.0 + 0.5):.2f})")
    
    # Zoom seviyeleri içinden en yakın olanı bulalım
    best_idx = np.argmin(np.abs(np.array(biases) - target_bias))
    found_zoom = zoom_levels[best_idx]
    found_bias = biases[best_idx]
    found_br = black_ratios[best_idx]

    print(f"Bulunan En İyi Zoom: {found_zoom:.2f}x")
    print(f"Bulunan Siyah Oran  : {found_br:.4f}")
    print(f"Bulunan Bias        : {found_bias:.4f}")

    print("\nOR Kapısı Doğrulama Testi:")
    correct = 0
    for (x1, x2), target in dataset:
        z = 2.0 * x1 + 2.0 * x2 + found_bias
        pred = 1.0 / (1.0 + np.exp(-z))
        predicted_class = 1 if pred >= 0.5 else 0
        is_ok = (predicted_class == target)
        if is_ok: correct += 1
        print(f"  Girdi: ({x1}, {x2}) -> Hedef: {target} | z: {z:+.2f} | Sigmoid: {pred:.3f} | Tahmin: {predicted_class} [{'BAŞARILI' if is_ok else 'HATALI'}]")
    
    print(f"Sonuç: %{correct/len(dataset)*100:.0f} Doğruluk!")

if __name__ == "__main__":
    run_tests_and_visualize()
