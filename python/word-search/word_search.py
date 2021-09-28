import enum
import itertools


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        x, y = self.x, self.y
        return f"{self.__class__.__name__}({x=}, {y=})"


class Direction(enum.Enum):
    left_right = [1, 0]
    right_left = [-1, 0]
    up_down = [0, -1]
    down_up = [0, 1]
    diag_left_right_up = [1, -1]
    diag_left_right_down = [1, 1]
    diag_right_left_up = [-1, -1]
    diag_right_left_down = [-1, 1]

    @property
    def dx(self):
        return self.value[0]

    @property
    def dy(self):
        return self.value[1]


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)  # y
        self.columns = len(puzzle[0])  # x

    def search(self, word):
        for y, x in itertools.product(range(self.rows), range(self.columns)):
            if self.puzzle[y][x] != word[0]:
                continue

            start = Point(x, y)

            for direction in Direction:
                dx, dy = direction.value

                for i in range(1, len(word) + 1):
                    _x, _y = x + i * dx, y + i * dy

                    if (0 <= _y < self.rows
                            and 0 <= _x < self.columns
                            and word[i] == self.puzzle[_y][_x]):

                        if i + 1 == len(word):
                            return self.get_endpoints(word, start, direction)
                    else:
                        break

    def get_endpoints(self, word, start, direction):
        len_word = len(word) - 1
        end = Point(
            start.x + len_word * direction.dx,
            start.y + len_word * direction.dy,
        )

        return start, end
