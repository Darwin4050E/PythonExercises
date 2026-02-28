import math
'''Function to calculate the score earned by a dart landing at a given point.
'''
def score(x, y):
    '''Calculate the score earned by a dart landing at a given point.

    :param x: float - x-coordinate of a given point.
    :param y: float - y-coordinate of a given point.
    :return: int - 1. 0 points if the dart lands outside the target.
                   2. 1 point if the dart lands in the outer circle (r=10) of the target.
                   3. 5 points if the dart lands int the middle circle (r=5) of the target.
                   4. 10 points if the dart lands in the inner circle (r=1) of the target.
    '''
    ratio = math.sqrt(math.pow(x,2) + math.pow(y,2))
    if ratio > 10:
        return 0
    if 5 < ratio <= 10:
        return 1
    if 1 < ratio <= 5:
        return 5
    return 10