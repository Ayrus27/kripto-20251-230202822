# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Surya Subekti]  
NIM: [230202822]  
Kelas: [5IKRA]  

---

## 1. Tujuan
- Membuat sertifikat digital sederhana.
- Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
- Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).


---

## 2. Dasar Teori
Public Key Infrastructure (PKI) merupakan suatu kerangka kerja keamanan yang dirancang untuk mengelola penggunaan kriptografi kunci publik dalam lingkungan digital. PKI menyediakan mekanisme untuk pembuatan, distribusi, penyimpanan, dan pencabutan sertifikat digital yang digunakan untuk menjamin keamanan komunikasi elektronik. Dengan adanya PKI, identitas suatu entitas seperti pengguna, server, atau aplikasi dapat diverifikasi secara terpercaya, sehingga pertukaran data dapat dilakukan secara aman dan terhindar dari ancaman penyadapan maupun pemalsuan identitas.

Salah satu komponen utama dalam PKI adalah Certificate Authority (CA), yaitu lembaga tepercaya yang bertugas menerbitkan dan memvalidasi sertifikat digital. CA berfungsi sebagai pihak ketiga yang menjamin keaslian identitas pemilik sertifikat dengan cara melakukan proses verifikasi sebelum sertifikat diterbitkan. Sertifikat digital yang dikeluarkan oleh CA berisi informasi penting seperti identitas pemilik, kunci publik, masa berlaku, serta tanda tangan digital dari CA itu sendiri. Dengan demikian, CA memiliki peran penting dalam membangun kepercayaan (trust) pada sistem keamanan berbasis kriptografi kunci publik.

Selain CA, PKI juga melibatkan beberapa komponen pendukung lainnya, seperti Registration Authority (RA), repository sertifikat, serta mekanisme Certificate Revocation List (CRL) atau Online Certificate Status Protocol (OCSP). RA bertugas membantu CA dalam proses verifikasi identitas pemohon sertifikat, sedangkan repository berfungsi sebagai tempat penyimpanan sertifikat yang dapat diakses publik. Sementara itu, CRL dan OCSP digunakan untuk memastikan status keabsahan sertifikat, khususnya dalam kondisi sertifikat telah dicabut sebelum masa berlakunya berakhir. Secara keseluruhan, PKI dan CA berperan penting dalam menjamin keamanan, integritas, dan kepercayaan dalam berbagai layanan digital seperti transaksi elektronik, sistem autentikasi, dan komunikasi berbasis internet.

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
