"""Unit tests for number operations.
"""
from mathematics.numbers import isqrt
from mathematics.numbers.decompose import decompose_efficient, decompose_full
from parameterized import parameterized

import unittest

class TestNumberOperations(unittest.TestCase):
    @parameterized.expand([
        (2, 1),
        (9, 3),
        (20, 4),
    ])
    def test_isqrt(self, value, expected_value):
        """Test integer square root.
        """
        self.assertEqual(expected_value, isqrt(value))

    @parameterized.expand([
        (2, [], 2),
        (9, [0, 2], 1),
        (20, [2, 0], 5),
    ])
    def test_decompose_efficient(self, value, expected_decomposition, expected_reminder):
        """Test number decomposition.
        """
        decomposition, reminder = decompose_efficient(value)
        self.assertListEqual(expected_decomposition, decomposition)
        self.assertEqual(expected_reminder, reminder)

    @parameterized.expand([
        (2, [1]),
        (9, [0, 2, 0, 0]),
        (20, [2, 0, 1, 0, 0, 0, 0, 0]),
    ])
    def test_decompose_full(self, value, expected_decomposition):
        """Test number decomposition.
        """
        self.assertListEqual(expected_decomposition, decompose_full(value))