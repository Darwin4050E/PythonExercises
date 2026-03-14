"""Solution to kinergarten-garden exeercise.
"""

class Garden:
    """Create a Garden object with a register of plants, diagram, and list of students,

    Attributes
    ----------
    plants_reg: dict - register of plants
    diagram: str - organization of plant in relation to the students.
    students: list - ordered students.

    Methods
    -------
    plants(student): returns the plants of a specific student.
    """

    plants_reg = {"C": "Clover", "G": "Grass", "R": "Radishes", "V": "Violets"}

    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", 
                         "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"] if not students else sorted(students)

    def plants(self, student):
        "Return the plants of a specific student."
        result = []
        diagram = self.diagram.split("\n")
        i_student = self.students.index(student)
        std_plants = "".join([diagram[0][i_student * 2:(i_student + 1) * 2], diagram[1][i_student * 2:(i_student + 1) * 2]])
        for plant in std_plants:
            result.append(self.plants_reg.get(plant, ""))
        return result
        
