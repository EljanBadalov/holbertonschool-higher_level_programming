#!/usr/bin/python3
"""Load and return an instance of CustomObject from a file."""

import pickle


class CustomObject():
    """Load and return an instance of CustomObject from a file."""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            return None
        except FileNotFoundError:
            return None
