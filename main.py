'''
    -SUDOKU SOLVER-

    Author: BranLight
    Date: 1/18/2021
    Functionality: 
        For any given valid Sudoku puzzle this
        program will solve it using a
        recursive, backtracking algorithm.
'''
import pprint


# Initial board pulled from www.websudoku.com
board = [
    [4, 3, 0, 0, 0, 2, 0, 8, 0],
    [1, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 9, 8, 0, 5, 0, 4, 0],
    [6, 4, 0, 3, 0, 0, 7, 0, 0],
    [0, 8, 2, 0, 0, 0, 6, 9, 0],
    [0, 0, 7, 0, 0, 4, 0, 3, 2],
    [0, 6, 0, 2, 0, 8, 4, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 1],
    [0, 2, 0, 1, 0, 0, 0, 7, 9]
]


def solve(board):
    if find_empty(board):
        row, col = find_empty(board)
        for num in range(1, 10):
            if valid_move(board, row, col, num):
                board[row][col] = num
                if solve(board):
                    return True
        board[row][col] = 0
    else:
        return True


# Check for empty positions
def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return False


# Check row, column and box for to see if num is valid
def valid_move(board, row, col, num):
    # Row check
    for i in range(9):
        if board[row][i] == num and i != col:
            return False

    # Col check
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # Box check
    r, c = [x//3*3 for x in (row, col)]

    for box_row in range(r, r+3):
        for col_row in range(c, c+3):
            if board[box_row][col_row] == num:
                return False
    return True


if __name__ == "__main__":
    solve(board)
    pprint.pprint(board)
