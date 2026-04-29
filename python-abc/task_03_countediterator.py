#!/usr/bin/python3
"""
this is global enviroment
"""


class CountedIterator:
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)   # may raise StopIteration
        self.count += 1
        return item
