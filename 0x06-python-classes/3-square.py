#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initialize the private instance attribute: size
        Raise the TypeError or ValueError according to given condition"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        """Create public instance method: def area(self)"""
        def area(self):
            sq_area = self.__size ** 2
            return (sq_area)
