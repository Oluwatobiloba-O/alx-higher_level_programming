#!/usr/bin/python3
"""Represents a square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes a square with the given size.

        Args:
            size (int): Calls for validation from the setter.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This calculates and return the area of the Square."""
        
        calculate = self.__size * self.__size
        return calculate