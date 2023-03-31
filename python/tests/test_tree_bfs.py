from unittest import TestCase
from src.tree_bfs import (
    level_order_traverse,
    reverse_level_order_traversal,
    TreeNode,
    zigzag_level_traversal
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

    def test_reverse_level_order_traversal(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        levels = reverse_level_order_traversal(root)
        self.assertEqual(levels, [[9, 10, 5], [7, 1], [12]])

    def test_zigzag_level_traversal(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(20)
        root.right.left.right = TreeNode(17)

        zigzag = zigzag_level_traversal(root)
        self.assertEqual(zigzag, [[12], [1, 7], [9, 10, 5], [17, 20]])

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        zigzag = zigzag_level_traversal(root)
        self.assertEqual(zigzag, [[1], [3, 2], [4, 5, 6, 7]])
    