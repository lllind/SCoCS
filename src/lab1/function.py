import constant

def func(number_1: float, number_2: float, operation: str):
    result = 0.0
    if operation == constant.ADD:
        result = number_1 + number_2
    if operation == constant.SUB:
        result = number_1 - number_2
    if operation == constant.MULT:
        result = number_1 * number_2
    if operation == constant.DIV:
        result == number_1 / number_2
    return result