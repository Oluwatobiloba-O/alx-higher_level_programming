#!/usr/bin/python3
"""
Function to find the max integer
"""

def max_integer(input_list=[]):
    """Function to find and return the max integer
    If the list is empty, the function returns None
    """

    if len(input_list) == 0:
        return None
    result = input_list[0]
    i = 1
    while i < len(input_list):
        if input_list[i] > result:
            result = input_list[i]
        i += 1
    return result