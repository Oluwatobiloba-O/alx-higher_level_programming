#!/usr/bin/python3
"""Class Rectangle inherits from Base"""
from models.base import Base
""" Base class module"""


class Rectangle(Base):
    """The class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is the class constructor.
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: x coordinates
            y: y coordinates
            id: Call the super class with id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This is the public getter ans setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter.
        Args:
            value: the value to be set for width
        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) is not int or value is None:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This is the public getter ans setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter
        Args:
            value: the value to be set for width
        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if type(value) is not int or value is None:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """This is the public getter ans setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The x setter
        Args:
            value: the value to be set for width
        Raises:
            TypeError: x must be an integer
            ValueError: x must be > 0
        """
        if type(value) is not int or value is None:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """This is the public getter ans setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The y setter
        Args:
            value: the value to be set for width
        Raises:
            TypeError: x must be an integer
            ValueError: x must be > 0
        """
        if type(value) is not int or value is None:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Public method that returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        Also takes into account the the coordinates.
        """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """This is the str special method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to each attribute
        Args:
            attribute_order(tuple): holds the order of the updated attributes
            args: arbituary positional arguments
            kwargs: arbituary kwyworded arguments
        Raises:
            AttributeError: If an invalid attribute name is passed
        """
        attribute_order = ('id', 'width', 'height', 'x', 'y')

        if args:
            for i, arg in enumerate(args):
                if i < len(attribute_order):
                    setattr(self, attribute_order[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key not in attribute_order:
                    raise AttributeError(
                            "The key '{}' is not an attribute".format(key)
                            )
                if key == 'width':
                    if value <= 0:
                        raise ValueError("width must be > 0")
                    self.__width = value
                elif key == 'height':
                    if value <= 0:
                        raise ValueError("height must be > 0")
                    self.__height = value
                elif key == 'x':
                    if value < 0:
                        raise ValueError("x must be >= 0")
                    self.__x = value
                elif key == 'y':
                    if value < 0:
                        raise ValueError("y must be >= 0")
                    self.__y = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }