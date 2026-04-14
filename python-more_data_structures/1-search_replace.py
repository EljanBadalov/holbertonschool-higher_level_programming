#!/usr/bin/python3
def search_replace(my_list, search, replace):
    arr = []
    for i in range(len(my_list)):
        arr.append(my_list[i])
        if my_list[i] == search:
            arr[i] = replace
    return arr
