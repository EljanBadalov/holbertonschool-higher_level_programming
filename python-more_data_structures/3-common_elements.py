#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    if len(set_1) > len(set_2):
        max_l = set_1
        min_l = set_2
    else:
        max_l = set_2
        min_l = set_1
    for i in max_l:
        if i in min_l:
            result.append(i)
    return result
