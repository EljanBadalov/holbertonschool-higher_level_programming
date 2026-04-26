#!/usr/bin/python3
"""
this is global enviroment
"""


class BaseGeometry:
    """
        this is local enviroment
    """
    def area(self):
        raise Exception("area() is not implemented")
