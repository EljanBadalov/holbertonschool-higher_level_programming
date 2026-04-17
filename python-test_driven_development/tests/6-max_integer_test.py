#!/usr/bin/python3
"""Unittest for max_integer function"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, -2, 3]), 3)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
