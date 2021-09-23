from collections import defaultdict
from functools import cache


@cache
def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]


def compute_palindromes(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError(
            "Minimum factor cannot be bigger than maximum factor.")

    palindromes = defaultdict(list)
    for a in range(min_factor, max_factor + 1):
        for b in range(a, max_factor + 1):
            ab = a * b
            if is_palindrome(ab):
                palindromes[a * b].append([a, b])

    return palindromes


def largest(min_factor, max_factor):

    palindromes = compute_palindromes(min_factor, max_factor)

    if not palindromes:
        return None, []

    largest_palindrome = max(palindromes.keys())

    return largest_palindrome, palindromes[largest_palindrome]


def smallest(min_factor, max_factor):

    palindromes = compute_palindromes(min_factor, max_factor)

    if not palindromes:
        return None, []

    smallest_palindrome = min(palindromes.keys())

    return smallest_palindrome, palindromes[smallest_palindrome]


if __name__ == '__main__':
    value, factors = largest(10, 99)
    print(value, factors)
