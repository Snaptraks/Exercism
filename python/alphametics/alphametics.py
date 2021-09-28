from collections import defaultdict
from itertools import permutations
import re


def solve(puzzle):
    # words in the puzzle, in reverse order
    # we cannot assume all words are surrounded by " + "
    words = re.findall(r"\w+", puzzle)[::-1]
    # order is important, so we insert letters one by one
    d = defaultdict(lambda: 0, {w[0]: 0 for w in words})
    d.update({c: 0 for c in puzzle if c.isalpha()})

    number_first_letters = len(set([w[0] for w in words]))

    for i, word in enumerate(words):
        for j, character in enumerate(word[::-1]):
            d[character] += 10**j * (min(i, 1) * 2 - 1)
    factors = d.values()

    for permutation in permutations(range(10), len(d)):
        if 0 in permutation[:number_first_letters]:
            # no word should start with 0
            continue

        if sum([f * p for f, p in zip(factors, permutation)]) == 0:
            return dict(zip(d.keys(), permutation))
