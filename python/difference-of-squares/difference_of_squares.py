import functools


@functools.cache
def sum_of_numbers(number):
    return number * (number + 1) // 2


def square_of_sum(number):
    return sum_of_numbers(number)**2


def sum_of_squares(number):
    return sum_of_numbers(number) * (2 * number + 1) // 3


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
