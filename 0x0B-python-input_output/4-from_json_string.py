#!/usr/bin/python3
""" Defines JSON to object function"""
import json


def from_json_string(my_str):
    """ returns object represented by json"""
    return json.loads(my_str)
