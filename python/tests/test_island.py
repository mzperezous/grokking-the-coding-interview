from unittest import TestCase
from src.island import (
    count_islands
)

class TestIsland(TestCase):

    def test_count_islands(self):
        self.assertEqual(count_islands([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]), 2)
        self.assertEqual(count_islands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 1)
        