#!/usr/bin/python3
"""
N queens: The N Queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""
import sys

def is_safe(board, row, col, n):
    # Check if it is safe to place a queen at board[row][col]
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(col):
        # Base case: If all queens are placed, add the solution
        if col == n:
            solutions.append([''.join(row) for row in board])
            return

        # Try placing a queen in each row of the current column
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'

    backtrack(0)

    return solutions

if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a valid integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)

    # Print the solutions
    for solution in solutions:
        print('\n'.join(solution))
        print()
