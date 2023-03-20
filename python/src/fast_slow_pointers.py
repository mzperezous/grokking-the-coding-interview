""" Provided data structures """

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

"""                          """

def has_cycle(head: Node):

    p1 = head
    p2 = head

    p2_pacer = 0
    
    while p1 != None:
        p1 = p1.next
        if p2_pacer != 0 and p2_pacer % 3 == 0:
            p2 = p2.next
        p2_pacer += 1
        if p1 == p2:
           return True
        
    return False
