"""adapterpattern

Example to show a Pythonic way of implementing an adapter pattern.

The example shows how to use Python's language feature, first-class
functions, to implement adapter pattern.

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

.. seealso:: `adapterpattern_multiple_methods.py`

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""


class ElfRider:
    """Class which confirms to our existing interface that client expects.

    The ElfRider represents a game character. It already has defined the methods
    that the client code expects. In this trivial example, it has the 'jump'

    .. seealso:: `WoodElf` , `ForeignUnitAdapter`
    """
    def jump(self):
        """Tell how the unit jumps (dummy method)"""
        print("Inside ElfRider.jump")


class WoodElf:
    """ An imaginary third-party class that has an incompatible interface.

    WoodElf represents a game character class that is provided by an imaginary
    'third party' developer. It does not have the 'jump' method that the client
    code expects (incompatible interface). This is used to illustrate how to
    implement adapter pattern.

    .. seealso:: `ElfRider` , `MountaiElf`, `ForeignUnitAdapter`
    """
    def leap(self):
        """leap method is equivalent to the 'jump' method client expects

        The adapter should have a jump method which in turn calls this method.
        """
        print("Inside WoodElf.leap")

    def climb(self):
        """Some other (dummy) method of the class.

        Adapter shouldn't do anything with this method. It should just delegate
        the call from the client to this method.
        """
        print("Inside WoodElf.climb")


class MountainElf:
    """Example class with an incompatible interface than what we expect

    Similar to WoodElf, this is yet another class which has a "spring" method
    which is equivalent to `jump` method of the client interface.
    """
    def spring(self):
        """spring method is equivalent to the 'jump' method client expects"""
        print("Inside MountainElf.spring")


class ForeignUnitAdapter:
    """Generalized adapter class for 'fixing' incompatible interfaces.

    :arg adaptee: An instance of the 'adaptee' class. For example, WoodElf
              is an adaptee as it has a method 'leap' when we expect 'jump'
    :arg adaptee_method: The method you want the adapter for. Example,
           when client calls 'jump' method on the adapter instance, it is
           delegated to 'leap' method of the adaptee.

    :ivar foreign_unit: The instance of the adaptee class
    :ivar jump: Instance variable jump is assigned as the adaptee_method
       (e.g. 'leap').

    .. todo:: This class is customized for jump method.To use it for multiple
        methods, take advantage of Python first-class functions. One example is
        shown in the book mentioned in the module docstrings.
    """
    def __init__(self, adaptee, adaptee_method):
        self.foreign_unit = adaptee
        self.jump = adaptee_method

    def __getattr__(self, item):
        """Handle all the undefined attributes the client code expects.

        :param item: name of the attribute.
        :return: Returns the corresponding attribute of the adaptee instance
        (self.foreign_unit)
        .. todo:: Add exception handling code.
        """
        return getattr(self.foreign_unit, item)

if __name__ == '__main__':
    elf = ElfRider()
    elf.jump()

    wood_elf = WoodElf()
    wood_elf_adapter = ForeignUnitAdapter(wood_elf, wood_elf.leap)
    # Internally the following calls wood_elf.leap()
    wood_elf_adapter.jump()

    # Internally the following calls__get_attr__
    # which in turn calls wood_elf.climb()
    wood_elf_adapter.climb()

    mountain_elf = MountainElf()
    mountain_elf_adapter = ForeignUnitAdapter(mountain_elf, mountain_elf.spring)
    mountain_elf_adapter.jump()



