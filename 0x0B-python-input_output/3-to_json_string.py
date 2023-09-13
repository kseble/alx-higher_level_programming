#!/usr/bin/python3
""" represents string to JSON function"""
import json


def to_json_string(my_obj):
    """ return the JSON representation of an object"""
    return json.dumps(my_obj)
