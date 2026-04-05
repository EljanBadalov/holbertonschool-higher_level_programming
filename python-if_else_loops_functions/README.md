# Python - if/else, loops, functions

## Description

This project covers the fundamental building blocks of Python programming. The focus is on control flow tools—allowing the program to make decisions and repeat actions—and the creation of functions to write modular, reusable code.

## Learning Objectives

By the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

  * The importance of indentation in Python.
  * How to use the `if`, `if ... else`, and `elif` statements.
  * How to use `while` and `for` loops.
  * The difference between Python's `for` loop and other languages.
  * How to use the `break` and `continue` statements.
  * How to use the `else` clause in loops.
  * What the `pass` statement does and when to use it.
  * How to use `range`.
  * What a function is and how to use functions.
  * What happens when a function does not have a `return` statement.
  * Variable scope and the `traceback`.

-----

## Core Concepts

### 1\. Control Flow (Conditionals)

Python uses standard logical conditions to perform different actions for different decisions.

[Image of Python if-else flow chart]

```python
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")
```

### 2\. Loops

Python has two primitive loop commands: `while` and `for`.

  * **For Loops:** Used for iterating over a sequence (like a list, a tuple, a dictionary, or a string).
  * **While Loops:** Executed as long as a condition is true.

### 3\. Functions

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function.

```python
def my_function(param):
    """Docstring explaining the function"""
    return param * 2
```

-----

## Requirements

  * **Allowed editors:** `vi`, `vim`, `emacs`.
  * **Operating System:** Ubuntu 20.04 LTS.
  * **Language Version:** Python 3.8.5.
  * **Style Guide:** All files must conform to `pycodestyle` (version 2.8.\*).
  * **Execution:** All files must be executable. The first line of all your files should be exactly `#!/usr/bin/python3`.

-----

## Task Summary

| File | Task Description |
| :--- | :--- |
| `0-positive_or_negative.py` | Assign a random signed number to a variable and print if it is positive/negative/zero. |
| `1-last_digit.py` | Print the last digit of a random number and its properties. |
| `2-print_alphabet.py` | Print the ASCII alphabet in lowercase using a loop. |
| `3-print_alphabt.py` | Print the alphabet excluding 'q' and 'e'. |
| `7-islower.py` | Function that checks for lowercase character. |
| `8-uppercase.py` | Function that prints a string in uppercase. |
| `11-pow.py` | Function that computes $a$ to the power of $b$. |

-----

## Usage

To run any script, ensure it has executable permissions:

```bash
chmod u+x 0-positive_or_negative.py
./0-positive_or_negative.py
```

## Author

  * **Your Name** - [Your GitHub](https://www.google.com/search?q=https://github.com/your-username)
