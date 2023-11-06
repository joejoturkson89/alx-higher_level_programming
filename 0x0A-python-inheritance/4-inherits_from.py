#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """This checks if an object(obj) is an inherited
        instance of a class(a_class).

    Return:
        If object(obj) is an inherited instance of
        a class(a_class) - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
