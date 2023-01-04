#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """creates a test class"""
    def test_max(self):
        """
            test for the correct outpt
        """
        self.assertEqual(max_integer([2, 3, 5, 7, 34, 4]), 34)
        self.assertEqual(max_integer([26, 3, 72, 76, 54, 54]), 76)
        self.assertIsNone(max_integer([]), None)
        self.assertEqual(max_integer([-26, -3, -72, -76, -54, -54]), -3)
        self.assertEqual(max_integer([0, -3, -2, -6, -4]), 0)
        self.assertEqual(max_integer([76]), 76)


if __name__ == "__main__":
    unittest.main()
