def is_armstrong_number(number):
    number_string = str(number)
    total = 0
    for i in range(len(number_string)):
        digit = int(number_string[i])
        total += digit ** len(number_string)
    if(total == number):
        return True
    return False