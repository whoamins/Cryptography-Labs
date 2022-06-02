v1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
v2 = bytes.fromhex('686974207468652062756c6c277320657965')


print(bytes.hex(''.join(chr(x ^ y) for x, y in zip(v1, v2)).encode()))
