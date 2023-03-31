from unittest import TestCase
from src.tree_dfs import (
    all_paths_for_sum,
    has_sum_path,
    sum_of_path_numbers,
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

    def test_all_paths_for_sum(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(9)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(7)

        self.assertEqual(all_paths_for_sum(root, 12), [[1, 7, 4], [1, 9, 2]])

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        self.assertEqual(all_paths_for_sum(root, 23), [[12, 7, 4], [12, 1, 10]])

    def test_sum_of_path_numbers(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(9)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(9)

        self.assertEqual(sum_of_path_numbers(root), 408)

        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)

        self.assertEqual(sum_of_path_numbers(root), 332)