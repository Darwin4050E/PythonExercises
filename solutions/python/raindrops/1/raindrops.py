def convert(number):
    is_divisible_by_3 = number % 3 == 0
    is_divisible_by_5 = number % 5 == 0
    is_divisible_by_7 = number % 7 == 0
    sound = ""
    if is_divisible_by_3:
        sound += "Pling"
    if is_divisible_by_5:
        sound += "Plang"
    if is_divisible_by_7:
        sound += "Plong"
    if not (is_divisible_by_3 or is_divisible_by_5 or is_divisible_by_7):
        sound += str(number)
    return sound
