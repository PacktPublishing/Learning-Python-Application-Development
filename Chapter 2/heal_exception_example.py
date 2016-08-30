from __future__ import print_function
"""heal_exception_example

Supporting example code for 'exception handling' (Chapter 2)

This module is compatible with Python 3.5.x AND Python 2.7.9 It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

This is a simplified version of the game to create an 'artificial bug'. This
bug is introduced just to demonstrate how implement custom exceptions.

This file contains the top level control code that:
  a) Creates a Knight instance,
  b) forcefully reduces the hit points (see knight.health_meter),
    as if the knight  has fought a combat and sustained injuries.
  c) In the end, it calls the heal function with heal_by argument.

See the section on Defining custom exceptions in the book for more details.

RUNNING THE PROGRAM:
--------------------
- Python 3.5.x must be installed on your system.
- It is assumed that you have Python 3.5 available in your environment
  variable PATH. It will be typically available as 'python' or 'python3'.
- Here is the command to execute this code from command prompt

        $ python heal_exception_example.py

- See the README file for more information. Or visit python.org for OS
  specific instructions on executing Python from a command prompt.

.. seealso:: `attackoftheorcs_v1_1.py`, `gameuniterror.py`

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""


from attackoftheorcs_v1_1 import Knight
from gameuniterror import GameUnitError

# See the module docstring for details.
if __name__ == '__main__':
    print("Creating a Knight..")
    knight = Knight("Sir Bar")
    # Assume the Knight has sustained injuries in the combat.
    knight.health_meter = 10
    knight.show_health()
    try:
        # Heal the knight by 100 hit points. This will raise an
        # exception as the Knight can have upto 40 hit points.
        knight.heal(heal_by=100, full_healing=False)
    except GameUnitError as e:
        # Print the information about the error
        print(e)
        print(e.error_message)

    knight.show_health()

