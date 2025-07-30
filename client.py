# Show diagonals for position (row, col)
def show_diagonals(n, row, col):
    board = [["." for _ in range(n)] for _ in range(n)]

    board[row][col] = "Q"

    # Mark left diagonals
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        board[i][j] = "/"
        i -= 1
        j -= 1

    # Mark right diagonals
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        board[i][j] = "\\"
        i -= 1
        j += 1

    print(f"Queen placed at ({row}, {col})")
    for r in board:
        print(" ".join(r))

show_diagonals(4, 2, 1)
