#!/usr/bin/python3
"""Represents a square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes a square with the given size.

        Args:
            size (int): A private attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This calculates and returns the area of the Square."""
        calculate = self.__size * self.__size
        return calculate