import pygame as pg
from typing import TypeVar

from pygame.surfarray import array_colorkey

TupleOrInt = TypeVar('TupleOrInt', tuple, int)

# Color definitions
COLORKEY         = pg.Color(0, 0, 0) # Colorkey is used for transparency (any pixel with this color will not be drawn on blit)
BLACK            = pg.Color(1, 1, 1)
BLUE             = pg.Color(0, 0, 255)
CYAN             = pg.Color(0, 255, 255)
DARK_GRAY        = pg.Color(64, 64, 64)
GRAY             = pg.Color(128, 128, 128)
GREEN            = pg.Color(0, 255, 0)
LIGHT_GRAY       = pg.Color(240, 240, 240)
MAGENTA          = pg.Color(255, 0, 255)
RED              = pg.Color(255, 0, 0)
WHITE            = pg.Color(255, 255, 255)
YELLOW           = pg.Color(255, 255, 0)

BUTTON_COLOR       = pg.Color(125, 125, 255)
BUTTON_COLOR_HOVER = pg.Color(150, 150, 255)
BUTTON_COLOR_DOWN  = pg.Color(100, 100, 255)
PLAYER1_COLOR      = pg.Color(107, 209, 129)
PLAYER2_COLOR      = pg.Color(204, 151, 222)

BACKGROUND_COLOR = WHITE

# You MUST call font.init() before loading any fonts
pg.font.init()
FONT_20 = pg.font.Font('fonts/Lato-Regular.ttf', 20)
FONT_16 = pg.font.Font('fonts/Lato-Regular.ttf', 16)

# Utility functions
def is_even(a):
    return False if a % 2 else True

def is_odd(a):
    return True if a % 2 else False
