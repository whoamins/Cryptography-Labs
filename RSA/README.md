# RSA Explanation

RSA - public key cryptosystem (asymmetric) is nowadays used in a wide variety of applications.

## Algorithm

Here I'll describe the encryption/decryption and key generation algorithms of RSA

1. Key Generation
    - Choose two random prime numbers _p_ and _q_
    - Calculate n. n = pq
    - Select a public exponent _e_. _e_ and (p - 1)(q - 1) must relatively prime.
    - Calculate d. d = e ^ -1 mod (p - 1)(q - 1)
    - Public key = (n, e). Secret Key = d
2. Encryption(publickey, message)
    - Return the c(iphertext) c = m ^ e mod n
3. Decryption(secretkey, ciphertext)
    - Return decrypted message m = c ^ d mod n


## Example
Let's imagine, that _p_ = 6 and _q_ = 11. Therefore, n = 66.
Let's select number 3 for public exponent (_e_) (VULNERABLE).

TODO......
