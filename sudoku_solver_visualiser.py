from tkinter import *
import tkinter.font as font
import numpy as np
import sudoku_solver_backtracking as solver

GRID_WIDTH = 540
GRID_HEIGHT = 540
GRID_SIZE = 9


canvasNumbers = []
randomizeCounter = 0


def newPuzzle(c, puzzles, cFont):
    global canvasNumbers, randomizeCounter

    randomizeCounter += 1

    for n in canvasNumbers:
        c.delete(n)

    if (randomizeCounter % len(puzzles) == 0):
        randomizeCounter = 0
        grid = puzzles[randomizeCounter]
    else:
        grid = puzzles[randomizeCounter]

    canvasNumbers = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (grid[i, j] != 0):
                num = c.create_text((30 * (j + 1)) + (30 * j), (30 * (i + 1)) + (30 * i),
                                    text=grid[i, j], fill="black", font=cFont)
                canvasNumbers.append(num)


def startSolving(c, grid, cFont):
    global canvasNumbers
    print(canvasNumbers)

    solvedGrid = np.copy(grid)

    solvedGrid = solver.solver(solvedGrid)

    for n in canvasNumbers:
        c.delete(n)

    canvasNumbers = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (solvedGrid[i, j] != 0):
                num = c.create_text((30 * (j + 1)) + (30 * j), (30 * (i + 1)) + (30 * i),
                                    text=solvedGrid[i, j], fill="black", font=cFont)
                canvasNumbers.append(num)


def createWindow(puzzles):
    global canvasNumbers

    grid = puzzles[0]

    window = Tk()
    window.title("Sudoku Solving Visualiser")
    window.geometry("540x700")
    window.resizable(False, False)

    cFrame = Frame(window, width=540, height=540)
    cFrame.pack()

    # canvas with the sudoku grid
    c = Canvas(cFrame, height=GRID_HEIGHT, width=GRID_WIDTH, bg="white")
    c.pack(expand=False)

    c.delete("grid_line")

    # vertical lines
    counter = 0
    for i in range(0, GRID_WIDTH, 60):
        if (counter % 3 == 0):
            c.create_line([(i, 0), (i, GRID_HEIGHT)], tag="grid_line", width=4)
        else:
            c.create_line([(i, 0), (i, GRID_HEIGHT)], tag="grid_line", width=2)

        counter += 1

    # horizontal lines
    counter = 0
    for i in range(0, GRID_HEIGHT, 60):
        if (counter % 3 == 0):
            c.create_line([(0, i), (GRID_WIDTH, i)], tag="grid_line", width=4)
        else:
            c.create_line([(0, i), (GRID_WIDTH, i)], tag="grid_line", width=2)

        counter += 1

    cFont = font.Font(size=28)

    # displaying the numbers

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (grid[i, j] != 0):
                num = c.create_text((30 * (j + 1)) + (30 * j), (30 * (i + 1)) + (30 * i),
                                    text=grid[i, j], fill="black", font=cFont)
                canvasNumbers.append(num)

    ###################### button creation ################################
    # virutal image to change width and height to be in pixels
    pixelVirtual = PhotoImage(width=1, height=1)

    bFrame = Frame(window, width=540, height=160, bg="grey")
    bFrame.pack()

    bFont = font.Font(size=15)

    startB = Button(bFrame, text="Start Solving", width=120, height=50,
                    image=pixelVirtual, compound="c", command=lambda: startSolving(c, grid, cFont))
    startB.place(x=80, y=40)

    randomizeB = Button(bFrame, text="New Puzzle", width=120, height=50,
                        image=pixelVirtual, compound="c", command=lambda: newPuzzle(c, puzzles, cFont))
    randomizeB.place(x=320, y=40)

    startB["font"] = bFont
    randomizeB["font"] = bFont

    ##### FOR PRINTING MOUSE POS, FOR DEBUG ONLY ##########################
    # def motion(event):
    #     x, y = event.x, event.y
    #     print('{}, {}'.format(x, y))

    # window.bind('<Motion>', motion)

    window.mainloop()


def main():

    puzzle1 = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                        [6, 0, 0, 1, 9, 5, 0, 0, 0],
                        [0, 9, 8, 0, 0, 0, 0, 6, 0],
                        [8, 0, 0, 0, 6, 0, 0, 0, 3],
                        [4, 0, 0, 8, 0, 3, 0, 0, 1],
                        [7, 0, 0, 0, 2, 0, 0, 0, 6],
                        [0, 6, 0, 0, 0, 0, 2, 8, 0],
                        [0, 0, 0, 4, 1, 9, 0, 0, 5],
                        [0, 0, 0, 0, 8, 0, 0, 7, 9]])

    puzzle2 = np.array([[0, 0, 0, 7, 1, 0, 5, 0, 0],
                        [7, 0, 2, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 9, 0, 1, 8, 0],
                        [0, 4, 0, 0, 0, 6, 0, 9, 0],
                        [9, 0, 0, 0, 0, 0, 0, 5, 0],
                        [3, 0, 7, 0, 0, 4, 0, 0, 0],
                        [0, 6, 0, 0, 0, 0, 0, 0, 2],
                        [0, 0, 0, 8, 7, 0, 0, 0, 0],
                        [5, 0, 8, 0, 0, 0, 0, 0, 3]])

    puzzle3 = np.array([[2, 5, 0, 0, 3, 0, 9, 0, 1],
                        [0, 1, 0, 0, 0, 4, 0, 0, 0],
                        [4, 0, 7, 0, 0, 0, 2, 0, 8],
                        [0, 0, 5, 2, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 9, 8, 1, 0, 0],
                        [0, 4, 0, 0, 0, 3, 0, 0, 0],
                        [0, 0, 0, 3, 6, 0, 0, 7, 2],
                        [0, 7, 0, 0, 0, 0, 0, 0, 3],
                        [9, 0, 3, 0, 0, 0, 6, 0, 4]])

    puzzle4 = np.array([[0, 0, 4, 0, 6, 0, 0, 0, 5],
                        [7, 8, 0, 4, 0, 0, 0, 2, 0],
                        [0, 0, 2, 6, 0, 1, 0, 7, 8],
                        [6, 1, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 7, 5, 4, 0, 0, 6, 1],
                        [0, 0, 1, 7, 5, 0, 9, 3, 0],
                        [0, 7, 0, 3, 0, 0, 0, 1, 0],
                        [0, 4, 0, 2, 0, 6, 0, 0, 7],
                        [0, 2, 0, 0, 0, 7, 4, 0, 0]])

    puzzles = list()
    puzzles.append(puzzle1)
    puzzles.append(puzzle2)
    puzzles.append(puzzle3)
    puzzles.append(puzzle4)

    createWindow(puzzles)


if (__name__ == '__main__'):
    main()
