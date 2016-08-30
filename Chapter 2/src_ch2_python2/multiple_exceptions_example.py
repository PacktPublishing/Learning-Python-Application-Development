from __future__ import print_function
"""multiple_exceptions_example

Supporting example code for 'exception handling' (Chapter 2)

This module is compatible with Python 3.5.x. AND Python 2.7.9 It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

The code is demonstrated in the book. This file is provided just in case
you want to quickly run one of the examples.

The file has simple code illustrations on exception handling in Python:
    1. Show how to specify multiple except clauses.
    2. Illustrates use of finally clause.
    3. Demonstrate how to re-raise an exception.

RUNNING THE PROGRAM:
--------------------
- Python 3.5.x must be installed on your system.
- It is assumed that you have Python 3.5 available in your environment
  variable PATH. It will be typically available as 'python'
- Here is the command to execute this code from command prompt

        $ python multiple_exception_example.py

- See the README file for more information. Or visit python.org for OS
  specific instructions on executing Python from a command prompt.

.. seealso:: `attackoftheorcs_v1_1.py`, `gameuniterror.py`

.. todo::

1. The code comments and function descriptions in this file are sparse.
    See a later chapter of the book to learn about the code documentation
    and best practices!

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

#re-raising exception example
def log_the_error(error_object):
    #print("error logged")
    # some code that writes to a file. (not shown here)
    pass


def solve_something():
    a = int(input("Enter (integer) number 'a':"))
    # Raises AssertionError if input number is <= 0
    assert a > 0
    print("Number entered is OK.")
    b = int(input("Enter (integer) number 'b':"))
    # Raises ZeroDivisionError
    a += a/b
    # Raises NameError
    d = x + a
    e = 2*d


def some_function():
    try:
        solve_something()
    except NameError as e:
        print("Uh oh..Name Error.", e.args)
    except AssertionError:
        print("Uh oh..Assertion Error.")
        print("Returning from function..")
        # Add a return to illustrate how finall clause will be called.
        return
    except Exception as e:
        print("Unhandled exception. Logging the error.")
        log_the_error(e)
        raise
    else:
        print("great! no exception occurred yet!")
    finally:
        print("finally! do some special cleanup!")


if __name__ == '__main__':
    some_function()
