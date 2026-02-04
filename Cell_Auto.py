import tkinter as tk
import time
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
                outline="black", fill="black"
            )
    return rects

def update_grid(canvas, rects, arr):
    for i in range(rows):
        for j in range(cols):
            color = "black" if arr[i][j] else "white"
            canvas.itemconfig(rects[i][j], fill=color, outline=color)

def Initialize_Arr(arr, density=0.50):
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = 1 if random.random() < density else 0

def Cell_Logic(arr):
    temp = [[0 for _ in range(cols)] for _ in range(rows)]

    for j in range(rows):
        for k in range(cols):
            live_neighbors = 0

            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue

                    y = j + dy
                    x = k + dx

                    if 0 <= y < rows and 0 <= x < cols:
                        live_neighbors += arr[y][x]

            if arr[j][k] == 1:
                temp[j][k] = 1 if live_neighbors >= 4 else 0
            else:
                temp[j][k] = 1 if live_neighbors >= 5 else 0
            

    return temp

def game_loop(iterations):
    if iterations <= 0:
       return  # stop looping

    global arr
    arr = Cell_Logic(arr)
    update_grid(canvas, rects, arr)

    root.after(1000, lambda: game_loop(iterations - 1))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cellular Automaton")
    root.geometry("1000x1000")

    canvas = tk.Canvas(root, width=1000, height=1000, bg="gray")

    rows = 200
    cols = 200

    iterations = 5

    arr = [[0 for _ in range(cols)] for _ in range(rows)]
    Initialize_Arr(arr)
    rects = create_grid(canvas, rows, cols, 5)

    canvas.pack()

    game_loop(iterations)

    root.mainloop()
