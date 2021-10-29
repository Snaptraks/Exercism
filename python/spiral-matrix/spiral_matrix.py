import itertools


def spiral_matrix(size):
    directions = itertools.cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    # initialize empty size x size matrix
    matrix = [[None for _ in range(size)] for __ in range(size)]

    i, j = 0, 0
    di, dj = next(directions)

    for n in range(size ** 2):
        matrix[i][j] = n + 1
        _i, _j = i + di, j + dj

        # change direction if we hit edge of matrix, or hit a number
        # we will never hit an IndexError since the matrix[_i][_j] is not
        # evaluated if one fo the first statements are True
        if _i == size or _j == size or matrix[_i][_j] is not None:
            di, dj = next(directions)

        i += di
        j += dj

    return matrix
