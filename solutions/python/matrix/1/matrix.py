"""Solution to matrix exercise.
"""

class Matrix:
    """Create a MAtrix objetc from a matrix string.

    Attributes
    ----------
    matrix_string: str - matrix in string format.
    matrix: list - matrix in list format.

    Methods
    -------
    create_matrix(): makes a matrix from a string matrix.
    row(index): returns a specified row.
    column(index): returns a specified column.
    """

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix = self.create_matrix()

    def create_matrix(self):
        "Make a matrix from a string matrix."
        result = []
        for row in self.matrix_string.split("\n"):
            result.append([int(number) for number in row.split()])
        return result

    def row(self, index):
        "Return a specified row."
        return self.matrix[index - 1]

    def column(self, index):
        "Return a specified column."
        return [self.matrix[i_row][index - 1] for i_row in range(len(self.matrix))]