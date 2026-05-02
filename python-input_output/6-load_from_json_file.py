#!/usr/bin/python3
"""Returns the JSON representation of an object."""

import json


def load_from_json_file(filename):
    """Returns the JSON representation of an object."""
    with open(filename, "r") as file:
        return json.load(file)
