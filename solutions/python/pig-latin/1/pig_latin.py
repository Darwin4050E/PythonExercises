def verify_no_consonants(subtext):
    for character in subtext:
        if character in "aeiouAEIOU":
            return False
    return True

def find_vowel(text):
    for i in range(len(text)):
        if text[i] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            return i
    return -1

def translate(text):
    text = text.strip()
    text_split = []
    if text:
        text_split = text.split(" ")
        for i in range(len(text_split)):
            word = text_split[i]
            rule_1 = word.startswith(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', "xr", "yt"))
            rule_2 = find_vowel(word) != -1 and word[:find_vowel(text)]
            rule_3 = "qu" in word and verify_no_consonants(word[:word.find("qu")])
            rule_4 = "y" in word and word[:word.find("y")] and verify_no_consonants(word[:word.find("y")])
            if rule_1:
                text_split[i] = word + "ay"
            elif rule_3:
                index = word.find("qu")
                text_split[i] = word[index+2:] + word[:index+2] + "ay"
            elif rule_4:
                index = word.find("y")
                text_split[i] = word[index:] + word[:index] + "ay"
            elif rule_2:
                index = find_vowel(word)
                text_split[i] = word[index:] + word[:index] + "ay"
    return " ".join(text_split)