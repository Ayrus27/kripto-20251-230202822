import random

# bilangan prima besar
PRIME = 208351617316091241234326746312124448251235562226470491514186331217050270460481

# konversi string ke integer
def str_to_int(s):
    return int.from_bytes(s.encode(), 'big')

# konversi integer ke string
def int_to_str(i):
    length = (i.bit_length() + 7) // 8
    return i.to_bytes(length, 'big').decode()

# fungsi polinomial
def polynom(x, coefficients):
    result = 0
    for power, coef in enumerate(coefficients):
        result = (result + coef * pow(x, power, PRIME)) % PRIME
    return result

# split secret
def split_secret(secret, k, n):
    secret_int = str_to_int(secret)
    coeffs = [secret_int] + [random.randrange(0, PRIME) for _ in range(k - 1)]

    shares = []
    for x in range(1, n + 1):
        y = polynom(x, coeffs)
        shares.append((x, y))
    return shares

# lagrange interpolation
def recover_secret(shares):
    secret = 0
    for i, (xi, yi) in enumerate(shares):
        num, den = 1, 1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                num = (num * (-xj)) % PRIME
                den = (den * (xi - xj)) % PRIME
        lagrange = yi * num * pow(den, -1, PRIME)
        secret = (PRIME + secret + lagrange) % PRIME
    return int_to_str(secret)

# ================== TEST ==================
secret = "KriptografiUPB2025"
shares = split_secret(secret, 3, 5)

print("Shares:")
for s in shares:
    print(s)

recovered = recover_secret(shares[:3])
print("\nRecovered secret:", recovered)
