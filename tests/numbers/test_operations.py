"""Unit tests for number operations.
"""
from mathematics.numbers import isqrt
from parameterized import parameterized

import unittest

class TestNumberOperations(unittest.TestCase):
    @parameterized.expand([
        (2, 1),
        (9, 3),
        (20, 4),
    ])
    def test_isqrt(self, value, expected_value):
        """Test binary search function.
        """
        self.assertEqual(expected_value, isqrt(value))