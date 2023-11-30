import heapq

class Node:
    def _init_(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def _lt_(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar_search(start, goal, neighbors_fn, heuristic_fn):
    open_set = [Node(start, None, 0, heuristic_fn(start))]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor in neighbors_fn(current_node.state):
            if neighbor in closed_set:
                continue

            cost = current_node.cost + 1  # Assuming a constant cost for each step
            heuristic = heuristic_fn(neighbor)
            new_node = Node(neighbor, current_node, cost, heuristic)

            if new_node not in open_set:
                heapq.heappush(open_set, new_node)

    return None  # If no path is found

# Example usage:
# Define a simple grid as a 2D list
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

def neighbors(state):
    x, y = state
    possible_moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return [(nx, ny) for nx, ny in possible_moves if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0]

def heuristic(state):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

path = astar_search(start, goal, neighbors, heuristic)

if path:
    print("A* Path found:", path)
else:
    print("No path found.")
