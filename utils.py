from letter_patterns import letters
from number_patterns import numbers
import config


combined_patterns = {**letters, **numbers}


def validate_password(value: str):
    for char in value:
        if char.isspace():
            continue

        if not combined_patterns.get(char):
            raise Exception(
                f"Please use only letters and numbers. The following is not a number or letter. ({char})"
            )


def mirror_text(letter_as_list: list) -> list[str]:
    """
    Example input:
    [
        "  A  ",
        " A A ",
        "A   A",
        "AAAAA",
        "A   A",
        "A   A",
    ]
    """
    return [line[::-1] for line in letter_as_list]


def convert_password_to_art(password: str) -> list[str]:
    max_height = max(
        len(combined_patterns[char]) for char in password if char in combined_patterns
    )

    lines = ["" for _ in range(max_height)]

    for char in password:
        if not combined_patterns.get(char):
            continue

        art = mirror_text(combined_patterns[char])
        for i in range(max_height):
            if i < len(art):
                lines[i] += art[i] + " " * getattr(config, "letter_spacing", 4)
                continue

            lines[i] += " " * (len(art[0]) + getattr(config, "letter_spacing", 4))

    return lines
