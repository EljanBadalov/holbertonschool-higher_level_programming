#!/usr/bin/python3
"""Returns the JSON representation of an object."""

import json


def save_to_json_file(my_obj, filename):
    """Returns the JSON representation of an object."""
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
