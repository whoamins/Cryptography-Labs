from sys import argv


def encrypt(text: str, key: int) -> str:
    result = str()

    for char in text:
        if char.isspace():
            result += ' '
        elif char.isupper():
            result += chr((ord(char) + key - ord('A')) % 26 + ord('A'))
        else:
            result += chr((ord(char) + key - ord('a')) % 26 + ord('a'))
    
    return result


if __name__ == "__main__":
    text = argv[1]
    key = int(argv[2])

    print(encrypt(text, key))
