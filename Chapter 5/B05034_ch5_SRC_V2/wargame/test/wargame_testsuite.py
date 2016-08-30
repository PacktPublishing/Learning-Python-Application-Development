"""wargame.test.testsuitedemo

This module contains class WarGameTestSuite

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
import unittest
from test_wargame import TestWarGame
from test_hut import TestHut


class WarGameTestSuite(unittest.TestSuite):
    """TestSuit example"""
    pass

if __name__ == '__main__':
    #suite = unittest.TestSuite()
    suite = WarGameTestSuite()
    suite.addTest(unittest.makeSuite(TestWarGame()))

    runner = unittest.TextTestRunner()

    runner.run(suite)

