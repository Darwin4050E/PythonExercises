"""Function to help calculate the isqrt of a positive integer using binary search.
More approaches here: https://en.wikipedia.org/wiki/Integer_square_root
"""
def square_root(number):
    """Calculate the insteger square root (isqrt) of a positive integer.

    :param number: int - positive integer.
    :return: int - positive integer square root of number.
    """
    lower_bound = 0
    upper_bound = number + 1
    while lower_bound != upper_bound - 1:
        mid = (lower_bound + upper_bound) // 2
        if mid * mid <= number:
            lower_bound = mid
        else:
            upper_bound = mid
    return lower_bound