#!/usr/bin/python3
""" DEfines object creating function from JSON"""
import json


def load_from_json_file(filename):
    """ Creates object file from json"""
    with open(filename) as f:
        return json.load(f)
