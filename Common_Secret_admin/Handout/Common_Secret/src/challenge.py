from Crypto.Util.number import getPrime, bytes_to_long

flag = "<REDACTED>"
m = bytes_to_long(flag.encode())

def gen_params(bits=1024):
    p = getPrime(bits)
    q = getPrime(bits)
    n = p * q
    return n, p, q

def e_gen(bits=20):
    e = getPrime(bits)
    return e

pub_key = (gen_params(1024)[0], e_gen(20))

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

def test(m):
    e1, e2 = e_gen(20), e_gen(20)
    n, p, q = gen_params(1024)
    ct1 = encrypt(m, e1, n)
    ct2 = encrypt(m, e2, n)
    print(f"Ciphertext 1 : {ct1}\nPublic Key : {n, e1}")
    print(f"Ciphertext 2 : {ct2}\nPublic Key : {n, e2}")

test(m)