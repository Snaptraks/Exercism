import numpy as np


def primes(limit):
    numbers = np.arange(2, limit + 1)
    sieve = np.zeros_like(numbers)

    while True:
        try:
            current_number = numbers[sieve == 0][0]
        except IndexError:
            break
        prime_index, = np.where(numbers == current_number)
        sieve[prime_index[0]::current_number] = 2  # mark as multiple
        sieve[prime_index] = 1  # mark as prime

    mask = sieve == 1  # marked as prime
    return list(numbers[mask])
