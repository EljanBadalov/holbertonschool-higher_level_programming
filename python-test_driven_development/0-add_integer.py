#!/usr/bin/python3
"""This module provides a function to add two integers."""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int or float): first number
        b (int or float): second number (default is 98)

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a != a:
        raise ValueError("a cannot be NaN")

    if b != b:
        raise ValueError("b cannot be NaN")

    a = int(a)
    b = int(b)

    return a + b
