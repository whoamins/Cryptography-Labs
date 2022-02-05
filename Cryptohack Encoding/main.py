import code
from pwn import * # pip install pwntools
import json
import string
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode

r = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

i = 0
while i != 101:
    print(i)
    received = json_recv()

    if i == 100:
        print("Flag:", received['flag'])
        break

    print("Received type: ")
    type1 = received["type"]
    print(type1)
    print("Received encoded value: ")
    encoded = received["encoded"]
    print(encoded)
    decoded = str()

    if type1 == "base64":
        decoded = b64decode(encoded).decode('utf-8')
    elif type1 == "hex":
        decoded = bytes.fromhex(encoded).decode('utf-8')
    elif type1 == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif type1 == "bigint":
        decoded = bytes.fromhex(encoded.lstrip('0x')).decode('utf-8')
    elif type1 == "utf-8":
        decoded = ''.join([chr(b) for b in encoded])

    to_send = {
        "decoded": decoded
    }

    json_send(to_send)
    i += 1
