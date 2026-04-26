#!/usr/bin/python3
"""
this is global enviroment
"""


def lookup(obj):
    """
        this is local enviroment
    """
    return dir(obj)
