from unittest import TestCase
from src.fast_slow_pointers import (
    find_cycle_start,
    has_cycle,
    is_magic_number,
    middle_of_linked_list,
    Node
)

class TestFastSlowPointers(TestCase):

    def test_has_cycle(self):
        # List with cycle
        n1_cycle = Node(1)
        n1_cycle.next = Node(2)
        n1_cycle.next.next = Node(3)
        n1_cycle.next.next.next = Node(4)
        n1_cycle.next.next.next.next = n1_cycle

        # List without cycle
        n2_cycle = Node(1)
        n2_cycle.next = Node(2)
        n2_cycle.next.next = Node(3)
        n2_cycle.next.next.next = Node(4)
        n2_cycle.next.next.next.next = Node(5)
        n2_cycle.next.next.next.next.next = Node(6)

        self.assertEqual(has_cycle(n1_cycle), True)
        self.assertEqual(has_cycle(n2_cycle), False)

    def test_find_cycle_start(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)

        head.next.next.next.next.next.next = head.next.next
        self.assertEqual(find_cycle_start(head).value, 3)

        head.next.next.next.next.next.next = head.next.next.next
        self.assertEqual(find_cycle_start(head).value, 4)

        head.next.next.next.next.next.next = head
        self.assertEqual(find_cycle_start(head).value, 1)

    def test_is_magic_number(self):
        self.assertEqual(is_magic_number(23), True)
        self.assertEqual(is_magic_number(12), False)

    def test_middle_of_linked_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        self.assertEqual(middle_of_linked_list(head).value, 3)

        head.next.next.next.next.next = Node(6)
        self.assertEqual(middle_of_linked_list(head).value, 4)

        head.next.next.next.next.next.next = Node(7)
        self.assertEqual(middle_of_linked_list(head).value, 4)
