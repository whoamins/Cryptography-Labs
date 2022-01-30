from sys import argv


def gcd(a: int, b: int):
    while True:
        if a > b:
            a -= b
        elif a < b:
            b -= a
        elif a == b:
            print(f"GCD is {a}")
            break


if __name__ == "__main__":
    # TODO: Find GCD for more than 2 numbers

    gcd(int(argv[1]), int(argv[2]))