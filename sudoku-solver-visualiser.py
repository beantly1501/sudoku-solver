from tkinter import *
import tkinter.font as font

GRID_WIDTH = 540
GRID_HEIGHT = 540


def randomizeGrid():
    print("RANDOMIZE")


def resetGrid():
    print("RESET")


def startSolving():
    print("SOLVING")


def createWindow():
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
    for i in range(0, GRID_WIDTH, 60):
        c.create_line([(i, 0), (i, GRID_HEIGHT)], tag="grid_line")

    # horizontal lines
    for i in range(0, GRID_HEIGHT, 60):
        c.create_line([(0, i), (GRID_WIDTH, i)], tag="grid_line")

    # button creation

    # virutal image to change width and height to be in pixels
    pixelVirtual = PhotoImage(width=1, height=1)

    bFrame = Frame(window, width=540, height=160, bg="grey")
    bFrame.pack()

    bFont = font.Font(size=15)

    resetB = Button(bFrame, text="Reset", width=120, height=50,
                    image=pixelVirtual, compound="c", command=resetGrid)
    resetB.place(x=30, y=40)

    startB = Button(bFrame, text="Start Solving", width=120, height=50,
                    image=pixelVirtual, compound="c", command=startSolving)
    startB.place(x=200, y=40)

    randomizeB = Button(bFrame, text="Randomize", width=120, height=50,
                        image=pixelVirtual, compound="c", command=randomizeGrid)
    randomizeB.place(x=370, y=40)

    resetB["font"] = bFont
    startB["font"] = bFont
    randomizeB["font"] = bFont

    window.mainloop()


def main():
    createWindow()


if (__name__ == '__main__'):
    main()
