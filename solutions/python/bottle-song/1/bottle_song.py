"""Function to help generate the lyrics of the song: "Ten Green Bottles".
"""

def recite(start, take=1):
    """Generate the lyrics of the song "Ten Green Bottles" given a start verse and how many to take.

    :param start: int - initial verse number from which to generate the song lyrics.
    :param take: int - how many verses to take from start verse.
    :return: list[str] - list containing each verse generated from the song lyrics.
    """
    bottles = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    result = []
    for stanza in range(start, start - take, -1):
        add_1_2 = " green bottles" if stanza != 1 else " green bottle"
        add_4 = " green bottles" if stanza != 2 else " green bottle"
        verse_1_2 = "".join([bottles[stanza].title(), add_1_2, " hanging on the wall,"])
        verse_3 = "And if one green bottle should accidentally fall,"
        verse_4 = "".join(["There'll be ", bottles[stanza - 1], add_4 ," hanging on the wall."])
        for verse in [verse_1_2, verse_1_2, verse_3, verse_4]:
            result.append(verse)
        if take != 1 and stanza != start - take + 1:
            result.append("")
    return result