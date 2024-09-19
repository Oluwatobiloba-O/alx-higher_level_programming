#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary.keys())
    for x in sorted_key:
        val = a_dictionary[x]
        print("{}: {}".format(x, val))
