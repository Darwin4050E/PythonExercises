"""Functions to help determine what the nth prime is.
   math module is used to calculate the squared root of a number.
"""

import math

def prime(number):
    """Given a number n, determine what the nth prime is.

    :param number: int - nth position.
    :return: int - nth prime.
    :raises ValueError: if number is zero.
    """
    if not number:
        raise ValueError('there is no zeroth prime')
    primes = prime_generator(number)
    for index in range(1, number + 1):
        value = next(primes)
        if index == number:
            return value
    return -1

def prime_generator(number):
    """Generate the first n primes.

    :param number: - n.
    """
    result = 2
    count = 0
    while count < number:
        if all(result % index != 0 for index in range(2, int(math.sqrt(result)) + 1)):
            yield result
            count += 1
        result += 1