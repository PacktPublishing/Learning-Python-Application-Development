from __future__ import print_function
"""ch01_ex02

A text-based game to acquire a hut by defeating the enemy (functional)

This module is compatible with Python 2.7.9. It contains
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
- Python 2.7.9 must be installed on your system.
- It is assumed that you have Python 2.7.9 available in your environment
  variable PATH. It will be typically available as 'python' or 'python2'.
- Here is the command to execute this code from command prompt

        $ python ch01_ex02.py

- See the README file for more information. Or visit python.org for OS
  specific instructions on executing Python from a command prompt.

.. todo::

1. The code comments and function descriptions in this file are
   intentionally kept to a minimum! See a later chapter of the book to
   learn about the code documentation and best practices!
   Feel free to add documentation after reading that chapter.
   Description of the code can be found in the book.

It is quite simple to make this code compatible with both versions
2.7.9 and 3.5 as follows. This is not used as this script is intended to be
a very simple Python illustration.
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

if sys.version_info >= (3, 0):
    print("This code requires Python 2.7.9 ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)


def show_theme_message(width):
    """Print the game theme in the terminal window"""
    print_dotted_line()
    print_bold("Attack of The Orcs v0.0.5:")
    msg = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he  decided to enter..")

    print(textwrap.fill(msg, width=width))


def show_game_mission():
    """Print the game mission in the terminal window"""
    print_bold("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print_bold("TIP:")
    print("Be careful as there are enemies lurking around!")
    print_dotted_line()


def reveal_occupants(idx, huts):
    """Print the occupants of the hut"""
    msg = ""
    print("Revealing the occupants...")
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i+1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "

    print("\t" + msg)
    print_dotted_line()


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
    user_choice = raw_input("\n" + msg)
    idx = int(user_choice)
    return idx


def show_health(health_meter, bold=False):
    """Show the remaining hit points of the player and the enemy"""
    msg = "Health: Sir Foo: %d, Enemy: %d" \
          % (health_meter['player'], health_meter['enemy'])

    if bold:
        print_bold(msg)
    else:
        print(msg)


def reset_health_meter(health_meter):
    """Reset the values of health_meter dict to the original ones"""
    health_meter['player'] = 40
    health_meter['enemy'] = 30


def print_bold(msg, end='\n'):
    """Print a string in 'bold' font"""
    print("\033[1m" + msg + "\033[0m", end=end)


def print_dotted_line(width=72):
    """Print a dotted (rather 'dashed') line"""
    print('-'*width)

def attack(health_meter):
    """The main logic to determine injured unit and amount of injury"""
    hit_list = 4 * ['player'] + 6 * ['enemy']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("ATTACK! ", end='')
    show_health(health_meter)


def play_game(health_meter):
    """The main control function for playing the game"""
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx, huts)

    if huts[idx - 1] != 'enemy':
        print_bold("Congratulations! YOU WIN!!!")
    else:
        print_bold('ENEMY SIGHTED! ', end='')
        show_health(health_meter, bold=True)
        continue_attack = True

        # Loop that actually runs the combat if user wants to attack
        while continue_attack:
            continue_attack = raw_input(".......continue attack? (y/n): ")
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
    """Top level control function for running the application."""
    keep_playing = 'y'
    health_meter = {}
    reset_health_meter(health_meter)
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = raw_input("\nPlay again? Yes(y)/No(n): ")


if __name__ == '__main__':
    run_application()

