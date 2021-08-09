import numpy as np

POPULATION_SIZE = 10
MUTATION_PROBABILITY = 0.1


class Puzzle:
    rng = np.random.default_rng()

    def __init__(self, puzzle):
        self.puzzle = puzzle.replace(" ", "")
        addends, answer = self.puzzle.split("==")
        self.addends = addends.split("+")
        self.answer = answer
        self.letters = list(set(self.puzzle) - set(["+", "="]))

    def solve(self):
        while True:
            individual = self.generate_individual()
            if self.evaluate_individual(individual) == 0:
                return individual

    def generate_individual(self):
        individual = {}
        for letter in self.letters:
            individual[letter] = self.rng.integers(10)

        return individual

    def is_individual_valid(self, individual):
        if len(set(individual.values())) != len(individual.values()):
            return False

        for element in self.addends + [self.answer]:
            if individual[element[0]] == 0:
                return False

        return True

    def generate_valid_individual(self):
        while not self.is_individual_valid(
                individual := self.generate_individual()):
            pass
        return individual

    def substitute_individual(self, individual):
        addends = [self.translate(element, individual)
                   for element in self.addends]
        answer = self.translate(self.answer, individual)
        return addends, answer

    def translate(self, element, individual):
        translation = str.maketrans({k: str(v) for k, v in individual.items()})
        return int(element.translate(translation))

    def evaluate_individual(self, individual):
        """return if the individual's mapping solves the puzzle"""

        addends, answer = self.substitute_individual(individual)
        addends_sum = sum(addends)
        return answer - addends_sum


def solve(puzzle):
    p = Puzzle(puzzle)
    return p.solve()


if __name__ == '__main__':
    solution = solve("I + BB == ILL")
    print(solution)
