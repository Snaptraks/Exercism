import sympy  # why not use pregenerated primes


def factors(value):
    prime_factors = []
    for prime in sympy.primerange(2, value + 1):
        while value % prime == 0:
            prime_factors.append(prime)
            value //= prime
        if value == 1:
            return prime_factors

    return prime_factors
