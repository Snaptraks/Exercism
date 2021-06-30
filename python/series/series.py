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
