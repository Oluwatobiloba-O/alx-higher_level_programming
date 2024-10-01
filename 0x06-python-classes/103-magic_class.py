#!/usr/bin/python3
"""Represents a square"""
import math


class MagicClass:
    """Determines the area and cir of a circle."""
    def __init__(self, radius=0):
        """radius: the radius of a circle"""

        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Determines the area of a circle.

        Returns:
            float: The calculated area of a circle.
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Determines the cir of a circle

        Returns:
            float: The calculated cir of a circle.
        """
        return 2 * math.pi * self._MagicClass__radius