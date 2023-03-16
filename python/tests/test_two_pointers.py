from unittest import TestCase

from src.two_pointers import pair_with_target_sum

def TestTwoPointers(TestCase):
    """ DesignGurus test case checks for two pointers module
    """

    def test_pair_with_target_sum(self):
        self.assertEqual(pair_with_target_sum([1, 2, 3, 4, 6], 6), [1, 3])
        self.assertEqual(pair_with_target_sum([2, 5, 9, 11], 11), [0, 2])
