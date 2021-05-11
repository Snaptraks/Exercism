class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append((grade, name))
        self.students.sort()

    def roster(self):
        return [student[1]
                for student in self.students]

    def grade(self, grade_number):
        return [student[1]
                for student in self.students
                if student[0] == grade_number]
