from sys import argv


def encrypt(text: str):
    result = str()

    for index, char in enumerate(text):
        result += text[len(text) - (index + 1)]

    return result


if __name__ == "__main__":
    print(encrypt(argv[1]))

