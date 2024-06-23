from utils import convert_password_to_art, validate_password


def run() -> None:
    password = input("Your password: ")
    validate_password(password)

    ascii_art = convert_password_to_art(password[::-1])
    for line in ascii_art:
        print(line)


run()
