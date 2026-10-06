import random

ROWS = 5
COLS = 5
CELL_SIZE = 60
SPACING = 6
OFFSET_X = 38 
OFFSET_Y = 100

SAVE_FILE = "save.txt"

grid = []
moves = 0
game_over = False

start_time = 0
final_time = 0

def setup():
    size(400, 480) 
    reset_game()

def reset_game():
    global grid, moves, game_over, start_time
    
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    game_over = False

    # สุ่มไฟเริ่มต้น
    for _ in range(12):
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        toggle(r, c)
        
    moves = 0
    start_time = millis()


def save_game():
    try:
        with open(SAVE_FILE, 'w') as f:
            f.write("count=\n" + str(moves) + "\n")
            f.write("check_win=\n" + ("1" if game_over else "0") + "\n")
            f.write("grid=\n")
            for row in grid:
                f.write(" ".join(str(cell) for cell in row) + "\n")
        print("Game Saved!")
    except:
        print("Save failed.")

def load_game():
    global grid, moves, start_time, game_over
    try:
        with open(SAVE_FILE, 'r') as f:
            lines = f.readlines()
            
        moves = int(lines[1])
        game_over = (int(lines[3]) == 1)
        
        grid = [[int(val) for val in lines[i].split()] for i in range(5, 5 + ROWS)]
        
        start_time = millis()
        print("Game Loaded!")
    except:
        print("Load failed. No file or wrong format.")

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

def draw():
    background(248, 250, 252)

    # ------------------ ส่วน Header ------------------
    fill(71, 85, 105) 
    textSize(24)
    textAlign(CENTER, CENTER)
    text("L I G H T S  O U T", width / 2, 35)

    if not game_over:
        elapsed_sec = (millis() - start_time) // 1000
    else:
        elapsed_sec = final_time
        
    mins = elapsed_sec // 60
    secs = elapsed_sec % 60
    time_str = "{:02d}:{:02d}".format(mins, secs)

    textSize(14)
    fill(148, 163, 184) 
    text("Moves: " + str(moves) + "    Time: " + time_str, width / 2, 65)

    # ------------------ ส่วน Hover Effects ------------------
    hover_r = -1
    hover_c = -1
    
    if not game_over:
        for r in range(ROWS):
            for c in range(COLS):
                x = OFFSET_X + c * (CELL_SIZE + SPACING)
                y = OFFSET_Y + r * (CELL_SIZE + SPACING)
                if x <= mouseX <= x + CELL_SIZE and y <= mouseY <= y + CELL_SIZE:
                    hover_r = r
                    hover_c = c
                    break

    affected_cells = []
    if hover_r != -1:
        affected_cells = [
            (hover_r, hover_c), 
            (hover_r - 1, hover_c), 
            (hover_r + 1, hover_c), 
            (hover_r, hover_c - 1), 
            (hover_r, hover_c + 1)
        ]
    # --------------------------------------------------------

    noStroke()

    for r in range(ROWS):
        for c in range(COLS):
            x = OFFSET_X + c * (CELL_SIZE + SPACING)
            y = OFFSET_Y + r * (CELL_SIZE + SPACING)
            
            is_hovered = (r, c) in affected_cells

            if grid[r][c] == 1:
                if is_hovered:
                    fill(245, 158, 11)
                else:
                    fill(250, 191, 36)
            else:
                if is_hovered:
                    fill(148, 163, 184)
                else:
                    fill(203, 213, 225)

            rect(x, y, CELL_SIZE, CELL_SIZE, 12)
            
    # ------------------ ส่วนอธิบายปุ่มกด (UI) ------------------
    if not game_over:
        fill(148, 163, 184)
        textSize(12)
        text("[R] Restart   [S] Save   [L] Load", width / 2, height - 20)

    # ------------------ ส่วนตอนจบเกม ------------------
    if game_over:
        fill(255, 255, 255, 220) 
        rect(0, 0, width, height)
        
        fill(51, 65, 85)
        textSize(28)
        text("Cleared!", width / 2, height / 2 - 30)
        
        textSize(16)
        fill(100, 116, 139)
        text("Moves: " + str(moves) + "   |   Time: " + time_str, width / 2, height / 2 + 10)
        
        fill(241, 245, 249) 
        rect(width / 2 - 70, height / 2 + 45, 140, 40, 20) 
        
        fill(71, 85, 105)
        textSize(14)
        text("Press 'R' to Restart", width / 2, height / 2 + 63)

def mousePressed():
    global moves, game_over, final_time

    if game_over:
        return

    for r in range(ROWS):
        for c in range(COLS):
            x = OFFSET_X + c * (CELL_SIZE + SPACING)
            y = OFFSET_Y + r * (CELL_SIZE + SPACING)

            if x <= mouseX <= x + CELL_SIZE and y <= mouseY <= y + CELL_SIZE:
                toggle(r, c)
                moves += 1
                
                if check_win():
                    game_over = True
                    final_time = (millis() - start_time) // 1000
                return

def keyPressed():
    if key == 'r' or key == 'R':
        reset_game()
    elif key == 's' or key == 'S':
        save_game()
    elif key == 'l' or key == 'L':
        load_game()
