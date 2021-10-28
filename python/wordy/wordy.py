import operator
import re

OPERATORS = {
    "plus": operator.add,
    "minus": operator.sub,
    "multiplied": operator.mul,
    "divided": operator.truediv,
}


def is_integer(value):
    return bool(re.fullmatch(r"-?\d+", value))


def answer(question):
    words = question.strip("?").replace(" by ", " ").split()
    operators = [word for word in words if word in OPERATORS]
    operands = [word for word in words if is_integer(word)]

    if len(operands) != len(operators) + 1:
        raise ValueError("Wrong number of operands or operators")

    value = int(words[2])
    i = 3
    while i < len(words):
        word = words[i]
        if word in OPERATORS:
            value = OPERATORS[word](value, int(words[i + 1]))
            i += 2

        else:
            raise ValueError("Wrong notation form")

    return value
