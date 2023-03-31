from unittest import TestCase
from src.tree_dfs import (
    has_sum_path,
    TreeNode
)

class TestTreeDFS(TestCase):
    
    def test_has_sum_path(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        self.assertEqual(has_sum_path(root, 10), True)
        self.assertEqual(has_sum_path(root, 12), False)

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        self.assertEqual(has_sum_path(root, 23), True)
        self.assertEqual(has_sum_path(root, 16), False)
