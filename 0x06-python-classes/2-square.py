#!/usr/bin/python3
"""
This module defines a square class.
"""

class Square:
    """
    A class that defines a square class.
    """

    def __init__(self, size=0):
        """
        Initialization of a new instance of the square class.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
