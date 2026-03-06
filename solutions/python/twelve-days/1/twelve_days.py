"""Function to help generate the lyrics of the song: "The Twelve Days of Christmas".
"""

def recite(start_verse, end_verse):
    """Generate the lyrics of the song "The Twelve Days of Christmas" given a start and end verse.

    :param start_verse: int - initial verse number from which to generate the song lyrics.
    :param end_verse: int - final verse number that indicates when the lyric generation stops.
    :return list[str] - list containing each verse generated from the song lyrics.
    """
    days = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")
    gifts = ("a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ", "four Calling Birds, ",
             "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ",
             "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, ")
    result = []
    for i_verse in range(start_verse, end_verse + 1):
        verse = "".join(["On the ", days[i_verse - 1], " day of Christmas my true love gave to me: "])
        for index in range(i_verse - 1, -1, -1):
            if i_verse != 1 and index == 0:
                verse += "and "
            verse += gifts[index]
        result.append(verse)
    return result