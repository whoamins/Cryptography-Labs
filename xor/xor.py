from cgitb import text
from itertools import cycle


def xor(text, key):
    if type(key) == int:
        result = ''

        for letter in text:
            result += chr(ord(letter) ^ key)

        return result
    
    return ''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(text, cycle(key)))
    

if __name__ == "__main__":
    print(repr(xor(text='some-text-haha', key=3)))
    print(xor(text='123', key='abc'))
