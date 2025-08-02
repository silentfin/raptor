import random

MIN_PASSWORD_LENGTH = 4
DEFAULT_PASSWORD_LENGTH = 8
LOWER_ASCII_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ASCII_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "~!@#$%^&*()"


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
        random.choice(UPPER_ASCII_CHARACTERS),
        random.choice(LOWER_ASCII_CHARACTERS),
        random.choice(DIGITS),
        random.choice(SYMBOLS),
    ]

    for _ in range(length_of_password - MIN_PASSWORD_LENGTH):
        password += random.choice(accepted_characters)

    # make it more complex by shuffling
    random.shuffle(password)

    # returns the super strong password :)
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

    print(f"Generate Password: {generate_password(n)}")
