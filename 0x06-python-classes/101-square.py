#!/usr/bin/python3
"""Represents a square"""


class Square:
    """Defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with given size and position.

        Args:
            size (int): Calls for validation from the setter
            position (tuple): Calls for validation from the setter
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the current size of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the size of the square."""
        if (
                (type(value) is not tuple) or (len(value) != 2) or
                (type(value[0]) is not int) or (type(value[1]) is not int) or
                (value[0] < 0) or (value[1] < 0)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
         """This calculates and return the area of the Square."""
         
         calculate = self.__size * self.__size
         return calculate

    def my_print(self):
        """Prints the square using '#' characters."""
        
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Delegate to my_print() for consistent output"""

        output = ""

        if self.__size == 0:
            output += "\n"
            return output
        else:
            for i in range(self.__position[1]):
                output += "\n"
            for i in range(self.__size):
                output += (" " * self.__position[0] + "#" * self.__size)
                if (i < self.__size - 1):
                    output += "\n"
            return output