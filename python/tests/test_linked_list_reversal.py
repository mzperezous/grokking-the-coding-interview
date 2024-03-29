from unittest import TestCase
from src.linked_list_reversal import (
    Node,
    reverse,
    reverse_alternate_k_elements,
    reverse_k_element_sublists,
    reverse_sublist,
    rotate_linked_list
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

    def test_reverse_sublist(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        reverse_sublist(head, 2, 4)

        self.assertEqual(str(head), "1 4 3 2 5")

    def test_reverse_k_element_sublists(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = Node(7)
        head.next.next.next.next.next.next.next = Node(8)

        head = reverse_k_element_sublists(head, 3)
        self.assertEqual(str(head), "3 2 1 6 5 4 8 7")

    def test_rotate_linked_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)

        head = rotate_linked_list(head, 3)
        self.assertEqual(str(head), "4 5 6 1 2 3")

    def test_reverse_alternate_k_elements(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = Node(7)
        head.next.next.next.next.next.next.next = Node(8)

        head = reverse_alternate_k_elements(head, 2)
        self.assertEqual(str(head), "2 1 3 4 6 5 7 8")