import numpy as np
from threading import Thread
import random
import time

GRID_SIZE = 9

def simpleSolver(puzzle):
    arr = puzzle

    #until a correct solution has been found
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (arr[i,j] == 0):

                #randomly generating a number, 3 times
                for _ in range(3):
                    rnd = random.randint(1, 9)

                    if (checkIfAvaliable(rnd, [i, j], arr)):
                        arr[i, j] = rnd
                    
                    #if no numbers were found, restart the function

                return False

    return arr

        

        


def checkIfAvaliable(num, index, arr):

    row, column = index

    #checking the row and column
    for i in range(GRID_SIZE):
        if (arr[row, i] == num or arr[i, column] == num):
            return False

    #checking the square
    if (row <= 2):
        if (column <= 2):
            for i in range(0, 3):
                for j in range(0, 3):
                    if (arr[i, j] == num):
                        return False
        elif (column <= 5):
            for i in range(0, 3):
                for j in range(3, 6):
                    if (arr[i, j] == num):
                        return False

        else:
            for i in range(0, 3):
                for j in range(6, 9):
                    if (arr[i, j] == num):
                        return False

    elif (row <= 5):
        if (column <= 2):
            for i in range(3, 6):
                for j in range(0, 3):
                    if (arr[i, j] == num):
                        return False

        elif (column <= 5):
            for i in range(3, 6):
                for j in range(3, 6):
                    if (arr[i, j] == num):
                        return False

        else:
            for i in range(3, 6):
                for j in range(6, 9):
                    if (arr[i, j] == num):
                        return False

    else:
        if (column <= 2):
            for i in range(6, 9):
                for j in range(0, 3):
                    if (arr[i, j] == num):
                        return False

        elif (column <= 5):
            for i in range(6, 9):
                for j in range(3, 6):
                    if (arr[i, j] == num):
                        return False

        else:
            for i in range(6, 9):
                for j in range(6, 9):
                    if (arr[i, j] == num):
                        return False

    return True


globalResult = None
foundSolution = False

globalPuzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]


globalCounter = 0

def threadSolving():
    global globalResult, globalPuzzle, globalCounter, foundSolution

    puzzle = np.array(globalPuzzle)

    counter = 0

    while(1):
        result = simpleSolver(puzzle)

        if (foundSolution):
            break

        if (type(result) != bool):
            globalResult = result
            foundSolution = True
            break
        else:
            counter += 1
            if (counter % 100000 == 0):
                globalCounter += counter
                print(f"failed {globalCounter}")
                counter = 0






def main():

    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 0]]


    puzzle = np.array(puzzle)
    solution = np.array(solution)

    threads = []

    for _ in range(64):
        t = Thread(target=threadSolving)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(globalResult)


if (__name__ == '__main__'):
    main()
