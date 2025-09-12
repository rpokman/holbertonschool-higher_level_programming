#!/usr/bin/python3
"""
Module 0-add_integer
contain function to add 2 integer
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        int: The sum of a and b converted to integers.

    Raises:
        TypeError: If a or b is not an integer or float (or not
                   convertible to int, e.g. inf / nan).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert safely: map OverflowError (e.g. inf) to the expected TypeError
    try:
        ai = int(a)
    except OverflowError:
        raise TypeError("a must be an integer")
    try:
        bi = int(b)
    except OverflowError:
        raise TypeError("b must be an integer")

    return ai + bi
