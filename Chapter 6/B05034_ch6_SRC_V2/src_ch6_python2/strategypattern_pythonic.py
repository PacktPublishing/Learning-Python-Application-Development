"""strategypattern_pythonic

Example to show a Pythonic way of implementing strategy design pattern.

The example shows how to use Python's first class functions to implement
strategy pattern.

This example is created to illustrate a design pattern discussed in the book
Learning Python Application Development (Packt Publishing). See the book for
further details.

This module is compatible with Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

RUNNING THE PROGRAM:
Assuming you have python in your environment variable PATH, type the following
in the command prompt to run the program:

                    python name_of_the_file.py

(Replace name_of_the_file.py with the name of this file)

.. seealso: For a somewhat 'traditional' approach, see the file
            strategypattern_traditional.py.
.. note:: The AbstractGameUnit is created as an abstract base class just to
          bring 'some order' in subclasses. For example it enforces the
          subclasses to implement info method. If you don't want to enforce such
          rule, you can optionally make this class a simple base class
          (not the abstract class)
.. todo:: You will find several classes put inside this module. This is done
          just for the ease of illustration. As an exercise, you can put each
          class in its own module. If you are using a Python IDE, you could also
           use refactoring feature of the IDE (if available) for this work.
:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import sys
from abc import ABCMeta, abstractmethod

# Make sure we are 'not' using Python 3. (should really be Python 2.7.9)
if sys.version_info >= (3, 0):
    print("This code requires Python 2.7.9 ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0], sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)

# Callable class moved to collections.callable starting from version 3.3
if sys.version_info < (3, 3):
    from collections import Callable
else:
    from collections.abc import Callable


class AbstractGameUnit:
    """Base class for all the game characters.

    :arg string name: Name of the game character.
    :arg jump_strategy: A callable (function) that represents an algorithm
                     to jump.
    :ivar jump: The jump_strategy function is assigned to this variable.

    .. note: This is created as an abstract class and requires subclasses to
    override the 'info' method. However, you can change this to a simple class
    (not abstract) if you don't want to enforce any interface on the subclasses.
    .. seealso: DwarfFighter (a subclass)
    """
    __metaclass__ = ABCMeta

    def __init__(self, name, jump_strategy):
        assert(isinstance(jump_strategy,  Callable))
        self.name = name
        self.jump = jump_strategy

    @abstractmethod
    def info(self):
        """"Print information about this game unit."""
        pass


class DwarfFighter(AbstractGameUnit):
    """Create a DwarfFighter instance"""
    def info(self):
        """Print info about thus unit, overrides superclass method."""
        print("I am a great dwarf of the eastern foo mountain!")


def can_not_jump():
    """A demo function representing a jump algorithm

    .. note:: No actual algorithm is implemented, It prints some information.
    """
    print("--> CanNotJump.jump: I can not jump")


def power_jump():
    """A demo function representing a jump algorithm

    .. note:: No actual algorithm is implemented, It prints some information.
    """
    print("--> PowerJump.jump: I can jump 100 feet from the ground!")


def horse_jump():
    """A demo function representing a jump algorithm

    .. note:: No actual algorithm is implemented, It prints some information.
    """
    print("--> HorseJump.jump: Jumping my horse.")

if __name__ == '__main__':
    # Pass the jump strategy (function) while instantiating the class.
    dwarf = DwarfFighter("Dwarf", can_not_jump)
    print("\n{STRATEGY-I} Dwarf trying to jump:")
    dwarf.jump()
    print("-"*56)

    # Optionally change the jump strategy later
    print("\n{STRATEGY-II} Dwarf given a 'magic potion' to jump:")
    dwarf.jump = power_jump
    dwarf.jump()
    print("-"*56)
