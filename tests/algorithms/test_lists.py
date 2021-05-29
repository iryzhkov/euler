"""Unit tests for lists algorithms.
"""
from mathematics.algorithms import binary_search
from parameterized import parameterized

import unittest

class TestListsAlgorithms(unittest.TestCase):
    @parameterized.expand([
        ([0, 1, 2, 4], 2, 2),
        ([0, 1, 2, 4], 4, 3),
        ([0, 1, 2, 4], 3, 3),
    ])
    def test_contains(self, array, value, expected_index):
        """Test binary search function.
        """
        self.assertEqual(expected_index, binary_search(array, value))