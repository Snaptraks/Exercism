def saddle_points(matrix):
    if not matrix:
        return []

    nrows = len(matrix)
    ncols = len(matrix[0])

    if any([len(row) != ncols for row in matrix]):
        raise ValueError("Irregular matrix")

    possible_rows = set()

    for i in range(nrows):
        row = matrix[i]
        max_in_row = max(row)
        col_index = [j for j in range(len(row)) if row[j] == max_in_row]
        for j in col_index:
            possible_rows.add((i, j))

    possible_cols = set()

    for j in range(ncols):
        col = [matrix[i][j] for i in range(nrows)]
        min_in_col = min(col)
        row_index = [i for i in range(len(col)) if col[i] == min_in_col]
        for i in row_index:
            possible_cols.add((i, j))

    return [{"row": i + 1, "column": j + 1}
            for i, j in (possible_cols & possible_rows)]
