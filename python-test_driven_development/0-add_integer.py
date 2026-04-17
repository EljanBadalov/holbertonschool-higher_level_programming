#!/usr/bin/python3
"""Module for adding two integers"""


def add_integer(a, b=98):
    """Adds two integers a and b

    Args:
        a (int or float): first number
        b (int or float): second number (default = 98)

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to int
    a = int(a)
    b = int(b)

    return a + b
