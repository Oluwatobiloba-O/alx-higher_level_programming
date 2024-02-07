#!/usr/bin/python3
"""100-append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text, after lines that has
    a string.

    Args:
        filename: name of file
        search_string: string to search for
        new_string: new string to add
    """
    with open(filename, "r", encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, "w", encoding='utf-8') as file:
        for row in lines:
            file.write(row)
            if search_string in row:
                file.write(new_string)