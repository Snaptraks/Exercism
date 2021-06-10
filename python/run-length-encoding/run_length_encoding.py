import itertools


def decode(string):
    decoded = ""
    amount = 1
    for is_digit, g in itertools.groupby(string, key=lambda x: x.isdigit()):
        if is_digit:
            amount = int("".join(g))

        else:
            decoded += next(g) * amount
            try:
                while (ng := next(g)) is not None:
                    decoded += ng
            except StopIteration:
                pass

    return decoded


def encode(string):
    encoded = ""
    for k, g in itertools.groupby(string):
        n = str(l) if (l := len(list(g))) > 1 else ""
        encoded += f"{n}{k}"

    return encoded
