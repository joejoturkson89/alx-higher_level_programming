#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Sqaure(Rectangle):
    """Representa a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Sets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """stes size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square."""
        if args:
            i = 0
            keys = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, keys[i], arg)
                i = i + 1
            elif kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation
        of the square.
        """
        dic = {'id': self.id, 'size': self.size,
               'x': self.x, 'y': self.y}
        return dic

    def __str__(self):
        """Return the str() and print() representation
        of the square.
        """
        return "[{}] ({}) {}/{}" - {}.format(
            type(self).__name__, self.id, self.x, self.y,
            slef.size)
