from unittest import TestCase
from src.sliding_window import (
    anagrams_in_string,
    fruits_into_baskets,
    length_of_longest_1s_after_k_substitutions,
    length_of_longest_substring_after_k_substitution,
    longest_substring_with_lte_k_distinct,
    max_sum_subarray,
    permutation_in_string,
    smallest_subarray_with_gte_sum,
    smallest_window_containing_substring
)

class TestSlidingWindow(TestCase):

    def test_max_sum_subarray(self):
        self.assertEqual(max_sum_subarray(3, [2, 1, 5, 1, 3, 2]), 9)
        self.assertEqual(max_sum_subarray(2, [2, 3, 4, 1, 5]), 7)

    def test_smallest_subarray_with_gte_sum(self):
        self.assertEqual(smallest_subarray_with_gte_sum(7, [2, 1, 5, 2, 3, 2]), 2)
        self.assertEqual(smallest_subarray_with_gte_sum(7, [2, 1, 5, 2, 8]), 1)
        self.assertEqual(smallest_subarray_with_gte_sum(8, [3, 4, 1, 1, 6]), 3)

    def test_longest_substring_with_lte_k_distinct(self):
        self.assertEqual(longest_substring_with_lte_k_distinct("araaci", 2), 4)
        self.assertEqual(longest_substring_with_lte_k_distinct("araaci", 1), 2)
        self.assertEqual(longest_substring_with_lte_k_distinct("cbbebi", 3), 5)

    def test_fruits_into_baskets(self):
        self.assertEqual(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']), 3)
        self.assertEqual(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']), 5)

    def test_length_of_longest_substring_after_k_substitution(self):
        self.assertEqual(length_of_longest_substring_after_k_substitution("aabccbb", 2), 5)
        self.assertEqual(length_of_longest_substring_after_k_substitution("abbcb", 1), 4)
        self.assertEqual(length_of_longest_substring_after_k_substitution("abccde", 1), 3)

    def test_length_of_longest_1s_after_k_substitutions(self):
        self.assertEqual(length_of_longest_1s_after_k_substitutions([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2), 6)
        self.assertEqual(length_of_longest_1s_after_k_substitutions([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3), 9)

    def test_permutation_in_string(self):
        self.assertEqual(permutation_in_string("oidbcaf", "ABC"), True)
        self.assertEqual(permutation_in_string("odicf", "dc"), False)
        self.assertEqual(permutation_in_string("bcdxabcdy", "bcdyabcdx"), True)
        self.assertEqual(permutation_in_string("aaacb", "abc"), True)

    def test_anagrams_in_string(self):
        self.assertEqual(anagrams_in_string("ppqp", "pq"), [1, 2])
        self.assertEqual(anagrams_in_string("abbcabc", "abc"), [2, 3, 4])
    
    def test_smallest_window_containing_substring(self):
        self.assertEqual(smallest_window_containing_substring("aabdec", "abc"), "abdec")