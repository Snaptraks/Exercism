PLANTS = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets",
}


class Garden:
    def __init__(self, diagram: str, students: list = None):
        self.diagram = diagram.split("\n")
        if students is None:
            self.students = [
                "Alice",
                "Bob",
                "Charlie",
                "David",
                "Eve",
                "Fred",
                "Ginny",
                "Harriet",
                "Ileana",
                "Joseph",
                "Kincaid",
                "Larry",
            ]
        else:
            self.students = students
        self.students.sort()

    def plants(self, student):
        i = self.students.index(student)
        student_plants = "".join([row[2 * i:2 * i + 2] for row in self.diagram])
        return [PLANTS[plant] for plant in student_plants]
