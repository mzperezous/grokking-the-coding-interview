from unittest import TestCase
from src.warmup import (
    contains_duplicates,
    is_palindrome,
    is_panagram,
    reverse_vowels,
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

    def test_reverse_vowels(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("DesignGurus"), "DusugnGires")
        self.assertEqual(reverse_vowels("AEIOU"), "UOIEA")
        self.assertEqual(reverse_vowels("aA"), "Aa")
        self.assertEqual(reverse_vowels(""), "")

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal, Panama!"), True)
        self.assertEqual(is_palindrome("race a car"), False)
        self.assertEqual(is_palindrome("Was it a car or a cat I saw?"), True)
        self.assertEqual(is_palindrome("Madam, in Eden, I'm Adam."), True)
        self.assertEqual(is_palindrome("''"), True)
