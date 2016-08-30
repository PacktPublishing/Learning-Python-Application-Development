"""simple_application_bind_method

A simple GUI app that shows use of Tkinter's bind method (grid manager)

This module is compatible with Python 3.5.x and Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

Running the code:
-----------------
$python simple_application_bind_method.py

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    from Tkinter import Tk, Label, Button, LEFT, RIGHT
else:
    from tkinter import Tk, Label, Button, LEFT, RIGHT


def exit_btn_callback(evt):
    """Callback function to handle the button click event.

    :param Event evt: The instance of class Event from tkinter module.
    """
    print("Inside exit_btn_callback. Event object is: ", evt)
    mainwin.destroy()

if __name__ == "__main__":
    # Create the main window or Tk instance.
    mainwin = Tk()
    mainwin.geometry("140x40")
    # Create a label widget and 'pack' it in a row (or column)
    lbl = Label(mainwin, text="Hello World!",  bg='yellow')
    lbl.pack(side=LEFT)
    exit_button = Button(mainwin, text='Exit')
    # Bind the button click event to function exit_btn_callback
    exit_button.bind("<Button-1>", exit_btn_callback)
    exit_button.pack(side=RIGHT)
    mainwin.mainloop()
