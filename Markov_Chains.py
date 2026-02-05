import tkinter as tk
import random

# Window
Window = tk.Tk()
window.bgcolor("grey")
Window.title("Cadenas Markov")
Window.geometry("900x800")

current_state = "A"

a_chance = tk.DoubleVar(value=0.5)
b_chance = tk.DoubleVar(value=0.5)

# UI
title = tk.Label(Window, text="Markov chain simulator", font=("Arial", 20))
title.pack(pady=50)

label_A = tk.Label(Window, text="Chances of going to A")
label_A.pack()

slider_A = tk.Scale(
    Window,
    from_=0,
    to=1,
    resolution=0.01,
    orient="horizontal",
    length=400,
    variable=a_chance
)
slider_A.pack()

label_B = tk.Label(Window, text="Chances of going to B")
label_B.pack()

slider_B = tk.Scale(
    Window,
    from_=0,
    to=1,
    resolution=0.01,
    orient="horizontal",
    length=400,
    variable=b_chance
)
slider_B.pack()

label_state = tk.Label(
    Window,
    text=f"Current state: {current_state}",
    font=("Arial", 18)
)
label_state.pack(pady=40)


def UpdateState():
    global current_state

    pa = a_chance.get()
    pb = b_chance.get()

    total = pa + pb
    if total == 0:
        Window.after(1000, UpdateState)
        return

    # normalize paths
    pa /= total
    pb /= total

    r = random.random()
    current_state = "A" if r < pa else "B"

    print(f"Current state: {current_state}")
    label_state.config(text=f"Current state: {current_state}")

    Window.after(1000, UpdateState)


UpdateState()
Window.mainloop()