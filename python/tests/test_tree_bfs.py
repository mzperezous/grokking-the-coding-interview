from unittest import TestCase
from src.tree_bfs import (
    level_order_traverse,
    TreeNode
)


class TestTreeBFS(TestCase):
    
    def test_level_order_traverse(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        
        levels = level_order_traverse(root)
        self.assertEqual(levels, [[12], [7, 1], [9, 10, 5]])

        