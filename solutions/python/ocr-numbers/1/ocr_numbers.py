"""Function to help implement OCR (Optical Character Recognition).
"""

def convert(input_grid):
    """Convert a grid of characters to a string of digits.

    Given a grid of characters representing some digits, convert the grid to a string of digits.
    If the grid has multiple rows of cells, the rows should be separated in the output with a ",".

        - The grid is made of one of more lines of cells.
        - Each line of the grid is made of one or more cells.
        - Each cell is three columns wide and four rows high (3x4) and represents one digit.
        - Digits are drawn using pipes ("|"), underscores ("_"), and spaces (" ").

    :param input_grid: list[str] - grid of characters that represents some digits.
    :return: str - grid converted to a string of digits.
    """
    numbers = {
        " _ | ||_|   ": "0",
        "     |  |   ": "1",
        " _  _||_    ": "2",
        " _  _| _|   ": "3",
        "   |_|  |   ": "4",
        " _ |_  _|   ": "5",
        " _ |_ |_|   ": "6",
        " _   |  |   ": "7",
        " _ |_||_|   ": "8",
        " _ |_| _|   ": "9"
    }
    n_rows = len(input_grid)
    n_cols = len(input_grid[0])
    if not n_rows % 4 == 0: raise ValueError("Number of input lines is not a multiple of four")
    if not n_cols % 3 == 0: raise ValueError("Number of input columns is not a multiple of three")
    result = ""
    for i_row in range(0, n_rows, 4):
        group = input_grid[i_row:i_row + 4]
        for i_col in range(0, n_cols, 3):
            result += numbers.get("".join(row[i_col:i_col + 3] for row in group), "?")
        if i_row != n_rows - 4:
            result += ","
    return result