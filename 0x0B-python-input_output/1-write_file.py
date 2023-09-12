#!/usr/bin/python3
'''Python Function to count number of lines in a file'''


def number_of_lines(filename=""):
    """ Function that reads from a file and prints its number of lines

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
    return count
