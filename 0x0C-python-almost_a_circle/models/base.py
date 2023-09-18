#!/usr/bin/python3
"""define a class Base """
import json
import csv
import turtle


class Base:
    """ """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
             self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
