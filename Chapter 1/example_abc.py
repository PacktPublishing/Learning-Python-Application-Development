"""example_abc

A simple example that shows how to use Abstract Base Class in Python

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from abc import ABCMeta, abstractmethod

class AbstractGameUnit(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def info(self):
        pass

class Knight(AbstractGameUnit):
    def __init__(self):
        pass
    # def info(self):
    #     print("INFO: Knight")

if __name__ == "__main__":
    # Inherits from ABC
    k1 = Knight()
    k1.info()



# class GameUnit:
#     def __init__(self):
#         pass
#
#
#     def info(self):
#         print("INFO: GameUnit")
#
# class Knight(GameUnit):
#     def __init__(self):
#         pass
#     def info(self):
#         print("INFO: Knight")
#
# if __name__ == "__main__":
#     # inherits simple base class
#     k2 = Knight()
#     k2.info()




