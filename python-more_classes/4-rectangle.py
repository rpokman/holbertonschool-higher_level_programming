#!/usr/bin/python3
"""
Module 3-rectangle
Defines a Rectangle class with width, height,
area, perimeter and string representation.
"""


class Rectangle:
    """
    Represents a rectangle.
    Defines width and height, and provides
    methods to compute area, perimeter,
    and string representation.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.
        Args:
            width (int): rectangle width (default 0).
            height (int): rectangle height (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.
        Args:
            value (int): new width.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.
        Args:
            value (int): new height.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If width or height is 0, perimeter must be 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle.
        The rectangle is drawn with the character '#'.
        If width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""

        lignes = []
        for i in range(self.height):
            lignes.append("#" * self.width)

        return "\n".join(lignes)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
