#!/usr/bin/python3
"""
Module 6-rectangle
Defines a Rectangle class with width, height,
area, perimeter, string representation,
and keeps track of the number of instances.
"""


class Rectangle:
    """
    Represents a rectangle.

    Class attributes:
        number_of_instances (int): Counter for the number of Rectangle.

    Instance attributes:
        width (int): The width of the rectangle (default 0).
        height (int): The height of the rectangle (default 0).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.
        Args:
            width (int): rectangle width (default 0).
            height (int): rectangle height (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        for _ in range(self.height):
            lignes.append(str(self.print_symbol) * self.width)
        return "\n".join(lignes)

    def __repr__(self):
        """Return a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area.
        If areas are equal, return rect_1.
        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.
        Raises:
            TypeError: if rect_1 or rect_2 is not an instance of Rectangle.
        Returns:
            Rectangle: the rectangle with the bigger area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __del__(self):
        """Print a message when a Rectangle instance is deleted,
        and decrement the instance counter.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
