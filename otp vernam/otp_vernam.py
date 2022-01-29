import sys

def make_vernam_cipher(text, key):
    result = str()
    counter = 0

    for char in text:
        result += chr(ord(char) ^ ord(key[counter]))
        counter += 1

        if counter == len(key):
            counter = 0
    
    return result


if __name__ == "__main__":
    plain_text = sys.argv[1]
    key = sys.argv[2]

    enc = make_vernam_cipher(plain_text, key)
    print("encrypted =", enc)
    print("decrypted =", make_vernam_cipher(enc, key))
    