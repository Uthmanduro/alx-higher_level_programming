#!/usr/bin/python3
def is_same_class(obj, a_class):
    """returns true if object is an instance of  the specifed class
        else false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
