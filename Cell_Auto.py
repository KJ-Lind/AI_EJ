import pygame as pg
from opensimplex import OpenSimplex
import numpy as np

ROWS, COLS = 200,200
CELL_SIZE = 5
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

def noise2d(noise, x, y, octaves=1, persistence=0.5, lacunarity=2.0):
    total = 0
    amplitude = 1
    frequency = 1

    for i in range(octaves):
        total += noise.noise2(x * frequency, y * frequency) * amplitude
        amplitude *= persistence
        frequency *= lacunarity

    return total

def Initialize_Arr(seed):
    noise = OpenSimplex(seed)
    grid = np.zeros((ROWS, COLS))

    scale = 0.02
    for i in range(ROWS):
        for j in range(COLS):
            val = noise2d(noise, j * scale, i * scale, octaves=6)
            grid[i][j] = 1 if val > 0.35 else 0

    return grid

def Cell_Logic(grid):
    rows, cols = grid.shape
    temp = np.zeros((rows, cols), dtype=np.uint8)

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
                        live_neighbors += grid[y][x]

            if grid[j][k] == 1:
                temp[j][k] = 1 if live_neighbors >= 4 else 0
            else:
                temp[j][k] = 1 if live_neighbors >= 5 else 0

    return temp

def draw(grid):
    surface = pg.Surface((COLS , ROWS))

    pixels = np.zeros((ROWS, COLS, 3), dtype=np.uint8)
    pixels[grid == 1] = [0, 0, 0]  # Black for alive cells
    pixels[grid == 0] = [255, 255, 255]        # White for dead cells

    pixels = np.transpose(pixels, (1, 0, 2))

    pg.surfarray.blit_array(surface, pixels)
    surface = pg.transform.scale(surface, (WIDTH, HEIGHT))
    screen.blit(surface, (0, 0))

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    running = True

    grid = Initialize_Arr(42)


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        grid = Cell_Logic(grid)
        draw(grid)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
