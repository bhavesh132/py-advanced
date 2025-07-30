def solvenQueen(n):
    """
    A function to solve the N-Queen problem using backtracking.

    Args:
    n (int): The size of the board.

    Returns:
    list: A list of lists, each containing a solution to the N-Queen problem represented as a 2D board.
    """
    col = set()   #This column is checked from prev row to exclude addition of queen to this particular column
    posDiag = set()  # (r+c) This condition rules out positive diagonals from repeating the queen placement
    negDiag = set()  # (r-c) This condition will check negitive diagonals so that no queen is placed in the same negitive diagonal next time

    board = [["." for i in range (n)] for j in range(n)] #This is the initial board with all . to represent empty spaces. We will place queens in this board
    res = [] #This will store all the solutions found

    def backtrack(r):
        if r == n:   #This is the solution condition, the backtracking has reached the last row without violating column positive Diagonal and negative diagonal conditions
            # Create a copy of the board to store the solution
            boardCopy = ["".join(row) for row in board]
            # Append the solution to the results
            res.append(boardCopy)
            # Exit the function as we have found a solution
            return

        for c in range(n):  #Iterate through columns
            if c in col or (r + c in posDiag) or (r - c in negDiag): #This condition checks if the queen can be placed in this column
                continue # If it cannot, continue to the next column
            
            col.add(c)  # Add the column to the set of used columns
            posDiag.add(r + c) # Add the positive diagonal to the set of used diagonals
            negDiag.add(r - c) # Add the negative diagonal to the set of used diagonals
            board[r][c] = "Q" # Place the queen on the board
            
            backtrack(r + 1) # Recursively call backtrack for the next row

            col.remove(c) # Remove the column from the set of used columns
            posDiag.remove(r + c) # Remove the positive diagonal from the set of used diagonals
            negDiag.remove(r - c)   # Remove the negative diagonal from the set of used diagonals
            board[r][c] = "." # Remove the queen from the board

    backtrack(0) # Start the backtracking from the first row
    return res # Return the list of solutions


print(solvenQueen(8))