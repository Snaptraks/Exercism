class Matrix:
    def __init__(self, matrix_string: str):
        self.entries = [[int(x) for x in row.split()]
                        for row in matrix_string.split("\n")]

    def row(self, index: int):
        return self.entries[index - 1]

    def column(self, index: int):
        return [row[index - 1] for row in self.entries]
