"""Functions to help simulate the FLower FIeld game.
"""

def validate_lens(garden):
    """Determine if each garden row has the same longitud.
    
    :param garden: list - 
    :return: bool - if all rows have the same longitud.
    """
    return len(set(len(row) for row in garden)) == 1

def validate_chars(garden):
    """Determine if each garden row has only allowed characters.
    
    :param garden: list - 
    :return: bool - if all rows have only allowed characters.
    """
    for square in garden:
        for char in square:
            if char not in {" ", "*"}:
                return False
    return True

def annotate(garden):
    """Replace the blank spaces of garden with the number of flowers around it. 
    
    :param garden: list - garden rows rows.
    :return: list - garden rows with the number of flowers around each blank space. If there are not flowers, blank space is kept.
    """
    if not garden:
        return garden
    if not (validate_lens(garden) and validate_chars(garden)):
        raise ValueError("The board is invalid with current input.")
    rows = len(garden)
    cols = len(garden[0])
    result = []
    for row in range(rows):
        row_str = ""
        for col in range(cols):
            if garden[row][col] == "*":
                row_str += "*"
                continue
            count = 0
            for digit_row in [-1, 0, 1]:
                for digit_col in [-1, 0, 1]:
                    if digit_row == 0 and digit_col == 0:
                        continue
                    new_row = row + digit_row
                    new_col = col + digit_col
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if garden[new_row][new_col] == "*":
                            count += 1
            row_str += str(count) if count > 0 else " "
        result.append(row_str)
    return result