import string
import random


class RobotNames:
    existing = set()


class Robot:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        if self._name is not None:
            return self._name

        while (name := self._generate_random_name()) in RobotNames.existing:
            # generate a new name if one already exists
            pass

        self._name = name
        RobotNames.existing.add(name)
        return name

    def reset(self):
        RobotNames.existing.remove(self._name)
        self._name = None

    def _generate_random_name(self):
        random.seed()  # make sure the generator is random
        prefix = "".join(random.choices(string.ascii_uppercase, k=2))
        suffix = random.randint(0, 999)
        name = f"{prefix}{suffix:03d}"
        return name
