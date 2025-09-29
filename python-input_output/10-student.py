#!/usr/bin/python3
"""Module defining a Student class with JSON"""


class Student:
    """Represent a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student.

        If attrs is a list of strings, only attributes with names
        in this list are included.

        Args:
            attrs (list, optional): List of attribute names.

        Returns:
            dict: Dictionary representation of the Student.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
                }
        return self.__dict__
