#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_cpy = a_dictionary.copy()
    for (k, v) in a_cpy.items():
        a_cpy[k] = v * 2
    return a_cpy
