"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

'''Functions to help classify a list in relation to another one.
'''

def sublist(list_one, list_two):
    '''Determine if list_one is EQUAL, SUBLIST, SUPERLIST, or UNEQUAL in relation to list_two.
    
    :param list_one: list - main list.
    :param list_two: list - secondary list.
    :return: str - 1. EQUAL if the sequence of elements in list_one is equals to the one in list_two.
                   2. SUBLIST if the sequence of elements in list_one is in list_two.
                   3. SUPERLIST if the sequence of elements in list_two is in list_one.
                   4. UNEQUAL if the sequence of elements in list_one is not equals to the one in list_two.
    '''
    if len(list_one) == len(list_two) and all(item1 == item2 for item1, item2 in zip(list_one, list_two)):
        return EQUAL
    if len(list_one) < len(list_two) and is_in(list_one, list_two):
        return SUBLIST
    if len(list_one) > len(list_two) and is_in(list_two, list_one):
        return SUPERLIST
    return UNEQUAL

def is_in(list_one, list_two):
    '''Determine if the sequence of elements in list_one is in list_two.
    
    :param list_one: list - main list.
    :param list_two: list - secondary list.
    :return: bool - if the sequence of elements in list_one is in list_two.
    '''
    for i in range(len(list_two) - len(list_one) + 1):
        if list_one == list_two[i:i + len(list_one)]:
            return True
    return False