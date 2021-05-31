"""Unit tests for number operations.
"""
from mathematics.numbers import Binomial
from parameterized import parameterized

import unittest

class TestBinomial(unittest.TestCase):
    def setUp(self):
        Binomial.reset()

    @parameterized.expand([
        (0, 0, 1),
        (2, 1, 2),
        (5, 2, 10),
    ])
    def test_get_value(self, n, k, expected_value):
        self.assertEqual(expected_value, Binomial(n, k))

    @parameterized.expand([
        (0, [1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
    ])
    def test_get_level(self, level, expected_values):
        self.assertListEqual(expected_values, Binomial(level))