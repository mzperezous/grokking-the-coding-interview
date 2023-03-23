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