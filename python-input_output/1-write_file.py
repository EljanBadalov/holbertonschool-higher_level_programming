#!/usr/bin/python3
"""
this is global enviroment
"""


def write_file(filename="", text=""):
    """
    this is internal enviroment
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
