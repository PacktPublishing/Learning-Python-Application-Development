"""wargame.knight

This module contains the Knight class implementation.

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
from abstractgameunit import AbstractGameUnit
from gameutils import print_bold


class Knight(AbstractGameUnit):
    """Class that represents the game character 'Knight'

    The player instance in the game is a Knight instance. Other Knight
    instances are considered as 'friends' of the player and is
    indicated by the attribute `self.unit_type` .

    :arg str name: Name of this game character (optional)

    :ivar int max_hp: Maximum number of hit points (health points)
    :ivar int health_meter: The actual number of hit points
                      or health points
    :ivar str unit_type: Stores id this character(unit) a friend
                    or an enemy
    :ivar AbstractGameUnit enemy: Stores who is the enemy (not implemented)
    """
    def __init__(self, name='Sir Foo'):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'

    def info(self):
        """Print basic information about this character.

        Overrides AbstractGameUnit.info
        """
        print("I am a Knight!")

    def acquire_hut(self, hut):
        """'Fight' the combat (command line) to acquire the hut

        :arg Hut hut: The hut that needs to be acquired.

        .. todo:: Refactor this method as an exercise
                  Example: Can you use self.enemy instead of calling
                  hut.occupant every time?
        """
        print_bold("Entering hut %d..." % hut.number, end=' ')
        is_enemy = (isinstance(hut.occupant, AbstractGameUnit) and
                    hut.occupant.unit_type == 'enemy')
        continue_attack = 'y'

        # Code block that tells what to do when you see, an enemy or a friend
        # or no one in the hut.
        # TODO: Refactor this.
        if is_enemy:
            print_bold("Enemy sighted!")
            self.show_health(bold=True, end=' ')
            hut.occupant.show_health(bold=True, end=' ')

            # Attack the enemy until the player says so.
            # TODO: The user must select either 'y' or 'n'. In
            # the current implementation there is a bug where you
            # do not need to enter 'y'... fix this as an exercise!
            while continue_attack:
                continue_attack = input("\n...continue attack? (y/n): ")
                if continue_attack == 'n':
                    self.run_away()
                    break

                # Player wants to attack, call the attack method.
                self.attack(hut.occupant)

                # This turn (iteration) of the combat is over, Check
                # if Player has won
                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self)
                    break

                # Player's health_meter is empty..
                # This indicates Player has lost the combat
                if self.health_meter <= 0:
                    print("")
                    break
        else:
            if hut.get_occupant_type() == 'unoccupied':
                print_bold("Hut is unoccupied")
            else:
                print_bold("Friend sighted!")
            hut.acquire(self)
            self.heal()

    def run_away(self):
        """Abandon the combat and run away from the hut

        If the player is losing the combat, there is an option
        to leave the hut. A strategy to rejuvenate and restart the combat
        for a better chance of winning.

        ..seealso :: :py:meth:`self.acquire_hut`
        """
        print_bold("RUNNING AWAY...")
        self.enemy = None



