"""gridmanager

This module illustrates how widgets can be placed using the grid layout.

This module is compatible with Python 3.5.x and Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    from Tkinter import Tk, Label, SUNKEN, RAISED, Frame
else:
    from tkinter import Tk, Label, SUNKEN, RAISED, Frame

# Create mainwindow (root) , a Tk instance
mainwin = Tk()
# Create a Frame which will 'hold' various widgets in a grid layout
content = Frame(mainwin)
# Create the Label widgets with the container object (Frame) as the parent.
l1 = Label(content, text="Cell [0,0]", relief=RAISED, bg='red')
l2 = Label(content, text="Cell [0,1]", relief=SUNKEN)
l3 = Label(content, text="Cell [0,2]", relief=RAISED, bg='red')
l4 = Label(content, text="Cell [1,1]", relief=RAISED, bg='green')
l5 = Label(content, text="Cell [1,3]", relief=RAISED, bg='green')
l6 = Label(content, text="Cell [2,4]", relief=SUNKEN)
l7 = Label(content, text="Cell [3,0] to [3-3] (spanning 4 cols)",
           relief=RAISED, bg='red')

# Define the grid layout for these labels. The sticky option helps place
# the widget along the edge of the cell (of the grid) to which it belongs.
# For example, sticky="nsew" will align the widget along top, bottom, right,
# and left edges of the cell respectively.
content.grid(column=0, row=0)
l1.grid(row=0, column=0)
l2.grid(row=0, column=1)
l3.grid(row=0, column=2)
l4.grid(row=1, column=1)
l5.grid(row=1, column=3,  rowspan=2, sticky="nsew")
l6.grid(row=2, column=4)
l7.grid(row=3, column=0, columnspan=4, sticky="nsew")

# Start the main event loop.
mainwin.mainloop()
