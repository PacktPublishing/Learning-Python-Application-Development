"""goldhunt_run_master

This is an optional module that will allow you to run a particular
optimization pass.

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

RUNNING THE PROGRAM
--------------------

        $ python goldhunt_run_master.py

Then specify the choice between 0 to 6. (NO ERROR CHECKING IS DONE!)

- See the README file for more information. Or visit python.org for OS
specific instructions on executing Python from a command prompt.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import cProfile
import pstats
import sys

from goldhunt_0 import GoldHunt as GoldHunt0
from goldhunt_pass1 import GoldHunt as GoldHunt1
from goldhunt_pass2 import GoldHunt as GoldHunt2
from goldhunt_pass3 import GoldHunt as GoldHunt3
from goldhunt_pass4 import GoldHunt as GoldHunt4
from goldhunt_pass5 import GoldHunt as GoldHunt5
from goldhunt_pass6_parallel import GoldHunt as GoldHunt6



def view_stats(fil, text_restriction):
    """View the pstats for the given file

    :param fil: The file name for printing the stats.
    :param text_restriction: UNUSED variable to define filter on the output

    .. todo:: Cleanup the unused text_restriction variable or implement it!
    """
    stats = pstats.Stats(fil)
    # Remove the long directory paths
    stats.strip_dirs()
    # Sort the stats by the total time (internal time)
    sorted_stats = stats.sort_stats('tottime')
    # Only show stats that have "goldhunt" in their 'name column'
    sorted_stats.print_stats("goldhunt")


def play_game(num_string):
    """Control function to execute the GoldHunt game"""
    GoldHunt_class = getattr(sys.modules[__name__], "GoldHunt%s"%num_string)
    game = GoldHunt_class(field_coins=2000000, search_radius=0.1)
    game.play()


if __name__ == '__main__':
    num_string = input("Enter optimization pass # ")
    filname = 'profile_output_pass_%s'%num_string
    cProfile.run('play_game(%s)'%num_string,filname)
    # View the pstats
    view_stats(filname, "goldhunt")
