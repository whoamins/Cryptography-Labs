def check_for_ascii(text: str) -> bool:
    for char in text:
        if ord(char) > 127:
            return False

    return True


flag = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

for i in range(257):
    result = ''.join([chr(x ^ i) for x in flag])

    if result.isprintable() and check_for_ascii(result):
        print(result)
