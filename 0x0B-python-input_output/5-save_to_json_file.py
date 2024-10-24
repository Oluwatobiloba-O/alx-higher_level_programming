#!/usr/bin/python3
"""5-save_to_json_file"""
import json
"""import json"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file
    Args:
        my_obj: object
        filename: file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)