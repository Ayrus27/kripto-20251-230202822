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
𝑥, x yang memenuhi persamaan 𝑎 × 𝑥 ≡ 1 (mod 𝑛) a×x≡1 (mod n). Tanpa adanya GCD yang sama dengan 1 (artinya 𝑎a dan 𝑛n saling relatif prima), invers modular tidak dapat ditemukan.

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
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

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
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
