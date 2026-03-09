"""Function to help generate the lyrics of the song: "I Know an Old Lady Who Swallowed a Fly".
"""

def recite(start_verse, end_verse):
    """Generate the lyrics of the song "I Know an Old Lady Who Swallowed a Fly" given a start and end verse.

    :param start_verse: int - initial verse number from which to generate the song lyrics.
    :param end_verse: int - final verse number that indicates when the lyric generation stops.
    :return" list[str] - list containing each verse generated from the song lyrics.
    """
    animals = ("fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse")
    phrases = (
        "",
        "It wriggled and jiggled and tickled inside her.",
        "How absurd to swallow a bird!",
        "Imagine that, to swallow a cat!",
        "What a hog, to swallow a dog!",
        "Just opened her throat and swallowed a goat!",
        "I don't know how she swallowed a cow!",
        ""
    )
    result = []
    for i_verse in range(start_verse, end_verse + 1):
        result.append("".join(["I know an old lady who swallowed a ", animals[i_verse - 1], "."]))
        if i_verse not in {1, 8}:
            result.append(phrases[i_verse - 1])
            for index in range(i_verse - 1, 0, -1):
                result.append("".join(["She swallowed the ", animals[index], " to catch the ", animals[index - 1], f" that {phrases[index - 1][3:]}" if index + 1 == 3 else "."]))
        if i_verse != 8:
            result.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        else:
            result.append("She's dead, of course!")
        if i_verse != end_verse:
            result.append("")
    return result