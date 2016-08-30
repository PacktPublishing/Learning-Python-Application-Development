"""simple_application_2

A 'Hello World' GUI application (OOP) using Tkinter module.

This module is compatible with Python 3.5.x and Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

Running the code:
-----------------
$python simple_application_2.py

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


class MyGame:
    def __init__(self, mainwin):
        """Simple Tkinter GUI example that shows a label and an exit button.

        :param mainwin: The Tk instance (also called 'root' sometimes
        """
        lbl = Label(mainwin, text="Hello World!",  bg='yellow')
        exit_button = Button(mainwin, text='Exit',
                             command=self.exit_btn_callback)
        # pack the widgets
        lbl.pack(side=LEFT)
        exit_button.pack(side=RIGHT)

    def exit_btn_callback(self):
        """Callback function to handle the button click event."""
        mainwin.destroy()

if __name__ == "__main__":
    # Create the main window or Tk instance.
    mainwin = Tk()
    mainwin.geometry("140x40")
    game_app = MyGame(mainwin)
    mainwin.mainloop()

