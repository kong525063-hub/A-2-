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
    targets = [(r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for dr, dc in targets:
        if 0 <= dr < ROWS and 0 <= dc < COLS:
            grid[dr][dc] = 1 - grid[dr][dc]

def check_win():
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                return False
    return True


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
