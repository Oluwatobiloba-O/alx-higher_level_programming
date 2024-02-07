#!/usr/bin/python3
"""4-from_json_string module"""
import json
"""import json"""


def from_json_string(my_str):
    """Returns an object
    Args:
        my_str: string converted to object
    """
    return json.loads(my_str)