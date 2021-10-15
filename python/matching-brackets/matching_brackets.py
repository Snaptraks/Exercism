from collections import defaultdict


LEFT = ["[", "{", "("]
RIGHT = ["]", "}", ")"]
BRACKETS = LEFT + RIGHT

MATCH = {left: right for left, right in zip(LEFT, RIGHT)}


def is_paired(input_string):
    count = defaultdict(lambda: 0)
    opened = []

    for character in input_string:
        if character in BRACKETS:
            if character in LEFT:
                opened.append(character)
                count[character] += 1

            elif character in RIGHT:
                if not opened:
                    return False

                elif character != MATCH[opened[-1]]:
                    return False

                else:
                    last_bracket = opened.pop()
                    count[last_bracket] -= 1

    return all(v == 0 for v in count.values())
