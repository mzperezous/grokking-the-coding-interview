from unittest import TestCase
from src.island import (
    count_closed_islands,
    count_islands,
    flood_fill,
    island_perimeter,
    max_area_island,
    num_distinct_islands
)

class TestIsland(TestCase):

    def test_count_islands(self):
        self.assertEqual(count_islands([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]), 2)
        self.assertEqual(count_islands([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]), 1)
        
    def test_max_area_island(self):
        self.assertEqual(max_area_island([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]), 5)
        
    def test_flood_fill(self):
        self.assertEqual(
            flood_fill(
            [
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]
            ], 1, 3, 2),
            [
                [0, 2, 2, 2, 0],
                [0, 0, 0, 2, 2],
                [0, 2, 2, 2, 0],
                [0, 2, 2, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        )
        self.assertEqual(
            flood_fill(
            [
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 1, 1, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 1, 0, 0]
            ], 3, 2, 5),
            [
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0], 
                [0, 0, 5, 5, 0], 
                [0, 0, 5, 0, 0], 
                [0, 0, 5, 0, 0]
            ]
        )

    def test_count_closed_islands(self):
        self.assertEqual(count_closed_islands(
            [
                [1, 1, 0, 0, 0], 
                [0, 1, 0, 0, 0], 
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0], 
                [0, 0, 0, 0, 0]
            ]), 
        1)
        self.assertEqual(count_closed_islands(
            [
                [0, 0, 0, 0], 
                [0, 1, 0, 0], 
                [0, 1, 0, 0], 
                [0, 0, 1, 0], 
                [0, 0, 0, 0]
            ]), 
        2)

    def test_island_perimeter(self):
        self.assertEqual(island_perimeter(
            [
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]
            ]), 
        14)
        self.assertEqual(island_perimeter(
            [
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 0, 0]
            ]), 
        12)

    def test_num_distinct_islands(self):
        self.assertEqual(num_distinct_islands(
            [
                [1, 1, 0, 1, 1],
                [1, 1, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1],
                [0, 1, 1, 0, 1]
            ]),
        2)
        self.assertEqual(num_distinct_islands(
            [
                [1, 1, 0, 1],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 1, 0]
            ]),
        2)