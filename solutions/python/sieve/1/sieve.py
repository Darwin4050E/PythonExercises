"""Function to help implement the Sieve of Eratosthenes algorithm to find all prime numbers less than or equal to a given number.
   module math is used for calculating the squared root of a number.
"""

import math

def primes(limit):
    """Find all prime numbers less than or equal to a given number.

    :param limit: int - given number.
    :return: list[int] - list of all prime numbers less than or equal to the given number.
    """
    res = []
    if limit == 1:
        return res
    marks = (limit - 1) * [0]
    numbers = range(2, limit + 1)
    for number in numbers:
        if marks[number - 2] == 0 and not any(number % index == 0 for index in range(2, int(math.sqrt(number)) + 1)):
            count = number
            while count + number <= limit:
                marks[count + number - 2] = 1
                count += number
    for index, element in enumerate(marks):
        if not element:
            res.append(numbers[index])
    return res
            