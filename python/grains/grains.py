def square(number):
    if number < 1 or number > 64:
        raise ValueError("number cannot be less than 1 or above 64.")
    return 2**(number - 1)


def total():
    # This is a (non-convergent) geometric series
    total_grains = 2**(64) - 1

    return total_grains
