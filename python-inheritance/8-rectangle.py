#!/usr/bin/python3
"""
this is global enviroment
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        this is local enviroment
    """
    def __init__(self, width, height):
        """
            this is local enviroment
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")
