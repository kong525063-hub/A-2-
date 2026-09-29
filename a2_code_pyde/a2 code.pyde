def setup():


def reset_game():
    global grid, moves, game_over


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
