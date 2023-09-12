#!/usr/bin/python3
""" Module that contains a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ Returns an object python
        it could also be said that it converts from JSON to python
    """
    return json.loads(my_str)
