import heapq

class Node:
    def __init__(self, position, cost, heuristic):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0

    def heuristic(x, y):
        return abs(x - goal[0]) + abs(y - goal[1])

    start_node = Node(start, 0, heuristic(*start))
    priority_queue = [start_node]
    visited = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        x, y = current_node.position
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_node = Node((new_x, new_y), current_node.cost + 1, heuristic(new_x, new_y))
                new_node.parent = current_node
                heapq.heappush(priority_queue, new_node)

    return None  # No path found

if __name__ == "__main__":
    # Example usage:
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start_point = (0, 0)
    end_point = (4, 4)

    path = astar(grid, start_point, end_point)

    if path:
        print(f"A* Path from {start_point} to {end_point}: {path}")
    else:
        print("No path found.")
