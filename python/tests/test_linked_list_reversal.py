from unittest import TestCase
from src.linked_list_reversal import (
    Node,
    reverse
)

class TestLLReversal(TestCase):

    def test_reverse(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(8)
        head.next.next.next.next = Node(10)

        reversed = reverse(head)

        self.assertEqual(str(reversed), "10 8 6 4 2")

        original = reverse(reversed)
        
        self.assertEqual(str(original), "2 4 6 8 10")