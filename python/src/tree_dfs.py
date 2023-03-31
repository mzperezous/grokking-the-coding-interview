class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_sum_path(root: TreeNode, goal: int) -> bool:
    
    def sum_dfs(node: TreeNode, curr_sum: int) -> bool:
        if node.val + curr_sum == goal and not node.left and not node.right:
            return True
        
        elif node.val + curr_sum < goal:
            if node.left and sum_dfs(node.left, node.val + curr_sum):
                return True
            if node.right and sum_dfs(node.right, node.val + curr_sum):
                return True

        return False

    return sum_dfs(root, 0)