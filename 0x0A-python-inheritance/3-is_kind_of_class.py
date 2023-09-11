#!/usr/bin/python3
"""  Defines a class and an inherited class check function"""


def is_kind_of_class(obj, a_class):
    """ Checks if an object is instance or inherited instance of class

    Args:
         obj(any): object to be checked
         a_class(type): The class to match the obj type
    Returns:
         If obj is instance or inherited instance of a_class - True
         Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
