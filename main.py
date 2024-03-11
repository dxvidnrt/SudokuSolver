import Sudoku
import SudokuInput


def main():
    sudoku = SudokuInput.load_sudoku('ExampleSudokus/simple_soduko.txt')
    solved_board = Sudoku.solve_board_depth(sudoku)
    print(solved_board)

if __name__ == "__main__":
    main()
