# simple sudoku solver
import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

print("The question is: ")
print(np.matrix(grid))

def possible(row,column,number):
    global grid
    # for checking same number in row
    for i in range(0,9):
        if grid[row][i] == number:
            return False
    
    # for checking same number in column
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    
    # for checking same number in 3x3 square
    x = (column // 3) * 3
    y = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y+i][x+j] == number:
                return False