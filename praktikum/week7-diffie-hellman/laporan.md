# Laporan Praktikum Kriptografi
Minggu ke-: 7  
Topik: [Diffiw Hellman]  
Nama: [Surya Subekti]  
NIM: [230202822]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
Protokol Diffie–Hellman Key Exchange merupakan suatu mekanisme kriptografi yang memungkinkan dua pihak atau lebih untuk membentuk kunci rahasia bersama melalui media komunikasi yang tidak aman. Keunikan protokol ini adalah kemampuan menghasilkan kunci bersama tanpa perlu menukarkan kunci rahasia secara langsung, sehingga mengurangi risiko penyadapan selama proses distribusi kunci.

Secara konseptual, Diffie–Hellman memanfaatkan sifat perhitungan modulo pada bilangan prima besar dan konsep logaritma diskrit, yaitu operasi matematika yang secara komputasional mudah dilakukan ke satu arah, namun sulit dibalik tanpa informasi tambahan. Hal ini menjadikan kunci yang dihasilkan sangat sulit direkonstruksi oleh pihak tidak berwenang.

Dalam prosesnya, kedua pihak terlebih dahulu menyepakati dua parameter publik: sebuah bilangan prima besar (p) dan sebuah generator (g). Masing-masing pihak kemudian menghasilkan kunci privat yang tidak dibagikan kepada siapapun, dan dari kunci privat tersebut mereka membentuk kunci publik melalui operasi perpangkatan modulo. Setelah kedua pihak saling bertukar kunci publik, mereka dapat menghitung kunci rahasia bersama dengan menggunakan kunci privat masing-masing. Kunci rahasia yang diperoleh kedua pihak tersebut identik, meskipun mereka tidak pernah bertukar kunci privat.

Keamanan Diffie–Hellman bergantung pada sulitnya memecahkan Diffie–Hellman Problem, yaitu menentukan nilai kunci rahasia hanya berdasarkan informasi publik (g, p, dan kunci publik kedua pihak). Selain itu, protokol ini menjadi dasar bagi berbagai skema keamanan modern, seperti TLS/SSL, VPN, dan metode Perfect Forward Secrecy, yang memerlukan pembentukan kunci aman secara dinamis.

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
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```


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

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
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
