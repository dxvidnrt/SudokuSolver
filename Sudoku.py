from typing import *


class SudokuBoard:
    def __init__(self, board=None):
        if board is None:
            # Initialize an empty board
            self.board = [['x' for _ in range(9)] for _ in range(9)]
        else:
            self.board = board
            for row in range(9):
                for col in range(9):
                    if self.board[row][col] == 'x':
                        self.board[row][col] = NumberHolder()

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

    def is_solved(self):
        for row in range(9):
            for col in range(9):
                if isinstance(self.board[row][col], NumberHolder):
                    return False
        return True

    def solve(self):
        changed = True
        while not self.is_solved() and changed:
            if not changed:
                print("Could not solve sudoku any further")
                return
            changed = False
            self.print_board()
            for row in range(9):
                for col in range(9):
                    field = self.board[row][col]
                    if isinstance(field, NumberHolder):
                        continue
                    if self.denote(row, col, field):
                        changed = True
        print("The board is solved:")
        self.print_board()

    def denote(self, row, col, num):
        # Check the row
        changed = False
        for i in range(9):
            if i != col and isinstance(self.board[row][i], NumberHolder):
                place_holder: NumberHolder = self.board[row][i]
                if place_holder.remove_number(num):
                    changed = True
                number: int = place_holder.is_defined()
                if number:
                    self.board[row][i] = number

        # Check the column
        for j in range(9):
            if j != row and isinstance(self.board[j][col], NumberHolder):
                place_holder: NumberHolder = self.board[j][col]
                if place_holder.remove_number(num):
                    changed = True
                number: int = place_holder.is_defined()
                if number:
                    self.board[j][col] = number

        # Check the box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if i == row and j == col:
                    continue
                if isinstance(self.board[i][j], NumberHolder):
                    place_holder: NumberHolder = self.board[i][j]
                    if place_holder.remove_number(num):
                        changed = True
                    number: int = place_holder.is_defined()
                    if number:
                        self.board[i][j] = number

        return changed

class NumberHolder:
    def __init__(self, numbers):
        if numbers is None:
            self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.numbers = numbers

    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __str__(self):
        return 'x'

    def remove_number(self, number: int) -> bool:
        try:
            self.numbers.remove(number)
            return True  # Number was successfully removed
        except ValueError:
            return False  # Number was not found, hence not removed

    def is_defined(self):
        if len(self.numbers) == 1:
            return self.numbers[0]
        return 0

