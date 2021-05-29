"""Unit tests for primes.
"""
from mathematics.sequences import Primes
from parameterized import parameterized

import unittest

class TestPrimes(unittest.TestCase):
    def setUp(self):
        Primes.reset()

    @parameterized.expand([
        (2, True),
        (3, True),
        (4, False),
        (10, False),
        (97, True),
    ])
    def test_contains(self, number, is_prime):
        """Test __contains__ function.
        """
        self.assertEqual(is_prime, number in Primes)

    @parameterized.expand([
        (0, 2),
        (1, 3),
        (2, 5),
        (3, 7),
        (4, 11),
    ])
    def test_get_item(self, index, expected_prime):
        """Test __getitem__ function.
        """
        self.assertEqual(expected_prime, Primes(index))

    @parameterized.expand([
        ((0, 10), [2, 3, 5, 7]),
        ((10, 20), [11, 13, 17, 19]),
    ])
    def test_range(self, range, expected_primes):
        """Test range function.
        """
        self.assertListEqual(expected_primes, list(Primes(*range)))