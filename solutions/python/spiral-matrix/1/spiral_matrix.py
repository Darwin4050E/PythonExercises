"""Function to help generate a spiral matrix of size*size.
"""

def spiral_matrix(size):
    """Generate a spiral matrix of size*size.

    :param size: int - dimension.
    :return: list - spiral matrix.
    """
    start_col = 0
    end_col = size - 1
    start_row = 0
    end_row = size - 1
    number = 1
    matrix = []
    for _ in range(size):
        matrix.append(size * [0])
    for _ in range(size // 2 if size % 2 == 0 else (size + 1) // 2):
        for i_col in range(start_col, end_col + 1):
            matrix[start_row][i_col] = number
            number += 1
        for i_row in range(start_row + 1, end_row + 1):
            matrix[i_row][end_col] = number
            number += 1
        for i_col in range(end_col - 1, start_col - 1, -1):
            matrix[end_row][i_col] = number
            number += 1
        for i_row in range(end_row - 1, start_col, -1):
            matrix[i_row][start_col] = number
            number +=1
        start_row += 1
        start_col += 1
        end_row -= 1
        end_col -= 1
    return matrix