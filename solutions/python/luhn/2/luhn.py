"""Solution to Luhn exercise."""

class Luhn:
    """Create a Luhn object with a card num.

    Attributes
    ----------
    card_num: str - credit card numbers, bank account numbers, transaction codes, or tracking IDs.

    Methods
    -------
    valid(): Return true if card_num is valid according to Luhn formula, otherwise False.
    """
    
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card_num = self.card_num.replace(" ", "")
        if len(card_num) <= 1 or not card_num.isdigit():
            return False
        list_card_num = [int(char) for char in card_num]
        for index in range(len(list_card_num) - 2, -1, -2):
            double_num = list_card_num[index] * 2
            if double_num > 9:
                double_num -= 9
            list_card_num[index] = double_num
        return sum(list_card_num) % 10 == 0