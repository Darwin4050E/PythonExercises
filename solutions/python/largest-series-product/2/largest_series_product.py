"""Functions to help calculate the largest product from a serie.
   math module is used to multiplie each element of a list.
"""

import math

def largest_product(series, size):
    """Calculate the largest product of the substrings, of len size, obtained from series.

    :param series: str - of digits.
    :param size: int - len of substrings.
    :return: int - largest product of substrings.
    """
    if size < 0: raise ValueError("span must not be negative")
    if size > len(series): raise ValueError("span must not exceed string length")
    if not series.isdigit(): raise ValueError("digits input must only contain digits")
    max_product = -1
    sub_gen = substring_generator(series, size)
    products = []
    try:
        while True:
            substring = next(sub_gen)
            products.append(math.prod([int(char) for char in substring]))
    except StopIteration:
        max_product = max(products)
    return max_product

def substring_generator(series, size):
    """Generate substrings of len "size" from "series".
    
    :param series: str - of digits.
    :param size: int - len of substrings.
    """
    start = 0
    end = size
    while end <= len(series):
        yield series[start:end]
        start += 1
        end += 1