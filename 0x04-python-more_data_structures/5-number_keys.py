#!/usr/bin/python3
def number_keys(a_dictionary):
    val = 0
    for x in a_dictionary:
        val = val + 1
        if isinstance(a_dictionary[x], dict):
            val = val + number_keys(a_dictionary[x])
    return val
