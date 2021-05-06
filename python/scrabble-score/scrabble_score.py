letter_points = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}


def score(word: str, bonus_letters: list = None, bonus_word: int = 1):
    if bonus_letters is None:
        bonus_letters = {}

    word = word.lower()
    sub_score = sum(letter_points[letter] for letter in word)

    for (letter, bonus) in bonus_letters:
        # each bonus letter in a tuple (letter, double or triple)
        # if letter counts double, add one of the value as it is
        # counted once already in sub_score (hence why we multiply
        # by (bonus - 1)
        sub_score += letter_points[letter] * (bonus - 1)

    return sub_score * bonus_word


if __name__ == '__main__':
    word = "zebra"
    print(score(word))
    print(score(word, bonus_word=3))
    print(score(word, bonus_letters=[("z", 3)], bonus_word=3))
