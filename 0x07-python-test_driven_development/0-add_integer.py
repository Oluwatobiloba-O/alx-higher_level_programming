#!/usr/bin/python3

def add_integer(a, b=98):
    """This function adds two float or int numbers.
    
    Args:
        a (float): this is either an int or float.
        b (int or float): this is either an int or float.
    Return:
        result (int): holds the sum of a and b.
    """
    
    if ((type(a) is not int) and (type(a) is not float)):
        raise TypeError("a must be an integer")

    if a is None:
        raise TypeError("a must be an integer")

    if ((type(b) is not int) and (type(b) is not float)):
        raise TypeError("b must be an integer")

    result = a + b

    if result == float('inf') or result == float('-inf'):
        raise OverflowError("float overflow")

    result = int(a) + int(b)
    return result