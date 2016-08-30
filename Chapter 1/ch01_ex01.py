from __future__ import print_function
"""ch01_ex01

A simple text-based game (script) - select a hut where Sir Foo can rest.

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

The is a simple command line script where the player input a hut number
to 'enter a hut'. Depending on the occupant, the player either
wins or loses! In the aforementioned book this is also referred to as
"Attack of the Orcs v0.0.1". More details can be found in the relevant
chapter of the book..

RUNNING THE PROGRAM:
--------------------
- Python 3.5.x must be installed on your system.
- It is assumed that you have Python 3.5 available in your environment
  variable PATH. It will be typically available as 'python' or 'python3'.
- Here is the command to execute this code from command prompt

        $ python ch01_ex01.py     ( OR $ python3 ch01_ex01.py)

- See the README file for more information. Or visit python.org for OS
  specific instructions on executing Python from a command prompt.

TODO:
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
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)

if __name__ == '__main__':
    keep_playing = 'y'
    occupants = ['enemy', 'friend', 'unoccupied']
    # Print the game mission
    width = 72
    dotted_line = '-' * width
    print(dotted_line)
    print("\033[1m" + "Attack of The Orcs v0.0.1:" + "\033[0m")
    msg = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he  decided to enter..")

    print(textwrap.fill(msg, width=width))
    print("\033[1m" + "Mission:" + "\033[0m")
    print("\tChoose a hut where Sir Foo can rest...")
    print("\033[1m" + "TIP:" + "\033[0m")
    print("Be careful as there are enemies lurking around!")
    print(dotted_line)

    # The main while loop. Keep playing depending on the user input.
    while keep_playing == 'y':
        huts = []
        # Randomly append 'enemy' or 'friend' or None to the huts list
        while len(huts) < 5:
            computer_choice = random.choice(occupants)
            huts.append(computer_choice)

        # Prompt user to select a hut
        msg = "\033[1m" + "Choose a hut number to enter (1-5): " + "\033[0m"
        user_choice = input("\n" + msg)
        idx = int(user_choice)

        # Print the occupant info
        print("Revealing the occupants...")
        msg = ""
        for i in range(len(huts)):
            occupant_info = "<%d:%s>"%(i+1, huts[i])
            if i + 1 == idx:
                occupant_info = "\033[1m" + occupant_info + "\033[0m"
            msg += occupant_info + " "
        print("\t" + msg)
        print(dotted_line)
        print("\033[1m" + "Entering hut %d... " % idx + "\033[0m", end=' ')

        # Determine and announce the winner
        if huts[idx-1] == 'enemy':
            print("\033[1m" + "YOU LOSE :( Better luck next time!" +
                  "\033[0m")
        else:
            print("\033[1m" + "Congratulations! YOU WIN!!!" + "\033[0m")

        print(dotted_line)
        keep_playing = input("Play again? Yes(y)/No(n):")

