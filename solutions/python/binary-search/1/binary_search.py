"""Function to help implement binary search.
"""

def find(search_list, value):
    """Determine the position of value within search_list.

    :param search_list: list[int] - list of integer numbers.
    :return: int - position of value within search_list.
    :raises ValueError: if value is not in search_list
    """
    list_ord = sorted(search_list)
    start = 0
    end = len(list_ord) - 1
    while start <= end:
        middle = (start + end) // 2
        if list_ord[middle] == value:
            return middle
        elif list_ord[middle] > value:
            end = middle - 1
        else:
            start = middle + 1
    raise ValueError("value not in array")