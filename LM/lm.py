import string
from sys import argv
from DES.DES_with_lib import encrypt


def truncate_password(password: str) -> str:
    if len(password) > 14:
        password = password[:15]
    else:
        while len(password) != 14:
            password += "0"

    return password


def split_password(password):
    return password[:8], password[7:]


if __name__ == "__main__":
    user_pass = "123456".upper()
    user_pass = truncate_password(user_pass)
    password1, password2 = split_password(user_pass)

    hash1 = encrypt(message=password1, key=b"KGS!@#$%")[1]
    hash2 = encrypt(message=password2, key=b"KGS!@#$%")[1]

    print(hash1, hash2)
    
    # It doesn't work correctly now
