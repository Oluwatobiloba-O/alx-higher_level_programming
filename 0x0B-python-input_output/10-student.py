#!/usr/bin/python3
"""10-student"""


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

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation
        of a Student instance.
        """
        result = {}
        if attrs is None:
            for key in self.__dict__:
                result[key] = getattr(self, key)
        else:
            for key in attrs:
                if hasattr(self, key):
                    result[key] = getattr(self, key)
        return result