from typing import List, Set, Tuple

def count_islands(matrix: List[List[int]]) -> int:
    
    seen: Set[Tuple[int, int]] = set()
    islands = 0

    def search_from_node_dfs(curr: Tuple[int, int], matrix: List[List[int]], seen: Set[Tuple[int, int]]) -> None:
        i, j = curr[0], curr[1]
        
        if (i, j) in seen:
            return
        
        seen.add((i, j))

        # Don't recurse unless it's a one
        if matrix[j][i] == 0:
            return
        
        if j > 0:
            search_from_node_dfs((i, j - 1), matrix, seen)  # Above
        if i > 0:
            search_from_node_dfs((i - 1, j), matrix, seen)  # Left
        if j < len(matrix) - 1:
            search_from_node_dfs((i, j + 1), matrix, seen)  # Below
        if i < len(matrix[j]) - 1:
            search_from_node_dfs((i + 1, j), matrix, seen)  # Right


    for j, row in enumerate(matrix):
        i = 0

        while i < len(row):
            if matrix[j][i] == 0:
                i += 1
                seen.add((i, j))
            else:
                if (i, j) not in seen:
                    islands += 1
                    search_from_node_dfs((i, j), matrix, seen)
                i += 1

    return islands
            