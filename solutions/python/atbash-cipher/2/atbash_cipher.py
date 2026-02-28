"""Functions to help code and decode text with the Atbash cipher.
"""

def encode(plain_text):
    """Encode text with Atbash cipher.
    
    :param plain_text: str - text in latin alphabet.
    :return: str - coded text with Atbash cipher.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    clean_text = plain_text
    for character in [" ", ",", "."]:
        clean_text = clean_text.replace(character, "").lower() 
    cipher = ""
    for letter in clean_text:
        cipher_len = len(cipher.replace(" ", ""))
        if cipher_len != 0 and cipher_len % 5 == 0:
            cipher += " "
        cipher += letters[25 - letters.find(letter)] if letter in letters else letter
    return cipher


def decode(ciphered_text):
    """Decode text with Atbash cipher.

    :param ciphered_text: str - coded text with Atbash cipher.
    :return: srt - decoded text in latin alphabet.
    """
    return encode(ciphered_text).replace(" ", "")