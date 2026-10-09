"""Static grid world used by the 2D navigation demo."""
ROWS, COLS = 22, 30
START = (1, 1)
GOAL = (20, 28)

def create_world():
    """Create a grid where True means occupied."""
    grid = [[False for _ in range(COLS)] for _ in range(ROWS)]
    # Boundary walls
    for r in range(ROWS):
        grid[r][0] = grid[r][COLS - 1] = True
    for c in range(COLS):
        grid[0][c] = grid[ROWS - 1][c] = True
    # Interior obstacles with gaps so a route remains possible.
    for r in range(3, 16):
        if r not in (7, 8):
            grid[r][7] = True
    for c in range(10, 25):
        if c not in (17, 18, 19):
            grid[6][c] = True
    for r in range(9, 19):
        if r not in (13, 14):
            grid[r][17] = True
    for c in range(3, 14):
        if c not in (8, 9):
            grid[17][c] = True
    for r in range(3, 11):
        grid[r][24] = True
    return grid
