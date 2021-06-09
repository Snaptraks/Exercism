import string


def is_pangram(sentence):
    letters = set(character for character in sentence.lower()
                  if character in string.ascii_lowercase)
    return len(letters) == 26
