#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value * value + 1:
            print("{:d}".format(value))
            return True
        else:
            return False
    except Exception:
        return False
