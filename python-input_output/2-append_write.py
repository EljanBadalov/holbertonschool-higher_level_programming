#!/usr/bin/python3
"""
this is global enviroment
"""


def append_write(filename="", text=""):
    """
    this is internal enviroment
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
