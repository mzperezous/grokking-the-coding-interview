from typing import List, Set, Tuple


"""  Refactors  """
def is_valid(x: int, y: int, matrix: List[List[int]]) -> bool:
        if x < 0 or y < 0 or y >= len(matrix) or x >= len(matrix[y]):
            return False
        return True
"""             """



def count_islands(matrix: List[List[int]]) -> int:
    
    seen: Set[Tuple[int, int]] = set()
    islands = 0

    def search_from_node_dfs(curr: Tuple[int, int], matrix: List[List[int]], seen: Set[Tuple[int, int]]) -> None:
        i, j = curr[0], curr[1]
        if not is_valid(i, j, matrix) or (i, j) in seen:
            return
        
        seen.add((i, j))

        # Don't recurse unless it's a one
        if matrix[j][i] == 0:
            return
        
        search_from_node_dfs((i, j - 1), matrix, seen)  # Above
        search_from_node_dfs((i - 1, j), matrix, seen)  # Left
        search_from_node_dfs((i, j + 1), matrix, seen)  # Below
        search_from_node_dfs((i + 1, j), matrix, seen)  # Right


    for j, row in enumerate(matrix):
        for i, val in enumerate(row):
            if val == 0:
                seen.add((i, j))
            else:
                if (i, j) not in seen:
                    islands += 1
                    search_from_node_dfs((i, j), matrix, seen)

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

def flood_fill(matrix: List[List[int]], x_start: int, y_start: int, new_color: int) -> List[List[int]]:
    from collections import deque

    if matrix[y_start][x_start] != 1:
        return matrix

    visited = set()
    to_visit = deque([(x_start, y_start)])

    while len(to_visit) > 0:
        current = to_visit.pop()
        x, y = current[0], current[1]

        if not is_valid(x, y, matrix):
            continue
        
        if matrix[y][x] == 1 and current not in visited:
            matrix[y][x] = new_color

            visited.add(current)
            to_visit.append((x + 1, y))
            to_visit.append((x, y + 1))
            to_visit.append((x - 1, y))
            to_visit.append((x, y - 1))

    return matrix
            

def count_closed_islands(matrix: List[List[int]]):

    def traverse_island_dfs(x: int, y: int, matrix: List[List[int]]) -> bool:
        # If we got to an out of bounds node, it means we came from an edge island node -> not closed
        if not is_valid(x, y, matrix):
            return False
        
        if matrix[y][x] == 0:
            return True
        
        matrix[y][x] = 0
        
        left = traverse_island_dfs(x - 1, y, matrix)
        right = traverse_island_dfs(x + 1, y, matrix)
        top = traverse_island_dfs(x, y + 1, matrix)
        bottom = traverse_island_dfs(x, y - 1, matrix)

        return left and right and top and bottom
    
    closed = 0

    for y, row in enumerate(matrix):
        for x, val in enumerate(row):
            if val == 1 and traverse_island_dfs(x, y, matrix):
                closed += 1

    return closed

""" Challenge problems """

def island_perimeter(matrix: List[List[int]]) -> int:
    """ Assumption: Matrix has a single island. """

    from collections import deque

    i = None
    j = None
    # Find the start of the island
    for column, row in enumerate(matrix):
        for tmp_i, val in enumerate(row):
            if val == 1:
                i = tmp_i
                j = column

    sides = 0
    visited = set()
    to_visit = deque([(i, j)])

    while len(to_visit) > 0:
        curr = to_visit.pop()
        visited.add(curr)
        x, y = curr[0], curr[1]

        # Left
        if x > 0:
            if matrix[y][x - 1] == 0:
                sides += 1
            elif (x - 1, y) not in visited:
                to_visit.appendleft((x - 1, y))
        else:
            sides += 1
        # Top
        if y > 0:
            if matrix[y - 1][x] == 0:
                sides += 1
            elif (x, y - 1) not in visited:
                to_visit.appendleft((x, y - 1))
        else:
            sides += 1

        # Right
        if x < len(matrix[y]) - 1:
            if matrix[y][x + 1] == 0:
                sides += 1
            elif (x + 1, y) not in visited:
                to_visit.appendleft((x + 1, y))
        else:
            sides += 1

        # Bottom
        if y < len(matrix) - 1:
            if matrix[y + 1][x] == 0:
                sides += 1
            elif (x, y + 1) not in visited:
                to_visit.appendleft((x, y + 1))
        else:
            sides += 1


    return sides

def num_distinct_islands(matrix: List[List[int]]) -> int:
    """ An island is distinct if they can be translated to equal one another """

    """ Post-submission notes: Check out why traversal strings are wrong """

    islands = set()

    def traverse_island_dfs_with_direction(matrix: List[List[int]], x: int, y: int, matrix_s: str = "", direction: str | None  = None) -> str:
        if not is_valid(x, y, matrix):
            return ""
        
        if matrix[y][x] == 0:
            return ""
        
        # Add traversal record (except on first call)
        if direction is not None:
            matrix_s += direction

        matrix[y][x] = 0
        matrix_s += traverse_island_dfs_with_direction(matrix, x + 1, y, matrix_s, "E")
        matrix_s += traverse_island_dfs_with_direction(matrix, x, y - 1, matrix_s, "N")
        matrix_s += traverse_island_dfs_with_direction(matrix, x, y + 1, matrix_s, "S")
        matrix_s += traverse_island_dfs_with_direction(matrix, x - 1, y, matrix_s, "W")

        return matrix_s
        
    for j, row in enumerate(matrix):
        for i, val in enumerate(row):
            if val == 1:
                island = traverse_island_dfs_with_direction(matrix, i, j)
                islands.add(island)

    return len(islands)
