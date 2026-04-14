#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary
    if a_dictionary.get(key) is not None:
        new_dict[key] = value
    else:
        new_dict[key] = value
    return new_dict
