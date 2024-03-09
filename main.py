import Sudoku
import SudokuInput


def main():
    sudoku = SudokuInput.get_sudoku()
    sudoku.solve()

if __name__ == "__main__":
    main()
