#!/usr/bin/python3
"""Module defining a Student class that can serialize to/from JSON-like dicts.
"""


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
        """Return a dictionary representation of the Student.

        If attrs is a list of strings, only those attributes are included.
        Otherwise, all public attributes are returned.

        Args:
            attrs (list|None): Optional list of attribute names to include.

        Returns:
            dict: Dictionary representation of the student.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student from a dictionary.

        Args:
            json (dict): Keys are attribute names, values are attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
