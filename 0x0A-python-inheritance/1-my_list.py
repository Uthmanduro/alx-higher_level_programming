#!/usr/bin/python3
"""
    writes a class that inherits from list
"""
class List:
    """the parent class"""
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
        """inittialize """

class MyList(List):
    """The subclass that inherits from list"""
    def __init__(self):
        """initialize the instance in the class"""

    def print_sorted(self):
        """prints the list nut sorted"""
        for item in zip(keys, values):
            self.items_list.append(item)
        print(self.items_list.sort())
