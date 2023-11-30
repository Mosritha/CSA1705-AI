import heapq
class State:
    def _init_(self, board, goal, parent=None, g=0, h=0):
        self.board = board  
        self.goal = goal  
        self.parent = parent 
        self.g = g  
        self.h = h 
    
    
    def _lt_(self, other):
        return (self.g + self.h) < (other.g + other.h)
def manhatten_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_position(board, number):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == number:
                return (i, j)
    
    return None


def generate_successors(state):
    successors = []
    move_directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] 
    
    zero_position = get_position(state.board, 0)  
    for move_direction in move_directions:
        neighbor_position = (zero_position[0] + move_direction[0], zero_position[1] + move_direction[1])
        if 0 <= neighbor_position[0] < len(state.board) and 0 <= neighbor_position[1] < len(state.board[neighbor_position[0]]):
            new_board = [row[:] for row in state.board]  
            new_board[zero_position[0]][zero_position[1]] = new_board[neighbor_position[0]][neighbor_position[1]]
            new_board[neighbor_position[0]][neighbor_position[1]] = 0
            
            successors.append(State(new_board, state.goal, state, state.g + 1, calculate_heuristic(new_board, state.goal)))
    
    return successors


def calculate_heuristic(board, goal):
    h = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != goal[i][j]:
                goal_position = get_position(goal, board[i][j])
                h += manhatten_distance((i, j), goal_position)
    
    return h


def reconstruct_path(state):
    path = []
    while state is not None:
        path.append(state.board)
        state = state.parent
    
    return path[::-1]

def solve_puzzle(initial, goal):
    open_list = []  # Priority queue to store the states
    closed_set = set()  # Set to store the visited states
    
    initial_state = State(initial, goal, None, 0, calculate_heuristic(initial, goal))
    heapq.heappush(open_list, initial_state)
    
    while open_list:
        current_state = heapq.heappop(open_list)
        
        if current_state.board == goal:
            return reconstruct_path(current_state)
        
        closed_set.add(tuple(map(tuple, current_state.board)))  
        
        successors = generate_successors(current_state)
        for successor in successors:
            if tuple(map(tuple, successor.board)) in closed_set:
                continue
            
            heapq.heappush(open_list, successor)
    
    return None


initial = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = solve_puzzle(initial, goal)
if solution:
    print("Solution:")
    for board in solution:
        for row in board:
            print(row)
        print()
else:
    print("No solution found.")
