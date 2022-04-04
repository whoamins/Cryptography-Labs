from GCD import gcd


def coprime(a: int, b: int) -> bool:
    if gcd.gcd_2(a, b) == 1:
        return True

    return False


if __name__ == "__main__":
    print(coprime(30, 7))