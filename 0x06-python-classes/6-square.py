#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the attribute : size"""
        self.size = size
        self.position = position

    """Size getter"""
    @property
    def size(self):
        return (self.__size)

    """Size setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Position getter"""
    @property
    def position(self):
        return (self.__position)

    """Position setter"""
    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
        type(value[0]) != int or type(value[1]) != int
        or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position= value

        """Create public instance method: area"""
        def area(self):
            sq_area = self.__size ** 2
            return (sq_area)

        """Create public instance method: my_print
        Line is not filles with spaces when position[1] > 0
        """
        def my_print(self):
            if self.__size > 0:
                for x in range(self.position[1]):
                    print("")
                for x in range(self.__size):
                    for y in range(self.__position[0]):
                        print(" ", end="")
                    for y in range(self.__size):
                        print("#", end="")
                    print("")
                print("")
