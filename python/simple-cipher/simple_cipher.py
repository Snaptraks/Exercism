from itertools import cycle
import string
import random


def char_to_int(character):
    return ord(character) - ord("a")


def int_to_char(integer):
    return chr(integer % 26 + ord("a"))


class Cipher:
    def __init__(self, key=None):
        self.key = key or "".join(random.choice(string.ascii_lowercase)
                                  for _ in range(100))

    def encode(self, text):
        return self._translate(text, 1)

    def decode(self, text):
        return self._translate(text, -1)

    def _translate(self, text, direction):
        return "".join(
            int_to_char(char_to_int(text_letter)
                        + direction * char_to_int(key_letter))
            for text_letter, key_letter in zip(text, cycle(self.key))
        )
