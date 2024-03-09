import Sudoku
import SudokuInput


def main():
    sudoku = SudokuInput.load_sudoku('ExampleSudokus/sudoku.txt')
    sudoku.solve()

if __name__ == "__main__":
    main()
