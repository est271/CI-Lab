"""Unittest for the prime_ef function"""

import unittest
import sys

sys.path.append('..')

from prime_ef import find_prime

class PrimeTest(unittest.TestCase):
    """Input test for find_prime function"""

    def test_is_int(self):
        """This method will test if the input is an integer"""

        with self.assertRaises(TypeError):
            find_prime("str")

        with self.assertRaises(TypeError):
            find_prime(10.101)

        with self.assertRaises(TypeError):
            find_prime(True)
            
        self.assertEqual(find_prime(2),0)
        
        self.assertEqual(find_prime(12),0)

    def test_lessthan_one(self):
        """Test if the value inserted is less than or equal to 1"""

        with self.assertRaises(ValueError):
            find_prime(0)

        with self.assertRaises(ValueError):
            find_prime(-10)
