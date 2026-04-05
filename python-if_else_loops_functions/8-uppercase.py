#!/usr/bin/python3

def uppercase(str):
    for x in str:
        letter = ord(x) - 32
        print(chr(letter), end="")

