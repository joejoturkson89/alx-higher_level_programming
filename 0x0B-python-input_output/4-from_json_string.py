#!/usr/bin/python3
"""Function that defines  JSON-to-object."""
import json


def from_json_string(my_str):
    """This returns the Python object representation of a JSON string."""
    return json.loads(my_str)
