from unittest import TestCase
from src.cyclic_sort import (
    cyclic_sort,
    find_missing_number
)


class TestCyclicSort(TestCase):

    def test_cyclic_sort(self):
        self.assertEqual(cyclic_sort([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(cyclic_sort([2, 6, 4, 3, 1, 5]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(cyclic_sort([1, 5, 6, 4, 3, 2]), [1, 2, 3, 4, 5, 6])

    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([4, 0, 3, 1]), 2)
        self.assertEqual(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]), 7)