from unittest import TestCase
from warmup import contains_duplicates


class TestWarmupExercises(TestCase):
    """ Tests ../warmup.py functions with test cases provided by Design Gurus.
    """

    def test_contains_duplicates(self):
        has_dups = [1, 2, 3, 1]
        no_dups = [3, 9, 1, 2]

        self.assertEqual(contains_duplicates(has_dups), False)
        self.assertEqual(contains_duplicates(no_dups), False)
