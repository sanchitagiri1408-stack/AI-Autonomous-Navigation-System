"""A* path planning on a four-connected occupancy grid."""
from heapq import heappush, heappop

def manhattan(a, b):
    """Admissible heuristic for four-direction movement."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_path(grid, start, goal):
    """
    Return a list of (row, col) cells from start to goal, or [] if no route.
    grid[row][col] is True for a blocked cell and False for free space.
    """
    rows, cols = len(grid), len(grid[0])
    def valid(cell):
        r, c = cell
        return 0 <= r < rows and 0 <= c < cols and not grid[r][c]

    if not valid(start) or not valid(goal):
        return []
    frontier = []
    heappush(frontier, (manhattan(start, goal), 0, start))
    came_from = {}
    cost = {start: 0}
    visited = set()
    while frontier:
        _, current_cost, current = heappop(frontier)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return list(reversed(path))
        r, c = current
        for nxt in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
            if not valid(nxt):
                continue
            new_cost = cost[current] + 1
            if new_cost < cost.get(nxt, float("inf")):
                cost[nxt] = new_cost
                came_from[nxt] = current
                heappush(frontier, (new_cost + manhattan(nxt, goal), new_cost, nxt))
    return []
