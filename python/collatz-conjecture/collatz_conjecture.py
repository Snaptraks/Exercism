def steps(number):
    if number < 1:
        raise ValueError("Number cannot be smaller than 1")
    n = 0
    while number > 1:
        if number % 2 == 0:
            number //= 2

        else:
            number = 3 * number + 1

        n += 1

    return n
