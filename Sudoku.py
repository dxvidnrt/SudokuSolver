from typing import *


class SudokuBoardSimple:
    def __init__(self, board=None):
        if board is None:
            # Initialize an empty board
            self.board = [['x' for _ in range(9)] for _ in range(9)]
        else:
            self.board = board
            for row in range(9):
                for col in range(9):
                    if self.board[row][col] == 'x':
                        self.board[row][col] = 0

    def clear_field(self, row, col):
        print(f"clear row: {row}, col: {col}.")
        self.set_field(row, col, 0)

    def set_field(self, row, col, num):
        print(f"Set {num} in row: {row}, col: {col}.")
        self.board[row][col] = num

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

    def get_free_field(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        raise ValueError("Board is solved")

    def is_valid_move(self, row, col, num):
        # Check the row
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Check the column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check the box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def is_solved(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return False
        return True


def solve_board_depth(board: SudokuBoardSimple):
    # Check if the board is already solved
    if board.is_solved():
        return board

    # Find the first empty field
    free_field = board.get_free_field()
    if not free_field:
        return None  # No solution found (should not happen if the input is valid)
    row, col = free_field

    for num in range(1, 10):
        if board.is_valid_move(row, col, num):
            # Make a move
            board.set_field(row, col, num)

            # Continue solving the rest of the board
            if solve_board_depth(board):
                return board  # If solved, return the solved board

            # Undo the move (backtrack) if it leads to no solution
            board.clear_field(row, col)

    return None  # No valid number found for this field, need to backtrack
