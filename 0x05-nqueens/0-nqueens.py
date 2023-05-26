#!/usr/bin/python3
import sys


def init_board(n):
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def board_deepcopy(board):
    return [row.copy() for row in board]


def get_solution(board):
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    n = len(board)
    for c in range(n):
        if board[row][c] == ' ':
            board[row][c] = 'x'
    for r in range(n):
        if board[r][col] == ' ':
            board[r][col] = 'x'
    for i in range(n):
        if row - i >= 0 and col - i >= 0:
            if board[row - i][col - i] == ' ':
                board[row - i][col - i] = 'x'
        if row + i < n and col + i < n:
            if board[row + i][col + i] == ' ':
                board[row + i][col + i] = 'x'
    for i in range(n):
        if row - i >= 0 and col + i < n:
            if board[row - i][col + i] == ' ':
                board[row - i][col + i] = 'x'
        if row + i < n and col - i >= 0:
            if board[row + i][col - i] == ' ':
                board[row + i][col - i] = 'x'


def recursive_solve(board, row, queens, solutions):
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
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
