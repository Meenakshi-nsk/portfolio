# Common Secret

## Challenge Description

We encrypted the message twice, just to be safe.
Different keys, same modulus.
What could possibly go wrong?

**MD5 Hash** : e06bb7f7695589dbe67d4e3e99ea2efd

## Writeup 
- The same flag is encrypted twice using the same RSA modulus but different coprime exponents.
- Using Bézout's identity and the extended Euclidean algorithm, we can find coefficients that combine the two ciphertexts to recover the flag.

### Flag
`bi0s{b3z0ut_f0und_1t}`

### Author 
**fih**