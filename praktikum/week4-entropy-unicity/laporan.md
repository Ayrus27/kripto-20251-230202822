# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik: [Entropy & Unicity Distance]  
Nama: [Surya Subekti]  
NIM: [230202822]  
Kelas: [5IKRA]  

---

## 1. Tujuan
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
Entropy dalam kriptografi merupakan ukuran tingkat ketidakpastian atau keacakan dalam suatu sistem kunci. Semakin tinggi nilai entropi, semakin sulit bagi penyerang untuk menebak atau memprediksi kunci yang digunakan. Entropi dihitung dalam satuan bit dan mencerminkan banyaknya kemungkinan kombinasi kunci yang mungkin terbentuk. Misalnya, sebuah kunci 128-bit memiliki entropi maksimum sebesar 128 bit, yang berarti ada $$2^{128}$$kemungkinan kombinasi. Konsep ini penting karena tingkat entropi menentukan sejauh mana sistem kriptografi tahan terhadap serangan brute force — serangan yang mencoba semua kombinasi kunci secara sistematis hingga menemukan yang benar.

Unicity Distance adalah konsep yang digunakan untuk mengukur seberapa banyak ciphertext yang dibutuhkan agar kunci yang digunakan dalam proses enkripsi dapat ditentukan secara unik. Istilah ini pertama kali diperkenalkan oleh Claude Shannon dalam teori informasi. Nilai Unicity Distance bergantung pada panjang kunci, ukuran alfabet pesan, dan redundansi bahasa dari plaintext. Semakin besar nilai Unicity Distance, semakin banyak data yang diperlukan bagi penyerang untuk memecahkan kunci dengan pasti. Dengan demikian, sistem dengan Unicity Distance yang tinggi dianggap lebih aman karena tidak mudah dipecahkan hanya dengan sejumlah kecil ciphertext.

Evaluasi kekuatan kunci terhadap serangan brute force dapat dilakukan dengan menganalisis hubungan antara entropi dan Unicity Distance. Kunci dengan entropi tinggi dan Unicity Distance besar akan memiliki tingkat keamanan yang lebih baik karena memperkecil peluang keberhasilan brute force dalam waktu yang wajar. Dalam praktiknya, kekuatan kriptografi juga dipengaruhi oleh kemampuan komputasi modern; meskipun secara teoretis kunci 64-bit dapat dipecahkan dengan brute force, dalam kenyataan waktu dan sumber daya yang dibutuhkan bisa sangat besar. Oleh karena itu, pemilihan panjang kunci yang sesuai dan pengelolaan entropi yang baik menjadi faktor utama dalam memastikan keamanan sistem kriptografi modern.
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
