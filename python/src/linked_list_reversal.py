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

    while curr is not None and i < p - 1:
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
    
    if k <= 1:
        return head
    curr, prev = head, None

    last_nodes_of_sublist = []
    first_nodes_of_sublist = []

    while curr is not None:
        i = 0

        last_nodes_of_sublist.append(curr)

        # Iterate over each sublist
        for i in range(k):
            if curr is None:
                break
            if curr.next is None or i == k - 1:
                first_nodes_of_sublist.append(curr)

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

    # Link all of the sublists
    for i, end_node in enumerate(last_nodes_of_sublist):
        if i == len(last_nodes_of_sublist) - 1:
            end_node.next = None
        else:
            end_node.next = first_nodes_of_sublist[i + 1]

    return first_nodes_of_sublist[0]


def rotate_linked_list(head: Node, k: int) -> Node:
    """ Rotate the list by k nodes """

    if head is None or head.next is None or k <= 0:
        return head

    # Find the length and last node
    list_length, last_node = 1, head
    while last_node.next is not None:
        list_length += 1
        last_node = last_node.next

    # Find last node of the sublist to be moved to the end
    last_node.next = head
    k %= list_length
    last_node_of_rotation = head
    for _ in range(list_length - k - 1):
        last_node_of_rotation = last_node_of_rotation.next
    
    head = last_node_of_rotation.next
    last_node_of_rotation.next = None
    return head
