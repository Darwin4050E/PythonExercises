import string
'''Function to apply Rotational Cipher.
'''
def rotate(text, key):
    '''Apply Rotational Cipher to a text, given a key.

    :param text: str - target text.
    :param key: int - value between 0 and 26 that sets how many values a letter is shifted.
    :return: str - text with rotational cipher applied.
    '''
    letters = string.ascii_lowercase
    rotated_text = ""
    for char in text:
        value = char
        if char.lower() in letters:
            value = letters[(letters.find(char.lower()) + key) % 26]
        rotated_text += value if char.islower() else value.upper()
    return rotated_text