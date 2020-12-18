import pygame

ROWS = 4
COLS = 4

# Color definitions
BLACK   = pygame.Color(0, 0, 0)
BLUE    = pygame.Color(0, 0, 255)
CYAN    = pygame.Color(0, 255, 255)
GRAY    = pygame.Color(225, 225, 225)
GREEN   = pygame.Color(0, 255, 0)
MAGENTA = pygame.Color(255, 0, 255)
RED     = pygame.Color(255, 0, 0)
WHITE   = pygame.Color(255, 255, 255)
YELLOW  = pygame.Color(255, 255, 0)
PLAYER1_COLOR = pygame.Color(110, 219, 139)
PLAYER2_COLOR = pygame.Color(204, 151, 222)

# Cell types
CELL = 'cell'
DOT = 'dot'
EDGE = 'edge'

# Dot attributes
DOT_RAD = 6
DOT_DIA = 2 * DOT_RAD
DOT_COLOR = BLACK

# Cell attributes
ORIGIN = (0, 0)
CELL_SIZE = (100, 100)
CELL_WIDTH = CELL_SIZE[0]
CELL_HEIGHT = CELL_SIZE[1]
CELL_COLOR_DEFAULT = WHITE

# Edge attributes
EDGE_THICKNESS = DOT_DIA
EDGE_COLOR_DEFAULT = GRAY
EDGE_COLOR_ACTIVATED = pygame.Color(125, 125, 255)

GUTTER_TOP    = 100
GUTTER_BOTTOM = 20
GUTTER_LEFT   = 20
GUTTER_RIGHT  = 20

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
