import enum

# Game status categories
# Change the values as you see fit


class Status(enum.IntEnum):
    STATUS_ONGOING = 0
    STATUS_WIN = 1
    STATUS_LOSE = 2


globals().update(Status.__members__)


class Hangman:
    def __init__(self, word):
        self.word = word
        self.correct_guesses = set()
        self.remaining_guesses = 9
        self.status = Status.STATUS_ONGOING

    def guess(self, char):
        if self.status is Status.STATUS_LOSE:
            raise ValueError("Game Over!")

        if self.status is Status.STATUS_WIN:
            raise ValueError("You already won!")

        if char in self.word and char not in self.correct_guesses:
            self.correct_guesses.add(char)

        else:
            self.remaining_guesses -= 1

        self._check_status()

    def get_masked_word(self):
        return "".join([char if char in self.correct_guesses else "_"
                        for char in self.word])

    def get_status(self):
        return self.status

    def _check_status(self):
        if self.remaining_guesses < 0:
            self.status = Status.STATUS_LOSE

        if all([char in self.correct_guesses for char in self.word]):
            self.status = Status.STATUS_WIN
