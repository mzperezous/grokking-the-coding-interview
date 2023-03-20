from unittest import TestCase
from src.fast_slow_pointers import (
    has_cycle,
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