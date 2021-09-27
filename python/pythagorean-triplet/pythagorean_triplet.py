def triplets_with_sum(number):
    """
    Algorithm taken from
    https://www.geeksforgeeks.org/pythagorean-triplet-with-given-sum-using-single-loop/
    """
    triplets = []

    for a in range(1, number):
        b = (number * number - 2 * number * a) // (2 * number - 2 * a)

        c = number - a - b

        if (b > 0 and c > 0
                and a * a + b * b == c * c):
            triplet = sorted([a, b, c])
            if triplet in triplets:
                # we've found a repeating triplet, break early
                break
            triplets.append(sorted([a, b, c]))

    return triplets
