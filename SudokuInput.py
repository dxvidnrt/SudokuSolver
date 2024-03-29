import Sudoku

def get_sudoku():
        print("Enter your Sudoku puzzle. Use numbers 1-9 for known values and 'x' for unknown values.")
        board = []
        for i in range(9):
            while True:
                row = input(f"Enter row {i + 1} (e.g., 5xx2x7xx4): ")
                if len(row) == 9 and all(c in "123456789x" for c in row):
                    board.append(['x' if c == 'x' else int(c) for c in row])
                    break
                else:
                    print(
                        "Invalid input. Each row must be exactly 9 characters long with numbers 1-9 or 'x' for unknowns.")

        sudoku = Sudoku.SudokuBoard(board)
        print("\nYour entered Sudoku puzzle is:")
        sudoku.print_board()
        return sudoku


def load_sudoku(filepath):
    board = []
    with open(filepath, 'r') as file:
        for line in file:
            row = line.strip()  # Remove any leading/trailing whitespace
            if len(row) == 9 and all(c in "123456789x" for c in row):
                board.append(['x' if c == 'x' else int(c) for c in row])
            else:
                raise ValueError(
                    "Invalid row in Sudoku file. Each row must be exactly 9 characters long with numbers 1-9 or 'x' for unknowns.")

    sudoku = Sudoku.SudokuBoard(board)
    print("\nLoaded Sudoku puzzle is:")
    sudoku.print_board()
    return sudoku
