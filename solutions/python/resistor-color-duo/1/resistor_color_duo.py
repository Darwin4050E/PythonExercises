'''Function to help determine the value of 2 color-code bands.
'''
def value(colors):
    '''Calculata the value of the first 2 color-code bands in colors.

    :param colors: list - colors, which only the first 2 will be proccessed.
    :return: int - the result of joining the values of the first 2 color-code bands in colors.
    '''
    color_bands = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return int(str(color_bands.index(colors[0])) + str(color_bands.index(colors[1])))
