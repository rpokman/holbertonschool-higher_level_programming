#!/usr/bin/python3
"""BaseGeometry"""


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
