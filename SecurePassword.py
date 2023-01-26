secure = (('a', '@'), ('s', '$'), ('o', '0'), ('and', '&'), ('i', '1'))


def secure_password(password):
    for a, b in secure:
        password = password.replace(a, b)
    return password


if __name__ == '__main__':
    password = input("Enter a password: ")
    password = secure_password(password)
    print(password)
