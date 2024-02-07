#!/usr/bin/python3
"""This is the  BaseGeometry class"""


class BaseGeometry:
   def area(self):
        """Public instance method -
        that raises an Exception with the message
        area() is not implemented
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")