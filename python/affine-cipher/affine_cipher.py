import string
from string import ascii_lowercase as letters
from math import gcd


def modular_inverse(x, p):
    """Return the value y such as x * y == 1 (mod p)"""

    return pow(x, -1, p)


def encode(plain_text, a, b):
    plain_text = plain_text.lower()
    encoded_letters = []

    def _encode_character(character):
        m = len(letters)
        if gcd(a, m) != 1:
            raise ValueError("a and m must be coprime")

        x = letters.index(character)

        return letters[(a * x + b) % m]

    for character in plain_text:
        if character in letters:
            encoded_letters.append(_encode_character(character))

        if character in string.digits:
            encoded_letters.append(character)

    # black magic that adds 1 to the number of groups if there is a remainder
    # of letters for groups of 5
    n_groups = len(encoded_letters) // 5 + bool(len(encoded_letters) % 5)

    encoded_text = " ".join([
        "".join(encoded_letters[i * 5:(i + 1) * 5])
        for i in range(n_groups)
    ])

    return encoded_text


def decode(ciphered_text, a, b):
    ciphered_text = ciphered_text.replace(" ", "")
    decoded_letters = []

    def _decode_character(character):
        m = len(letters)
        if gcd(a, m) != 1:
            raise ValueError("a and m must be coprime")

        n = modular_inverse(a, m)

        y = letters.index(character)

        return letters[n * (y - b) % m]

    for character in ciphered_text:
        if character in letters:
            decoded_letters.append(_decode_character(character))

        if character in string.digits:
            decoded_letters.append(character)

    return "".join(decoded_letters)
