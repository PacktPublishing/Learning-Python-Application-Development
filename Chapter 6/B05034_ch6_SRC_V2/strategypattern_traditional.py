"""strategypattern_traditional

Example to show one way of implementing strategy design pattern in Python.

The example shown here resembles a 'traditional' implementation of strategy
pattern in Python (traditional = the one you may implement in languages like
C++). For a more Pythonic approach, see the file strategypattern_pythonic.py.

This example is created to illustrate a design pattern discussed in the book
Learning Python Application Development (Packt Publishing). See the book for
further details.

This module is compatible with Python 3.5. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

RUNNING THE PROGRAM:
Assuming you have python in your environment variable PATH, type the following
in the command prompt to run the program:

                    python name_of_the_file.py

(Replace name_of_the_file.py with the name of this file)

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

if sys.version_info < (3, 0):
    print("This code requires Python 3.x, It is tested only with 3.5 ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0], sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)


class AbstractGameUnit(metaclass=ABCMeta):
    """Base class for all the game characters.

    :arg string name: Name of the game character.
    :arg JumpStrategy jump_object: Could be an instance of JumpStrategy or
                                 its subclasses.(or None if unspecified)
    :ivar jump_strategy: Choose the algorithm for jumping.
    """
    def __init__(self, name, jump_object=None):
        self.jump_strategy = None
        self.name = name
        self.set_jump_strategy(jump_object)

    def set_jump_strategy(self, jump_object=None):
        """Set up the object that defines the jump strategy.

        Choose an algorithm that defines the jump behavior. The algorithm is
        represented by a 'strategy object'.

        :arg JumpStrategy jump_object: Instance of the class that should handle
                    how this game unit 'jumps' . Could be instance of
                    JumpStrategy or its subclasses (or None if unspecified)
        """
        if isinstance(jump_object, JumpStrategy):
            self.jump_strategy = jump_object
        else:
            self.jump_strategy = JumpStrategy()

        # print("\tset_jump_strategy: self.jump_strategy:",
        #       type(self.jump_strategy).__name__)

    def jump(self):
        """Perform jump operation (delegated)"""
        try:
            self.jump_strategy.jump()
        except AttributeError as e:
            print("Error: AbstractGameUnit.jump: self.jump_strategy: {} "
                  "\nError details: {} ".format(self.jump_strategy, e.args))

    @abstractmethod
    def info(self):
        """"Print information about this game unit."""
        pass


class DwarfFighter(AbstractGameUnit):
    """Create a DwarfFighter instance"""
    def info(self):
        """Print info about thus unit, overrides superclass method."""
        print("I am a great dwarf of the eastern foo mountain!")


class JumpStrategy:
    """Base Class representing a jump strategy (an algorithm)."""
    def jump(self):
        """The actual jump algorithm.

         .. seealso: AbstractGameUnit.jump() where this is called
                  (if this jump strategy is chosen)
        """
        print("--> JumpStrategy.jump: Default jump")


class CanNotJump(JumpStrategy):
    """Class whose instance represents a jump algorithm."""
    def jump(self):
        """The actual jump algorithm.

         .. seealso: AbstractGameUnit.jump() where this is called
                  (if this jump strategy is chosen)
        """
        print("--> CanNotJump.jump: I can not jump")


class HorseJump(JumpStrategy):
    """Class whose instance represents a jump algorithm."""
    def jump(self):
        """The actual jump algorithm.

         .. seealso: AbstractGameUnit.jump() where this is called
                  (if this jump strategy is chosen)
        """
        print("--> HorseJump.jump: Jumping my horse.")


class PowerJump(JumpStrategy):
    """Class whose instance represents a jump algorithm."""
    def jump(self):
        """The actual jump algorithm.

         .. seealso: AbstractGameUnit.jump() where this is called
                  (if this jump strategy is chosen)
        """
        print("--> PowerJump.jump: I can jump 100 feet from the ground!")


if __name__ == '__main__':
    # Create a jump strategy instance (algorithm representing a jump behavior)
    jump_strategy = CanNotJump()
    # Pass it to the DwarfFighter.
    dwarf = DwarfFighter("Dwarf", jump_strategy)
    print("\n{STRATEGY-I} Dwarf trying to jump:")
    # The dwarf instance will use the jump strategy represented by CanNotJump()
    dwarf.jump()
    print("-"*56)

    # Optionally change the jump strategy later
    print("\n{STRATEGY-II} Dwarf given a 'magic potion' to jump:")
    dwarf.set_jump_strategy(PowerJump())
    dwarf.jump()
    print("-"*56)
