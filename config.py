# -----------------------------------------
# WINDOW SETTINGS
# -----------------------------------------

WIDTH = 840

GRID_HEIGHT = 600
HUD_HEIGHT = 160

HEIGHT = GRID_HEIGHT + HUD_HEIGHT


# -----------------------------------------
# MAZE SETTINGS
# -----------------------------------------

ROWS = 15
COLS = 21

CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = GRID_HEIGHT // ROWS


# -----------------------------------------
# START AND END
# -----------------------------------------

START = (1, 1)

END = (
    ROWS - 2,
    COLS - 2
)


# -----------------------------------------
# COLORS
# -----------------------------------------

BACKGROUND = (30, 30, 30)

WALL_COLOR = (220, 220, 220)
GRID_COLOR = (80, 80, 80)

START_COLOR = (0, 200, 0)
END_COLOR = (200, 0, 0)

VISITED_COLOR = (150, 100, 220)
PATH_COLOR = (0, 120, 255)

TEXT_COLOR = (240, 240, 240)
SECONDARY_TEXT = (180, 180, 180)


# -----------------------------------------
# ANIMATION
# -----------------------------------------

ANIMATION_DELAY = 15