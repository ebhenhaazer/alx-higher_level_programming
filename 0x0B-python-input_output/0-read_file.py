#!/usr/bin/python3
'''Python Function that reads a file and prints to stdout'''

def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """
    with open(filename, 'r', encoding ='utf-8') as f:
        for line in f:
            print(line, end="")
