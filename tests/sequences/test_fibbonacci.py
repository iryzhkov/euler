"""Unit tests for primes.
"""
from mathematics.sequences import Fibbonacci
from parameterized import parameterized

import unittest

class TestFibbonacci(unittest.TestCase):
    def setUp(self):
        Fibbonacci.reset()

    @parameterized.expand([
        (0, True),
        (1, True),
        (2, True),
        (3, True),
        (4, False),
    ])
    def test_contains(self, number, is_prime):
        """Test __contains__ function.
        """
        self.assertEqual(is_prime, number in Fibbonacci)

    @parameterized.expand([
        (0, 0),
        (1, 1),
        (3, 2),
        (5, 5),
        (6, 8),
    ])
    def test_get_item(self, index, expected_prime):
        """Test __getitem__ function.
        """
        self.assertEqual(expected_prime, Fibbonacci(index))

    @parameterized.expand([
        ((0, 10), [0, 1, 1, 2, 3, 5, 8]),
        ((10, 22), [13, 21]),
    ])
    def test_range(self, range, expected_primes):
        """Test range function.
        """
        self.assertListEqual(expected_primes, list(Fibbonacci(*range)))