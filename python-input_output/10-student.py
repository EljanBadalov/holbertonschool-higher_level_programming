#!/usr/bin/python3
"""Adds all command line arguments to a Pyfile."""


class Student():
    """Adds all command line arguments to a Pyfile."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        temp = {}
        data = self.__dict__
        if not attrs and attrs != []:
            return self.__dict__
        if attrs == []:
            return {}
        else:
            for element in self.__dict__:
                if element in attrs:
                    temp[element] = data[element]
            return temp
