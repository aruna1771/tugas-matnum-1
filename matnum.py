
import math
import numpy as np
import matplotlib.pyplot as plt

# Fungsi persamaan
def f(x):
    return math.exp(x) - 5 * x**2

# Batas awal dan toleransi
a = 0
b = 1
epsilon = 0.00001

iterasi = 0

print("METODE")
print("f(x) = e^x - 5x^2")
print("Lebar awal =", abs(b - a))
print()

print("Iterasi |    a     |    c     |    b     |   f(a)   |   f(c)   |   f(b)   | Selang Baru | Lebar")
print("-" * 125)

while abs(b - a) > epsilon:
    # Titik tengah
    c = (a + b) / 2

    # Nilai fungsi
    fa = f(a)
    fc = f(c)
    fb = f(b)

    # Menentukan selang baru
    if fa * fc < 0:
        selang = "[a, c]"
        a_baru = a
        b_baru = c
    else:
        selang = "[c, b]"
        a_baru = c
        b_baru = b

    # Menghitung lebar interval
    lebar = abs(b_baru - a_baru)

    # Menampilkan hasil iterasi
    print(f"{iterasi:7d} | {a:.6f} | {c:.6f} | {b:.6f} | "
          f"{fa:8.6f} | {fc:8.6f} | {fb:8.6f} | "
          f"{selang:11s} | {lebar:.8f}")

    # Memperbarui batas
    a = a_baru
    b = b_baru
    iterasi += 1

# Perkiraan akar
akar = (a + b) / 2

print("-" * 125)
print("Jumlah iterasi =", iterasi)
print(f"Interval akhir = [{a:.8f}, {b:.8f}]")
print(f"Lebar = {abs(b-a):.8f}")
print(f"Akar persamaan = {akar:.8f}")
print(f"Nilai f(akar) = {f(akar):.10f}")

# Membuat grafik
x = np.linspace(0, 1, 400)
y = np.exp(x) - 5 * x**2

plt.figure(figsize=(9, 5))
plt.plot(x, y, label="f(x) = e^x - 5x^2")
plt.axhline(0, linewidth=1)
plt.axvline(akar, linestyle="--",
            label=f"Akar = {akar:.6f}")
plt.scatter(akar, f(akar), zorder=3)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Grafik")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
