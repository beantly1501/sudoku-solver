import sudoku_solver_backtracking as sudoku_solver
import numpy as np
import random

GRID_SIZE = 9

puzzles = []

puzzles.append(np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                         [6, 0, 0, 1, 9, 5, 0, 0, 0],
                         [0, 9, 8, 0, 0, 0, 0, 6, 0],
                         [8, 0, 0, 0, 6, 0, 0, 0, 3],
                         [4, 0, 0, 8, 0, 3, 0, 0, 1],
                         [7, 0, 0, 0, 2, 0, 0, 0, 6],
                         [0, 6, 0, 0, 0, 0, 2, 8, 0],
                         [0, 0, 0, 4, 1, 9, 0, 0, 5],
                         [0, 0, 0, 0, 8, 0, 0, 7, 9]]))

puzzles.append(np.array([[0, 0, 0, 7, 1, 0, 5, 0, 0],
                         [7, 0, 2, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 9, 0, 1, 8, 0],
                         [0, 4, 0, 0, 0, 6, 0, 9, 0],
                         [9, 0, 0, 0, 0, 0, 0, 5, 0],
                         [3, 0, 7, 0, 0, 4, 0, 0, 0],
                         [0, 6, 0, 0, 0, 0, 0, 0, 2],
                         [0, 0, 0, 8, 7, 0, 0, 0, 0],
                         [5, 0, 8, 0, 0, 0, 0, 0, 3]]))

puzzles.append(np.array([[2, 5, 0, 0, 3, 0, 9, 0, 1],
                         [0, 1, 0, 0, 0, 4, 0, 0, 0],
                         [4, 0, 7, 0, 0, 0, 2, 0, 8],
                         [0, 0, 5, 2, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 9, 8, 1, 0, 0],
                         [0, 4, 0, 0, 0, 3, 0, 0, 0],
                         [0, 0, 0, 3, 6, 0, 0, 7, 2],
                         [0, 7, 0, 0, 0, 0, 0, 0, 3],
                         [9, 0, 3, 0, 0, 0, 6, 0, 4]]))

puzzles.append(np.array([[7, 8, 0, 4, 0, 0, 1, 2, 0],
                         [6, 0, 0, 0, 7, 5, 0, 0, 9],
                         [0, 0, 0, 6, 0, 1, 0, 7, 8],
                         [0, 0, 7, 0, 4, 0, 2, 6, 0],
                         [0, 0, 1, 0, 5, 0, 9, 3, 0],
                         [9, 0, 4, 0, 6, 0, 0, 0, 5],
                         [0, 7, 0, 3, 0, 0, 0, 1, 2],
                         [1, 2, 0, 0, 0, 7, 4, 0, 0],
                         [0, 4, 9, 2, 0, 6, 0, 0, 7]]))

puzzles.append(np.array([[3, 0, 0, 8, 0, 0, 0, 0, 1],
                         [0, 0, 0, 0, 0, 2, 0, 0, 0],
                         [0, 4, 1, 5, 0, 0, 8, 3, 0],
                         [0, 2, 0, 0, 0, 1, 0, 0, 0],
                         [8, 5, 0, 4, 0, 3, 0, 1, 7],
                         [0, 0, 0, 7, 0, 0, 0, 2, 0],
                         [0, 8, 5, 0, 0, 9, 7, 4, 0],
                         [0, 0, 0, 1, 0, 0, 0, 0, 0],
                         [9, 0, 0, 0, 0, 7, 0, 0, 6]]))

puzzles.append(np.array([[0, 0, 0, 4, 0, 0, 0, 7, 5],
                         [0, 4, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 6, 8, 1, 0, 0, 0, 3],
                         [4, 0, 1, 7, 0, 0, 0, 6, 2],
                         [0, 0, 0, 6, 0, 4, 0, 0, 0],
                         [6, 2, 0, 0, 0, 1, 9, 0, 8],
                         [3, 0, 0, 0, 8, 7, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 3, 0],
                         [5, 1, 0, 0, 0, 2, 0, 0, 0]]))


def checkRandomness(pBefore, pAfter):

    counter = 0

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (pBefore[i, j] != pAfter[i, j]):
                counter += 1

    return counter


def randomizeGrid():
    puzzleBefore = puzzles[random.randint(0, len(puzzles) - 1)]

    # autopep8: off
    while(1):
        rndRows = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
        if (rndRows[0] != rndRows[1]):
            break


    while(1):
        rndColumns = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
        if (rndColumns[0] != rndColumns[1]):
            break

    puzzleAfter = np.copy(puzzleBefore)



    puzzleAfter[:, [rndColumns[0], rndColumns[1]]] = puzzleAfter[:, [rndColumns[1], rndColumns[0]]]
    puzzleAfter[[rndRows[0], rndRows[1]], :] = puzzleAfter[[rndRows[1], rndRows[0]], :]
    # autopep8: on

    return puzzleAfter
