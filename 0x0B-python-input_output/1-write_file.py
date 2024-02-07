#!/usr/bin/python3
"""1-write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file
    Args:
        filename: name of file
        text: text in the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        str_txt = file.write(text)

        return str_txt