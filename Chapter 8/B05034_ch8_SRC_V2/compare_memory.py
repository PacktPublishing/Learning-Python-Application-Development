"""compare_memory

This module can be used by the memory_profiler to get line by line
memory consumption output for the given functions. See the relevant
performance chapter for more details.

This module is compatible with Python 3.5.x and Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

RUNNING THE PROGRAM
--------------------
Run memory_profiler as follows:

$ python -m memory_profiler compare_memory.py

Typical usage of this module is to compare the memory consumption
of two functions.(the chapter has more info)

You can add a decorator @profile above the functions
you want to monitor for memory usage. Example:
      @profile
      def list_com_memory
          # some code follows..

      @profile
      def generator_expr_memory:
          #some code follows..

Make sure you call these functions:
if __name__ == '__main__':
    list_comp_memory()
    generator_expr_memory()

See the README file for more information. Or visit python.org for OS
specific instructions on executing Python from a command prompt.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
from itertools import chain


def get_data():
    for i in range(3):
        yield i


# Enable the @profile decorator only when you are running line_profiler
# or memory_profiler. Otherwise it will throw an error.
@profile
def list_comp_memory():
    sample_size = 10000
    my_data = [i for i in range(sample_size)]


# Enable the @profile decorator only when you are running line_profiler
# or memory_profiler. Otherwise it will throw an error.
@profile
def generator_expr_memory():
    sample_size = 10000
    my_data = (i for i in range(sample_size))


# Create some lists. these will be 'chained' together
data_1 = ['x']*10000
data_2 = ['y']*10000
data_3 = ['z']*10000


# Enable the @profile decorator only when you are running line_profiler
# or memory_profiler. Otherwise it will throw an error.
#@profile
def chain_memory():
    mychain = chain(data_1, data_2, data_3)
    for i in mychain:
        pass


# Enable the @profile decorator only when you are running line_profiler
# or memory_profiler. Otherwise it will throw an error.
#@profile
def list_memory():
    mylist = data_1 + data_2 + data_3
    for i in mylist:
        pass

if __name__ == '__main__':
    list_comp_memory()
    generator_expr_memory()
    #chain_memory()
    #list_memory()
