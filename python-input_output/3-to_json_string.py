#!/usr/bin/python3
"""Module for converting Python objects to JSON string representation."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of a Python object.

    Args:
        my_obj (any): The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
