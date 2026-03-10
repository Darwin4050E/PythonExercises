"""Function to help count how many times each word occurs in a subtitle of a drama.
"""

def count_words(sentence):
    """Count how many times each word occurs in a subtitle of a drama.

    :param sentence: str - subtitle of a drama.
    :return: dict - dictionary with each word and its number of ocurrances.
    """
    char_spec = """!"#$%&()*+,-./:;<=>?@[\\]^_{|}~`.\n\t?"""
    result = {}
    new_sent = sentence
    for char in new_sent:
        if char in char_spec:
            new_sent = new_sent.replace(char, " ")
    split_sent = new_sent.lower().split(" ")
    for word in split_sent:
        new_word = word.strip("'")
        if new_word != "" and new_word not in result:
            result[new_word] = 1
        elif new_word != "":
            result[new_word] += 1
    return result