#!/usr/bin/python3
""" tests 6-max_interger"""

import importlib
import unittest
toTest = importlib.import_module('6-max_integer')


class Testmaxint(unittest.TestCase):

    def test_maxAtEnd(self):
        self.assertEqual(toTest.max_integer([5, 3, 1, 0, 7]), 7)

    def test_maxAtStart(self):
        self.assertEqual(toTest.max_integer([5, 3, 1, 0, 4]), 5)

    def test_maxInMiddle(self):
        self.assertEqual(toTest.max_integer([5, 3, 10, 0, 4]), 10)

    def test_1negative(self):
        self.assertEqual(toTest.max_integer([5, 3, 1, 0, -4]), 5)

    def test_allnegative(self):
        self.assertEqual(toTest.max_integer([-5, -3, -1, -4]), -1)

    def test_1elem(self):
        self.assertEqual(toTest.max_integer([2]), 2)


    def test_emptyu(self):
        self.assertEqual(toTest.max_integer([]), None)



if __name__ == '__main__':
    unittest.main()
