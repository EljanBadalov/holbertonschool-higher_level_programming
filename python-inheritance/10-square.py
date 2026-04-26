#!/usr/bin/python3
"""
this is global enviroment
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        this is global enviroment
    """
    def __init__(self, size):
        self.__size = size

        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
