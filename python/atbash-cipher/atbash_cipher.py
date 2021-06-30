import string


def parse_text(text):
    return remove_whitespace(remove_punctuation(text))


def remove_punctuation(text):
    return _remove(text, string.punctuation)


def remove_whitespace(text):
    return _remove(text, string.whitespace)


def _remove(text, to_remove):
    return text.translate(str.maketrans("", "", to_remove))


def _cipher(letter, m=26):
    E = - (string.ascii_lowercase.index(letter) + 1) % m
    return string.ascii_lowercase[E]


def encode(plain_text):
    plain_text = parse_text(plain_text)
    encoded = ""
    for i, letter in enumerate(plain_text.lower()):
        if letter in string.ascii_lowercase:
            encoded += _cipher(letter)
        else:
            encoded += letter

        if (i + 1) % 5 == 0:
            encoded += " "

    return encoded.strip()


def decode(ciphered_text):
    ciphered_text = parse_text(ciphered_text)
    decoded = ""
    for letter in ciphered_text:
        if letter in string.ascii_lowercase:
            decoded += _cipher(letter)
        else:
            decoded += letter

    return decoded
