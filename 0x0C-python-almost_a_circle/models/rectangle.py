#!/usr/bin/python3
"""Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a new rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def to_dictionary(self):
        """Return the dictionary representation of a rectangle."""
        dic = {'id': self.id, 'width': self.width, 'height': self.height,
               'x': self.x, 'y': self.y}
        return dic

    def update(self, *args, **kwargs):
        """Updates the attributes of a rectangle."""
        if args:
            i = 0
            keys = ['id', 'width', 'height', 'x', 'y']
            for arg in args:
                setattr(self, keys[i], arg)
                i = i + 1
            elif kwargs:
                for key, value in kwargs.items():
                    iif hasattr(self, key):
                        setattr(self, key, value)

    def validator(self, name, value):
        """Validates a rectangle."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name is 'width' or name is 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name is 'x' or name is 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Set the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Set the height of the rectangle."""
        return self.__height

    @property
    def x(self):
        """Set the x value of the rectangle."""
        return self.__x

    @property
    def y(self):
        """Set the y value of the rectangle."""
        return self.__y

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints a rectangle using the # character."""
        print('\n' * self.y, end="")
        print(''.join(' ' * self.x + '#' * self.width + '\n'
                      for times in range(self.height)), end="")

    def __str__(self):
        """Return the print() and str() reprsentation
        of the rectangle.
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width, self.height)
