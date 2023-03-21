from unittest import TestCase
from src.sliding_window import (
    max_sum_subarray
)

class TestSlidingWindow(TestCase):

    def test_max_sum_subarray(self):
        self.assertEqual(max_sum_subarray(3, [2, 1, 5, 1, 3, 2]), 9)
        self.assertEqual(max_sum_subarray(2, [2, 3, 4, 1, 5]), 7)