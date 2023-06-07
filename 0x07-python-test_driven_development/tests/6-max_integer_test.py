#!/usr/bin/python3
"""
    unittest
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class for unittests """
    def test_max_integer(self):
        """ check possible cases edge cases """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-2]), -2)
        self.assertEqual(max_integer([-1, -4, -2]), -1)
        self.assertEqual(max_integer([18, 11, 4]), 18)
        self.assertEqual(max_integer([24, 9, 13, -3, -13, -4]), 24)
        self.assertEqual(max_integer([18, 18, 18]), 18)

    def test_type_error(self):
        """ type_errors """
        self.assertRaises(TypeError, max_integer, ["j", 1])
        self.assertRaises(TypeError, max_integer, [5, [3, 0]])
