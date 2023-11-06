#!/usr/bin/python3
"""Defines a base class for geometry."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Raise an exception indicating area() is not
            implemented.
        """
        raise Exception("area() is not implemented")
