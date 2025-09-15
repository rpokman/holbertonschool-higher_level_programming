#!/usr/bin/python3
"""Module 1-square
Defines a class Square with a private size attribute.
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size):
        """Initialize a new Square instance
        Args:
            size: size of the square (no type/value verification at this stage)
        """
        self.__size = size
