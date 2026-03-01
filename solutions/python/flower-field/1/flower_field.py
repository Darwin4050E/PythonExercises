"""Functions to help simulate the FLower FIeld game.
"""

def validate_lens(garden):
    """Determine if each garden row has the same longitud.
    
    :param garden: list - 
    :return: bool - if all rows have the same longitud.
    """
    len_first_square = len(garden[0])
    return all(len(square) == len_first_square for square in garden)

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
    if len(garden) > 0: 
        if not(validate_lens(garden) and validate_chars(garden)):
            raise ValueError("The board is invalid with current input.")
        for index_square, square in enumerate(garden):
            new_square = ""
            for index_char, char in enumerate(square):
                count = 0
                if char in " ":
                    can_up = index_square - 1 >= 0
                    can_down = index_square + 1 < len(garden)
                    can_left = index_char - 1 >= 0
                    can_right = index_char + 1 < len(square)
                    if can_up:
                        if can_left:
                            count += 1 if garden[index_square - 1][index_char - 1] in "*" else 0
                        if can_right:
                            count += 1 if garden[index_square - 1][index_char + 1] in "*" else 0
                        count += 1 if garden[index_square - 1][index_char] in "*" else 0
                    if can_down:
                        if can_left:
                            count += 1 if garden[index_square + 1][index_char - 1] in "*" else 0
                        if can_right:
                            count += 1 if garden[index_square + 1][index_char + 1] in "*" else 0
                        count += 1 if garden[index_square + 1][index_char] in "*" else 0
                    if can_left:
                        count += 1 if garden[index_square][index_char - 1] in "*" else 0
                    if can_right:
                        count += 1 if garden[index_square][index_char + 1] in "*" else 0
                new_square += char if count == 0 else str(count)
            garden[index_square] = new_square
    return garden