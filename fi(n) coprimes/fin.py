from Coprime import coprime


def print_all_coprime(n: int) -> None:
    for i in range(n):
        if coprime.coprime(n, i):
            print(i)


if __name__ == "__main__":
    print_all_coprime(30)