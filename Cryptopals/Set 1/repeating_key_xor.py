from itertools import cycle


def xor(str1: str, key: str) -> str:
    return bytes.hex(''.join([chr(ord(x) ^ ord(y)) for x, y in zip(str1, cycle(key))]).encode())


print(xor("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal", "ICE"))
