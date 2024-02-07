#!/usr/bin/python3
"""6-load_from_json_file"""
import json
"""import json"""


def load_from_json_file(filename):
    """Creates an Object from a “JSON file.
    Args:
        filename:file
    """
    with open(filename, "r") as file:
        return json.load(file)