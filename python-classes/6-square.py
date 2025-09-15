#!/usr/bin/python3
"""Module 6-square
Defines a Square with size & position, validation,
area computation, and a custom print method.
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance
        Args:
            size (int): size of the square (default 0)
            position (tuple): (x, y) offsets, both >= 0 (default (0, 0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position (getter)"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position (setter) with validation
        Args:
            value (tuple): must be a tuple of 2 positive integers
        Raises:
            TypeError: if value is not a valid position tuple
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' respecting size & position
        - If size == 0, print an empty line
        - position[1] adds blank lines before the square
        - position[0] adds spaces to the left on each printed line
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
