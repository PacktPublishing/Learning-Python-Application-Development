"""wargame.test.mocktest

This module contains code to demonstrate use of mock.patch functionality

This module is compatible with Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
import unittest
from unittest.mock import patch


class ClassA:
    """Class to illustrate use of path objects"""

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data


class TestClassA(unittest.TestCase):
    """Unittest class for testing ClassA

    This is a trivial example.
    """
    a = ClassA(100.)

    def test_get_data(self):
        """unit test for ClassA.get_data"""
        with patch.object(a, 'data', new= 200.):
            self.assertEqual(200., a.get_data())

if __name__ == '__main__':
    unittest.main()
