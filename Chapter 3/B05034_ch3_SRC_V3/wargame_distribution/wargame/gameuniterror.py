"""wargame.gameuniterror

Shows how to create a custom exception class for the Attack of the Orcs game

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

The use of this module is illustrated in Chapter 2, exception handling.

RUNNING THE PROGRAM:
--------------------
This is NOT run as a standalone program. See `wargame/attackoftheorcs.py`

# --------------------------------------------------------------------------
# Alternate implementation where you subclass the custom exception,
# GameUniError. The following code would eliminate the need of
# maintaining an error_dict object in GameUnitError. See the chapter for
# further details.
# --------------------------------------------------------------------------
# class GameUnitError(Exception):
#     def __init__(self, message=''):
#         super().__init__(message)
#         self.padding = '~'*50 + '\n'
#         self.error_message = " Unspecified Error!"
#
# class HealthMeterException(GameUnitError):
#     def __init__(self, message=''):
#         super().__init__(message)
#         self.error_message = (self.padding +
#                              "ERROR: Health Meter Problem" +
#                              '\n' + self.padding )
#
# class AttackException(GameUnitError):
#     # Code similar to that of HealthMeterException .
#     pass

.. seealso:: `wargame/attackoftheorcs.py`

.. todo::

   The code comments and function descriptions in this file are
   intentionally kept to a minimum! See Chapter 4 of the book to
   learn about the code documentation and best practices!

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

class GameUnitError(Exception):
    """Custom exceptions class for the `AbstractGameUnit` and its subclasses"""
    def __init__(self, message='', code=000):
        super().__init__(message)
        self.error_message = '~'*50 + '\n'

        # Alternative approach is to subclass GameUnitError
        self.error_dict = {
            000: "ERROR-000: Unspecified Error!",
            101: "ERROR-101: Health Meter Problem!",
            102: "ERROR-102: Attack issue! Ignored",
        }
        try:
            self.error_message += self.error_dict[code]
        except KeyError:
            self.error_message += self.error_dict[000]
        self.error_message += '\n' + '~'*50

