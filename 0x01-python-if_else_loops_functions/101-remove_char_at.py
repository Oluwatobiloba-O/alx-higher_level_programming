#!/usr/bin/python3
def replace_c(x, y):
    if y < 0 or y >= len(x):
        return x
    output = ""
    for z in range(len(x)):
        if z != y:
            output += x[z]
    return output
