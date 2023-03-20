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
            

def max_area_island(matrix: List[List[int]]) -> int:
    
    max_area = -1

    def visit_node_dfs(location: Tuple[int, int], matrix: List[List[int]]):
        x, y = location[0], location[1]

        if y < 0 or y == len(matrix) or x < 0 or x >= len(matrix[y]) or matrix[y][x] == 0:
            return 0
        
        matrix[y][x] = 0  # Mark as visited
        area = 1

        area += visit_node_dfs((x + 1, y), matrix)
        area += visit_node_dfs((x, y + 1), matrix)
        area += visit_node_dfs((x - 1, y), matrix)
        area += visit_node_dfs((x, y - 1), matrix)

        return area
    
    max_area = -1
    
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 1:
                max_area = max(visit_node_dfs((i, j), matrix), max_area)

    return max_area
