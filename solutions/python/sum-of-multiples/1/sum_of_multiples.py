"""Function to hel calculate the energy points that get awarded to players when they complete a level.
"""

def sum_of_multiples(limit, multiples):
    """Calculate the energy points that get awarded to players when they complete a level.

    The points awarded depend on two things:
      - The level (a number) that the player completed.
      - The base value of each magical item collected by the player during that level.

    The energy points are awarded according to the following rules:
      1. For each magical item, take the base value and find all the multiples of that value that are less than the level number.
      2. Combine the sets of numbers.
      3. Remove any duplicates.
      4. Calculate the sum of all the numbers that are left.

    :param limit: int - the level that the player completed.
    :param multiples: list[int] - the base value of each magical item collected by the player during that level.
    :return: int - the sum of all the multiples that are less than the limit.
    """
    mult_res = []
    for multiple in multiples:
        if not multiple:
            continue
        mult_set = set()
        count = 1
        res = 0
        while True:
            res = multiple * count
            if res >= limit:
                break
            mult_set.add(res)
            count += 1
        mult_res.append(mult_set)
    result = set()
    for element in mult_res:
        result |= element
    return sum(result)            