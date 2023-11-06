#!/usr/bin/python3
""" Defines a subclass or child list class Mylist."""


class MyList(list):
    """This class is a subclass of a built-in list class."""

    def print_sorted(self):
        """This prints a sorted list in ascending order."""
        print(sorted(self))
