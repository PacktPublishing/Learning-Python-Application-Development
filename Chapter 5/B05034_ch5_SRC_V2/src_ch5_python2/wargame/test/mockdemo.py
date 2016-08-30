"""wargame.test.mockdemo

This module contains a demo for Mock class

This module is compatible with Python 2.7.9. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""

from __future__ import print_function
import unittest
from unittest.mock import Mock, call


class MyClassA:
    """Class for mock demo"""

    def foo(self):
        """Return a number.

        Used for illustrating use of Mock objects.
        """
        # Assume it does some lengthy computation here.
        # (not shown in this a trivial example)
        return 100

    def foo2(self, num):
        """Return a number.

        Used for illustrating use of Mock objects. similar to `foo()`.
        """
        # Assume it does some lengthy computation here.
        # (not shown in this a trivial example)
        return num + 200

    def compute(self):
        """Demonstrate use of mock objects"""
        x1 = self.foo()
        x2 = self.foo2(x1)
        print("x1 = %d, x2 = %d"%(x1, x2))
        result = x1 + x2
        print("In MyClassA.compute, result = x1 + x2 = ", result)
        return result


class TestA(unittest.TestCase):
    """Write test cases for methods from class MyClassA"""

    def test_compute(self):
        """Unit test for MyClassA.compute"""
        a = MyClassA()

        # Create a mock object and mock methods of MyClassA
        mockObj = Mock()
        a.foo = mockObj.foo
        a.foo2 = mockObj.foo2

        # Assuming you know the return values, set those for the mocks
        a.foo.return_value = 100
        a.foo2.return_value = 300

        # Run the computation. Calls to foo and foo2 in compute method are
        # now replaced with mock object calls that return the desired values
        result = a.compute()

        # Verify the results
        self.assertEqual(result, 400)

        # Get info on how the mock objects are actually called by compute.
        test_call_list = mockObj.mock_calls
        print("test_call_list =", test_call_list)

        # Compare it against some reference calling order
        reference_call_list = [call.foo(), call.foo2()]
        self.assertEqual(test_call_list, reference_call_list)

    def test_compute_with_patch(self):
        """Unit test for MyClassA.compute using mock.patch"""
        print("Running test_compute_with_patch...")
        with unittest.mock.patch('__main__.MyClassA.foo',
                                 new=Mock(return_value=500)):
            a = MyClassA()
            result = a.compute()

            # Verify the results. The test is expected to fail since we
            # are using a return value of 500 using MyClassA.foo!
            self.assertEqual(result, 400)

    def test_compute_with_patch_alternate(self):
        """Unit test for MyClassA.compute, using mock.patch

        .. note:: This uses `mock.patch` but does not use the `new` arg
        """
        print("Running test_compute_with_patch_alternate...")
        with unittest.mock.patch('__main__.MyClassA.foo') as foo_patch:
            foo_patch.return_value = 500
            a = MyClassA()
            result = a.compute()

            # Verify the results. The test is expected to fail since we
            # are using a return value of 500 using MyClassA.foo!
            self.assertEqual(result, 400)


if __name__== '__main__':
    unittest.main()


