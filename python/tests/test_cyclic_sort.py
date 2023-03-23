from unittest import TestCase
from src.cyclic_sort import (
    cyclic_sort,
    find_all_duplicates,
    find_all_missing_numbers,
    find_corrupt_pair,
    find_duplicate,
    find_k_missing_positive_numbers,
    find_missing_number,
    find_smallest_missing_positive_num
)


class TestCyclicSort(TestCase):

    def test_cyclic_sort(self):
        self.assertEqual(cyclic_sort([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(cyclic_sort([2, 6, 4, 3, 1, 5]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(cyclic_sort([1, 5, 6, 4, 3, 2]), [1, 2, 3, 4, 5, 6])

    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([4, 0, 3, 1]), 2)
        self.assertEqual(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]), 7)

    def test_find_all_missing_numbers(self):
        self.assertEqual(find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]), [4, 6, 7])
        self.assertEqual(find_all_missing_numbers([2, 4, 1, 2]), [3])
        self.assertEqual(find_all_missing_numbers([2, 3, 2, 1]), [4])

    def test_find_duplicate(self):
        self.assertEqual(find_duplicate([1, 4, 4, 3, 2]), 4)
        self.assertEqual(find_duplicate([2, 1, 3, 3, 5, 4]), 3)
        self.assertEqual(find_duplicate([2, 4, 1, 4, 4]), 4)
    
    def test_find_all_duplicates(self):
        self.assertCountEqual(find_all_duplicates([3, 4, 4, 5, 5]), [4, 5])
        self.assertCountEqual(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]), [3, 5])

    def test_find_corrupt_pair(self):
        self.assertEqual(find_corrupt_pair([3, 1, 2, 5, 2]), [2, 4])
        self.assertEqual(find_corrupt_pair([3, 1, 2, 3, 6, 4]), [3, 5])

    def test_find_smallest_missing_positive_num(self):
        self.assertEqual(find_smallest_missing_positive_num([-3, 1, 5, 4, 2]), 3)
        self.assertEqual(find_smallest_missing_positive_num([3, -2, 0, 1, 2]), 4)
        self.assertEqual(find_smallest_missing_positive_num([3, 2, 5, 1]), 4)
        self.assertEqual(find_smallest_missing_positive_num([33, 37, 5]), 1)

    def test_find_k_missing_positive_numbers(self):
        self.assertEqual(find_k_missing_positive_numbers([3, -1, 4, 5, 5], 3), [1, 2, 6])
        self.assertEqual(find_k_missing_positive_numbers([2, 3, 4], 3), [1, 5, 6])
        self.assertEqual(find_k_missing_positive_numbers([-2, -3, 4], 2), [1, 2])
