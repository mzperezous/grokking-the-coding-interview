from unittest import TestCase
from src.warmup import (
    contains_duplicates,
    is_panagram,
    square_root
)


class TestWarmupExercises(TestCase):
    """ Tests ../warmup.py functions with test cases provided by Design Gurus.
    """

    def test_contains_duplicates(self):
        has_dups = [1, 2, 3, 1]
        no_dups = [3, 9, 1, 2]

        self.assertEqual(contains_duplicates(has_dups), True)
        self.assertEqual(contains_duplicates(no_dups), False)

    def test_is_panagram(self):
        panagram = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        not_panagram = "This is not a pangram"

        self.assertEqual(is_panagram(panagram), True)
        self.assertEqual(is_panagram(not_panagram), False)

    def test_square_root(self):
        # Edge cases
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(1), 1)

        self.assertEqual(square_root(5), 2)
        self.assertEqual(square_root(13), 3)
        self.assertEqual(square_root(66), 8)