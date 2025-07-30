def is_safe (board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs (r- row):
            return False
    return True

def solve_n_queen(n):
    stack = []
    row= 0
    col = 0
    solutions = []
    while True:
        while col < n:
            if is_safe(stack,row,col):
                stack.append(col)
                row += 1
                col = 0
                break
            else:
                col + 1
            
        if row == n or col == n:
            if row == n:
                print("Solution found:", stack)
                solutions.append(stack[:])
            if not stack:
                break
            col = stack.pop() + 1
            row -= 1
        
    return solutions

def print_solution(solutions, n):
    for sol in solutions:
        for row in sol:
            print("".join('Q' if i == row else '.' for i in range(n)))
        print("\n" + "-" * n + "\n")


n = 8
solutions = solve_n_queen(n)
print_solution(solutions, n)