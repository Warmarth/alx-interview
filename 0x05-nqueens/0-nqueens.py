"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
"""
import sys
import copy

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return copy.deepcopy(board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution

def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    r = row + 1
    c = col + 1
    while r < len(board) and c < len(board):
        board[r][c] = "x"
        r += 1
        c += 1
    # X out all spots diagonally up to the left
    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        board[r][c] = "x"
        r -= 1
        c -= 1
    # X out all spots diagonally up to the right
    r = row - 1
    c = col + 1
    while r >= 0 and c < len(board):
        board[r][c] = "x"
        r -= 1
        c += 1
    # X out all spots diagonally down to the left
    r = row + 1
    c = col - 1
    while r < len(board) and c >= 0:
        board[r][c] = "x"
        r += 1
        c -= 1



def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for solved in solutions:
        print(solved)
