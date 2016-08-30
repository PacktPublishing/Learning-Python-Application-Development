"""mainloop_example

This module shows the simplest GUI application you could create with Tkinter

This module is compatible with Python 3.5.x and Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    from Tkinter import Tk
else:
    from tkinter import Tk


if __name__ == '__main__':
    print("Python version: ", sys.version_info)
    # Create a Tk instance
    mainwin = Tk()
    # Start the main event loop.
    mainwin.mainloop()