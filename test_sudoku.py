import unittest
from Sudoku import Sudoku

class TestSudoku(unittest.TestCase):

    def test_Sudoku_Ingresar_Fila_1(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.ingresar_numero(0, 2, 5))

    def test_Sudoku_Ingresar_Fila_2(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.ingresar_numero(6, 4, 6))

    def test_Sudoku_Ingresar_Fila_3(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.ingresar_numero(3, 1, 8))

    def test_Sudoku_Ingresar_Fila_4(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.ingresar_numero(1, 2, 6))


    def test_Sudoku_Ingresar_Columna_1(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.ingresar_numero(8, 0, 5))

    def test_Sudoku_Ingresar_Columna_2(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.ingresar_numero(0, 8, 9))

    def test_Sudoku_Ingresar_Columna_3(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.ingresar_numero(6, 4, 6))

    def test_Sudoku_Ingresar_Columna_4(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.ingresar_numero(2, 0, 5))

    def test_Sudoku_Ingresar_Zona(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.ingresar_numero(2, 2, 5))

    def test_Sudoku_Perdio(self):

        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],

                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],

                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],

                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],

                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],

                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],

                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],

                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],

                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])

        self.assertFalse(sudoku.gano())   

    def test_Sudoku_Gano(self):

        sudoku = Sudoku([["4", "1", "3", "8", "2", "5", "6", "7", "9"],

                         ["5", "6", "7", "1", "4", "9", "8", "3", "2"],

                         ["2", "8", "9", "7", "3", "6", "1", "4", "5"],

                         ["1", "9", "5", "4", "6", "2", "7", "8", "3"],

                         ["7", "2", "6", "9", "8", "3", "5", "1", "4"],

                         ["3", "4", "8", "5", "1", "7", "2", "9", "6"],

                         ["8", "5", "1", "6", "9", "4", "3", "2", "7"],

                         ["9", "7", "2", "3", "5", "8", "4", "6", "1"],

                         ["6", "3", "4", "2", "7", "1", "9", "5", "8"]])

        self.assertTrue(sudoku.gano())    


if __name__ == '__main__':    
    unittest.main()

