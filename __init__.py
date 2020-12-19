import pygame

ROWS = 4
COLS = 4

# Color definitions
BLACK         = pygame.Color(0, 0, 0)
BLUE          = pygame.Color(0, 0, 255)
CYAN          = pygame.Color(0, 255, 255)
DARK_GRAY     = pygame.Color(64, 64, 64)
GRAY          = pygame.Color(128, 128, 128)
GREEN         = pygame.Color(0, 255, 0)
LIGHT_GRAY    = pygame.Color(240, 240, 240)
MAGENTA       = pygame.Color(255, 0, 255)
RED           = pygame.Color(255, 0, 0)
WHITE         = pygame.Color(255, 255, 255)
YELLOW        = pygame.Color(255, 255, 0)
PLAYER1_COLOR = pygame.Color(107, 209, 129)
PLAYER2_COLOR = pygame.Color(204, 151, 222)

# Dot attributes
DOT_RAD = 5
DOT_DIA = 2 * DOT_RAD
DOT_COLOR = BLACK

# Cell attributes
CELL_SIZE = (100, 100)
CELL_WIDTH = CELL_SIZE[0]
CELL_HEIGHT = CELL_SIZE[1]
CELL_COLOR_DEFAULT = WHITE

# Edge attributes
EDGE_THICKNESS = DOT_DIA
EDGE_COLOR_DEFAULT = LIGHT_GRAY
EDGE_COLOR_ACTIVATED = pygame.Color(125, 125, 255)

# Gutter attributes
GUTTER_TOP    = 20
GUTTER_BOTTOM = 20
GUTTER_LEFT   = 20
GUTTER_RIGHT  = 20

# Scoreboard attributes
SCOREBOARD_ORIGIN = (GUTTER_LEFT, GUTTER_TOP)
SCOREBOARD_WIDTH = COLS * CELL_WIDTH + (COLS + 1) * EDGE_THICKNESS
SCOREBOARD_HEIGHT = 70
SCOREBOARD_SIZE = (SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT)

# Footer attributes
FOOTER_ORIGIN = (GUTTER_LEFT, GUTTER_TOP * 2 + SCOREBOARD_HEIGHT + ROWS * CELL_WIDTH + (ROWS + 1) * EDGE_THICKNESS + GUTTER_BOTTOM)
FOOTER_WIDTH = SCOREBOARD_WIDTH
FOOTER_HEIGHT = 70
FOOTER_SIZE = (FOOTER_WIDTH, FOOTER_HEIGHT)

TOP    = 'top'
BOTTOM = 'bottom'
RIGHT  = 'right'
LEFT   = 'left'

# You MUST call font.init() before loading any fonts
pygame.font.init()
FONT_LATO_REGULAR_20 = pygame.font.Font('fonts/Lato-Regular.ttf', 20)
FONT_DEFAULT = pygame.font.Font(None, 18)

def is_even(a):
    return False if a % 2 else True

def is_odd(a):
    return True if a % 2 else False
