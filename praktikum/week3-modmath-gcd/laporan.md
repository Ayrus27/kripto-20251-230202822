# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: [Modular Math]  
Nama: [Surya Subekti]  
NIM: [230202822]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Aritmetika Modular adalah cabang matematika yang berfokus pada operasi bilangan dalam sistem bilangan terbatas, di mana hasil operasi dibagi dengan suatu bilangan tertentu yang disebut modulus dan hanya sisanya yang diperhatikan. Konsep ini sering disebut juga sebagai “aritmetika jam,” karena setelah mencapai batas tertentu, perhitungan kembali ke awal. Misalnya, dalam modulus 12, setelah angka 11, hasil berikutnya adalah 0 (seperti jam menunjukkan pukul 12 kembali ke 0). Aritmetika modular sangat penting dalam komputasi karena memungkinkan perhitungan efisien pada bilangan besar tanpa kehilangan makna matematis.

Greatest Common Divisor (GCD) atau faktor persekutuan terbesar adalah konsep yang menentukan bilangan bulat terbesar yang dapat membagi dua bilangan tanpa meninggalkan sisa. Algoritma Euclidean merupakan metode paling efisien untuk menghitung GCD dan menjadi dasar dalam banyak sistem kriptografi, termasuk dalam mencari invers modular. Invers modular diperlukan ketika ingin menemukan bilangan 
 x yang memenuhi persamaan 𝑎 × 𝑥 ≡ 1 (mod 𝑛) a×x≡1 (mod n). Tanpa adanya GCD yang sama dengan 1 (artinya 𝑎a dan 𝑛n saling relatif prima), invers modular tidak dapat ditemukan.

Bilangan Prima dan Logaritma Diskrit berperan penting dalam keamanan kriptografi modern. Bilangan prima digunakan sebagai kunci dasar dalam algoritma seperti RSA dan Diffie-Hellman karena sifat uniknya yang sulit untuk diuraikan menjadi faktor bilangan besar. Sementara itu, logaritma diskrit adalah kebalikan dari operasi perpangkatan dalam sistem modular, di mana diberikan gx ≡ y (mod p),maka mencari
x adalah masalah yang sangat sulit secara komputasional. Kompleksitas perhitungan logaritma diskrit inilah yang menjadikan banyak sistem keamanan digital tetap aman dari serangan brute-force, sekaligus menjadi fondasi penting dalam kriptografi kunci publik. 

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
```python
# modular_math.py

# --- Langkah 1: Aritmetika Modular ---
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))

# --- Langkah 2: GCD (Euclidean Algorithm) ---
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))

# --- Langkah 3: Extended Euclidean & Invers Modular ---
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))

# --- Langkah 4: Logaritma Diskrit ---
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))
```
)

---

## 6. Hasil dan Pembahasan

| Fungsi | Input | Output | Keterangan |
|---------|--------|---------|------------|
| mod_add | 7, 5, 12 | 0 | Operasi penjumlahan modular berhasil |
| mod_mul | 7, 5, 12 | 11 | Perkalian modular sesuai teori |
| mod_exp | 7^128 mod 13 | 3 | Eksponensiasi modular berhasil |
| gcd | 54, 24 | 6 | GCD sesuai hasil perhitungan manual |
| modinv | 3 mod 11 | 4 | Invers modular benar karena 3×4 ≡ 1 (mod 11) |
| discrete_log | 3^x ≡ 4 (mod 7) | x=4 | Hasil sesuai ekspektasi |

Semua hasil sesuai ekspektasi teori. Tidak ditemukan error selama eksekusi.

---

## 7. Jawaban Pertanyaan Diskusi
1. Apa peran aritmetika modular dalam kriptografi modern?
   - Aritmetika modular memainkan peran fundamental dalam kriptografi modern. Konsep ini digunakan secara luas karena sifat matematisnya yang cocok untuk membangun sistem kriptografi yang aman, efisien, dan tahan terhadap serangan. Berikut adalah beberapa peran utama aritmetika modular dalam kriptografi modern:
        - Mendukung Keamanan melalui Kesulitan Masalah Matematis
        - Menjamin hasil tetap dalam rentang tertentu (tidak tak hingga).
        - Membuat proses enkripsi dan dekripsi dapat dibalik (reversible) dengan aturan tertentu.
3. Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
   - Karena invers modular memungkinkan proses enkripsi dan dekripsi dalam algoritma kunci publik seperti RSA saling membatalkan satu sama lain secara matematis.
5. Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
   - Tidak adanya algoritma klasik yang efisien (polinomial),
   - Kompleksitas waktu dan memori yang ekstrem, bahkan dengan algoritma terbaik saat ini,
   - Ketergantungan pada struktur matematis grup, yang harus dirancang hati-hati untuk menghindari kelemahan,
   - Ancaman teoretis dari komputasi kuantum, meski belum praktis saat ini.
---

## 8. Kesimpulan
Berdasarkan hasil percobaan, konsep aritmetika modular terbukti menjadi dasar utama dalam berbagai operasi kriptografi, seperti penjumlahan, perkalian, eksponensiasi, serta pencarian invers modular. Melalui implementasi program, seluruh fungsi berjalan sesuai teori dan menunjukkan pentingnya keterkaitan antara GCD, bilangan prima, dan logaritma diskrit dalam menjaga keamanan sistem kriptografi. Dengan demikian, pemahaman aritmetika modular sangat penting untuk membangun dan menganalisis algoritma enkripsi modern seperti RSA dan Diffie-Hellman.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit f5bfaf1dc9eb2c699a0c89b5bf17814c6b09706e
Author: Surya Subekti <115227173+Ayrus27@users.noreply.github.com>
Date:   Sat Oct 18 10:27:33 2025 +0700

    week3-modmath-gcd: Modular Math
```
