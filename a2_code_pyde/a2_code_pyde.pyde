import random

ROWS = 5
COLS = 5
CELL_SIZE = 65
OFFSET_X = 37
OFFSET_Y = 100

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
moves = 0
game_over = False


def setup():
    size(400, 480)
    reset_game()


def reset_game():
    global grid, moves, game_over
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    moves = 0
    game_over = False

    for _ in range(12):
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        toggle(r, c)
    moves = 0
def toggle(r, c):
    global grid
    if 0 <= r < ROWS and 0 <= c < COLS:

    else:


def check_win():
    if not any(1 in row for row in grid):
        return True
    else:
        return False


def draw_bulb(cx, cy, is_on):
    if is_on:

    else:


def draw_grid_recursive(r, c):
    if r >= ROWS:
        return
    else:
        if c + 1 >= COLS:

        else:


def draw():
    if game_over:

    else:


def mousePressed():
    global moves, game_over
    if game_over:
        return
    else:
        if 0 <= r < ROWS and 0 <= c < COLS:
            if check_win():

            else:

        else:


def keyPressed():
    if key == 'r' or key == 'R':

    else:
