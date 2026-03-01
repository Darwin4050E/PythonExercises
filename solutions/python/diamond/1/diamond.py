"""Function to help form a diamond given a letter.
"""

def rows(letter):
    """Given a letter, it forms the rows of a diamond with a specific structure.
    
    :param letter: str - cappital letter with respect to which the diamond is formed.
    :return: list - diamond's rows in relation to the next requierements: 1. The first row contains one 'A'.
                                                                          2. The last row contains one 'A'.
                                                                          3. All rows, except the first and last, have exactly two identical letters.
                                                                          4. All rows have as many trailing spaces as leading spaces. (This might be 0).
                                                                          5. The diamond is horizontally symmetric.
                                                                          6. The diamond is vertically symmetric.
                                                                          7. The diamond has a square shape (width equals height).
                                                                          8. The letters form a diamond shape.
                                                                          9. The top half has the letters in ascending order.
                                                                          10. The bottom half has the letters in descending order.
                                                                          11. The four corners (containing the spaces) are triangles.
    """
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_to_print = letters[:letters.find(letter) + 1]
    diamond = []
    for index, letter_to_print in enumerate(letters_to_print):
        side_spaces = (len(letters_to_print) - (index + 1)) * " "
        intermediate_spaces = ((index * 2) - 1) * " "
        second_letter_to_print = "" if index == 0 else letter_to_print
        diamond.append(side_spaces + letter_to_print + intermediate_spaces + second_letter_to_print + side_spaces)
    for index in range(len(diamond) - 2, -1, -1):
        diamond.append(diamond[index])
    return diamond