#!/usr/bin/python3
"""Function that defines a class student."""


class Student:
    """This represents Students."""

    def __init__(self, first_name, last_name, age):
        """This initializes a new student."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This gets a dictionary representation of students."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
