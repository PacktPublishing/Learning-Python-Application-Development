"""hutgame

A simple game where the player has to select a hut where Sir Foo can rest.

This module is compatible with Python 3.5.x and Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

The application is a trivial game where the player has to select a
radiobutton to 'enter a hut'. Depending on the occupant, the player either
wins or loses! In the aforementioned book this is also referred to as
"Attack of the Orcs V 10.0.0". More details can be found in the relevant
chapter of the book..

See also: hutgame_mvc.py which has implements Model-View-Controller
architecture for the same example.

Running the application
------------------------
The application can be run from the command prompt as:

$ python hutgame.py

The program initially puts 'enemy' or a 'friend' inside each hut. Some huts
could also be left 'unoccupied'. You are asked to select a hut. You win if
the hut occupant is either a 'friend' OR if the hut is unoccupied.

To EXIT the game, click on the 'x' mark icon in the title bar of the game's
application window.

TODO:
  As an exercise, implement the "Restart Game" button! When clicked,
  the program should restart. In other words:
   (a) randomly distribute the occupants (call occupy_huts())
   (b) Clear the state of the radio buttons i.e. all the buttons
          should be 'unselected'


:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import sys
import random

if sys.version_info < (3, 0):
    from Tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
    import tkMessageBox as messagebox
else:
    from tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
    from tkinter import messagebox


class HutGame:
    def __init__(self, parent):
        """A game where the player selects a hut where 'Sir Foo' to rest.

        The program initially puts 'enemy' or a 'friend' inside each hut.
        Some huts could also be left 'unoccupied'. You are asked to select
        a hut. You win if the hut occupant is either a 'friend' OR if the
        hut is not occupied,

        :param parent: The parent tkinter widget.
        :ivar list huts: List to store occupant types (as strings)
        :ivar int hut_width: The width of the application window in pixels.
        :ivar int hut_height: The height of the application window in pixels
        :ivar PhotoImage village_image: Background image for the app
        :ivar PhotoImage hut_image: The hut image for the radio buttons.
        :ivar Tk container: The main widget serving as a parent for others.
               In this example it is just the main Tk instance.
        :ivar str result: The string to declare the result via a messagebox.
        """
        self.village_image = PhotoImage(file="Jungle_small.gif")
        self.hut_image = PhotoImage(file="Hut_small.gif")
        # ------------------------------------------------------------------
        # Important: Set the hut_width to about 70 pixels if the radio
        # button is configured with "indicatoron=0" option (i.e. without
        # the radio button indicator
        # ------------------------------------------------------------------
        self.hut_width = 40
        self.hut_height = 56
        self.container = parent

        self.huts = []
        self.result = ""
        # The preparatory work that populates the self.huts list
        # (no UI involved)
        self.occupy_huts()
        # Setup the user interface
        self.setup()

    def occupy_huts(self):
        """Randomly occupy the huts: enemy or friend or keep unoccupied."""
        occupants = ['enemy', 'friend', 'unoccupied']
        while len(self.huts) < 5:
            computer_choice = random.choice(occupants)
            self.huts.append(computer_choice)
        # Alternatively you can also use list comprehension like so:
        # self.huts  = [random.choice(occupants) for _ in range(5)]
        print("Hut occupants are:", self.huts)

    def enter_hut(self, hut_number):
        """Enter the selected hut and determine the winner.

        This method checks the hut occupant stored in self.huts for the
        given hut_number. Depending on the occupant the winner is
        'announced'.

        :param hut_number: The number assigned to the selected hut

        .. seealso:: :py:meth:`occupy_huts`
        .. seealso:: The equivalent method in file hutgame_mvc.py
        """
        print("Entering hut #:", hut_number)
        hut_occupant = self.huts[hut_number-1]
        print("Hut occupant is: ", hut_occupant)

        if hut_occupant == 'enemy':
            self.result = "Enemy sighted in Hut # %d \n\n" % hut_number
            self.result += "YOU LOSE :( Better luck next time!"
        elif hut_occupant == 'unoccupied':
            self.result = "Hut # %d is unoccupied\n\n" % hut_number
            self.result += "Congratulations! YOU WIN!!!"
        else:
            self.result = "Friend sighted in Hut # %d \n\n" % hut_number
            self.result += "Congratulations! YOU WIN!!!"

        # Announce the winner!
        self.announce_winner(self.result)

    def create_widgets(self):
        """Create various widgets in the tkinter main window."""
        self.var = IntVar()
        self.background_label = Label(self.container,
                                      image=self.village_image)
        txt = "Select a hut to enter. You win if:\n"
        txt += "The hut is unoccupied or the occupant is a friend!"
        self.info_label = Label(self.container, text=txt, bg='yellow')
        # Create a dictionary for radio button config options.
        r_btn_config = {'variable': self.var,
                        'bg': '#A8884C',
                        'activebackground': 'yellow',
                        'image': self.hut_image,
                        'height': self.hut_height,
                        'width': self.hut_width,
                        'command': self.radio_btn_pressed}

        self.r1 = Radiobutton(self.container, r_btn_config, value=1)
        self.r2 = Radiobutton(self.container, r_btn_config, value=2)
        self.r3 = Radiobutton(self.container, r_btn_config, value=3)
        self.r4 = Radiobutton(self.container, r_btn_config, value=4)
        self.r5 = Radiobutton(self.container, r_btn_config, value=5)

    def setup(self):
        """Calls methods to setup the user interface."""
        self.create_widgets()
        self.setup_layout()

    def setup_layout(self):
        """Use the grid geometry manager to place widgets."""
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(4, weight=1)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.info_label.grid(row=0, column=0, columnspan=5, sticky='nsew')
        self.r1.grid(row=1, column=0)
        self.r2.grid(row=1, column=4)
        self.r3.grid(row=2, column=3)
        self.r4.grid(row=3, column=0)
        self.r5.grid(row=4, column=4)

    def announce_winner(self, data):
        """Declare the winner by displaying a tkinter messagebox.

        :param data: The data to be 'published'. This could be any object.
           Here, it is a string.
        """
        messagebox.showinfo("Winner Announcement", message=data)

    # Handle Events
    def radio_btn_pressed(self):
        """Command callback when radio button is pressed.

        .. seealso:: :py:meth:`create_widgets`
        """
        self.enter_hut(self.var.get())


if __name__ == "__main__":
    # Create Tk instance. This is popularly called 'root' But let's
    # call it mainwin (the 'main window' of the application. )
    mainwin = Tk()
    WIDTH = 494
    HEIGHT = 307
    mainwin.geometry("%sx%s" % (WIDTH, HEIGHT))
    mainwin.resizable(0, 0)
    mainwin.title("Attack of the Orcs Game")
    game_app = HutGame(mainwin)
    mainwin.mainloop()
