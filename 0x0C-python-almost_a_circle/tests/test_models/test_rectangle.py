#!/usr/bin/python3
""" Unit tests for base module """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    """ class test for testing rectangle class """

    def setUp(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        """ check if rectangle is instance of Base and Rect """
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)

    def test_number_arguments(self):
        """ check if number of arg is right """
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_correct_arguments(self):
        """ test correct arguments """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, x=3, y=4, i=5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, x=3, e=4, id=5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, g=3, y=4, id=5)

    def test_continues_id1(self):
        """ check if the id is continuous """
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(1, 2, 3, 4, id=100)
        r4 = Rectangle(1, 2, 3, 4)
        r5 = Rectangle(1, 2, 3, 4, 101)
        r6 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 100)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r5.id, 101)
        self.assertEqual(r6.id, 4)


    def test_private_width(self):
        """ check if private var width is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__width

    def test_private_height(self):
        """ check if private var height is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__height

    def test_private_x(self):
        """ check if private var x is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__x

    def test_private_y(self):
        """ check if private var y is private """
        r = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            r.__y

    def test_getter_method_x(self):
        """ check getter x """
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)
        r = Rectangle(1, 2, x=4)
        self.assertEqual(r.x, 4)

    def test_getter_method_y(self):
        """ check getter y """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)
        r = Rectangle(1, 2, 3, y=5)
        self.assertEqual(r.y, 5)

    def test_setter_method_width(self):
        """ check setter method width """
        r = Rectangle(1, 2)
        r.width = 3
        self.assertEqual(r.width, 3)

    def test_setter_method_height(self):
        """ check setter method height """
        r = Rectangle(1, 2)
        r.height = 3
        self.assertEqual(r.height, 3)

    def test_setter_method_x(self):
        """ check setter method x"""
        r = Rectangle(1, 2)
        r.x = 3
        self.assertEqual(r.x, 3)
        r = Rectangle(1, 2, x=3)
        r.x = 4
        self.assertEqual(r.x, 4)

    def test_setter_method_y(self):
        """ check setter method y"""
        r = Rectangle(1, 2)
        r.y = 3
        self.assertEqual(r.y, 3)
        r = Rectangle(1, 2, y=3)
        r.y = 4
        self.assertEqual(r.y, 4)
