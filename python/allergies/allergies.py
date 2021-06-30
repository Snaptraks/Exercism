import enum


class AllergiesFlag(enum.IntFlag):
    eggs = 1
    peanuts = 2
    shellfish = 4
    strawberries = 8
    tomatoes = 16
    chocolate = 32
    pollen = 64
    cats = 128


class Allergies:

    def __init__(self, score):
        self.score = AllergiesFlag(score)

    def allergic_to(self, item):
        return bool(self.score & AllergiesFlag[item])

    @property
    def lst(self):
        allergies = []
        for allergy in AllergiesFlag:
            if self.score & allergy:
                allergies.append(allergy.name)

        return allergies
