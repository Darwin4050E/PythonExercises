"""Function to help with the count of the eggs in a coop.a
"""

def egg_count(display_value):
    """Calculate total eggs in a coop in relation to binary representation of a given display_value.

    :param display_value: int - value in the screen.
    :return: int - 1's withing the binary representation of display_value.
    """
    return bin(display_value)[2:].count("1")