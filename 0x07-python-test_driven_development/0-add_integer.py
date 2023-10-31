#!/usr/bin/python3
"""
Script defines a function for integer additions
"""


def add_integer(a, b=98):
    """
    This function returns the addition of a and b.

    If a or b is a non-integer and float, TypeError is raised.
    Float arguments are typecasted.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b, must be an integer")
    return int(a) + int(b)
