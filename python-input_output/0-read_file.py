#!/usr/bin/python3
"""Module that provides a function to read and display a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout.

    Args:
        filename (str): Name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu, end="")
