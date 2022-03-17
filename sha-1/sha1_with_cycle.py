from hashlib import sha1


def hash_message(message: bytes):
    hash_1 = sha1(message)
    print(hash_1.hexdigest())
    return hash_1.hexdigest()


def main(message: str, rounds: int):
    result_hash = hash_message(bytes(message))

    for i in range(rounds):
        result_hash = hash_message(result_hash.encode('utf-8'))

    return result_hash


if __name__ == "__main__":
    main(message=b"hello world ahahhaha you dumb", rounds=0)

