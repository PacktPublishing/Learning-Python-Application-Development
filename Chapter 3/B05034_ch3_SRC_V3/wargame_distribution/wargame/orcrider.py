"""wargame.orcrider

This module contains the OrcRider class implementation.

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
from abstractgameunit import AbstractGameUnit


class OrcRider(AbstractGameUnit):
    """Class that represents the game character

    .. seealso:: The class `Knight` and the superclass `AbstractGameUnit`
    """
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        """Print basic information about this character."""
        print("Grrrr..I am an Orc Rider. Don't mess with me.")



