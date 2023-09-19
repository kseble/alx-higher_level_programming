#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """ represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize a new rectangle

        Args:
            width(int): the width of the new rectangle
            height(int): the height of the new rectangle
            x (int): the coordinate of the new rectangle
            y (int): the coordinates of the new rectangle
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either width or height <= 0.
            TypeError: If either x or y is not an int.
            ValueError: If either x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
