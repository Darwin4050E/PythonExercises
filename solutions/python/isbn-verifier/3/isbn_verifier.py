'''Function to help identify a valid ISBN-10.
'''
def is_valid(isbn):
    '''Determine if a ISBN has a valid ISBN-10 format.

    :param isbn: str - given isbn.
    :return: bool - if a given isbn has a valid ISBN-10 format.
    '''
    if isbn:
        result = 0
        isbn_ = isbn.replace("-", "")
        valid_check_char = True
        if "X" in isbn_ and isbn_.find("X") != (len(isbn_) - 1):
            valid_check_char = False
        if len(isbn_) == 10 and all(char in "0123456789X" for char in isbn_) and valid_check_char:
            for index, char in enumerate(isbn_):
                if char in "X":
                    char = "10"
                result += int(char) * (10 - index)
            return result % 11 == 0
    return False