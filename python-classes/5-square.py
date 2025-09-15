#!/usr/bin/python3
"""Module 4-square
Defines a class Square with a private size attribute,
validation, and getter/setter methods.
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new Square instance
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size (getter)"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size (setter) with validation
        Args:
            value (int): new size
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # characters"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
