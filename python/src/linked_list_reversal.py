class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        temp = self
        s = ""
        while temp is not None:
            s += str(temp.value) + " "
            temp = temp.next
        return s.rstrip()

def reverse(head: Node) -> Node:
    
    prev, curr = None, head

    while curr is not None:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

    return prev

def reverse_sublist(head: Node, p: int, q: int) -> Node:
    """ p and q are one-indexed """

    """ REVIEW """
    
    if p == q:
        return head
    
    i = 0
    curr, prev = head, None

    while head is not None and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1

    last_part_1 = prev
    last_middle = curr

    i, next  = 0, None
    while curr is not None and i < q - p + 1:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1

    last_part_1.next = prev
    last_middle.next = next

    return head

def reverse_k_element_sublists(head: Node, k: int) -> Node:
    ...