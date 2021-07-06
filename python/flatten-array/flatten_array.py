def flatten(iterable):
    subiterable = []
    for item in iterable:
        if isinstance(item, list):
            subiterable += flatten(item)
        elif item is not None:
            subiterable.append(item)

    return subiterable
