"""Solution to grade-school exercise.
   defaultdict function is used to create efficiently a dict with lists as default value.
"""

from collections import defaultdict

class School:
    """Create an School object.
    
    Attributes
    ----------
    grades: dict - grade as key, list of students as value.
    all_students: set - students in all grades.
    log: list - logs about added students.
    
    Methods
    -------
    add_student(name, grade): adds an student if this is not in any grade.
    roster(): returns a sorted list with all students of each grade.
    grade(grade_numbers): returns a sorted list with all students of a given grade.
    added(): returns a boolean list with logs about added students.
    """

    def __init__(self):
        self.grades = defaultdict(list)
        self.all_students = set()
        self.log = []

    def add_student(self, name, grade):
        if name in self.all_students:
            self.log.append(False)
            return
        self.grades[grade].append(name)
        self.all_students.add(name)
        self.log.append(True)

    def roster(self):
        result = []
        for grade_number in sorted(self.grades.keys()):
            result.extend(sorted(self.grades[grade_number]))
        return result

    def grade(self, grade_number):
        return sorted(self.grades.get(grade_number, []))

    def added(self):
        return self.log