from unittest import TestCase
from src.sliding_window import (
    max_sum_subarray,
    smallest_subarray_with_gte_sum
)

class TestSlidingWindow(TestCase):

    def test_max_sum_subarray(self):
        self.assertEqual(max_sum_subarray(3, [2, 1, 5, 1, 3, 2]), 9)
        self.assertEqual(max_sum_subarray(2, [2, 3, 4, 1, 5]), 7)

    def test_smallest_subarray_with_gte_sum(self):
        self.assertEqual(smallest_subarray_with_gte_sum(7, [2, 1, 5, 2, 3, 2]), 2)
        self.assertEqual(smallest_subarray_with_gte_sum(7, [2, 1, 5, 2, 8]), 1)
        self.assertEqual(smallest_subarray_with_gte_sum(8, [3, 4, 1, 1, 6]), 3)