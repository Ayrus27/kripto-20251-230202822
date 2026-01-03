# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Surya Subekti]  
NIM: [230202822]  
Kelas: [5IKRA]  

---

## 1. Tujuan
- Penggunaan kriptografi pada email dan SSL/TLS.
- Menjelaskan enkripsi dalam transaksi e-commerce.
- Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

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
```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```


---

## 6. Hasil dan Pembahasan
Hasil eksekusi program Aplikasi TLS:

![Hasil Output](screenshots/output.png)


---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara HTTP dan HTTPS?
    - HTTP (Hypertext Transfer Protocol) merupakan protokol komunikasi web yang mengirimkan data dalam bentuk teks biasa (plaintext) sehingga rentan terhadap penyadapan dan manipulasi oleh pihak tidak berwenang. Sebaliknya, HTTPS (Hypertext Transfer Protocol Secure) adalah versi aman dari HTTP yang menggunakan TLS/SSL untuk mengenkripsi data selama proses transmisi. Dengan HTTPS, kerahasiaan, integritas, dan keaslian data lebih terjamin, sehingga pengguna terlindungi dari serangan seperti man-in-the-middle.
2. Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
    - Sertifikat digital berfungsi untuk memverifikasi identitas pihak yang berkomunikasi (misalnya server web) dalam protokol TLS. Sertifikat ini diterbitkan oleh Certificate Authority (CA) yang terpercaya dan berisi informasi identitas serta kunci publik pemilik sertifikat. Dengan adanya sertifikat digital, klien dapat memastikan bahwa koneksi yang terjalin benar-benar menuju server yang sah, sehingga mencegah pemalsuan identitas dan meningkatkan kepercayaan dalam komunikasi aman.
3. Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?
    - Kriptografi mendukung privasi dalam komunikasi digital dengan cara melindungi kerahasiaan data, menjamin integritas informasi, serta memastikan autentikasi pihak yang berkomunikasi. Namun, di sisi lain, penggunaan kriptografi—terutama enkripsi kuat dan end-to-end encryption—menimbulkan tantangan hukum dan etika. Aparat penegak hukum dapat mengalami kesulitan dalam proses penyelidikan karena data tidak dapat diakses, sementara secara etis muncul dilema antara hak atas privasi individu dan kepentingan keamanan publik. Oleh karena itu, diperlukan regulasi dan kebijakan yang seimbang agar perlindungan privasi tetap terjaga tanpa menghambat penegakan hukum.
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
    week12-aplikasi-tls

commit 4667d8ab1158fd88e53fc60826f06538c17a2b63
Author: Surya Subekti <115227173+Ayrus27@users.noreply.github.com>
Date:   Sat Jan 3 18:17:44 2026 +0700

```
