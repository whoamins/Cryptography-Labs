from Coprime import coprime


def print_all_coprime_less_than_n(n: int) -> int:
    count = 0
    for i in range(n):
        if coprime.coprime(n, i):
            print(i)
            count += 1

    return count


if __name__ == "__main__":
    print("fi(n)=", print_all_coprime_less_than_n(10))
