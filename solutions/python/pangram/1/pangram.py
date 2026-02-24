def is_pangram(sentence):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_procesed = ""
    count = 0
    sentence = sentence.lower()
    for letter in sentence:
        if letter in letters and letter not in letters_procesed:
            letters_procesed = letters_procesed + letter
            count += 1
    return count == 26