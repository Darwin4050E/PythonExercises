"""Function to help identify if a word or phrase is an isogram.
"""
def is_isogram(string):
    """Determine if a word or phrase is an isogram.

    :param string: str - given word or phrase.
    :return: bool - if a word or phrase is an isogram.
    """
    string = string.lower()
    return not any(char != " " and char != "-" and string.count(char) != 1 for char in string)