import pygame as pg
import pygame_gui
import numpy as np
import random


# Settings
ROWS, COLS = 150, 150
CELL_SIZE = 5
GRID_WIDTH, GRID_HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

UI_HEIGHT = 100
WIDTH, HEIGHT = GRID_WIDTH, GRID_HEIGHT + UI_HEIGHT

# Markov values
p_birth = 0.9
p_death = 0.1


def initialize_grid():
    return np.random.choice([0, 1], size=(ROWS, COLS), p=[0.7, 0.3])


def markov_cell_logic(grid):
    global p_birth, p_death

    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):

            live_neighbors = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue
                    y = i + dy
                    x = j + dx
                    if 0 <= y < rows and 0 <= x < cols:
                        live_neighbors += grid[y][x]

            neighbor_factor = live_neighbors / 8.0

            if grid[i][j] == 1:
                survive_prob = (1 - p_death) * (0.5 + neighbor_factor / 2)
                new_grid[i][j] = 1 if random.random() < survive_prob else 0
            else:
                birth_prob = p_birth * neighbor_factor
                new_grid[i][j] = 1 if random.random() < birth_prob else 0

    return new_grid


def draw(screen, grid):
    surface = pg.Surface((COLS, ROWS))

    pixels = np.zeros((ROWS, COLS, 3), dtype=np.uint8)
    pixels[grid == 1] = [0, 0, 0]
    pixels[grid == 0] = [255, 255, 255]

    pixels = np.transpose(pixels, (1, 0, 2))

    pg.surfarray.blit_array(surface, pixels)
    surface = pg.transform.scale(surface, (GRID_WIDTH, GRID_HEIGHT))

    screen.blit(surface, (0, UI_HEIGHT))


def main():
    global p_birth, p_death

    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Cell Auto with Markov")

    manager = pygame_gui.UIManager((WIDTH, HEIGHT))

    # Sliders
    birth_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pg.Rect((50, 20), (300, 25)),
        start_value=p_birth,
        value_range=(0.0, 1.0),
        manager=manager
    )

    death_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pg.Rect((50, 60), (300, 25)),
        start_value=p_death,
        value_range=(0.0, 1.0),
        manager=manager
    )

    birth_label = pygame_gui.elements.UILabel(
        relative_rect=pg.Rect((370, 20), (200, 25)),
        text=f"p_birth: {p_birth:.2f}",
        manager=manager
    )

    death_label = pygame_gui.elements.UILabel(
        relative_rect=pg.Rect((370, 60), (200, 25)),
        text=f"p_death: {p_death:.2f}",
        manager=manager
    )

    clock = pg.time.Clock()
    grid = initialize_grid()

    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == birth_slider:
                    p_birth = event.value
                if event.ui_element == death_slider:
                    p_death = event.value

            manager.process_events(event)

        manager.update(time_delta)

        grid = markov_cell_logic(grid)

        screen.fill((200, 200, 200))

        draw(screen, grid)

        birth_label.set_text(f"p_birth: {p_birth:.2f}")
        death_label.set_text(f"p_death: {p_death:.2f}")

        manager.draw_ui(screen)

        pg.display.flip()

    pg.quit()


main()
