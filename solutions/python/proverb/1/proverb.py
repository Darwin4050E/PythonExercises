"""Function to help generate the relevant proverb given a list of inputs.
"""

def proverb(*args, qualifier):
    """Generate the relevant proverb given a list of inputs.

    :param: arbitrary number of strings.
    :param qualifier: str - keyword argument value to modify the final verse of your Proverb.
    :return: list[str] - list with the sentences of the relevant Proverb.
    """
    if not args:
        return []
    first, *left = args
    *list1, = *left, first
    result = []
    for el1, el2 in zip(args, list1):
        if el2 != first:
            result.append("".join(["For want of a ", el1 ," the ", el2 ," was lost."]))
        else:
            result.append("".join(["And all for the want of a ", f"{qualifier} " if qualifier else "" , first, "."]))
    return result