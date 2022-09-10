import math
import numpy as np
import time
import sudoku_puzzle_generator as puzzle_generator

GRID_SIZE = 9


def checkIfAvaliable(num, index, arr):

    row, column = index

    # checking the row and column
    for i in range(GRID_SIZE):
        if (arr[row, i] == num or arr[i, column] == num):
            return False

    # checking the 3x3 square
    sqRow = math.floor(row / 3)
    sqClmn = math.floor(column / 3)

    for i in range(sqRow * 3, (sqRow + 1) * 3):
        for j in range(sqClmn * 3, (sqClmn + 1) * 3):
            if (arr[i, j] == num):
                return False
    return True


def solver(puzzle):

    modifiedCoords = []

    arr = puzzle
    kStartValue = 1

    # until a correct solution has been found
    i, j = 0, 0
    while (i < GRID_SIZE):
        while (j < GRID_SIZE):
            found = False
            if (arr[i, j] == 0):
                for k in range(kStartValue, 10):
                    if (checkIfAvaliable(k, [i, j], arr)):
                        arr[i, j] = k
                        modifiedCoords.append([i, j])
                        found = True
                        break

                # no appropriate numbers found
                kStartValue = 1
                if (not found):
                    i, j = modifiedCoords[-1]
                    kStartValue = arr[i, j] + 1
                    arr[i, j] = 0
                    j -= 1
                    modifiedCoords.pop()

            j += 1

        i += 1
        j = 0

    return arr


def main():

    time1 = time.monotonic()
    puzzle1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    puzzle2 = [[0, 0, 0, 7, 1, 0, 5, 0, 0],
               [7, 0, 2, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 9, 0, 1, 8, 0],
               [0, 4, 0, 0, 0, 6, 0, 9, 0],
               [9, 0, 0, 0, 0, 0, 0, 5, 0],
               [3, 0, 7, 0, 0, 4, 0, 0, 0],
               [0, 6, 0, 0, 0, 0, 0, 0, 2],
               [0, 0, 0, 8, 7, 0, 0, 0, 0],
               [5, 0, 8, 0, 0, 0, 0, 0, 3]]

    solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    puzzle = np.array(puzzle2)
    print(solver(puzzle))
    time2 = time.monotonic()

    print(time2 - time1)


if (__name__ == '__main__'):
    main()
