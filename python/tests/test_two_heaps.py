from unittest import TestCase
from src.two_heaps import (
    MedianOfAStream,
    SlidingWindowMedian,
    SlidingWindowMedianSol
)


class TestTwoHeaps(TestCase):

    def test_median_of_a_stream(self):
        stream = MedianOfAStream()

        stream.insert_num(3)
        stream.insert_num(1)
        self.assertEqual(stream.find_median(), 2)

        stream.insert_num(5)
        self.assertEqual(stream.find_median(), 3)

        stream.insert_num(4)
        self.assertEqual(stream.find_median(), 3.5)

    def test_sliding_window_median(self):
        stream = SlidingWindowMedianSol()

        result = stream.find_sliding_window_median([1, 2, -1, 3, 5], 2)
        self.assertEqual(result, [1.5, 0.5, 1.0, 4.0])

        result = stream.find_sliding_window_median([1, 2, -1, 3, 5], 3)
        self.assertEqual(result, [1.0, 2.0, 3.0])
