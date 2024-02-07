#!/usr/bin/python3
"""2-append_write"""


def append_write(filename="", text=""):
    """Appends to a text file and
    Args:
        filename: the file
        text: what to append
    """
    with open(filename, "a", encoding="utf-8") as file:
        append_str = file.write(text)
        return append_str