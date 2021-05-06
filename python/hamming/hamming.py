def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(
            "Length of both strands are different "
            f"({len(strand_a)} != {len(strand_b)})."
        )

    # strands have the same length here
    differences = 0
    for (a, b) in zip(strand_a, strand_b):
        if a != b:
            differences += 1

    return differences
