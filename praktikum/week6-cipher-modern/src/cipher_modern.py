# ============================================
# 🔐 Modern Cipher Demonstration: DES, AES, and RSA
# ============================================
# Library: PyCryptodome (install via `pip install pycryptodome`)
# ============================================

from Crypto.Cipher import DES, AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

print("===== DES (Data Encryption Standard) =====")
# DES membutuhkan kunci 8 byte (64 bit)
key_des = get_random_bytes(8)
cipher_des = DES.new(key_des, DES.MODE_ECB)

# Plaintext harus 8 byte atau kelipatan 8
plaintext_des = b"ABCDEFGH"
ciphertext_des = cipher_des.encrypt(plaintext_des)
print("Ciphertext (DES):", ciphertext_des)

# Dekripsi
decipher_des = DES.new(key_des, DES.MODE_ECB)
decrypted_des = decipher_des.decrypt(ciphertext_des)
print("Decrypted (DES):", decrypted_des)
print()

# ============================================
print("===== AES (Advanced Encryption Standard) =====")
# AES menggunakan kunci 16 byte (128 bit), 24 byte (192 bit), atau 32 byte (256 bit)
key_aes = get_random_bytes(16)
cipher_aes = AES.new(key_aes, AES.MODE_EAX)

plaintext_aes = b"Modern Cipher AES Example"
ciphertext_aes, tag = cipher_aes.encrypt_and_digest(plaintext_aes)

print("Ciphertext (AES):", ciphertext_aes)

# Dekripsi
cipher_aes_dec = AES.new(key_aes, AES.MODE_EAX, nonce=cipher_aes.nonce)
decrypted_aes = cipher_aes_dec.decrypt(ciphertext_aes)
print("Decrypted (AES):", decrypted_aes.decode())
print()

# ============================================
print("===== RSA (Rivest–Shamir–Adleman) =====")
# RSA adalah algoritma asimetris (dua kunci berbeda)
key_rsa = RSA.generate(2048)
public_key = key_rsa.publickey()

# Enkripsi menggunakan kunci publik
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext_rsa = b"RSA Example"
ciphertext_rsa = cipher_rsa.encrypt(plaintext_rsa)
print("Ciphertext (RSA):", ciphertext_rsa)

# Dekripsi menggunakan kunci privat
decipher_rsa = PKCS1_OAEP.new(key_rsa)
decrypted_rsa = decipher_rsa.decrypt(ciphertext_rsa)
print("Decrypted (RSA):", decrypted_rsa.decode())

print("\n===== Semua Proses Selesai =====")
