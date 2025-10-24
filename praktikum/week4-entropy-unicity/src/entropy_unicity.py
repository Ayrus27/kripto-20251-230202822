# entropy_unicity.py
import math

# Langkah 1 — Perhitungan Entropi
def entropy(keyspace_size):
    # Rumus: H(K) = log2(|K|)
    return math.log2(keyspace_size)

# Langkah 2 — Menghitung Unicity Distance
def unicity_distance(HK, R=0.75, A=26):
    # Rumus: U = H(K) / (R * log2(|A|))
    # R = redundansi bahasa (misal: 0.75 untuk bahasa Inggris)
    # A = ukuran alfabet (default 26 untuk huruf A–Z)
    return HK / (R * math.log2(A))

# Langkah 3 — Analisis Brute Force
def brute_force_time_days(keyspace_size, attempts_per_second=1e6):
    # Menghitung waktu brute force dalam satuan hari
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

def human_readable_time(days):
    # Mengubah satuan waktu agar mudah dibaca (hari → tahun / jam / menit)
    if days >= 365:
        years = days / 365
        return f"{years:,.3g} tahun ({days:,.0f} hari)"
    elif days >= 1:
        return f"{days:,.3f} hari"
    elif days * 24 >= 1:
        return f"{days * 24:,.3f} jam"
    else:
        return f"{days * 24 * 60:,.3f} menit"

# Langkah 4 — Menampilkan Hasil Analisis
def print_summary(name, keyspace_size, attempts_per_second=1e6, R=0.75, A=26):
    HK = entropy(keyspace_size)
    U = unicity_distance(HK, R, A)
    days = brute_force_time_days(keyspace_size, attempts_per_second)
    
    print(f"# Analisis: {name}")
    print(f"Ruang kunci (|K|) = {keyspace_size:,}")
    print(f"Entropi H(K) = {HK:.6f} bit")
    print(f"Unicity Distance U = {U:.3f} karakter ciphertext (asumsi R={R}, |A|={A})")
    print(f"Waktu brute force @ {attempts_per_second:.0f} percobaan/s = {human_readable_time(days)}")
    print()

# Langkah 5 — Eksekusi Program
if __name__ == "__main__":
    # Contoh analisis untuk Caesar Cipher dan AES-128
    print_summary("Caesar Cipher (k = 26)", 26)
    print_summary("AES-128 (k = 2^128)", 2**128)
