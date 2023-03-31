from typing import List

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

def all_paths_for_sum(root: TreeNode, goal: int) -> List[List[int]]:
    
    result = []

    def check_path(node: TreeNode, curr_sum: int, curr_path: List[int]) -> None:
        if node is None:
            return
        
        path = curr_path + [node.val]

        if node.val + curr_sum == goal:
            result.append(path)

        elif goal > curr_sum + node.val:
            check_path(node.left, curr_sum + node.val, path)
            check_path(node.right, curr_sum + node.val, path)

        return

    check_path(root, 0, [])

    return result

def sum_of_path_numbers(root: TreeNode):
    """ 
    Post-submission: 
        Track via integers to save space by multiplying curr_path by 10 
    """
    paths = []

    def get_paths(node: TreeNode, curr_path: str = "") -> None:
        if node is None:
            return

        if node.left is None and node.right is None:
            paths.append(curr_path + str(node.val))

        get_paths(node.left, curr_path + str(node.val))
        get_paths(node.right, curr_path + str(node.val))

    get_paths(root)
        
    return sum(map(lambda x: int(x), paths))


def has_path_with_given_sequence(root: TreeNode, sequence: List[int]) -> bool:
    
    def check_path(node: TreeNode, curr_path: List[int]) -> bool:
        if node is None:
            return False

        curr_path.append(node.val)

        res = False
        if curr_path == sequence:
            res = True
        elif len(curr_path) < len(sequence):
            res = check_path(node.left, curr_path) or check_path(node.right, curr_path)

        del curr_path[-1]

        return res

    if [root.val] == sequence:
        return True
    
    return check_path(root, [])