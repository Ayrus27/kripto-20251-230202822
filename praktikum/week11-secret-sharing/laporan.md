# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: [Secret Sharing (Shamir’s Secret Sharing)]  
Nama: [Surya Subekti]  
NIM: [230202822]  
Kelas: [5IKRA]  

---

## 1. Tujuan
- Menjelaskan konsep Shamir Secret Sharing (SSS).
- Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
- Menganalisis keamanan skema distribusi rahasia.


---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

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
Hasil eksekusi program Secret Sharing:

![Hasil Output](screenshots/output.png)


---

## 7. Jawaban Pertanyaan
1. Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?
    - Shamir Secret Sharing memiliki keunggulan karena tidak menyimpan kunci secara utuh pada satu pihak atau dalam bentuk salinan penuh. Setiap pihak hanya memegang sebagian informasi yang secara individual tidak bermakna, sehingga kebocoran satu atau beberapa bagian tidak langsung membahayakan kerahasiaan kunci utama.
2. Apa peran threshold (k) dalam keamanan secret sharing?
    - Nilai threshold (k) berfungsi sebagai batas minimum jumlah bagian yang harus digabungkan untuk merekonstruksi secret. Mekanisme ini memastikan bahwa secret tetap aman selama jumlah bagian yang terkumpul kurang dari k, sekaligus memberikan kontrol terhadap tingkat toleransi kegagalan atau kompromi sistem.
3. Berikan satu contoh skenario nyata di mana SSS sangat bermanfaat.
    - Salah satu contoh penerapan SSS adalah pada pengelolaan kunci enkripsi data pusat (data center). Kunci utama dibagi ke beberapa administrator, sehingga hanya jika sejumlah administrator tertentu bekerja sama, kunci tersebut dapat diakses. Pendekatan ini mencegah penyalahgunaan akses oleh satu individu dan meningkatkan keamanan organisasi.

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
```
    week11-secret-sharing

commit 584407bc1f15693f1f350ae1eea3adcba7a1043b
Author: Surya Subekti <115227173+Ayrus27@users.noreply.github.com>
Date:   Sat Jan 3 17:52:03 2026 +0700

```
