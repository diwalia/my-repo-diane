"""
Question 1
Use the Simple ATM program to write unit tests for your functions.
You are allowed to re-factor your function to ‘untangle’ some logic into smaller blocks of code to make it easier to write tests.
Try to write at least 5 unit tests in total covering various cases.

"""
import unittest
from T2Q1_ATM import pin_code
from T2Q1_ATM import menu_options


class TestATM(unittest.TestCase):

    def test_pin_attempt(self):
        attempt = 3
        result = T2Q1_ATM.pin_code(attempt)
        self.assertEqual(result, 3)

    def test_pin_int(self):
        self.assertEqual(pin_code(1111, 0000), 1234)

    def test_balance(self):
        result = balance(100)
        self.assertEqual(result, balance(100),None)

    def test_withdraw(self):
        result = withdraw(100)
        self.assertEqual(result, balance(100),None)

    def test_menu_as_number(self):
        with self.assertRaises(ValueError):
            menu_options([], )

if __name__ == '__main__':
    unittest.main()