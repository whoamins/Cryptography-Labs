from gcd import gcd_2

def extended_gcd(a: int, b: int):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)
    
    return gcd, y1 - (b // a) * x1, x1


if __name__ == "__main__":
    g, u, v = extended_gcd(26513, 32321)
    print(g, u, v)
