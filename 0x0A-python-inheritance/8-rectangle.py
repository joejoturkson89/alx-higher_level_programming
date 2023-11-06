#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raise an exception indicating area() is not
            implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a parameter as an integer.
        Args:
            name(str): the name of the parameter.
            value(int): the parameter to validate.
        Raise:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""Defines a class rectangle that inherits from BaseGeometry."""

class Rectangle(BaseGeometry):
    """Creates rectangle class"""
    def __init__(self, width, height):
        """Initializes rectangle."""
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height
