#!/usr/bin/python3
"""
this is global enviroment
"""


class VerboseList(list):
    """
    this is global enviroment
    """

    def append(self, element):
        super().append(element)
        print(f"Added [{element}] to the list.")

    def extend(self, elements):
        for element in elements:
            super().append(element)
        print(f"Extended the list with [{len(elements)}] items.")

    def remove(self, element):
        super().remove(element)
        print(f"Removed [{element}] from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item

    def __str__(self):
        return f"array {super().__str__()}"
