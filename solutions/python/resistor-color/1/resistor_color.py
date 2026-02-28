'''Functions to help work with color-code bands.
'''

def color_code(color):
    '''Calculate the value of a color-code band.

    :param color: str - a specific color-code band.
    :return: int - a value of the given color-code band.
    '''
    return colors().index(color)


def colors():
    '''List all color-code bands.

    :return: list - color-code bands.
    '''
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
