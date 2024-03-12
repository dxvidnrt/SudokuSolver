import Sudoku
import SudokuInput


def main():
    sudoku = SudokuInput.load_sudoku('ExampleSudokus/sudoku.txt')
    solved_board = Sudoku.solve_board_depth(sudoku)
    solved_board.print_board()

if __name__ == "__main__":
    main()
