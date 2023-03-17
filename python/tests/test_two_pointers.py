from unittest import TestCase
from src.two_pointers import (
    pair_with_target_sum, 
    remove_duplicates,
    square_sorted,
    triplet_sum_closest_to_target,
    triplet_sum_to_zero,
    triplets_with_smaller_sum
)

class TestTwoPointers(TestCase):
    """ DesignGurus test case checks for two pointers module
    """

    def test_pair_with_target_sum(self):
        self.assertEqual(pair_with_target_sum([1, 2, 3, 4, 6], 6), [1, 3])
        self.assertEqual(pair_with_target_sum([2, 5, 9, 11], 11), [0, 2])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([2, 3, 3, 3, 6, 9, 9]), 4)
        self.assertEqual(remove_duplicates([2, 2, 2, 11]), 2)

    def test_square_sorted(self):
        self.assertEqual(square_sorted([-2, -1, 0, 2, 3]), [0, 1, 4, 4, 9])
        self.assertEqual(square_sorted([-3, -1, 0, 1, 2]), [0, 1, 1, 4, 9])

    def test_triplet_sum_to_zero(self):
        self.assertEqual(triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]), [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])
        self.assertEqual(triplet_sum_to_zero([-5, 2, -1, -2, 3]), [[-5, 2, 3], [-2, -1, 3]])

    def test_triplet_sum_closest_to_target(self):
        self.assertEqual(triplet_sum_closest_to_target([-1, 0, 2, 3], 3), 2)
        self.assertEqual(triplet_sum_closest_to_target([-3, -1, 1, 2], 1), 0)
        self.assertEqual(triplet_sum_closest_to_target([1, 0, 1, 1], 100), 3)
        self.assertEqual(triplet_sum_closest_to_target([0, 0, 1, 1, 2, 6], 5), 4)
    
    def test_triplets_with_smaller_sum(self):
        self.assertEqual(triplets_with_smaller_sum([-1, 0, 2, 3], 3), 2)
        self.assertEqual(triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5), 4)
