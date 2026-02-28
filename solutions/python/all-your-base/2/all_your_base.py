'''Function to help convert a number from one base to another.
'''

def rebase(input_base, digits, output_base):
    '''Convert number in digits from input_base to ouput_base.
    
    :param input_base: int - base of the number represented ih digits.
    :param digits: list - number represented through digits.
    :param output_base: int - base of the number resulting from the conversion.
    :return: list - number resulting from the conversion.
    '''
    if input_base < 2: raise ValueError("input base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits): raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2: raise ValueError("output base must be >= 2")
    decimal = sum([digit * (input_base ** exponent) for digit, exponent in zip(digits, range(len(digits) -1, -1, -1))])
    result = []
    while decimal >= output_base:
        result.insert(0, decimal % output_base)
        decimal = decimal // output_base
    result.insert(0, decimal)
    return result