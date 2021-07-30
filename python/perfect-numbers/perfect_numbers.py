from sympy import proper_divisors


def classify(number):
    if number < 1:
        raise ValueError(f"{number} is not a positive integer.")

    divisors = proper_divisors(number)
    aliquot_sum = sum(divisors)
    if aliquot_sum == number:
        return "perfect"

    elif aliquot_sum > number:
        return "abundant"

    elif aliquot_sum < number:
        return "deficient"
