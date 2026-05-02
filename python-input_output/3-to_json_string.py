#!/usr/bin/python3
"""Returns the JSON representation of an object."""

import json


def to_json_string(my_obj):
    """
    this is global enviroment
    """
    data = my_obj
    return json.dumps(data)
