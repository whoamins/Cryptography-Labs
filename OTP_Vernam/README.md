# What if I found out the key from the OTP algorithm and it's not a one-time key o_0?

I'll give you an example, where P - Plain Text, C - Ciphertext, K - Key.
```
P1 = 01101101
P2 = 01011010
K  = 10110100

C1 = P1 ^ K = 11011001
C2 = P2 ^ K = 11101110
```
# How can I get plaintext if I have only the key and Ciphertext.


```
C1 ^ C2 = P1 ^ P2. 
```

Let's prove it.
```
C1 ^ C2 = 00110111
P1 ^ P2 = 00110111
```

Here XOR properties come into play, I'm talking about Reversibility

```
(a ^ b) ^ b = a
```

Let's try to get P1

```
(С1 ^ С2) ^ P2 = 00110111 ^ 01011010 = 01101101 = P1
```

And now let's try to get P2

```
(С1 ^ С2) ^ P1 = 00110111 ^ 01101101 = 01011010 = P2
```
