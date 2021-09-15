from collections import Counter
from functools import cache


PER_BOOK = 800
PER_GROUP = {
    n + 1: (n + 1) * PER_BOOK * discount for n, discount in enumerate(
        [1., .95, .90, .80, .75])
}


@cache
def find_biggest_discount(basket):
    """basket needs to be a tuple to be hashable to cache"""

    volumes = Counter(basket)
    num_books = len(basket)
    num_volumes = len(volumes)

    if num_volumes == 1:
        # only one volume, multiple books
        return num_books * PER_BOOK

    if num_books == num_volumes:
        # one copy of each volume
        return PER_GROUP[num_volumes]

    # recurse to find other arrangements
    price = num_books * PER_BOOK
    for n in range(1, num_volumes + 1):
        group = volumes - Counter(k for k, _ in volumes.most_common(n))
        subbasket = tuple(sorted(group.elements()))
        price = min(price, PER_GROUP[n] + find_biggest_discount(subbasket))

    return price


def total(basket):
    if len(basket) == 0:
        return 0

    return find_biggest_discount(tuple(sorted(basket)))
