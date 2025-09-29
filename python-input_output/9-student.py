#!/usr/bin/python3
"""Module defining a Student class with JSON serialization capability."""


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

    def to_json(self):
        """Retrieve a dictionary representation of the Student.

        Returns:
            dict: Dictionary of the student's attributes.
        """
        return self.__dict__
