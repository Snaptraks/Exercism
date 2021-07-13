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
import enum


class Category(enum.IntEnum):
    SUBLIST = 1
    SUPERLIST = 2
    EQUAL = 3
    UNEQUAL = 4


globals().update(Category.__members__)


def is_sublist(list_one, list_two):
    len_list_one, len_list_two = len(list_one), len(list_two)
    for i in range(len_list_two - len_list_one + 1):
        sublist = list_two[i:len_list_one + i]
        if list_one == sublist:
            return True

    return False


def sublist(list_one, list_two):
    len_list_one, len_list_two = len(list_one), len(list_two)
    if len_list_one == len_list_two:
        if list_one == list_two:
            return Category.EQUAL

    else:
        if len_list_one < len_list_two:
            # check is one is subset of two
            if is_sublist(list_one, list_two):
                return Category.SUBLIST

        else:
            # check if two is subset of one
            if is_sublist(list_two, list_one):
                return Category.SUPERLIST

    return Category.UNEQUAL
