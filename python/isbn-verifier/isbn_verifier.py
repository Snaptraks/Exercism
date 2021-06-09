import string


def has_correct_characters(isbn):
    if len(isbn) != 10:
        return False

    # check if first 9 characters are digits
    first_9_digits = all([c in string.digits for c in isbn[:-1]])
    # check if last character is digit or capital X
    last_character = isbn[-1] in string.digits or isbn[-1] == "X"

    return first_9_digits and last_character


def is_valid(isbn):
    stripped = isbn.replace("-", "").replace(" ", "")
    if has_correct_characters(stripped):
        digits = []
        for character in stripped:
            try:
                digits.append(int(character))

            except ValueError:
                digits.append(10)

        valid = sum(
            [x * m for x, m in zip(digits, range(10, 0, -1))]) % 11 == 0
        return valid

    return False
