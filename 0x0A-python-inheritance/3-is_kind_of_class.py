#!/usr/bin/python3
"""Defines a class and an inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object(obj) is an instance or inherited
        instance of a class.

    Return:
        if object(obj) is an instance or inherited instance
        of a given class(a_class) - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
