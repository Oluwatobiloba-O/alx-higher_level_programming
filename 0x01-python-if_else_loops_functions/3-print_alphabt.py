#!/usr/bin/python3
for x in range(97, 123):
    if chr(x) not in ['q', 'e']:
        print("{}".format(chr(x)), end="")
