import random

from sys import argv


alphabet = {
    "a": 1, "b": 86, "c": 2, "d": 20, "e": [62, 82], "f": 22,
    "g": 6, "h": 60, "i": 3, "j": 7, "k": 87,
    "l": 24, "m": 26, "n": 84, "o": 9, "p": 66, "q": 68,
    "r": 28, "s": 42, "t": 80, "u": [4, 40], "z": 88, "et": 8, 
    "con": 64, "non": 00, "che": 44, "v": 67, "y": 45
}

def encrypt(message: str) -> str:
    result = str()

    for char in message:
        try:
            char = alphabet[char.lower()]

            if isinstance(char, list):
                result += str(random.choice(char))
                continue

            result += str(char)

        except KeyError:
            continue

    return result


if __name__ == "__main__":
    print(argv[1])
    