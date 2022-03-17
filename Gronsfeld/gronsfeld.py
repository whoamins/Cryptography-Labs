import string


alphabet = string.ascii_lowercase
key = str(2015)


def encrypt(message: str):
    result = str()

    i = 0
    for _, char in enumerate(message):
        if i >= len(key):
            i = 0

        index = int(key[i])
        char_index = alphabet.index(char)

        if char_index + index >= len(alphabet):
            new_index = len(alphabet) - (len(alphabet) - 1 - index)
            result += alphabet[new_index]
            continue

        result += alphabet[char_index + index]

        i += 1

    return result


if __name__ == "__main__":
    print(encrypt("gronsfeld"))
