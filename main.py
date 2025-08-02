import random

DEFAULT_PASSWORD_LENGTH = 8
LOWER_ASCII_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ASCII_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "~!@#$%^&*()"


def generate_password(length_of_password=DEFAULT_PASSWORD_LENGTH):

    accepted_characters = (
        LOWER_ASCII_CHARACTERS + UPPER_ASCII_CHARACTERS + DIGITS + SYMBOLS
    )
    print(accepted_characters)
    print(length_of_password)


if __name__ == "__main__":
    print("Generate Passwords :) \n")
    n = int(input("Enter the length of password: "))
    generate_password(n)
