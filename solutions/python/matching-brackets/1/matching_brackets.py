"""Function to help ifentify the parity of grouping symbols in an string expression.
"""
def is_paired(input_string):
    """Determine if a string has a pair quantity of grouping symbols.

    :param input_string: str - string to be evaluated.
    :return: bool - if input_string contains complet pairs of brackets, braces, or parentheses.
    """
    auxiliar_list = []
    for character in input_string:
        if character in ["[", "{", "("]:
            auxiliar_list.append(character)
        if character in ["]", "}", ")"]:
            if len(auxiliar_list) != 0 and (auxiliar_list[-1] + character) in ["[]", "{}", "()"]:
                auxiliar_list.pop()
            else:
                return False
    return len(auxiliar_list) == 0