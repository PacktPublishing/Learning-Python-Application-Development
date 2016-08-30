"""wargame.gameutils

This module contains some utility function for the game Attack of the Orcs

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
import random


def weighted_random_selection(obj1, obj2):
    """Randomly return one of the following, obj1 or obj2


    :arg obj1: An instance of class AbstractGameUnit. It can
                be any object. The calling code should ensure the correct
                object is passed to this function.
    :arg obj2: Another instance of class AbstractGameUnit.
                See the comment for o

    :return: obj1 or obj2

    .. seealso: :py:func:`weighted_random_selection_alternate` which is an
                         alternative implementation that is used to demonstrate
                         importance of unit testing.
    """
    weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1

    return obj2


def print_bold(msg, end='\n'):
    """Convenience function to print a message in bold style

    Optionally you can also specify how the bold text should end. By default
    it ends with a new line character.

    :arg msg: Message to be converted to bold style
    :arg end: Tell how the printed string should end (newline, space etc)
    """
    print("\033[1m" + msg + "\033[0m", end=end)

