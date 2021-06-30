# Globals for the directions
# Change the values as you see fit
NORTH = 0
WEST = 1
SOUTH = 2
EAST = 3


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self._x, self._y = x, y
        self.direction = direction

    @property
    def coordinates(self):
        return self._x, self._y

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "A":
                self.advance()

            else:
                # MUST be L or R
                self.turn(instruction)

    def turn(self, direction):
        if direction == "L":
            self.direction += 1

        elif direction == "R":
            self.direction -= 1

        self.direction %= 4

    def advance(self):
        if self.direction == NORTH:
            self._y += 1

        elif self.direction == SOUTH:
            self._y -= 1

        elif self.direction == EAST:
            self._x += 1

        elif self.direction == WEST:
            self._x -= 1
