'''Function to help identify a valid ISBN-10.
'''
def is_valid(isbn):
    '''Determine if a ISBN has a valid ISBN-10 format.

    :param isbn: str - given isbn.
    :return: bool - if a given isbn has a valid ISBN-10 format.
    '''
    if isbn:
        result = 0
        isbn_new = isbn.replace("-", "")
        valid_check_char = True
        if "X" in isbn_new and isbn_new.find("X") != (len(isbn_new) - 1):
            valid_check_char = False
        if len(isbn_new) == 10 and all(char in "0123456789X" for char in isbn_new) and valid_check_char:
            for index, char in enumerate(isbn_new):
                if char in "X":
                    char = "10"
                result += int(char) * (10 - index)
            return result % 11 == 0
    return False