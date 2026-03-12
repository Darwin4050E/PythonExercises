"""Function to help determine transposed text of a given text.
   zip_longest function is used to combine multiple iterables into touple, continuing unitl the longest iterable
   is exahusted. This fills missing values with a specified fillvalue.
"""
from itertools import zip_longest

def transpose(text):
    """Determine transposed text of a given text.

    :param text: - text to be transposed.
    :return: str - transposed text.
    """
    if not text:
        return ""
    lines = text.split("\n")
    transposed = zip_longest(*lines, fillvalue=None)
    result = []
    for row in transposed:
        row_list = list(row)
        while row_list and row_list[-1] is None:
            row_list.pop()
        cleaned_row = [char if char is not None else " " for char in row_list]
        result.append("".join(cleaned_row))
    return "\n".join(result)