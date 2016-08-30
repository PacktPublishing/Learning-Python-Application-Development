"""wargame.test.testcasedemo

This module contains code to demonstrate use of unittest.TestCase

This module is compatible with Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
import unittest


class MyUnitTests(unittest.TestCase):
    """Illustration for unittest.TestCase"""

    def setUp(self):
        """setUp fixture of unittest.TestCase"""
        print("In setUp..")

    def tearDown(self):
        """tearDown method of unittest.TestCase"""
        print("Tearing Down the test.")
        print("~" * 10)

    @unittest.expectedFailure
    def test_2(self):
        """Illustrate how to use unittest.expectedFailure"""
        print("in test_2")
        self.assertEqual(1 + 1, 3)

    @unittest.skip("Skipping test_1")
    def test_1(self):
        """Illustrate how to skip a test"""
        print("in test_1")
        self.assertTrue(1 + 1 == 2)

    def will_not_be_called(self):
        """Method not considered as a unit test by default"""
        print("this method will not be called automatically")

if __name__ == '__main__':
    unittest.main()
