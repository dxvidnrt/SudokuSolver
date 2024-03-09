from typing import *


class SudokuBoard:
    def __init__(self, board=None):
        if board is None:
            # Initialize an empty board
            self.board = [[0 for _ in range(9)] for _ in range(9)]
        else:
            self.board = board

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

    def solve(self):
        # Placeholder for a solving algorithm
        pass


class NumberHolder:
    def __init__(self, numbers):
        if numbers is None:
            self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.numbers = numbers

    def remove_numbers(self, number: int):
        try:
            self.numbers.remove(number)
        except ValueError:
            pass

    def remove_numbers(self, numbers: List[int]):
        for number in numbers:
            self.remove_numbers(number)

