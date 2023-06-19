#!/usr/bin/python3
""" Unit tests for base module """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """ test class for Square class """

    def setUp(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        """ 10 check if square is instance of Base and Rect """
        s = Square(1)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_number_arguments(self):
        """ 10 check if number of arg is right """
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5)

    def test_correct_arguments(self):
        """ test correct arguments """
        with self.assertRaises(TypeError):
            s = Square(1, x=3, y=4, i=5)
        with self.assertRaises(TypeError):
            s = Square(1, x=3, e=4, id=5)
        with self.assertRaises(TypeError):
            s = Square(1, g=3, y=4, id=5)

    def test_continues_id1(self):
        """ 10 check if the id is continuous """
        s1 = Square(2, 3, 4)
        s2 = Square(2, 3, 4)
        s3 = Square(2, 3, 4, id=100)
        s4 = Square(2, 3, 4)
        s5 = Square(2, 3, 4, 101)
        s6 = Square(2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 100)
        self.assertEqual(s4.id, 3)
        self.assertEqual(s5.id, 101)
        self.assertEqual(s6.id, 4)

    def test_printing(self):
        """ 10 check overloading of __str__ """
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")
        s2 = Square(5, 5, 1)
        self.assertEqual(s2.__str__(), "[Square] (1) 5/1 - 5")
        s3 = Square(1, 2)
        self.assertEqual(s3.__str__(), "[Square] (2) 2/0 - 1")
        output = io.StringIO()
        sys.stdout = output
        s1 = Square(4, 2, 1, 12)
        print(s1)
        self.assertEqual(output.getvalue(), "[Square] (12) 2/1 - 4\n")
        sys.stdout = sys.__stdout__

    def test_getter_method_size(self):
        """ check getter width """
        s = Square(20)
        self.assertEqual(s.size, 20)

    def test_setter_method_size(self):
        """ check setter method """
        s = Square(1)
        s.size = 3
        self.assertEqual(s.size, 3)
