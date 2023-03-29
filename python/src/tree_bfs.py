from collections import deque
from typing import List

class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left, self.right = None, None

def level_order_traverse(root: TreeNode) -> List[int]:
    
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