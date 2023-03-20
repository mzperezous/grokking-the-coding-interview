from unittest import TestCase
from src.two_pointers import (
    backspace_compare,
    dutch_flag_problem,
    minimum_window_sort,
    pair_with_target_sum, 
    remove_duplicates,
    square_sorted,
    subarrays_product_less_than_target,
    triplet_sum_closest_to_target,
    triplet_sum_to_zero,
    triplets_with_smaller_sum,
    quad_sum_to_target
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

    def test_subarrays_product_less_than_target(self):
        self.assertEqual(
            subarrays_product_less_than_target([2, 5, 3, 10], 30),
            [[2], [2, 5], [5], [5, 3], [3], [10]]
        )
        self.assertEqual(
            subarrays_product_less_than_target([8, 2, 6, 5], 50),
            [[8], [8, 2], [2], [2, 6], [6], [6, 5], [5]]
        )

    def test_dutch_flag_problem(self):
        nums = [1, 0, 2, 1, 0]
        dutch_flag_problem(nums)
        self.assertEqual(nums, sorted(nums))
        nums = [2, 2, 0, 1, 2, 0]
        dutch_flag_problem(nums)
        self.assertEqual(nums, sorted(nums))

    def test_quad_sum_to_target(self):
        self.assertEqual(quad_sum_to_target([4, 1, 2, -1, 1, -3], 1), [[-3, -1, 1, 4], [-3, 1, 1, 2]])
        self.assertEqual(quad_sum_to_target([2, 0, -1, 1, -2, 2], 2), [[-2, 0, 2, 2], [-1, 0, 1, 2]])
    
    def test_backspace_compare(self):
        self.assertEqual(backspace_compare("xy#z", "xzz#"), True)
        self.assertEqual(backspace_compare("xy#z", "xyz#"), False)
        self.assertEqual(backspace_compare("xp#", "xyz##"), True)
        self.assertEqual(backspace_compare("xywrrmp", "xywrrmu#p"), True)

    def test_minimum_window_sort(self):
        self.assertEqual(minimum_window_sort([1, 2, 5, 3, 7, 10, 9, 12]), 5)
        self.assertEqual(minimum_window_sort([1, 3, 2, 0, -1, 7, 10]), 5)
        self.assertEqual(minimum_window_sort([1, 2, 3]), 0)
        self.assertEqual(minimum_window_sort([3, 2, 1]), 3)
