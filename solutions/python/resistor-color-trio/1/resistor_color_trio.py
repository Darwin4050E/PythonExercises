'''Function to help determine ohms in relation to three color-code bands.
'''
def label(colors):
    '''Calculate ohms in relation to colors.

    :param colors: list - colors to be evuluated.
    :return: str - ohms in relation to colors.
    '''
    color_bands = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    ohms = str((color_bands.index(colors[0]) * 10 + color_bands.index(colors[1])) * 10 ** color_bands.index(colors[2]))
    zeros = ohms.count("0")
    if 0 <= zeros < 3:
        return ohms + " ohms"
    if 3 <= zeros < 6:
        return ohms[:len(ohms)-3] + " kiloohms"
    if 6 <= zeros < 9:
        return ohms[:len(ohms)-6] + " megaohms"
    if 9 <= zeros < 12:
        return ohms[:len(ohms)-9] + " gigaohms"