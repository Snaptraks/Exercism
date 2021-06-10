"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from collections import Counter
import enum

# Score categories.
# Change the values as you see fit.


class Categories(enum.IntEnum):
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    LITTLE_STRAIGHT = 9
    BIG_STRAIGHT = 10
    CHOICE = 11
    YACHT = 12


globals().update(Categories.__members__)


def score(dice, category):
    counter = Counter(dice)
    face, count = counter.most_common(1)[0]  # used a few times

    if category in (
        Categories.ONES,
        Categories.TWOS,
        Categories.THREES,
        Categories.FOURS,
        Categories.FIVES,
        Categories.SIXES,
    ):
        return category * counter[category]

    if category is Categories.FULL_HOUSE:
        if set(counter.values()) == set([3, 2]):
            return sum(dice)

    if category is Categories.FOUR_OF_A_KIND:
        if count >= 4:
            return face * 4

    if category is Categories.LITTLE_STRAIGHT:
        if set(dice) == set([1, 2, 3, 4, 5]):
            return 30

    if category is Categories.BIG_STRAIGHT:
        if set(dice) == set([2, 3, 4, 5, 6]):
            return 30

    if category is Categories.CHOICE:
        return sum(dice)

    if category is Categories.YACHT:
        if count == 5:
            return 50

    # if everything fails
    return 0
