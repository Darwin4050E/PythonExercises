"""Function to help identify anagrams of a word.
"""

def find_anagrams(word, candidates):
    """Determine the candidate words that are anagrams of a given word.
    
    :param word: str - given word.
    :param candidates: list - candidate words.
    :return: list - candidate words that are anagrams of word.
    """
    l_word = word.lower()
    result = []
    for candidate in candidates:
        l_cand = candidate.lower()
        if l_word != l_cand and all(l_cand.count(char) == l_word.count(char) for char in l_cand):
            result.append(candidate)
    return result