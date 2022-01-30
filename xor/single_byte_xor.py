def single_byte_xor(text: bytes, key: int) -> bytes:
    return bytes([x ^ key for x in text])

if __name__ == "__main__":
    cipher = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
    cipher = bytes.fromhex(cipher)
    for i in range(257):
        print(i, single_byte_xor(cipher, i).decode("utf-8", errors='ignore'))