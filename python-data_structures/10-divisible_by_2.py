#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            copy_list.insert(i, True)
        else:
            copy_list.insert(i, False)
    return copy_list
