def sum_of_multiples(limit, multiples):
    total = 0
    for n in range(limit):
        for m in multiples:
            if m == 0:
                continue
            if n % m == 0:
                total += n
                break
    return total
