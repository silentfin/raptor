import random
import secrets
import pyperclip
import string

MIN_PASSWORD_LENGTH = 4
DEFAULT_PASSWORD_LENGTH = 8
LOWER_ASCII_CHARACTERS = string.ascii_lowercase
UPPER_ASCII_CHARACTERS = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation


def generate_password(length_of_password=DEFAULT_PASSWORD_LENGTH):
    """Generates a password of specified length
    Default:
        1. Length of password is 8
        2. Contains one lowercase, uppercase, digit and symbol

    Returns:
        String: Returns the generated password
    """

    accepted_characters = (
        LOWER_ASCII_CHARACTERS + UPPER_ASCII_CHARACTERS + DIGITS + SYMBOLS
    )
    print("AcceptedChars: ", accepted_characters)
    print("LengthOfPass: ", length_of_password)

    # atleast one uppercase, lowercase, digit, symbol = MIN_PASSWORD_LENGTH
    password = [
        secrets.choice(UPPER_ASCII_CHARACTERS),
        secrets.choice(LOWER_ASCII_CHARACTERS),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]

    for _ in range(length_of_password - MIN_PASSWORD_LENGTH):
        password.append(secrets.choice(accepted_characters))

    random.shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print("Generate Passwords :)")
    try:
        n = int(input("Enter the length of password (min. 4): "))
    except ValueError:
        n = DEFAULT_PASSWORD_LENGTH
    if n < MIN_PASSWORD_LENGTH:
        print("That will generate a weak password.")
        print(f"Generating password of minimum length: {MIN_PASSWORD_LENGTH}")
        n = MIN_PASSWORD_LENGTH

    generated_password = generate_password(n)
    print(f"Generate Password: {generated_password}")

    pyperclip.copy(generated_password)
    print(
        "Copied to Clipboard !!!\nPlease clear your clipboard manually for security purposes."
    )
