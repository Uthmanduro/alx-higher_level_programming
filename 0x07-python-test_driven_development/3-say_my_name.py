#!/usr/bin/python3
"""
    Prints the name passed to the functione on scrren
"""


def say_my_name(first_name, last_name=""):
    """
        prints the name

        Args:
            first_name: first name passed to the function
            last_name: lastname passed to the function
                    if none is passed it sets the name as None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
