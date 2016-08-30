"""pool_example

Shows a trivial examples on how to use various methods of the class Pool.
The code illustrated below is for apply_async method. Other methods, apply
and map are also commented out. See the chapter for more details.

This module is compatible with Python 3.5.x and Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

RUNNING THE PROGRAM
-------------------

        $ python pool_example.py

(see the book for further information.)

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
from __future__ import print_function
import multiprocessing


def get_result(num):
    """Trivial function used in multiprocessing example"""
    process_name = multiprocessing.current_process().name
    print("Current process:", process_name, ", Input Number:", num)
    return 10*num

if __name__ == '__main__':
    numbers = [2, 4, 6, 8, 10]
    # Create two worker processes.
    pool = multiprocessing.Pool(2)

    # Use Pool.apply method to run the task using pool of processes
    #mylist = [pool.apply(get_result, args=(num,)) for num in numbers]

    # Use Pool.map method to run the task using the pool of processes.
    #mylist = pool.map(func=get_result, iterable=numbers)

    # Use Pool.apply_async method to run the tasks
    results = [pool.apply_async(get_result, args=(num,))
               for num in numbers]

    # The elements of results list are instances of Pool.ApplyResult.
    # Use the object's get() method to get the final values.
    mylist = [p.get() for p in results]

    # Optionally You can also use generator expression instead of
    # list comprehension. It could be marginally slower,
    # but for bigger problem size will consume much less memory

    # Stop the worker processes
    pool.close()
    # Join the processes
    pool.join()
    print("Output:", mylist)
