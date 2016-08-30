"""simple_application_1

A 'Hello World' GUI application ( a script) using Tkinter module.

This module is compatible with Python 3.5.x and Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

Running the code:
-----------------
$python simple_application_1.py

.. seealso:: `hutgame.py`

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    from Tkinter import Tk, Label, Button, LEFT, RIGHT
else:
    from tkinter import Tk, Label, Button, LEFT, RIGHT

if __name__ == "__main__":
    # Create the main window or Tk instance.
    mainwin = Tk()
    mainwin.geometry("140x40")
    # Create a label widget and 'pack' it in a row (or column)
    lbl = Label(mainwin, text="Hello World!",  bg='yellow')
    lbl.pack(side=LEFT)
    # 'Exit' button that calls mainwin.destroy when clicked
    exit_button = Button(mainwin, text='Exit', command=mainwin.destroy)
    exit_button.pack(side=RIGHT)
    mainwin.mainloop()

