#!/usr/bin/python3
""" Unit tests for base module """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ tests cases for base clase """

    def reset(self):
        """ reset nb_objects var to zero before each test """
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        """ Test if isinstance """
        b1 = Base()
        self.assertIsInstance(b1, Base)
        b2 = Base(100)
        self.assertIsInstance(b2, Base)

    def test_continues_id1(self):
        """ check if the id is continuous """
        b1 = Base()
        b2 = Base()
        b3 = Base(100)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 100)
        self.assertEqual(b4.id, 3)


    def test_number_arguments(self):
        """ check if it has right amount of args """
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_private_class_var(self):
        """ check if private var nb_object is private """
        with self.assertRaises(AttributeError):
            Base.__nb_objects
