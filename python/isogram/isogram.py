from collections import Counter


def is_isogram(string):
    if string == "":
        return True

    stripped = string.replace(" ", "").replace("-", "").lower()

    counter = Counter(stripped)
    return counter.most_common(1)[0][1] == 1
