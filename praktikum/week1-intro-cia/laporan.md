# Laporan Praktikum Kriptografi
Minggu ke-: 1  
Topik: [RIngkasan Sejarah dan Quiz]  
Nama: [Surya Subekti]  
NIM: [230202822]  
Kelas: [5IKRA]  

---

## 1. Ringkasan Sejarah Kriptografi
Kriptografi adalah ilmu dan seni mengamankan informasi untuk menjaga kerahasiaan, integritas, dan keaslian data. Istilah ini berasal dari bahasa Yunani "kryptos", yang berarti "tersembunyi", dan "graphein", yang berarti "menulis". Dalam kriptografi, data diubah menjadi bentuk yang tidak dapat dipahami oleh pihak yang tidak berwenang, biasanya melalui proses enkripsi.

Memasuki abad ke-20, terutama setelah Perang Dunia II dan kemunculan komputer dan kemajuan ilmu matematika, kriptografi mengalami lompatan besar menuju era modern. Kriptografu modern didasarkan pada prinsip matematika dan teori informasi yang kuat, serta dirancang untuk tahan terhadap komputer canggih. Dua contoh utama adalah AES (Advanced Encryption Standard) dan RSA. AES merupakan algoritma simetris yang digunakan secara luas untuk enkripsi data karena kecepatan dan keamanannya, ia mengenkripsi blok data 128-bit dengan kunci 123, 192, atau 256 bit. Sementara itu, RSA adalah algoritma asimetris pertama yang praktis, memanfaatkan kesulitan faktorisasi bilangan prima besar untuk mengamankan komunikasi tanpa pertukaran kunci rahasia menjadi tulang punggung keamanan internet modern seperti SSL/TLS.

Era kriptografi klasik mencakup metode enkripsi sederhana yang umumnya bergantung pada susbtitusi dan transposisi karakter. Salah satu contoh paling terkenal adalah Caesar Cipher, yang digunakan oleh Julius Caesar pada abad ke-1 SM. Metode ini menggeser setiap huruf dalam alfabet sebanhyak tiga posisi ke depan (misalnya, A mmenjadi D). Meski mudah dipecahkan dengan analisis frekuensi, Caesar Cipher menjadi fondasi awal kriptografi. Kemudian muncul Vigenere Cipher pada abad ke-16, yang menggunakan kunci berulang untuk mengenkripsi teks, sehingga lebih tahan terhadap analisis frekuensi sederhana. Meski demikian, keduanya tetap rentan terhadap serangan kriptoanalisis modern. Selain itu, muncul pula bidang seperti homomorphic encryption, zero-knowledge proofs, dan kriptografi pasca-kuantum yang dirancang untuk menghadapi ancaman komputer kuantum di masa depan.

Pada abad ke-21, kriptografi terus berkembang menjadi kriptografi kontemporer, yang tidak hanya fokus pada kerahasiaan data, tetapi juga pada integritas, otentikasi, dan desentralisasi. inovasi seperti blockchain dan cryptocurrency (misalnya Bitcoin) memanfaatkan fungsi hash kriptografis (seperti SHA-256) dan tanda tangan digital berbasis kriptografi asimetris untuk menciptakan sistem transaksi yang transparan, aman, dan tidak bergantung pada otoritas pusat.
## 2. Prinsip CIA
- Confidentiality → Menjaga kerahasiaan yang kita simpan atau akses, bertujuan untuk mencegah akses tidak sah terhadap data sensitif.
Contoh Nyata: Kasus kebocoran data pelanggan Tokopedia (2020), di mana data jutaan pengguna seperti email dan password bocor ke forum gelap. Hal ini menunjukkan pelanggaran prinsip confidentiality karena informasi yang seharusnya rahasia justru diakses oleh pihak tidak berwenang.
- Integrity → Menjamin bahwa data tetap akurat, konsisten, dan tidak diubah seacara tidak sah selama penyimpanan, pemrosesan, atau transmisi.
Contoh Nyata: Kasus manipulasi data hasil pemilu yang pernah mencuat di media sosial. Meskipun terbukti hoaks, isu tersebut menunjukkan pentingnya menjaga integritas sistem Sirekap KPU agar data perhitungan suara tidak dapat dimodifikasi secara ilegal oleh pihak luar.
- Availability → Menjamin ketersedian sistem , layanan, dan data tersedia saat dibutuhkan oleh pengguna yang sah. Agar gangguan seperti serangan siber, kegagalan perangkat keras, atau bencana alam harus diminimalkan agar layanan tetap berjalan.
Contoh Nyata: Pada tahun 2021, layanan e-HAC (Kemenkes) dan PeduliLindungi sempat tidak dapat diakses karena lonjakan pengguna dan gangguan server. Hal ini menjadi contoh gangguan pada aspek availability karena masyarakat tidak bisa menggunakan layanan penting tersebut tepat waktu.
Tambahkan contoh nyata minimal 1 untuk tiap aspek.
## 3. Quiz Singkat
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
    - Whitfield Diffie dan Martin Hellman
2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
    - RSA (Rivest-Shamir-Adleman)
    - ECC (Elliptic Curve Cryptography)
    - Diffie-Hellman Key Exchange
    - DSA (Digital Signature Algorithm)
3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
    - Dasar matematis: Dimana kriptografi klasik mengandalkan  substitusi dan transposisi sederhana tanpa landasan matematika yang kuat, sedangkan kriptografi modern dibangun di atas teori matematika dan komputasi kompleks.
    - Keamanan: Kriptografi klasik rentan terhadap analisis frekuensi dan serangan manual, sedangkan kriptografi modern dirancang untuk tahan terhadap serangan komputasi canggih.
    - Skema Kunci: Kriptografi klasik hanya menggunakan kunci simetris(satu kunci untuk enkripsi dan deskripsi), sedangkan kriptografi modern menggunakan kunci asimetris (kunci publik dan privat).
    - Aplikasi: Kriptografi klasik digunakan untuk komunikasi rahasia sederhana, sedangkan kriptografi modern mendukung keamanan digital modern saat ini seperti e-commerce, blockchain, otentitikasi, dan komunikasi aman di internet.

## 4. Commit Log

commit week1-intro-cia
Author: Surya Subekti <suryasubekti28@gmail.com>
Date:   2025-10-04
