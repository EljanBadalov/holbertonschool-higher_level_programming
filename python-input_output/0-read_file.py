#!/usr/bin/python3
"""
this is global enviroment
"""


def read_file(filename=""):
    """
    this is internal enviroment
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        print(data, end="")
