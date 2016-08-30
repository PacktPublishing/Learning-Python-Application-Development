"""hutgame_mvc_pubsub

GUI implementing MVC and PyPubSub for View->Ctrl, Model->Ctrl communication

This module is compatible with Python 3.5.x and Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

The application is a trivial game where the player has to select a
radiobutton to 'enter a hut'. Depending on the occupant, the player either
wins or loses! In the aforementioned book this is also referred to as
"Attack of the Orcs V 10.1.0". More details can be found in the relevant
chapter of the book..

The module shows just one simple way of implementing Model-View-Controller
architecture for Python GUI application. It also uses PyPubSub (Python
publish-subscribe API) for communicating information from View to Controller
and also from Model to Controller.

This code uses Python's tkinter gui library to create a trivial application.
Along with tkinter, it requires an external package call 'pypubsub' that
provides a Publish-subscribe API for event-driven programming.

This dependency can be installed using pip:
$pip install pypubsub

Running the application
------------------------
First make sure you have the required dependency installed. Then run the
application from the command prompt as:

$python hutgame_mvc_pubsub.py

The program initially puts 'enemy' or a 'friend' inside each hut. Some huts
could also be left 'unoccupied'. You are asked to select a hut. You win if
the hut occupant is either a 'friend' OR if the hut is unoccupied.

To EXIT the game, click on the 'x' mark icon in the title bar of the game's
application window.

.. note:: A possible variant of this is where you can use pubsub for
       publish-subscribe communication from View to Model and vice versa.
       This is not illustrated here.

TODO:
  Do the following as an exercise.
  1. Put the Model View and Controller classes in their own modules!
  2. Implement the "Restart Game" button! When clicked,
  the 'game' should restart. In other words, you should do the following:
     a) Randomly distribute the occupants again by calling occupy_huts()
     b) Clear the state of the radio buttons i.e. all the buttons
          should be 'deselected'

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import sys
import random
from pubsub import pub

if sys.version_info < (3, 0):
    from Tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
    import tkMessageBox as messagebox
else:
    from tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
    from tkinter import messagebox


class Model:
    def __init__(self):
        self.huts = []
        self.result = ""
        # The preparatory work that populates the self.huts list
        self.occupy_huts()

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
        """Enter the hut,determine the winner and 'publish' the result.

        This method checks the hut occupant stored in self.huts for the
        given hut_number. Depending on the occupant the winner is
        'announced'. Here, the result is 'published'using the `pubsub`
        library. There could be multiple 'subscribers' waiting for this
        message to arrive. In this case the subscriber is a method from the
        `Controller` class.

        :param hut_number: The number assigned to the selected hut

        .. seealso:: :py:meth:`occupy_huts`
        .. seealso:: :py:meth:`Controller.model_change_handler`
        .. seealso:: :py:meth:`Controller.__init__`
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

        # 'Publish' a message saying the model has changed
        # Here, the 'winner' is announced. Then the subscribers to
        # this message (the controller) can take necessary action.
        pub.sendMessage("WINNER ANNOUNCEMENT", data=self.result)


class View:
    def __init__(self, parent):
        """The View component of the Hut Game.

        This class represents the view component of a MVC architecture.
        It defines and sets up graphical user interface. In this example,
        the View has no knowledge of the Controller or the model. However,
        the Controller sets up the necessary callback functions that are
        invoked when various events are triggered.

        :param parent: The parent tkinter widget.In this example it is the
            instance of Tk class (called mainwin)
        :ivar int hut_width: The width of the application window in pixels.
        :ivar int hut_height: The height of the application window in pixels
        :ivar PhotoImage village_image: Background image for the app
        :ivar PhotoImage hut_image: The hut image for the radio buttons.
        :ivar container: The main widget serving as a parent for others.
            In this example it is just the main Tk instance passed as
        :ivar str result: The string to declare the result via a messagebox.
        """
        self.village_image = PhotoImage(file="Jungle_small.gif")
        self.hut_image = PhotoImage(file="Hut_small.gif")
        self.container = parent
        # ------------------------------------------------------------------
        # Important: Set the hut_width to about 70 pixels if the radio
        # button is configured with "indicatoron=0" option (i.e. without the
        # radio button indicator
        # ------------------------------------------------------------------
        self.hut_width = 40
        self.hut_height = 56

    def radio_btn_pressed(self):
        """Publishes a message to notify the Controller.

         Uses PyPubSub to publish a message to a topic Radio_button_pressed.
         The 'subscriber' here is the Controller which gets notified.
         """
        pub.sendMessage("Radio_Button_Pressed")

    def setup(self):
        """Calls methods to setup the user interface."""
        self.create_widgets()
        self.setup_layout()

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

        :param string data: The data to be displayed in the messagebox.
        """
        messagebox.showinfo("Winner Announcement", message=data)


class Controller:
    def __init__(self, parent):
        """The Controller class of the Hut game (MVC architecture).

        This class enables a handshake between `Model` and `View`.

        :param parent: The parent object.Here it i the Tk instance, mainwin.
        :ivar Model model: Instance representing the Model of a MVC
        :ivar View view: Instance representing the View of a MVC
        """
        self.parent = parent
        self.model = Model()
        self.view = View(parent)
        self.view.setup()
        # 'Subscribe' to the topic 'WINNER ANNOUNCEMENT" The publisher is
        # the model.
        pub.subscribe(self.model_change_handler, "WINNER ANNOUNCEMENT")
        # 'Subscribe' to the topic "Radio_Button_Pressed". The publisher is
        # the View.
        pub.subscribe(self.radio_btn_pressed, "Radio_Button_Pressed")

    # Handle Events
    def radio_btn_pressed(self):
        """Command callback when radio button is in the view pressed.

        .. seaalso:: :py:meth:`View.create_widgets`
        .. seaalso:: :py:meth:`Model.enter_hut`
        """
        self.model.enter_hut(self.view.var.get())

    def model_change_handler(self, data):
        self.view.announce_winner(data)

if __name__ == "__main__":
    # Create an instance of Tk. This is popularly called 'root' But let's
    # call it mainwin (the 'main window' of the application. )
    mainwin = Tk()
    WIDTH = 494
    HEIGHT = 307
    mainwin.geometry("%sx%s" % (WIDTH, HEIGHT))
    mainwin.resizable(0, 0)
    mainwin.title("Attack of the Orcs Game")

    game_app = Controller(mainwin)

    mainwin.mainloop()
