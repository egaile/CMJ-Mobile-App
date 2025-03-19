#!/usr/bin/env python
"""
This contains basic unit tests for main.py. This is executed every time we
deploy to Bitbucket.

Created by: David Tran

"""

# Adding comment
# Import Python libraries.
import unittest
import sys

# Import our library. Specifically we are removing the namespace associated to 
# the file. This makes calling said functions easier.
from main import addition, subtraction, multiplication, division, database_connect


# Check Version Number
#
# This matters for division in Python.
# Reference: https://www.python.org/dev/peps/pep-0238/
python_verison = sys.version_info[0]


class MainTester(unittest.TestCase):
    """
    This is the generic unit test class in Python to test our main script.

    References:
    https://docs.python.org/2.7/library/unittest.html
    https://docs.python.org/3.7/library/unittest.html

    """


    def setUp(self):
         """ 
         This provides initial setup on each test case we run. We don't have 
         any in our case but it is good to know if every test method has to have 
         the same setup. Thus this removes redundant boilerplate setup code 
         that would be shared across all the tests.

         """


         # This tells Python there is a blank command (NO OP).
         # This is needed else this will be an invalid method with no 
         # operations.
         pass


    def test_addition(self):
        """
        This tests the addition function against known correct values.

        """


        self.assertEqual(addition(3, 5), 8)
        self.assertEqual(addition(-3, 5), 2)
        self.assertEqual(addition(3, -5), -2)
        self.assertEqual(addition(-3, -5), -8)

        self.assertEqual(addition(0, -0), 0)
        self.assertEqual(addition(0, -1), -1)
        self.assertEqual(addition(-1, 0), -1)


    def test_subtraction(self):
        """
        This tests the subtraction function against known correct values.

        """


        self.assertEqual(subtraction(3, 5), -2)
        self.assertEqual(subtraction(-3, 5), -8)
        self.assertEqual(subtraction(3, -5), 8)
        self.assertEqual(subtraction(-3, -5), 2)

        self.assertEqual(subtraction(0, -0), 0)
        self.assertEqual(subtraction(0, -1), 1)
        self.assertEqual(subtraction(-1, 0), -1)


    def test_multiplication(self):
        """
        This tests the multiplication function against known correct values.

        """


        self.assertEqual(multiplication(3, 5), 15)
        self.assertEqual(multiplication(-3, 5), -15)
        self.assertEqual(multiplication(3, -5), -15)
        self.assertEqual(multiplication(-3, -5), 15)

        self.assertEqual(multiplication(0, -0), 0)
        self.assertEqual(multiplication(0, -1), 0)
        self.assertEqual(multiplication(-1, 0), 0)


    def test_division(self):
        """
        This tests the division function against known correct values.

        Note:
            Due to a PEP talk, link below, division can have multiple meanings 
            depending on the version in question. We do not know exactly how
            division executes on version 1.X but assume it preforms similar 
            actions to version 2.X.

            Reference: https://www.python.org/dev/peps/pep-0238/

        """


        if python_verison <= 2:


          self.assertEqual(division(3, 5), 0)
          self.assertEqual(division(-3, 5), -1)
          self.assertEqual(division(3, -5), -1)
          self.assertEqual(division(-3, -5), 0)

          self.assertRaises(ZeroDivisionError, division, 0, -0)
          self.assertEqual(division(0, -1), 0)
          self.assertRaises(ZeroDivisionError, division, -1, 0)


        elif python_verison >= 3:


          self.assertEqual(division(3, 5), 0.6)
          self.assertEqual(division(-3, 5), -0.6)
          self.assertEqual(division(3, -5), -0.6)
          self.assertEqual(division(-3, -5), 0.6)

          self.assertRaises(ZeroDivisionError, division, 0, -0)
          self.assertEqual(division(0, -1), 0)
          self.assertRaises(ZeroDivisionError, division, -1, 0)


    def test_database(self):
        """
        This tests the database connection.

        """


        client = database_connect()

        # Connects to the database called test.
        db = client.test

        # Grabs the collection called Test, or creates it if it does not exist.
        collection = db.Test


# Executes the test if called directly, rather than being imported.
if __name__ == '__main__':
    unittest.main()


