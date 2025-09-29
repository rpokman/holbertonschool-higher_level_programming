#!/usr/bin/python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the number of characters.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written into the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
