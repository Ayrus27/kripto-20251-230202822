def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(cipher, key):
    return encrypt(cipher, -key)

# Contoh penggunaan
plain_text = input("Masukkan teks asli: ")
key = int(input("Masukkan kunci pergeseran: "))

cipher_text = encrypt(plain_text, key)
print("Teks terenkripsi:", cipher_text)

decrypted_text = decrypt(cipher_text, key)
print("Teks terdekripsi:", decrypted_text)
