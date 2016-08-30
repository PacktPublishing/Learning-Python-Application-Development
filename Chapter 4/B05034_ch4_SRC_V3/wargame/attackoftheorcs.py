"""wargame.attackoftheorcs

This module contains the AttackOfTheOrcs class implementation.

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    print("This code requires Python 3.x and is tested with version 3.5.x ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)


import random
from hut import Hut
from knight import Knight
from orcrider import OrcRider
from gameutils import print_bold


class AttackOfTheOrcs:
    """Main class with the high level logic to play Attack of The Orcs game

     :ivar huts: List object to hold instances of `Hut` class.
     :ivar player: Represents the player playing this game. This is an
                instance of class `Knight` in current implementation.

    .. seealso:: :py:meth:`self.play` where the main action happens.

    """
    def __init__(self):
        self.huts = []
        self.player = None

    def get_occupants(self):
        """Return a list of occupant types for all huts.

        This is mainly used for printing information on current status of the hut
        (whether unoccupied or acquired etc)

        If the occupant is not `None` the occupant type will be 'enemy' or
        'friend'. But if there is no occupant or is already 'acquired' the
        occupant_type will display that information instead. See
        `Hut.get_occupant_type()` for more details.

        Return a list that collects this information from all the huts.
        This is a list comprehension example. More on the list comprehension
        in a chapter on Performance.

        :return: A list containing occupant types (strings)

        .. seealso:: :py:meth:`Hut.get_occupant_type`
        """
        return [x.get_occupant_type() for x in self.huts]

    def show_game_mission(self):
        """Print the game mission in the console"""
        print_bold("Mission:")
        print("  1. Fight with the enemy.")
        print("  2. Bring all the huts in the village under your control")
        print("---------------------------------------------------------\n")

    def _process_user_choice(self):
        """Process the user input for choice of hut to enter

        Returns the hut number to enter based on the user input. This method
        makes sure that the hut number user has entered is valid. If not, it
        prompts the user to re-enter this information.

        :return: hut index to enter.
        """
        verifying_choice = True
        idx = 0
        print("Current occupants: %s" % self.get_occupants())
        while verifying_choice:
            user_choice = input("Choose a hut number to enter (1-5): ")
            # --------------------------------------------------------------
            # try...except illustration for chapter on exception handling.
            # (Attack Of The Orcs v1.1.0)
            # --------------------------------------------------------------
            try:
                idx = int(user_choice)
            except ValueError as e:
                print("Invalid input, args: %s \n" % e.args)
                continue

            try:
                if self.huts[idx-1].is_acquired:
                    print("You have already acquired this hut. Try again."
                     "<INFO: You can NOT get healed in already acquired hut.>")
                else:
                    verifying_choice = False
            except IndexError:
                print("Invalid input : ", idx)
                print("Number should be in the range 1-5. Try again")
                continue

        return idx

    def _occupy_huts(self):
        """Randomly occupy the huts with one of, friend, enemy or 'None'

        .. todo::
           Here we assume there are exactly 5 huts. As an exercise, make it a
           user input. Note that after such change, the unit test is expected to
           fail!
        """
        for i in range(5):
            choice_lst = ['enemy', 'friend', None]
            computer_choice = random.choice(choice_lst)
            if computer_choice == 'enemy':
                name = 'enemy-' + str(i+1)
                self.huts.append(Hut(i+1, OrcRider(name)))
            elif computer_choice == 'friend':
                name = 'knight-' + str(i+1)
                self.huts.append(Hut(i+1, Knight(name)))
            else:
                self.huts.append(Hut(i+1, computer_choice))

    def play(self):
        """Workhorse method to play the game.

        Controls the high level logic to play the game. This is called from
        the main program to begin the game execution.

        In summary, this method has the high level logic that does the following
        by calling appropriate functionality:

        * Set up instance variables for the game
        * Accept the user input for hut number to enter
        * Attempt to acquire the hut ( :py:meth:`Knight.acquire_hut` )
        * Determine if the player wins or loses.

        .. seealso:: :py:meth:`Knight.acquire_hut`
        """
        self.player = Knight()
        self._occupy_huts()
        acquired_hut_counter = 0

        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquired_hut_counter < 5:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <= 0:
                print_bold("YOU LOSE  :(  Better luck next time")
                break

            if self.huts[idx-1].is_acquired:
                acquired_hut_counter += 1

        if acquired_hut_counter == 5:
            print_bold("Congratulations! YOU WIN!!!")


if __name__ == '__main__':
    # The main program is executed here.
    game = AttackOfTheOrcs()
    game.play()

