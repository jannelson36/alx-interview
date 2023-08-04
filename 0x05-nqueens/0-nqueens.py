#!/usr/bin/python3
''' Python3 program to solve N Queen '''
import sys

def is_safe(board, row, col, N):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal - left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal - left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    def backtrack(board, col, N):
        if col == N:
            for i in range(N):
                print("".join(["Q" if board[i][j] == 1 else "." for j in range(N)]))
            print()
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 1
                backtrack(board, col + 1, N)
                board[i][col] = 0

    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    backtrack(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
