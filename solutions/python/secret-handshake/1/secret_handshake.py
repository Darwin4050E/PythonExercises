"""Function to help convert a number between 0 and 31 
"""
def commands(binary_str):
    """

    :param binary_str: str - binary number as a string.
    :return: list - actions in relation decodification of binary_str.
    """
    patterns = {"0": "wink", "1": "double blink", "2": "close your eyes", "3": "jump", "4": "reverse"}
    result = []
    for index, binary in enumerate(binary_str[::-1]):
        if binary == "1":
            result.append(patterns.get(str(index)))
    return result[-2::-1] if "reverse" in result else result