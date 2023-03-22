from unittest import TestCase
from src.merge_intervals import (
    employee_free_time,
    has_conflicting_appointments,
    insert,
    intersection,
    Interval,
    Job,
    max_cpu_load,
    Meeting,
    merge,
    minimum_meeting_rooms
)

class TestMergeIntervals(TestCase):
    
    def test_merge(self):
        self.assertEqual(list(map(str, merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))), ["[1, 5]", "[7, 9]"])
        self.assertEqual(list(map(str, merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]))), ["[2, 4]", "[5, 9]"])

    def test_insert(self):
        self.assertEqual(list(map(str, insert([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6)))), ["[1, 3]", "[4, 7]", "[8, 12]"])
        self.assertEqual(list(map(str, insert([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10)))), ["[1, 3]", "[4, 12]"])
        self.assertEqual(list(map(str, insert([Interval(2, 3), Interval(5, 7)], Interval(1, 4)))), ["[1, 4]", "[5, 7]"])
    
    def test_intersection(self):
        self.assertEqual(list(map(str, intersection(
            [Interval(1, 3), Interval(5, 6), Interval(7, 9)], 
            [Interval(2, 3), Interval(5, 7)])
        )), ["[2, 3]", "[5, 6]", "[7, 7]"])
        self.assertEqual(list(map(str, intersection(
            [Interval(1, 3), Interval(5, 7), Interval(9, 12)], 
            [Interval(5, 10)])
        )), ["[5, 7]", "[9, 10]"])

    def test_has_conflicting_appointments(self):
        self.assertEqual(has_conflicting_appointments([Interval(1, 4), Interval(2, 5), Interval(7, 9)]), True)
        self.assertEqual(has_conflicting_appointments([Interval(6, 7), Interval(2, 4), Interval(8, 12)]), False)
        self.assertEqual(has_conflicting_appointments([Interval(4, 5), Interval(2, 3), Interval(3, 6)]), True)

    def test_minimum_meeting_rooms(self):
        self.assertEqual(minimum_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]), 2)
        self.assertEqual(minimum_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]), 1)
        self.assertEqual(minimum_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]), 2)
        self.assertEqual(minimum_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]), 2)

    def test_max_cpu_load(self):
        self.assertEqual(max_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]), 7)
        self.assertEqual(max_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)]), 15)
        self.assertEqual(max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]), 8)

    def test_employee_free_time(self):
        self.assertEqual(
            list(map(str, employee_free_time([[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(5, 6)]]))),
            ["[3, 5]"]
        )
        self.assertEqual(
            list(map(str, employee_free_time([[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]))),
            ["[4, 6]", "[8, 9]"]
        )
        self.assertEqual(
            list(map(str, employee_free_time([[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]))),
            ["[5, 7]"]
        )
