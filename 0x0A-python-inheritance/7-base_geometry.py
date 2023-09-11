#!/usr/bin/python3
'''7-base_geometry.py'''
"""
This module contains a class
with public instance and Raises
exception when required
"""


class BaseGeometry:
    '''
    class BaseGeometry
    class Base has 2 public instances
    '''

    def __init__(self):
        pass

    def area(self):
        '''
        function to raise an exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        check value input is correct type/validate value
        '''
        '''
        if not isinstance(value, int):
        '''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
