from unittest import TestCase
from src.merge_intervals import (
    insert,
    Interval,
    merge
)

class TestMergeIntervals(TestCase):
    
    def test_merge(self):
        self.assertEqual(list(map(str, merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))), ["[1, 5]", "[7, 9]"])
        self.assertEqual(list(map(str, merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]))), ["[2, 4]", "[5, 9]"])

    def test_insert(self):
        self.assertEqual(list(map(str, insert([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6)))), ["[1, 3]", "[4, 7]", "[8, 12]"])
        self.assertEqual(list(map(str, insert([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10)))), ["[1, 3]", "[4, 12]"])
        self.assertEqual(list(map(str, insert([Interval(2, 3), Interval(5, 7)], Interval(1, 4)))), ["[1, 4]", "[5, 7]"])