#!/usr/bin/python3
"""Module that provides a function for text indentation."""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = True

    for char in text:
        if start and char == " ":
            continue

        print(char, end="")

        if char in ".?:":
            print("\n", end="")
            start = True
        else:
            start = False
