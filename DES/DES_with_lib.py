from Crypto.Cipher import DES
from secrets import token_bytes
from sys import argv


def encrypt(message, key):
    cipher = DES.new(key, DES.MODE_OFB)
    cipher_text = cipher.iv + cipher.encrypt(message.encode('ascii'))

    return cipher_text.hex()


def decrypt(nonce, ciphertext, tag, key):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plain_text = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plain_text.decode('ascii')
    except ValueError:
        return False


if __name__ == "__main__":
    nonce, ciphertext, tag = encrypt(argv[1])
    plaintext = decrypt(nonce, ciphertext, tag)

    print(ciphertext)

    if not plaintext:
        print("Message is corrupted!")
    else:
        print(plaintext)


