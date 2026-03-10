"""Function to help change the data format of letters and their point values in the Lexiconia game.
"""

def transform(legacy_data):
    """Change the data format of letters and their point values in the game.
       
       Currently, letters are stored in groups based on their score, in a one-to-many mapping.
        - 1 point: "A", "E", "I", "O", "U", "L", "N", "R", "S", "T",
        - 2 points: "D", "G"
       This needs to be changed to store each individual letter with its score in a one-to-one mapping.
        - "a" is worth 1 point.
        - "b" is worth 3 points.
       As part of this change, the team has also decided to change the letters to be lower-case rather than upper-case.

    :param legacy_data: dict - 
    :return: dict - 
    """
    result = {}
    for point, letters in legacy_data.items():
        for letter in letters:
            result.setdefault(letter.lower(), point)
    return result