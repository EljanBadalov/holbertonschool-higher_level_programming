#!/usr/bin/python3
"""
this is global enviroment
"""


def is_same_class(obj, a_class):
    """
    this is function enviroment
    """
    if type(obj) is a_class:
        return True
    else:
        return False
