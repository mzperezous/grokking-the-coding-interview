from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left, self.right, self.next = None, None, None

    def level_connected_string(self):
        s = ""
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                s += f"{current.value} "
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
        return s.rstrip()

    def full_connection_string(self):
        current = self
        s = ""
        while current:
            s += f"{current.value} "
            current = current.next

        return s.rstrip()

def level_order_traverse(root: TreeNode) -> List[List[int]]:
    
    queue = deque()
    queue.append(root)

    result = []
    
    while queue:
        level, level_size = [], len(queue)

        for _ in range(level_size):
            curr = queue.popleft()
            level.append(curr.value)

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

        result.append(level)

    return result

def reverse_level_order_traversal(root: TreeNode) -> List[List[int]]:

    queue = deque()
    result = deque()
    queue.append(root)

    while queue:
        level, level_size = [], len(queue)

        for _ in range(level_size):
            curr = queue.popleft()
            level.append(curr.value)

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

        result.appendleft(level)

    return list(result)

def zigzag_level_traversal(root: TreeNode) -> List[List[int]]:

    queue = deque()
    result = []

    queue.append(root)
    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            current_node = queue.popleft()

            if left_to_right:
                current_level.append(current_node.value)
            else:
                current_level.appendleft(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        result.append(list(current_level))
        left_to_right = not left_to_right

    return list(result)

def binary_tree_level_averages(root: TreeNode) -> List[int]:
    result = []

    queue = deque()
    queue.append([root])

    while queue:
        level_list = queue.popleft()
        level_sum, level_size = 0, len(level_list)
        next_level = []

        for node in level_list:
            level_sum += node.value
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.append(level_sum / level_size)

        if next_level:
            queue.append(next_level)

    return result

def minimum_depth_of_binary_tree(root: TreeNode) -> int:
    depth = 0

    queue = deque()
    queue.append(root)
    
    while queue:
        level_size = len(queue)

        depth += 1

        for _ in range(level_size):
            node = queue.popleft()

            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def level_order_successor(root: TreeNode, key: int) -> int | None:
    queue = deque()
    queue.append(root)

    found = False

    while queue:
        node = queue.popleft()

        if found:
            return node.value

        if node.value == key:
            found = True

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return None


def connect_level_order_siblings(root: TreeNode) -> None:
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        prev = None
        for _ in range(level_size):
            node = queue.popleft()
            if prev:
                prev.next = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            prev = node

        node.next = None

    return

def connect_all_level_order_siblings(root: TreeNode) -> None:
    queue = deque()
    queue.append(root)

    node, prev = None, None
    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            if prev:
                prev.next = node
            
            prev = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    if node:
        node.next = None  # Unnecessary but illustrates algo w/o data structure init

    return

def binary_tree_right_view(root: TreeNode) -> List[int]:
    queue = deque()
    queue.append(root)

    result = []

    while queue:
        level_size = len(queue)

        node = None
        for _ in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if node:
            result.append(node.value)

    return result