from numpy import *
import sys

class Sudoku:
    def __init__(self):
        self.tabla = array(
        [
        [[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]
        ])
    def sudoku_show(self):
        for l in range(len(self.tabla[0])):
            for j in range(len(self.tabla[0])):
                for i in range(len(self.tabla[0])):
                    for k in range(len(self.tabla[0][0])):
                        sys.stdout.write(str(self.tabla[i + l*3][j][k]) + " ")
                    if(i != 2):
                        sys.stdout.write("| ")
                print ""
            if(l != 2):
                print("----------------------")

sudoku = Sudoku()
sudoku.sudoku_show()

#
# 1 2 3   1 2 3   1 2 3
# 4 5 6   4 5 6   4 5 6
# 7 8 9   7 8 9   7 8 9
#
# 1 2 3   1 2 3   1 2 3
# 4 5 6   4 5 6   4 5 6
# 7 8 9   7 8 9   7 8 9
#
# 1 2 3   1 2 3   1 2 3
# 4 5 6   4 5 6   4 5 6
# 7 8 9   7 8 9   7 8 9
