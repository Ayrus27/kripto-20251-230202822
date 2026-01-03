PRIME = 2089

def polynom(x, coeffs):
    result = 0
    for i, c in enumerate(coeffs):
        result = (result + c * pow(x, i, PRIME)) % PRIME
    return result

def split_secret(secret, coeffs, n):
    shares = []
    for x in range(1, n + 1):
        shares.append((x, polynom(x, coeffs)))
    return shares

def recover_secret(shares):
    secret = 0
    for i, (xi, yi) in enumerate(shares):
        num, den = 1, 1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                num = (num * (-xj)) % PRIME
                den = (den * (xi - xj)) % PRIME
        secret = (secret + yi * num * pow(den, -1, PRIME)) % PRIME
    return secret

# ====== SIMULASI ======
coefficients = [123, 166, 94]  # a0, a1, a2
shares = split_secret(123, coefficients, 5)

print("Shares:", shares)
print("Recovered Secret:", recover_secret(shares[:3]))
