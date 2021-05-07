import re


def abbreviate(words):
    pattern = "(?P<word>[0-9a-z]+(?P<ap>')?(?(ap)[a-z]|))"
    matches = re.findall(pattern, words.lower())
    return "".join(word[0][0] for word in matches).upper()
