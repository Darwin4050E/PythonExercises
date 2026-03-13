"""Solution to dnd-character exercise.
   math module is used to get the floor of a number.
   random modules is used to get a random integer number.
"""

import math, random

class Character:
    """Create a character object with six abilities.

    Attributes
    ----------
    (Class)stats: list[str]
    
    Methods
    -------
    ability(): Return a random character skill value.
    """

    stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma", "hitpoints"]

    def __init__(self):
        for stat in self.stats[:-1]:
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            total = sum(rolls)
            setattr(self, stat, total)
        self.hitpoints = 10 + math.floor((self.constitution - 10) / 2)

    def ability(self):
        return getattr(self, self.stats[random.randint(0, 6)])

def modifier(value):
    """Modify a given value.

    :param value: int - given value.
    :return: int - modified value.
    """
    return math.floor((value - 10) / 2)