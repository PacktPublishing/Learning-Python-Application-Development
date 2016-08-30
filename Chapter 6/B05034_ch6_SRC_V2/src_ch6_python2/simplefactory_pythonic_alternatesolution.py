"""simplefactory_pythonic_alternatesolution

Example to show an alternativve Pythonic way of implementing a simple factory

The example shows how to use Python's language feature, (classes are first-class
 objects) to implement a simple factory. However, in this approach we create
 an instance of the factory (unlike in simplefactory_pythonic.py).

 As you would notice, in this approach, UnitFactory.create_unit is NOT
 a "class method" but is just a regular "instance method"

This example is created to illustrate a design pattern discussed in the book
Learning Python Application Development (Packt Publishing). See the book for
further details.

This module is compatible with Python version 2.7.9 as well as version 3.5.
It contains supporting code for the book, Learning Python Application Development,
Packt Publishing.

RUNNING THE PROGRAM:
Assuming you have python in your environment variable PATH, type the following
in the command prompt to run the program:

                    python name_of_the_file.py

(Replace name_of_the_file.py with the name of this file)

.. seealso: The file simplefactory_pythonic.py that illustrates the approach
            discussed in the book.
            For a somewhat 'traditional' approach, see the file
               simplefactory_traditional.py.

.. todo:: You will find several classes put inside this module. This is done
          just for the ease of illustration. As an exercise, you can put each
          class in its own module. If you are using a Python IDE, you could also
           use refactoring feature of the IDE (if available) for this work.
.. note:: The classes such as ElfRider, Knight etc are created
          just to show how to implement a simple factory.  It is just a trivial
          example and these are just dummy classes to represent concrete
          factory products. (things that the factory creates).

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function

# Some dummy classes to represent factory products (not documented)
class ElfRider:
    pass
class Knight:
    pass
class OrcRider:
    pass
class DwarfFighter:
    pass
class OrcRider:
    pass
class Fairy:
    pass
class Wizard:
    pass
class ElfLord:
    pass
class OrcFighter:
    pass


class UnitFactory:
    """A factory class to create game units.

    This is an example that shows how we can use Python classes (which are
    first-class objects) to create 'concrete products' of the factory.

    :cvar units_dict: Python dictionary created as a class variable. This
            dictionary holds names (types) of the game units as its keys and
            the corresponding values are the concrete classes representing the
            game character.
    .. seealso:: `Kingdom` class and various classes like `ElfRider`, `Knight`
    """
    units_dict = {
        'elfrider': ElfRider,
        'knight': Knight,
        'dwarffighter': DwarfFighter,
        'orcrider': OrcRider,
        'fairy': Fairy,
        'wizard': Wizard,
        'elflord': ElfLord,
        'orcfighter': OrcFighter
    }

    def create_unit(self, unit_type):
        key = unit_type.lower()
        return self.__class__.units_dict.get(key)()


class Kingdom:
    """Class that uses a 'factory' to get an instance of a game character.

    :ivar UnitFactory factory: This is an instance of UnitFactory

    .. seealso:: class `UnitFactory`
    """
    def __init__(self, factory):
        self.factory = factory

    def recruit(self, unit_type):
        """Recruit a new game unit, creating it first using a factory.

        This method recruits a new unit for the 'kingdom'. First it 'orders' a
        unit from the factory instance. Then pays the
        price and updates some record. The pay_gold and update_record methods
        are dummy, they just print some information.

        :arg string unit_type:  The type (name) of unit requested.
        :return: A game unit instance returned by the factory.
        """
        unit = self.factory.create_unit(unit_type)
        self.pay_gold(unit)
        self.update_records(unit)
        return unit

    def pay_gold(self, something):
        """Pay gold for the recruited unit (dummy method)."""
        print("GOLD PAID")

    def update_records(self, something):
        """Update some record to reflect new recruit(dummy method)."""
        print("Some logic (not shown) to update database of units")

if __name__ == "__main__":
    print("Simple factory example")
    print("-"*25)
    factory = UnitFactory()
    k = Kingdom(factory)
    elf_unit = k.recruit("ElfRider")
    print("Created an instance of :", elf_unit.__class__.__name__)
