from typing import List

""" Provided data structures """

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        string = ""
        while temp is not None:
            print(str(temp.value) + " ", end='')
            string += str(temp.value) + " "
            temp = temp.next
        print()
        return string.rstrip()

"""                          """

def has_cycle(head: Node) -> bool:
    """ Post submission-notes: You can just go 1 and 2 steps and they'll still eventually reach. See solution """

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


def find_cycle_start(head: Node) -> Node:
    """ Assume there is a cycle. """
    from collections import defaultdict, Counter

    slow, fast = head, head
    pointers = defaultdict(set)

    while fast is not None and fast.next is not None:

            pointers[fast.next.next.value].add(fast.next.value)
            fast = fast.next.next
            pointers[slow.next.value].add(slow.value)
            slow = slow.next
            if slow.value == fast.value:
                # Edge case: head is cycle start
                double_pointers = list(filter(lambda node_to_pointers: len(node_to_pointers[1]) > 1, list(pointers.items())))
                if len(list(double_pointers)) == 0:
                    return head
                
                # Now that we have the value, find the node from the start
                curr = head
                while curr.value != double_pointers[0][0]:
                    curr = curr.next
                return curr
                
def is_magic_number(num: int) -> bool:
    
    sum_digits_squared = lambda number: sum(digit ** 2 for digit in map(int, str(number)))

    node = Node(sum_digits_squared(num))
    pointer = node

    while node.value != 1:
        node.next = Node(sum_digits_squared(node.value))
        node.next.next = Node(sum_digits_squared(node.next.value))
        node = node.next.next
        pointer = pointer.next

        # Found cycle
        if node.value == pointer.value and node.value != 1:
            return False

    return True


def middle_of_linked_list(head: Node) -> Node:
    p1 = head
    p2 = head


    while p1 is not None and p1.next is not None:
        p1 = p1.next.next
        p2 = p2.next

    return p2
    

def is_palindrome_linked_list(head: Node) -> bool:
    """ Review this one """

    def reverse(head: Node):
        previous = None
        while head is not None:
            nxt = head.next
            head.next = previous
            previous = head
            head = nxt

        return previous
    
    fast, slow = head, head

    # Find middle
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    reversed_second_half = reverse(slow)

    copy = reversed_second_half

    while head is not None and reversed_second_half is not None:
        if head.value != reversed_second_half.value:
            reverse(copy)
            return False
        
        head = head.next
        reversed_second_half = reversed_second_half.next

    reverse(copy)
    return True

def reorder(head: Node) -> None:
    middle, end = head, head

    def reverse(head: Node):
        previous = None
        while head is not None:
            nxt = head.next
            head.next = previous
            previous = head
            head = nxt

        return previous

    # Find middle
    while end is not None and end.next is not None:
        end = end.next.next
        middle = middle.next
    
    head_first_half = head
    head_second_half = reverse(middle)

    while head_first_half is not None and head_second_half is not None:
        tmp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = tmp

        tmp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = tmp 

    if head_first_half is not None:
        head_first_half.next = None


def cycle_in_circular_array(nums: List[int]) -> bool:

    slow, fast = 0, 0
    length = len(nums)
    first_iteration = True

    while first_iteration or slow != fast:
        first_iteration = False

        slow = (slow + nums[slow]) % length
        fast = (fast + nums[fast]) % length
        fast = (fast + nums[fast]) % length

    is_positive = nums[slow] > 0
    initial = slow
    first_iteration = True

    while first_iteration or slow != initial:
        slow = (slow + nums[slow]) % length

        # One element cycle != cycle
        if first_iteration and slow == initial:
            return False

        if is_positive and nums[slow] < 0:
            return False
        elif not is_positive and nums[slow] > 0:
            return False
        
        first_iteration = False
        
    return True
