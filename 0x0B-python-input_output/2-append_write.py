#!/usr/bin/python3
"""Python Function to append string to a file"""


def append_write(filename="", text=""):
    """ Append content to a file, it doesn´t exist then is created """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
