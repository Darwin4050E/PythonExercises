"""Function to help evaluate simple math word problems.
   re module is used to verify the math between a pattern and a string.
"""

import re


def operate(operation, num1, num2):
    """Do the operation indicated between num1 and num2.

    :param operation: str - operation to do (plus, minus, multiplied, divided).
    :param num1: int - first number.
    :param num2: int - second number.
    """
    result = 0
    if operation == "plus": result = num1 + num2
    if operation == "minus": result = num1 - num2
    if operation == "multiplied": result = num1 * num2
    if operation == "divided": result = int(num1 / num2)
    return result


def answer(question):
    """Parse and evaluate simple math word problems returning the answer as an integer.
    
    :param question: str -  simple math word problem.
    :return: int - answer as an integer.
    :raise ValueError: 1. unknown operation if operation is not recognized.
                       2. syntax error if the question has grammatical error.
    """
    is_number = re.fullmatch(r"^What is -?\d+\?$", question)
    is_one_operation = re.fullmatch(r"^What is -?\d+ (plus|minus|multiplied by|divided by) -?\d+\?$", question)
    is_two_operation = re.fullmatch(r"^What is -?\d+ (plus|minus|multiplied by|divided by) -?\d+ (plus|minus|multiplied by|divided by) -?\d+\?$", question)
    operation = question.strip("What is ?").replace("multiplied by", "multiplied").replace("divided by", "divided").split(" ")
    if is_number: return int(operation[0])
    if is_one_operation: return operate(operation[1], int(operation[0]), int(operation[-1]))
    if is_two_operation: return operate(operation[3], operate(operation[1], int(operation[0]), int(operation[2])), int(operation[-1]))
    if any(unknow in question for unknow in ["squared", "cubed", "square root", "cube root", "modulo", "logarithm", "factorial"]): raise ValueError("unknown operation")
    raise ValueError("syntax error")