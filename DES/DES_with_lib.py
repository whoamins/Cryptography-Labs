from Crypto.Cipher import DES
from secrets import token_bytes
from sys import argv


def encrypt(message, key):
    cipher = DES.new(key, DES.MODE_EAX)
    cipher_nonce = cipher.nonce
    cipher_text, cipher_tag = cipher.encrypt_and_digest(message.encode('ascii'))

    return cipher_nonce, cipher_text, cipher_tag


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


