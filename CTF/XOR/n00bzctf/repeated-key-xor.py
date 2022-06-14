from Crypto.Util.number import *
from pwn import xor
from itertools import cycle

flag = b'n00bz{pREDACTED}'
key1 = b'REDACTED'
enc = '_\x03\x03U\x11\x1e\t]\x07J\x06\x05\x02&F\x02G_4\x1dICl^\x07\x19V&]\x02X\x044\x15\x15\x05J\x02Y\x0c:\x0e\x00G[h\rT\x0b\x02N'
flag_format = "n00bz{p"
key = [chr(ord(o1) ^ ord(o2)) for (o1, o2) in zip(enc, flag_format)]
print(key)

plaintext = [chr(ord(o1) ^ ord(o2)) for (o1, o2) in zip(enc, cycle(key))]
print(''.join(plaintext))
