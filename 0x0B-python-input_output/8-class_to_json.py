#!/usr/bin/python3
"""Function defines Python class-to-JSON."""


def class_to_json(obj):
    """This returns the dictionary representation of a
    simple data structure.
    """
    return obj.__dict__
