'''Function to help calculate the value in ohms of a resitance with 4 or 5 bands. 
'''

def resistor_label(colors):
    '''Determine the value in ohms of a resistance with 4 or 5 bands.

    :param colors: list - color-code bands to be evaluated.
    :return: str - result in ohms. if it is necessary, the result has a prefix or a tolerance.
    '''
    color_bands = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    color_tolerances = ["grey", "violet", "blue", "green", "brown", "red", "gold", "silver"]
    value_tolerances = ["±0.05%", "±0.1%", "±0.25%", "±0.5%", "±1%", "±2%", "±5%", "±10%"]
    total_resistance = 0
    for color, index in zip(colors[:len(colors)-2], range(len(colors)-3, -1, -1)):
        total_resistance += color_bands.index(color) * (10 ** index)
    total_resistance *= 10 ** color_bands.index(colors[-2]) if len(colors) >= 4 else 1
    prefix = ""
    if 1000 <= total_resistance < 1000000:
        total_resistance = total_resistance / 1000
        prefix = "kilo"
    if 1000000 <= total_resistance < 1000000000:
        total_resistance = total_resistance / 1000000
        prefix = "mega"
    if 1000000000 <= total_resistance < 1000000000000:
        total_resistance = total_resistance / 1000000000
        prefix = "giga"
    total_resistance = str(total_resistance).replace(".0", "") if str(total_resistance).endswith(".0") else str(total_resistance)
    tolerance = value_tolerances[color_tolerances.index(colors[-1])] if len(colors) >= 4 else ""
    return f"{total_resistance} {prefix}ohms {tolerance}".strip(" ") 