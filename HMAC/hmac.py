import hashlib


def xor(s1, s2):
        return bytes([s1[m] ^ s2[m] for m in range(min(len(s1), len(s2)))])


def hmac(key, msg):
        block_size = 64

        if len(key) > block_size:
                key = hashlib.sha1(key)
        elif len(key) < block_size:
                key = key + b'\x00' * (block_size - len(key))

        ikeypad = xor(b'\x36' * block_size, key)
        okeypad = xor(b'\x5c' * block_size, key)

        return hashlib.sha1(okeypad + hashlib.sha1(ikeypad + msg).digest()).hexdigest()


print(hmac(key=b"sdfbghjsdfg", msg=b"bla-bla-bla"))
