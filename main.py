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
        None: For now, it just prints the password as is.
    """

    accepted_characters = (
        LOWER_ASCII_CHARACTERS + UPPER_ASCII_CHARACTERS + DIGITS + SYMBOLS
    )
    print("AcceptedChars: ", accepted_characters)
    print("LengthOfPass: ", length_of_password)

    password = []
    for i in range(length_of_password):
        password += random.choice(accepted_characters)

    # make it more complex by shuffling i guess
    random.shuffle(password)
    password = "".join(password)
    print(f"Generate Password: {password}")


if __name__ == "__main__":
    print("Generate Passwords :)")
    n = int(input("Enter the length of password: "))
    generate_password(n)
