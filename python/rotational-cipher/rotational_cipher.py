import string


def rotate(text, key):
    rotated_text = ""
    for letter in text:
        if letter in string.ascii_letters:
            if letter.islower():
                letters = string.ascii_lowercase
            else:
                letters = string.ascii_uppercase
            rotated_text += letters[(
                letters.index(letter) + key) % 26]
        else:
            rotated_text += letter

    return rotated_text
