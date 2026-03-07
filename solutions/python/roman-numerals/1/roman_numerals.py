"""Function to help convert a number from arabic to roman.
"""

def roman(number):
    """Convert a number from arabic to roman. 

    :param number: int - arabic number between 1 and 3999.
    :return: str - roman number.
    """
    conversion = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    len_num = len(str(number))
    digits = []
    for index in range(len_num - 1, -1, -1):
        digits.append((number // 10**index) % 10)
    roman_number = ""
    for index in range(len_num):
        digit = digits[index]
        if 1 <= digit <= 3:
            roman_number += digit * conversion.get(10**(len_num - 1 - index))
        elif 6 <= digit <= 8:
            roman_number += conversion.get(5 * 10**(len_num - 1 - index)) + ((digit % 3) + 1) * conversion.get(10**(len_num - 1 - index))
        else: 
            roman_number += conversion.get(digit * 10**(len_num - 1 - index), "")
    return roman_number