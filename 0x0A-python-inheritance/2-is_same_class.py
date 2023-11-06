#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an insatnce of a given class.

    Returns:
        if object (obj) is exactly an instance of the
        given class(a_class) - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
