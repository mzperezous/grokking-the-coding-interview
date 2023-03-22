from unittest import TestCase
from src.merge_intervals import (
    Interval,
    merge
)

class TestMergeIntervals(TestCase):
    
    def test_merge(self):
        self.assertEqual(list(map(str, merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))), ["[1, 5]", "[7, 9]"])
        self.assertEqual(list(map(str, merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]))), ["[2, 4]", "[5, 9]"])