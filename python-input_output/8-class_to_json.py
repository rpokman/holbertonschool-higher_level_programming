#!/usr/bin/python3
"""Module that provides a function to return a dictionary
description for JSON serialization of an object.
"""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj (object): Instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing all attributes of the object.
    """
    return obj.__dict__
