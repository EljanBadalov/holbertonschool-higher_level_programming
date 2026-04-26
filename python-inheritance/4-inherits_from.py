#!/usr/bin/python3
"""
this is global enviroment
"""


def inherits_from(obj, a_class):
    """
    this is function enviroment
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
