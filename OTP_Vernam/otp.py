import random


def otp(text):
    result = str()
    key = ''.join(random.choice([chr(i) for i in range(ord('a'), ord('z'))]) for _ in range(len(text)))

    for index, char in enumerate(text):
        result += chr(ord(char) ^ ord(key[index]))

    return result


if __name__ == "__main__":
    print(otp("hello"))
