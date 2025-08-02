import random

DEFAULT_PASSWORD_LENGTH = 8
LOWER_ASCII_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ASCII_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "~!@#$%^&*()"


def generate_password(length_of_password=DEFAULT_PASSWORD_LENGTH):
    """Generates a password of specified length
    Default:
        1. Length of password is 8
        2. Conttains one lowercase, uppercase, digit and symbol

    Returns:
        String: Returns the generated password
    """

    accepted_characters = (
        LOWER_ASCII_CHARACTERS + UPPER_ASCII_CHARACTERS + DIGITS + SYMBOLS
    )
    print("AcceptedChars: ", accepted_characters)
    print("LengthOfPass: ", length_of_password)

    # atleast one uppercase, lowercase, digit, symbol
    password = [
        random.choice(UPPER_ASCII_CHARACTERS),
        random.choice(LOWER_ASCII_CHARACTERS),
        random.choice(DIGITS),
        random.choice(SYMBOLS),
    ]

    for _ in range(length_of_password - 4):
        password += random.choice(accepted_characters)

    # make it more complex by shuffling
    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print("Generate Passwords :)")
    n = int(input("Enter the length of password (min. 4): "))
    if n < 4:
        print("That will generate a weak password.")
    else:
        print(f"Generate Password: {generate_password(n)}")
