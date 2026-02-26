import string
def rotate(text, key):
    letters = string.ascii_lowercase
    rotated_text = ""
    for char in text:
        value = char
        if char.lower() in letters:
            value = letters[(letters.find(char.lower()) + key) % 26]
        rotated_text += value if char.islower() else value.upper()
    return rotated_text