"""goldhunt_pass6_parallel

This module illustrates the 6th optimization pass for the Gold Hunt
program.

Here, we parallelize the search operation using Python's multiprocessing
module. See GoldHunt.play and GoldHunt.find_coins for more details.

This module is compatible with Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

NOTE: This may also work with Python 3.5.x but not tested.
Python 3.5.x compatible code is provided separately.

RUNNING THE PROGRAM
--------------------
$ python goldhunt_pass6_parallel.py

- See the README file for more information. Or visit python.org for OS
specific instructions on executing Python from a command prompt.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import sys
import cProfile
import pstats
import numpy as np
import multiprocessing
import itertools

# Make sure we are 'not' using Python 3. (should really be Python 2.7.9)
if sys.version_info >= (3, 0):
    print("This code requires Python 2.7.9 ")
    print("Looks like you are trying to run this using "
          "Python version: %d.%d " % (sys.version_info[0], sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)

try:
    import matplotlib.pyplot as plt
except ImportError:
    msg = "You won't be able to visualize the random point distribution."
    print("ImportError: matplotlib.pyplot ",msg)


# For Python 2.x only:
def global_function_find_coins(self_arg, x_list, y_list, x_ref, circle_num):
    """A workaround for the 'PickleError'

     This Pickle error is seen when using the instance method
     self.find_coins inside the apply_async function call. The workaround
     is to have this global method which in turn calls the class method
     GoldHunt.find_coins. Note that we even have to pass the 'instance'
     'self'. This is passed as the first argument to this method 'self_arg'
     """
    return GoldHunt.find_coins(self_arg, x_list, y_list, x_ref, circle_num)


def plot_points(ref_radius, x_coords, y_coords):
    """Utility function to show the 'Gold Field!

    :param float ref_radius: Reference radius to determine axis limits
    :param list x_coords: X coordinates of the points to be plotted
    :param list y_coords: Y coordinates of the points to be plotted
    """
    # Define axis limits
    a1 = ref_radius + 1
    a2 = a1*(-1.0)
    plt.plot(x_coords, y_coords, ".", color='#A67C00', ms=4)
    plt.axis([a2, a1, a2, a1])
    plt.show()


def generate_random_points(ref_radius, total_points):
    """Return x, y coordinate lists representing random points inside a circle.

    This function illustrates NumPy capabilities. It is used in the
    optimization pass 4, 5, 6 in the chapter on performance of the book
    Learning Python  Application Development (Packt Publishing).

    The run time performance of this function will be
    significantly faster compared to the previous optimization pass.

    Generates random points inside a circle with center at (0,0). For any
    point, it randomly picks a radius between 0 and ref_radius.

    :param ref_radius: The random point lies between 0 and this radius.
    :param total_points: total number of random points to be created
    :return: x and y coordinates as lists

    .. todo:: Refactor! Move the function to a module like gameutilities.py
    """
    # Combination of avoiding the dots (function reevaluations)
    # and using local variable. This is similar to the
    # optimization pass-3 but here we use equivalent NumPy functions.
    l_uniform = np.random.uniform
    l_sqrt = np.sqrt
    l_pi = np.pi
    l_cos = np.cos
    l_sin = np.sin

    # Note that the variables theta and radius are now NumPy arrays.
    theta = l_uniform(0.0, 2.0*l_pi, total_points)
    radius = ref_radius*l_sqrt(l_uniform(0.0, 1.0, total_points))
    x = radius*l_cos(theta)
    y = radius*l_sin(theta)

    # Unlike optimization pass-4 (which returns x and y as Python lists,
    # here it returns the NumPy arrays directly to be consumed by
    # the GoldHunt.find_coins method
    return x, y


class GoldHunt:
    """Class to play a game scenario 'Gold Hunt' in 'Attack of The Orcs'.

    This class is created to illustrate a scenario discussed in the book:
    'Learning Python Application Development (Packt Publishing).

    This class illustrates various bottlenecks that impact
    the performance of the application. The bottlenecks will be visible if
    appropriately change the input arguments to __init__. For example,
    setting field_coins to a large number and/or making the search radius very
    small. A word of caution: if you do such changes, it will likely
    consume a lot of memory and you may notice performance lag on your computer.
    So do it at your own risk!

    :ivar int field_coins: Gold coins scattered over a circular field
    :ivar float field_radius: Radius of the circular field with gold coins
    :ivar float search radius: Radius of a circle. The gold search will be
            constrained within this circle.
    :ivar float x_ref: X-coordinate of the game unit searching for gold.
    :ivar float y_ref: Y-coordinate of the game unit searching for gold.
    :ivar float move_distance: Distance by which the game unit advances for the
           next search.
    """
    def __init__(self, field_coins=5000, field_radius=10.0, search_radius=1.0):
        self.field_coins = field_coins
        self.field_radius = field_radius
        self.search_radius = search_radius

        # Sir Foo's initial coordinates e.g. (-9.0, 0)
        self.x_ref = - (self.field_radius - self.search_radius)
        self.y_ref = 0.0
        # Distance by which Sir Foo (or any unit) advances for the
        # next search
        self.move_distance = 2*self.search_radius

    def reset_params(self):
        """Resets some dependent params to their default computed value."""
        self.x_ref = - (self.field_radius - self.search_radius)
        self.move_distance = 2*self.search_radius

    def find_coins(self, x_list, y_list, process_x_ref, circle_num):
        """Return list of coins that lie within a given distance.

        :param x_list: List of x coordinates of all the coins (points)
        :param y_list: List of y coordinates of all the coins (points)
        :param process_x_ref: The x-coordinate of the current search circle.
           It is the circle inside which the find_coins is actively
           searching for coins (parallel processes)
        :param circle_num: Circle number or id (used for printing purpose)
        :return: A list containing (x,y) coords of all the eligible coins
        """
        collected_coins = []
        # Compute the square of the search radius needed later
        search_radius_square = self.search_radius*self.search_radius
        # Assign collected_coins.append to a local function
        append_coins_function = collected_coins.append

        # Create a single 'points' array from
        # (x_list, y_list) representing x, y coordinates.
        points = np.dstack((x_list, y_list))
        # Array representing the center of search circle
        # process_x_ref is the x-coordinate of the current search circle
        center = np.array([process_x_ref, self.y_ref])
        diff = points - center

        # Use einsum to get array representing distance squares
        distance_squares = np.einsum('...i,...i', diff, diff)
        # Convert it to Python list (list of 'distance squares')
        dist_sq_list = distance_squares[0].tolist()

        for i, d in enumerate(dist_sq_list):
            # i is the index. d is the value of the list item
            if d <= search_radius_square:
                # See the definition of append_coins_function
                # before the for loop. It is used in place of
                # collected_coins.append for speedup
                append_coins_function((x_list[i], y_list[i]))

        print("Circle# {num}, center:({x}, {y}), coins: {gold}".format(
                num=circle_num, x=process_x_ref, y=self.y_ref,
                gold=len(collected_coins)))
        return collected_coins

    def play(self):
        """Top level logic to play the game"""
        x_ref = self.x_ref
        x_centers = []
        circle_numbers = []
        x_list, y_list = generate_random_points(self.field_radius,
                                                self.field_coins)
        # Prepare a list to store all the circle centers (x_ref).
        count = 0
        while x_ref <= 9.0:
            count += 1
            x_centers.append(x_ref)
            x_ref += self.move_distance
            circle_numbers.append(count)

        # Parallelize the find_coins operation. Choose the
        # number of processes depending on your machine specs!
        pool = multiprocessing.Pool(processes=3)
        # ------------------------------------------------------------------
        # For Python 2.7 only ... to avoid PicklingError: Can't pickle...
        # Here we pass global_function_find_coins as an argument to
        # apply_async See the function at the top of this file.
        # ------------------------------------------------------------------
        results = [pool.apply_async(global_function_find_coins,
                                    args=(self, x_list, y_list, x_ref, num))
                        for x_ref, num in zip(x_centers, circle_numbers)]

        # ------------------------------------------------------------------
        # Python 3.5 equivalent code. As an exercise, you can use the
        # sys.version_info (see top of this file) to check the Python
        # version and execute the code accordingly.
        # ------------------------------------------------------------------
        # results = [pool.apply_async( self.find_coins,
        #                              args=( x_list, y_list, x_ref, num))
        #           for x_ref, num in zip(x_centers, circle_numbers)]
        pool.close()
        pool.join()

        # The elements of results list are instances of Pool.ApplyResult.
        # Use the object's get() method to get the final values.
        # Optionally You can also use generator expression here.
        output = [p.get() for p in results]

        # Optionally You can also use generator expression here.
        # It could be marginally slower, but will not consume much memory.
        #output = (p.get() for p in results)

        # Merge the results
        total_collected_coins = list(itertools.chain(*output))
        print("Total_collected_coins =", len(total_collected_coins))


# Functions for profiling the code.
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


def play_game():
    """Control function to execute the GoldHunt game"""
    # IMPORTANT: The choice of input suggested below can consume a lot of
    # computational resources on your machine. See what your computer can
    # handle first by choosing a smaller size for field_coins and a LARGER
    # search_radius!
    game = GoldHunt(field_coins=2000000, search_radius=0.1)
    game.play()

if __name__ == '__main__':
    filname = 'profile_output_new'
    cProfile.run('play_game()', filname)
    # View the pstats
    view_stats(filname, "goldhunt")
