"""wargame.test.testsuitedemo

This module contains code to demonstrate unittest.TestSuite

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
import unittest


class MyUnitTestA(unittest.TestCase):
    """A class to help illustrate how to use unitTest.TestSuite"""
    def test_a2(self):
        print("MyUnitTestA.test_a2")
        self.assertNotEqual(1 + 1, 3)

    def test_a1(self):
        print("MyUnitTestA.test_a1")
        self.assertTrue(1 + 1 == 2)

    def not_called_by_default(self):
        print("MyUnitTestA: This method will not be called by default")


class MyUnitTestB(unittest.TestCase):
    """A class to help illustrate how to use unitTest.TestSuite"""
    def test_b2(self):
        print("MyUnitTestB.test_b2")
        self.assertNotEqual( 4*4 , 15)

    def test_b1(self):
        print("MyUnitTestB.test_b1")
        self.assertTrue(4 + 4 == 8)

    def not_called_by_default(self):
        print("MyUnitTestB: This method will not be called by default")


def suite():
    """Return a composite testsuite that aggregates two testsuits.

     These sub-testsuites, in turn, aggragate all the tests in classes
     `MyUnitTestA` and `MyUnitTestB`.
     :return: Instance of `unittest.Testsuite`
    """
    print("Inside suite()...")

    # Create a test suite by collecting all test cases defined
    # in MyUnitTestA. By default it only looks for methods starting
    # with test*
    suite_a = unittest.makeSuite(MyUnitTestA)

    # Similarly, create suite_b  using testcases from MyUnitTestB
    suite_b = unittest.makeSuite(MyUnitTestB)

    # Add a new testcase to suite_b.
    suite_b.addTest(MyUnitTestB("not_called_by_default"))

    # Return a composite test suite containing suite_a and suite_b
    return unittest.TestSuite((suite_a, suite_b))


if __name__ == '__main__':
    # Run the tests.
    unittest.main(defaultTest='suite')
