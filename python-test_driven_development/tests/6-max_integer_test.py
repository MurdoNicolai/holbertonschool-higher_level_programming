#!/usr/bin/python3
""" tests 6-max_interger"""

import importlib
import unittest
toTest = importlib.import_module('6-max_integer')


class Testmaxint(unittest.TestCase):

    def test_Normalcase(self):
        self.assertEqual(toTest.max_integer([5, 3, 1, 0, -4]), 5)
        self.assertEqual(toTest.max_integer([]), None)
        with self.assertRaises(TypeError):
            toTest.max_integer("word")
        with self.assertRaises(TypeError):
            toTest.max_integer(["ball", "word"])


if __name__ == '__main__':
    unittest.main()
