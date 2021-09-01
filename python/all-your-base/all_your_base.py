def to_decimal(digits: list, base: int) -> int:
    decimal = 0
    for i, digit in enumerate(reversed(digits)):
        decimal += digit * base**i

    return decimal


def from_decimal(decimal: int, base: int) -> list:
    digits = []
    while decimal > 0:
        digits.append(decimal % base)
        decimal //= base

    digits.reverse()
    return digits or [0]


def rebase(input_base, digits, output_base):
    if input_base <= 1 or output_base <= 1:
        raise ValueError("One or both bases are invalid.")

    if any([d < 0 or d >= input_base for d in digits]):
        raise ValueError("One or many digits are invalid.")

    return from_decimal(to_decimal(digits, input_base), output_base)
