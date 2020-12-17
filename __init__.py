import pygame

ROWS = 3
COLS = 3

# Color definitions
BLACK   = pygame.Color(0, 0, 0)
BLUE    = pygame.Color(125, 125, 255)
CYAN    = pygame.Color(0, 255, 255)
GRAY    = pygame.Color(225, 225, 225)
GREEN   = pygame.Color(0, 255, 0)
MAGENTA = pygame.Color(255, 0, 255)
RED     = pygame.Color(255, 0, 0)
WHITE   = pygame.Color(255, 255, 255)
YELLOW  = pygame.Color(255, 255, 0)
PLAYER1_COLOR = pygame.Color(110, 219, 139)
PLAYER2_COLOR = pygame.Color(204, 151, 222)

HIGHLIGHT_COLOR = pygame.Color(163, 209, 167)

# Dot attributes
DOT_RAD = 8
DOT_DIA = 2 * DOT_RAD
DOT_COLOR = BLACK

# Cell attributes
ORIGIN = (0, 0)
CELL_SIZE = (100, 100)
CELL_WIDTH = CELL_SIZE[0]
CELL_HEIGHT = CELL_SIZE[1]

HIGHLIGHT_WIDTH = 4

GUTTER_TOP    = 100
GUTTER_BOTTOM = 20
GUTTER_LEFT   = 20
GUTTER_RIGHT  = 20

TOP    = 'top'
BOTTOM = 'bottom'
RIGHT  = 'right'
LEFT   = 'left'

PLAYER1 = 'player1'
PLAYER2 = 'player2'

# You MUST call font.init() before loading any fonts
pygame.font.init()
FONT_LATO_REGULAR_20 = pygame.font.Font('fonts/Lato-Regular.ttf', 20)
FONT_DEFAULT = pygame.font.Font(None, 18)
