#!/usr/bin/python3
"""10-student.py"""


class Student:
    """
    Creates a Student
    """

    def __init__(self, first_name, last_name, age):
        '''Instantiation with first_name, last_name and age'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student'''

        if isinstance(attrs, list) and
        all(isinstance(k, str) for k in attrs):
            res = {}
            for i in attrs:
                if hasattr(self, i):
                    res[i] = getattr(self, i)
            return res

        return self.__dict__
