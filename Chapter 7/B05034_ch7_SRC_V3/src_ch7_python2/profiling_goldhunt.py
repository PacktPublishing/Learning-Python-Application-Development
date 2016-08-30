"""profiling_goldhunt

This module contains code to profile the "Gold Hunt" scenario
using cProfile and then view the profiling statistics using pstats module

This module is compatible with Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import sys

if sys.version_info >= (3, 0):
    print("This code requires Python 2.7.9 ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0],
                                      sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)

import cProfile
import pstats
from goldhunt_inefficient import GoldHunt


def view_stats(fil, text_restriction):
    """View the pstats for the given file"""

    stats = pstats.Stats(fil)
    # Remove the long directory paths
    stats.strip_dirs()
    # Sort the stats by the total time (internal time)
    sorted_stats = stats.sort_stats('tottime')
    # Only show stats that have "goldhunt" in their 'name column'
    sorted_stats.print_stats("goldhunt")


def play_game():
    """Control function to execute the GoldHunt game"""
    game = GoldHunt()
    game.play()

if __name__ == '__main__':
    filname = 'profile_output_new'
    cProfile.run('play_game()',filname)
    # View the pstats
    view_stats(filname, "goldhunt")
