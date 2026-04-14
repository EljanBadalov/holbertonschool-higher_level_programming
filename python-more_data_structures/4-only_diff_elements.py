#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    result_total = []
    result.extend(list(set_1))
    result.extend(list(set_2))
    for i in result:
        if result.count(i) < 2:
            result_total.append(i)
    return set(result_total)
