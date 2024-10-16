#!/usr/bin/python3
"""3-to_json_string module"""
import json
"""import json"""


def to_json_string(my_obj):
    """Returns JSON representation
    Args:
        my_obj: the object in json.
    """
    return json.dumps(my_obj)