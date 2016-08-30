"""wargame.test.test_hut

This module contains unit test for wargame.hut.Hut class.

This module is compatible with Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
import unittest
import sys

# Add the top level directory wargame to sys,path
sys.path.append("../")

from knight import Knight
from hut import Hut


class TestHut(unittest.TestCase):
    """Contains unit tests for the game Attack of The Orcs.

    .. seealso::
       :py:meth: `wargame.hut.Hut.acquire`
    """
    def setUp(self):
        """Overrides the setUp fixture of the superclass.

        This method is called just before the calling each  unit test.
        Here, it creates instances of Knight for use by various unit tests.

        .. seealso:: :py:meth:`TestCase.tearDown`
        """
        self.knight = Knight()

    def test_acquire_hut(self):
        """Unittest to verify hut occupant after it is acquired

        Unit test to ensure that when hut is 'acquired', the
        `hut.occupant` is updated to the `Knight` instance.
        """
        print("\nCalling test_hut.test_acquire_hut..")
        hut = Hut(4, None)
        hut.acquire(self.knight)
        self.assertIs(hut.occupant, self.knight)


if __name__ == '__main__':
    unittest.main()
