#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = dict()
    for key, num in a_dictionary.items():
        mul[key] = num * 2
    return mul
