def leap_year(year):
    is_divisible_by_4 = year % 4 == 0
    is_divisible_by_100 = year % 100 == 0
    is_divisible_by_400 = year % 400 == 0
    if(is_divisible_by_4 and not is_divisible_by_100):
        return True
    if(is_divisible_by_4 and is_divisible_by_100 and is_divisible_by_400):
        return True
    return False