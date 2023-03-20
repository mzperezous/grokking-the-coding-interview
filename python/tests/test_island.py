from unittest import TestCase
from src.island import (
    count_islands,
    max_area_island
)

class TestIsland(TestCase):

    def test_count_islands(self):
        self.assertEqual(count_islands([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]), 2)
        self.assertEqual(count_islands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 1)
        
    def test_max_area_island(self):
        self.assertEqual(max_area_island([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]), 5)
