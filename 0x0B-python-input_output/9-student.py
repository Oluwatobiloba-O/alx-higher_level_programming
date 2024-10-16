#!/usr/bin/python3
"""9-student"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """The class constructor.
        Args:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves a dictionary representation
        of a Student.
        """
        if hasattr(self, '__dict__'):
            return self.__dict__