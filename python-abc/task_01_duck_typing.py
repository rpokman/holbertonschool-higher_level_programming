#!/usr/bin/env python3

from abc import ABC, abstractmethod

PI = 3.141592653589793


class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class, inherits from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * (self.radius ** 2)

    def perimeter(self):
        return 2 * PI * self.radius


class Rectangle(Shape):
    """Rectangle class, inherits from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
