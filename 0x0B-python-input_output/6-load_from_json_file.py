#!/usr/bin/python3
"""Function that defines JSON file-reading."""
import json


def load_from_json_file(filename):
    """This creates a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
