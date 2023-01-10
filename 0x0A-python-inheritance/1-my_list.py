#!/usr/bin/python3
"""
    writes a class that inherits from list
"""


class MyList(list):
    """The subclass that inherits from list"""
    def __init__(self):
        """initialize my list"""
        super().__init__(self)

    def print_sorted(self):
        """prints the list sorted"""
        print(sorted(self))
