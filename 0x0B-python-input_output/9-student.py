#!/usr/bin/python3
"""Function that defines a class student."""


class Student:
    """This represents Students."""

    def __init__(self, first_name, last_name, age):
        """This initializes a new student."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This gets a dictionary representation of students."""
        return self.__dict__
