from itertools import permutations

def is_valid(puzzle, solution):
    # Check if the solution satisfies the puzzle
    for equation in puzzle:
        if sum(solution[c] * 10 ** i for i, c in enumerate(equation[:-1][::-1])) != solution[equation[-1]]:
            return False
    return True

def solve_cryptarithmetic(puzzle):
    # Extract unique letters from the puzzle
    unique_letters = set("".join(puzzle))
    
    # Generate all possible permutations of digits for unique letters
    for perm in permutations(range(10), len(unique_letters)):
        solution = dict(zip(unique_letters, perm))
        
        # Check if the current permutation is valid
        if is_valid(puzzle, solution):
            return solution
    
    return None

if __name__ == "__main__":
    # Example cryptarithmetic puzzle: SEND + MORE = MONEY
    puzzle = ["SEND", "MORE", "MONEY"]

    solution = solve_cryptarithmetic(puzzle)

    if solution:
        print("Solution found:")
        for word in puzzle:
            print(f"{word}: {''.join(str(solution[c]) for c in word)}")
    else:
        print("No solution found.")
