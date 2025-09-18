#!/usr/bin/python3
"""Define a class MyList that inherits from list"""


class MyList(list):
    """Print the list sorted in ascending order"""
    def print_sorted(self):
        print(sorted(self))
