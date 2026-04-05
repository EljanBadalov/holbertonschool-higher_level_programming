#!/usr/bin/python3
def uppercase(letter):
    lst = ""
    for i in letter:
        a = 0
        if 97 <= ord(i) <= 122:
            a = ord(i) - 32
            lst += chr(a)
        else:
            lst += i
    print("{}".format(lst))
