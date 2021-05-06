from collections import Counter
import re


def count_words(sentence):
    # magic regex capturing
    pattern = "(?P<word>[0-9a-z]+(?P<ap>')?(?(ap)[a-z]|))"
    matches = re.findall(pattern, sentence.lower())
    return Counter([m[0] for m in matches])
