#!/usr/bin/python3
"""function that returns True if the object is an instance"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a_class"""
    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    return False
