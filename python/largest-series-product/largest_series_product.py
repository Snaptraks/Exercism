def largest_product(series, size):
    if series and not series.isdigit():
        raise ValueError("Series is not all numerical.")

    if size == 0:
        return 1

    max_product = 0

    for slice in slices(series, size):
        print(slice, product(slice))
        max_product = max(max_product, product(slice))

    return max_product


def product(slice):
    prod = 1
    for d in slice:
        prod *= int(d)

    return prod


def slices(series, length):
    if length > (len_series := len(series)):
        raise ValueError(
            f"Length is greater than the series ({length} > {len_series})")

    if length <= 0:
        raise ValueError(f"Length cannot be less or equal to zero ({length})")

    slices = []
    for i in range(len_series - length + 1):
        slices.append(series[i:i + length])

    return slices
