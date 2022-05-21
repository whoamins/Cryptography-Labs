from Crypto.Cipher import DES
from binascii import *


key = b"\x17\x52\x6b\x06\x23\x4e\x58\x07"
cipher = DES.new(key, DES.MODE_OFB)
text = unhexlify('D7A514D8C556AADE')
msg = cipher.decrypt(text)
print(text)