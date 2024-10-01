#!/usr/bin/python3
"""Represents a square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes a square with given size and position.

        Args:
            size (int): Calls for validation from the setter
            position (tuple): Calls for validation from the setter
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

    def __eq__(self, other):
        """Compaires two squares with equality"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compaires with not equal to"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compaires with greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compaires with greater than or equal to"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compaires with less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compaires with less than or equal to"""
        return self.area() <= other.area()