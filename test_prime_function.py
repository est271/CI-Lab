"""Unittest for the prime_ef function"""

import unittest
from prime_ef import find_prime

class PrimeTest(unittest.TestCase):
    """Input test for find_prime function"""

    def test_not_int(self):
        """This method will test if the input is an integer"""

        with self.assertRaises(TypeError):
            find_prime("str")

        with self.assertRaises(TypeError):
            find_prime(10.101)

        with self.assertRaises(TypeError):
            find_prime(True)

    def test_lessthan_one(self):
        """Test if the value inserted is less than or equal to 1"""

        with self.assertRaises(ValueError):
            find_prime(0)

        with self.assertRaises(ValueError):
            find_prime(-10)

if __name__ == '__main__':
    unittest.main()
