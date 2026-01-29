import tkinter as tk
import random


def create_grid(canvas, rows, cols, cell_size):
    rects = [[None for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            rects[i][j] = canvas.create_rectangle(
                x1, y1, x2, y2,
                outline="white", fill="black"
            )
    return rects

def update_grid(canvas, rects, arr):
    for i in range(rows):
        for j in range(cols):
            color = "blue" if arr[i][j] == 1 else "black"
            canvas.itemconfig(rects[i][j], fill=color, outline="white")

def Initialize_Arr(arr):
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = random.choice([0, 1])

def Cell_Logic(arr):
    temp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    ni, nj = i + x, j + y
                    if 0 <= ni < rows and 0 <= nj < cols:
                        live_neighbors += arr[ni][nj]

            if arr[i][j] == 1:
                if live_neighbors < 5:
                    temp[i][j] = 0
                else:
                    temp[i][j] = 1
            if arr[i][j] == 0:
                if live_neighbors > 4:
                    temp[i][j] = 1
                else:
                    temp[i][j] = 0
            else:
                if live_neighbors == 3:
                    temp[i][j] = 1

    return temp

def game_loop():
    update_grid(canvas, rects, arr)
    root.after(60, game_loop)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cellular Automaton")
    root.geometry("800x600")

    canvas = tk.Canvas(root, width=800, height=600,bg="gray")

    rows = 50
    cols = 50

    arr = [[0 for _ in range(cols)] for _ in range(rows)]
    Initialize_Arr(arr)
    rects = create_grid(canvas, rows, cols, 12)

    canvas.pack()

    game_loop()

    root.mainloop()
