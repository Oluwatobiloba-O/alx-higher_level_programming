#!/usr/bin/python3

def print_square(size):
    """
    This prints a square with the character #.
    Raises:

    size must be an integer.
    size must be >= 0.
    """

    if size is None:
        raise TypeError("missing one argument - size")
    
    if type(size) is not int:
        if type(size) is float and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)