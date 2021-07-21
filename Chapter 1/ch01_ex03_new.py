from __future__ import print_function
"""ch01_ex02

A text-based game to acquire a hut by defeating the enemy (functional)

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

This is a supporting example code for example 2 of Chapter 1. It is a
command line program that illustrates use of Python functions.
The player inputs a hut number. If the occupant is an enemy, the player is
given an option to 'attack'. Player wins if he defeats the enemy.
In the aforementioned book this is also referred to as
"Attack of the Orcs v0.0.5". More details can be found in the relevant
chapter of the book..

RUNNING THE PROGRAM:
--------------------
- Python 3.5.x must be installed on your system.
- It is assumed that you have Python 3.5 available in your environment
  variable PATH. It will be typically available as 'python' or 'python3'.
- Here is the command to execute this code from command prompt

        $ python ch01_ex02.py     ( OR $ python3 ch01_ex02.py)

- See the README file for more information. Or visit python.org for OS
  specific instructions on executing Python from a command prompt.

.. todo::

1. The code comments and function descriptions in this file are
   intentionally kept to a minimum! See a later chapter of the book to
   learn about the code documentation and best practices!
   Feel free to add documentation after reading that chapter.
   Description of the code can be found in the book.

It is quite simple to make this code compatible even with Python 2.7.9
as follows. This is not used as this script is intended to be a very simple
Python illustration.
# --------------------------------------------------------------------------
# For backward compatibility with Python 2.7.9
# Python 2.x, the built-in function 'input' is equivalent to
# eval(raw_input(prompt)). So we should use just raw_input instead.
# Also note that we are importing print_function from module __future__
# for the same reason (see the first line of this file)
# --------------------------------------------------------------------------
user_input_function = None

if sys.version_info < (3, 0):
    user_input_function = raw_input
else:
    user_input_function = input

# Then call user_input_function() in places where we call input()

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
import random
import textwrap
import sys


if sys.version_info < (3, 0):
    print("This code requires Python 3.x and is tested with version 3.5.x ")
    print("Looks like you are trying to run this using " + 
    "Python version: {}.{} ".format(sys.version_info[0], sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)


def weighted_random_selection(obj1, obj2):
    """Randomly select between two objects based on assigned 'weight'

    .. todo:: How about creating a utility module for common functionality?
    """
    weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)]
    selection = random.choice(weighted_list)
    if selection == id(obj1):
        return obj1
    return obj2


def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)


class GameUnit:
    """A base class for creating various game characters"""
    def __init__(self, name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    def info(self):
        """Information on the unit (overridden in subclasses)"""
        pass

    def attack(self, enemy):
        """The main logic to determine injured unit and amount of injury

        .. todo:: Check if enemy exists!
        """
        injured_unit = weighted_random_selection(self, enemy)
        injury = random.randint(10, 15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("ATTACK! ", end='')
        self.show_health(end='  ')
        enemy.show_health(end='  ')

    def heal(self, heal_by=2, full_healing=True):
        """Heal the unit replenishing all the hit points"""
        if self.health_meter == self.max_hp:
            return

        if full_healing:
            self.health_meter = self.max_hp
        else:
            # TODO: Do you see a bug here? it can exceed max hit points!
            self.health_meter += heal_by

        print_bold("You are HEALED!", end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        """Reset the `health_meter` (assign default hit points)"""
        self.health_meter = self.max_hp

    def show_health(self, bold=False, end='\n'):
        """Show the remaining hit points of the player and the enemy"""
        # TODO: what if there is no enemy?
        msg = "Health: {}: {}".format(self.name, self.health_meter)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)


class Knight(GameUnit):
    """ Class that represents the game character 'Knight'

    The player instance in the game is a Knight instance. Other Knight
    instances are considered as 'friends' of the player and is
    indicated by the attribute `self.unit_type` .
    """
    def __init__(self, name='Sir Foo'):
        super().__init__(name=name)
        self.max_hp = 40
        self.health_meter = self.max_hp
        self.unit_type = 'friend'

    def info(self):
        """Print basic information about this character"""
        print("I  am a Knight!")

    def acquire_hut(self, hut):
        """Fight the combat (command line) to acquire the hut

        .. todo::   acquire_hut method can be refactored.
                   Example: Can you use self.enemy instead of calling
                   hut.occupant every time?
        """
        print_bold("Entering hut {}...".format(hut.number), end=' ')
        is_enemy = (isinstance(hut.occupant, GameUnit) and
                    hut.occupant.unit_type == 'enemy')
        continue_attack = 'y'
        if is_enemy:
            print_bold("Enemy sighted!")
            self.show_health(bold=True, end=' ')
            hut.occupant.show_health(bold=True, end=' ')
            while continue_attack:
                continue_attack = input(".......continue attack? (y/n): ")
                if continue_attack == 'n':
                    self.run_away()
                    break

                self.attack(hut.occupant)

                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self)
                    break
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


def reset_health_meter(health_meter):
    """Reset the values of health_meter dict to the original ones"""
    health_meter['player'] = 40
    health_meter['enemy'] = 30


def show_game_mission():
    """Print the game mission in the terminal window"""
    print_bold("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print_bold("TIP:")
    print("Be careful as there are enemies lurking around!")


def occupy_huts():
    """Randomly populate the `huts` list with occupants"""
    huts = []
    occupants = ['enemy', 'friend', 'unoccupied']
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts


def process_user_choice():
    """Accepts the hut number from the user"""
    msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx


def reveal_occupants(huts, idx):
    """Print the occupants of the hut"""
    print("Revealing the occupants...")
    msg = ""
    for i in range(len(huts)):
        occupant_info = "<{}:{}>".format(i+1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "
    print("\t" + msg)


def show_health(health_meter, bold=False):
    """Show the remaining hit points of the player and the enemy"""
    msg = "Health: Sir Foo: {}, Enemy: {}".format(
        health_meter['player'], health_meter['enemy'])
    if bold:
        print_bold(msg)
    else:
        print(msg)


def attack(health_meter):
    """The main logic to determine injured unit and amount of injury"""
    hit_list = 4 * ['player'] + 6 * ['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK! ", end='')
    show_health(health_meter)


def play_game(health_meter, huts, idx):
    """The main control function for playing the game"""
    if huts[idx - 1] != 'enemy':
        print_bold("Congratulations! YOU WIN!!!")
    else:
        print_bold('ENEMY SIGHTED! ', end='')
        show_health(health_meter, bold=True)
        continue_attack = True

        # Loop that actually runs the combat if user wants to attack
        while continue_attack:
            continue_attack = input(".......continue attack? (y/n): ")
            if continue_attack == 'n':
                print_bold("RUNNING AWAY with following health status...")
                show_health(health_meter, bold=True)
                print_bold("GAME OVER!")
                break

            attack(health_meter)

            # Check if either one of the opponents is defeated
            if health_meter['enemy'] <= 0:
                print_bold("GOOD JOB! Enemy defeated! YOU WIN!!!")
                break

            if health_meter['player'] <= 0:
                print_bold("YOU LOSE  :(  Better luck next time")
                break


def run_application():
    keep_playing = 'y'
    health_meter = {}
    
    reset_health_meter(health_meter)
    show_game_mission()

    # The main while loop. Keep playing depending on the user input.
    while keep_playing == 'y':
        reset_health_meter(health_meter)
        huts = occupy_huts()
        idx = process_user_choice()
        reveal_occupants(huts, idx)

        play_game(health_meter, huts, idx)

        keep_playing = input("Play again? Yes(y)/No(n):")


if __name__ == '__main__':
    run_application()
