#!/usr/bin/python3
"""
0-add_integer module.

Provides a single function, add_integer(a, b=98), which adds two numbers.
Both arguments can be ints or floats; floats are converted to ints before
addition. Any other type, or non-convertible floats like inf/nan, raises
a TypeError with the required message.
"""


def add_integer(a, b=98):
    """
    Add two numbers as integers.

    Args:
        a (int|float): First operand. If float, it is cast to int.
        b (int|float): Second operand. Defaults to 98. If float, cast to int.

    Returns:
        int: The integer sum of a and b after casting.

    Raises:
        TypeError: If a or b is not int/float, or is a float not convertible
                   to int (e.g. inf or nan), with the exact expected message.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        ai = int(a)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer")
    try:
        bi = int(b)
    except (OverflowError, ValueError):
        raise TypeError("b must be an integer")

    return ai + bi
