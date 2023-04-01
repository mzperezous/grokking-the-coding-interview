from unittest import TestCase
from src.two_heaps import (
    MedianOfAStream
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
