import Sudoku
import SudokuInput
import sys


def main():
    user_mode = input("write \"load\" if you want to load a stored sudoku.\nwrite \"give\" if you want to input your "
                      "sudoku yourself.")
    if user_mode == "load":
        file_path = input("enter the file name of your sudoku stored in \"ExampleSudokus\"")
        if not file_path.endswith('.txt'):
            file_path += '.txt'
        sudoku = SudokuInput.load_sudoku(f'ExampleSudokus/{file_path}')
    elif user_mode == "give":
        sudoku = SudokuInput.get_sudoku()
    else:
        sys.exit("Could not read input.")

    solved_board = Sudoku.solve_board_depth(sudoku)
    if solved_board is None:
        print(f"Could not solve board\n{sudoku}")
    else:
        print("Solved board:")
        solved_board.print_board()


if __name__ == "__main__":
    main()
