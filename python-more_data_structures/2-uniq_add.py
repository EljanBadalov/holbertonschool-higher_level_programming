#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = list(map(lambda x: x, set(my_list)))
    return sum(result)
