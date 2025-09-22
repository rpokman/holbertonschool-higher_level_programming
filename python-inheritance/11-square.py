#!/usr/bin/python3
"""
Module 10-square
Defines a Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize square with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return square description"""
        return f"[Square] {self.__size}/{self.__size}"
