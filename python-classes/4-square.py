#!/usr/bin/python3
"""This is the module docstring."""


class Square:
    """Represents a system user."""
    def __init__(self, size=0):
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        if type(self.__size) is not int:
            return "size must be an integer"
        else:
            return self.__size

    @size.setter
    def size(self, data):
        self.__size = data
