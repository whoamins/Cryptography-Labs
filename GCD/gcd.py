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
    
    return a

def gcd_2(a: int, b: int):
    while b:
        a, b = b, a % b
    
    return a


def gcd_for_multiple_numbers():
    numbers = argv[1:]
    gcd = gcd_2(int(numbers[0]), int(numbers[1]))

    for i in range(2, len(numbers)):
        gcd = gcd_2(gcd, int(numbers[i]))

    return gcd


if __name__ == "__main__":
    print(gcd_for_multiple_numbers())
