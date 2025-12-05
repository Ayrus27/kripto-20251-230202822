# Laporan Praktikum Kriptografi
Minggu ke-: 9  
Topik: [Digital Signature]  
Nama: [Surya Subekti]  
NIM: [230202822]  
Kelas: [5IKRA]  

---

## 1. Tujuan
- Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
- Memverifikasi keaslian tanda tangan digital.
- Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.(Tuliskan tujuan pembelajaran praktikum sesuai modul.)

---

## 2. Dasar Teori
Tanda tangan digital (digital signature) adalah mekanisme kriptografi yang digunakan untuk menjamin integritas, autentikasi, dan non-repudiation pada sebuah pesan atau dokumen digital. Konsep ini bekerja dengan prinsip matematika kriptografi kunci publik (public key cryptography), di mana proses penandatanganan dilakukan menggunakan kunci privat, sedangkan verifikasi dilakukan menggunakan kunci publik. Ketika sebuah pesan ditandatangani, sistem biasanya terlebih dahulu membuat hash dari pesan tersebut, kemudian hash tersebut dienkripsi menggunakan kunci privat pembuat tanda tangan. Hasil enkripsi inilah yang disebut sebagai digital signature.

Pada skema RSA Digital Signature, algoritma RSA dimanfaatkan bukan untuk enkripsi pesan, tetapi untuk melakukan proses sign–verify berbasis operasi eksponensial modular. Pengirim meng-hash pesan, lalu mengenkripsi hash tersebut menggunakan kunci privat RSA. Penerima kemudian mendekripsi tanda tangan menggunakan kunci publik untuk memperoleh hash yang asli. Jika hash tersebut identik dengan hash pesan yang dihitung ulang, maka validitas tanda tangan dapat dipastikan. RSA cenderung lebih sederhana dalam implementasi karena tidak memerlukan parameter acak setiap proses penandatanganan.

Berbeda dengan RSA, Digital Signature Algorithm (DSA) menggunakan komputasi pada domain bilangan diskrit dan modular exponentiation yang melibatkan parameter acak (nonce) pada setiap pembuatan tanda tangan. Keamanan DSA sangat bergantung pada kerahasiaan dan keunikan nilai nonce tersebut; jika nonce pernah bocor atau digunakan ulang, kunci privat dapat direkonstruksi. DSA lebih efisien dalam proses penandatanganan, sedangkan RSA biasanya lebih cepat pada proses verifikasi. Keduanya tetap menjadi standar internasional untuk memastikan keamanan komunikasi digital modern.

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
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())

try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
    
    # Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```


---

## 6. Hasil dan Pembahasan
Hasil eksekusi program Digital Signature:

![Hasil Output](screenshots/output1.png)
![Hasil Output](screenshots/output2.png)
![Hasil Output](screenshots/output3.png)


---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
    - Enkripsi RSA dan tanda tangan digital RSA sebenarnya menggunakan algoritma yang sama, tetapi keduanya memiliki tujuan dan alur kerja yang berbeda. Enkripsi RSA digunakan ketika pengirim ingin menjaga kerahasiaan isi pesan. Dalam proses ini, pengirim mengenkripsi pesan menggunakan kunci publik penerima, sehingga hanya penerima yang memiliki kunci privat dapat membuka dan membaca isi pesan tersebut. Dengan demikian, enkripsi RSA berfokus pada perlindungan isi pesan agar tidak dapat dipahami oleh pihak yang tidak berwenang.
    - Sebaliknya, tanda tangan digital RSA digunakan untuk memastikan keaslian dan integritas suatu pesan. Tujuan utamanya bukan untuk merahasiakan isi pesan, melainkan untuk membuktikan bahwa pesan benar-benar berasal dari pengirim dan tidak mengalami perubahan selama pengiriman. Pada proses ini, pengirim menggunakan kunci privatnya untuk membuat tanda tangan digital, biasanya dengan cara mengenkripsi nilai hash dari pesan. Penerima kemudian menggunakan kunci publik pengirim untuk memverifikasi tanda tangan tersebut. Jika tanda tangan valid, berarti pesan asli dan identitas pengirim dapat dipercaya.
    - Dengan demikian, perbedaan paling mendasar terletak pada arah penggunaan kunci serta tujuan keamanan yang ingin dicapai. Enkripsi RSA menjaga kerahasiaan dengan mengenkripsi menggunakan kunci publik penerima, sedangkan tanda tangan digital RSA memastikan keaslian pesan dengan menandatangani menggunakan kunci privat pengirim. Meski mekanisme matematis RSA sama, fungsi keduanya berada pada aspek keamanan yang berbeda dalam komunikasi digital modern.

2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
    - Tanda tangan digital menjamin integritas karena yang ditandatangani adalah hash dari pesan. Jika isi pesan berubah sedikit saja, hash yang dihitung ulang oleh penerima tidak akan sama dengan hash yang ada di dalam tanda tangan, sehingga perubahan langsung terdeteksi. Selain itu, tanda tangan digital memberi otentikasi karena hanya pemilik kunci privat yang dapat membuat tanda tangan tersebut. Ketika penerima memverifikasi dengan kunci publik pengirim dan tanda tangan dinyatakan valid, berarti pesan benar-benar berasal dari pemilik kunci privat tersebut. Dengan dua mekanisme ini—hashing dan kriptografi kunci publik—tanda tangan digital dapat memastikan pesan tidak diubah dan identitas pengirim terjamin.

3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?
    - Dalam sistem tanda tangan digital modern, Certificate Authority (CA) berperan sebagai lembaga terpercaya yang bertugas memverifikasi identitas seseorang atau suatu organisasi sebelum menerbitkan sertifikat digital. Sertifikat digital ini berisi kunci publik pemiliknya beserta informasi identitas yang sudah divalidasi oleh CA, sehingga pihak lain dapat yakin bahwa kunci publik tersebut benar-benar milik pemilik yang sah.
    - CA memastikan keaslian hubungan antara identitas dan kunci publik, sehingga mencegah pihak tidak bertanggung jawab membuat tanda tangan digital palsu menggunakan kunci yang tidak valid. Ketika penerima pesan memverifikasi tanda tangan digital, ia tidak hanya memeriksa validitas tanda tangan, tetapi juga memeriksa sertifikat digital yang ditandatangani oleh CA. Jika sertifikat tersebut valid dan terpercaya, maka penerima dapat yakin bahwa kunci publik yang digunakan memang milik pengirim asli.
    - Dengan demikian, CA berfungsi sebagai otoritas kepercayaan (trust anchor) dalam seluruh ekosistem kriptografi modern. Tanpa CA, pengguna tidak akan memiliki cara yang aman untuk memastikan apakah sebuah kunci publik benar-benar milik pihak tertentu, sehingga tanda tangan digital tidak dapat digunakan secara luas dan aman di internet, termasuk dalam HTTPS, email aman, dan transaksi elektronik.


---

## 8. Kesimpulan
Berdasarkan percobaan yang dilakukan, proses tanda tangan digital berhasil dibuktikan dapat menjamin integritas dan otentikasi pesan melalui mekanisme hashing dan verifikasi menggunakan pasangan kunci publik–privat. Hasil pengujian menunjukkan bahwa tanda tangan hanya valid untuk pesan asli dan langsung gagal ketika pesan dimodifikasi, sehingga membuktikan fungsi keamanan digital signature. Dengan demikian, algoritma RSA/DSA dapat digunakan sebagai solusi yang efektif untuk memastikan keaslian komunikasi digital modern.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
    week9-digital-signature

commit 769d3f77231b1237f197e163b8a99d8da9fed9b8
Author: Surya Subekti <115227173+Ayrus27@users.noreply.github.com>
Date:   Sat Dec 6 06:50:51 2025 +0700

```
