from tkinter import *
import tkinter.font as font
import numpy as np
import sudoku_solver_backtracking as solver

GRID_WIDTH = 540
GRID_HEIGHT = 540
GRID_SIZE = 9


canvasNumbers = []
currentPuzzle = 0
puzzles = []


def newPuzzle(c, puzzles, cFont, buttons):
    global canvasNumbers, currentPuzzle

    currentPuzzle += 1
    for b in buttons:
        b.configure(state=NORMAL)

    for n in canvasNumbers:
        c.delete(n)

    if (currentPuzzle % len(puzzles) == 0):
        currentPuzzle = 0
        grid = puzzles[currentPuzzle]
    else:
        grid = puzzles[currentPuzzle]

    canvasNumbers = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (grid[i, j] != 0):
                num = c.create_text((30 * (j + 1)) + (30 * j), (30 * (i + 1)) + (30 * i),
                                    text=grid[i, j], fill="black", font=cFont)
                canvasNumbers.append(num)


def instantSolve(c, grid, cFont, buttons):
    global canvasNumbers, currentPuzzle

    buttons[0].configure(state=DISABLED)
    buttons[1].configure(state=DISABLED)

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


def visualSolve(c, grid, cFont, window, buttons):
    global canvasNumbers, currentPuzzle

    buttons[0].configure(state=DISABLED)
    buttons[1].configure(state=DISABLED)
    buttons[2].configure(state=DISABLED)

    unsolvedGrid = np.copy(grid)

    solvedGrid = solver.solver(np.copy(unsolvedGrid))

    for n in canvasNumbers:
        c.delete(n)

    canvasNumbers = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (unsolvedGrid[i, j] != 0):
                num = c.create_text((30 * (j + 1)) + (30 * j), (30 * (i + 1)) + (30 * i),
                                    text=unsolvedGrid[i, j], fill="black", font=cFont)
                canvasNumbers.append(num)

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (unsolvedGrid[i, j] != solvedGrid[i, j]):
                num = c.create_text((30 * (j + 1)) + (30 * j), (30 * (i + 1)) + (30 * i),
                                    text="1", fill="black", font=cFont)
                canvasNumbers.append(num)
                k = 0
                while (k < ((9*2) + 1)):
                    c.delete(num)
                    canvasNumbers.pop()

                    num = c.create_text((30 * (j + 1)) + (30 * j), (30 * (i + 1)) + (30 * i),
                                        text=(k % 10), fill="black", font=cFont)
                    canvasNumbers.append(num)

                    window.after(10)
                    window.update()

                    k += 1

                c.delete(num)
                canvasNumbers.pop()
                num = c.create_text((30 * (j + 1)) + (30 * j), (30 * (i + 1)) + (30 * i),
                                    text=solvedGrid[i, j], fill="black", font=cFont)
                canvasNumbers.append(num)

    buttons[2].configure(state=NORMAL)


def createWindow():
    global canvasNumbers, puzzles, currentPuzzle

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

    startB = Button(bFrame, text="Instant Solve", width=120, height=50,
                    image=pixelVirtual, compound="c", command=lambda: instantSolve(c, puzzles[currentPuzzle], cFont, buttons))
    startB.place(x=30, y=40)

    visualB = Button(bFrame, text="Visual Solving", width=120, height=50,
                     image=pixelVirtual, compound="c", command=lambda: visualSolve(c, puzzles[currentPuzzle], cFont, window, buttons))
    visualB.place(x=210, y=40)

    randomizeB = Button(bFrame, text="New Puzzle", width=120, height=50,
                        image=pixelVirtual, compound="c", command=lambda: newPuzzle(c, puzzles, cFont, buttons))
    randomizeB.place(x=540 - 30 - 120, y=40)

    buttons = [startB, visualB, randomizeB]

    startB["font"] = bFont
    visualB["font"] = bFont
    randomizeB["font"] = bFont

    ##### FOR PRINTING MOUSE POS, FOR DEBUG ONLY ##########################
    # def motion(event):
    #     x, y = event.x, event.y
    #     print('{}, {}'.format(x, y))

    # window.bind('<Motion>', motion)

    window.mainloop()


def main():
    global puzzles

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

    puzzle4 = np.array([[7, 8, 0, 4, 0, 0, 1, 2, 0],
                        [6, 0, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 0, 6, 0, 1, 0, 7, 8],
                        [0, 0, 7, 0, 4, 0, 2, 6, 0],
                        [0, 0, 1, 0, 5, 0, 9, 3, 0],
                        [9, 0, 4, 0, 6, 0, 0, 0, 5],
                        [0, 7, 0, 3, 0, 0, 0, 1, 2],
                        [1, 2, 0, 0, 0, 7, 4, 0, 0],
                        [0, 4, 9, 2, 0, 6, 0, 0, 7]])

    puzzle5 = np.array([[3, 0, 0, 8, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 2, 0, 0, 0],
                        [0, 4, 1, 5, 0, 0, 8, 3, 0],
                        [0, 2, 0, 0, 0, 1, 0, 0, 0],
                        [8, 5, 0, 4, 0, 3, 0, 1, 7],
                        [0, 0, 0, 7, 0, 0, 0, 2, 0],
                        [0, 8, 5, 0, 0, 9, 7, 4, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [9, 0, 0, 0, 0, 7, 0, 0, 6]])

    puzzles.append(puzzle1)
    puzzles.append(puzzle2)
    puzzles.append(puzzle3)
    puzzles.append(puzzle4)
    puzzles.append(puzzle5)

    createWindow()


if (__name__ == '__main__'):
    main()
