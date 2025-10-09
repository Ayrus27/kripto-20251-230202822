# Laporan Praktikum Kriptografi
Minggu ke-: 2
Topik: [Praktikum Cryptosystem]  
Nama: [Surya Subekti]  
NIM: [230202822]  
Kelas: [5IKRA]  

---

## 1. Tujuan
(Tujuan dari implementasi Caesar Cipher adalah untuk memahami konsep dasar kriptografi klasik, khususnya proses enkripsi dan dekripsi menggunakan metode substitusi sederhana. Melalui penerapan algoritma ini, mahasiswa dapat mempelajari bagaimana pesan teks dapat diubah menjadi bentuk yang tidak dapat dibaca tanpa kunci tertentu, serta bagaimana kunci digunakan untuk mengembalikan pesan ke bentuk aslinya. Selain itu, implementasi Caesar Cipher juga bertujuan untuk menunjukkan kelemahan sistem kriptografi sederhana terhadap serangan brute force dan analisis frekuensi, sehingga dapat menjadi dasar pemahaman bagi algoritma kriptografi modern yang lebih kompleks.)
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
Jawab pertanyaan diskusi yang diberikan pada modul.  
1. Sebutkan komponen utama dalam sebuah kriptosistem. 
    - Sebuah kriptosistem (sistem kriptografi) terdiri dari lima komponen utama:
        - Plaintext (Teks Asli):
            Data atau pesan asli yang akan diamankan sebelum dikirim.
        - Algoritma Enkripsi:
            Prosedur matematis yang digunakan untuk mengubah plaintext menjadi ciphertext (teks terenkripsi).
        - Ciphertext (Teks Terenkripsi):
            Hasil dari proses enkripsi; data yang tidak dapat dibaca tanpa dekripsi.
        - Algoritma:
            Prosedur matematis yang digunakan untuk mengembalikan ciphertext menjadi plaintext.
        - Kunci (Key):
            Parameter rahasia yang digunakan dalam proses enkripsi dan/atau dekripsi. Keamanan sistem sangat bergantung pada kerahasiaan dan kekuatan kunci.
2. Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?
    - Simetris
        - Kelebihan:
            - Lebih cepat dan efisien secara komputasi.
            - Cocok untuk enkripsi data dalam jumlah besar (misalnya file, komunikasi real-time).
        - Kekurangan:
            - Masalah distribusi kunci: kedua pihak harus memiliki kunci yang sama dan menjaganya tetap rahasia.
            - Tidak mendukung tanda tangan digital secara alami.
    - Asimetris
        - Kelebihan:
            - Tidak memerlukan pertukaran kunci rahasia secara aman sebelum komunikasi.
            - Mendukung fitur seperti tanda tangan digital dan autentikasi.
        - Kekurangan:
            - Jauh lebih lambat dan membutuhkan sumber daya komputasi lebih besar.
            - Tidak efisien untuk enkripsi data besar secara langsung.
3. Pertanyaan 3: Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?
    - Karena pada kriptografi simetris proses enkripsi dan dekripsi menggunakan kunci yang sama, maka pengirim dan penerima pesan harus memiliki kunci identik agar komunikasi dapat berlangsung. Masalah muncul pada tahap distribusi kunci, yaitu bagaimana cara mengirimkan kunci rahasia tersebut kepada pihak penerima tanpa diketahui oleh pihak lain. Jika kunci berhasil disadap atau dicuri selama proses distribusi, maka seluruh sistem keamanan akan terganggu karena pihak ketiga dapat membaca pesan yang terenkripsi. Oleh sebab itu, distribusi kunci menjadi masalah utama dalam kriptografi simetris dan sering diatasi dengan memanfaatkan kriptografi asimetris untuk menukar kunci secara aman.

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
