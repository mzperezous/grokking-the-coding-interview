from collections import deque
from typing import List

class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left, self.right = None, None

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