# Copyright 2021 Curt Bathras
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pygame as pg

SHOW_OUTLINE = False

# Color definitions
# Colorkey is used for transparency (any pixel with this color will not be drawn
# on blit)
COLORKEY: pg.Color           = pg.Color(0, 0, 0)
BLACK: pg.Color              = pg.Color(1, 1, 1)
BLUE: pg.Color               = pg.Color(0, 0, 255)
CYAN: pg.Color               = pg.Color(0, 255, 255)
DARK_GRAY: pg.Color          = pg.Color(64, 64, 64)
GRAY: pg.Color               = pg.Color(128, 128, 128)
GREEN: pg.Color              = pg.Color(0, 255, 0)
LIGHT_GRAY: pg.Color         = pg.Color(240, 240, 240)
MAGENTA: pg.Color            = pg.Color(255, 0, 255)
PINK: pg.Color               = pg.Color(255, 214, 214)
RED: pg.Color                = pg.Color(255, 0, 0)
WHITE: pg.Color              = pg.Color(255, 255, 255)
YELLOW: pg.Color             = pg.Color(255, 255, 0)

BUTTON_COLOR: pg.Color       = pg.Color(76, 97, 237)
BUTTON_COLOR_HOVER: pg.Color = pg.Color(120, 136, 242)
BUTTON_COLOR_DOWN: pg.Color  = pg.Color(28, 55, 233)

PLAYER_COLORS: list[pg.Color] = [
    pg.Color(225, 232, 81),
    pg.Color(245, 158, 66),
    pg.Color(204, 151, 222),
    pg.Color(107, 209, 129),
]

BACKGROUND_COLOR: pg.Color      = WHITE
EDGE_COLOR_DEFAULT: pg.Color    = LIGHT_GRAY
EDGE_COLOR_CAPTURED: pg.Color   = pg.Color(125, 125, 255)
CELL_COLOR_DEFAULT: pg.Color    = WHITE
DOT_COLOR: pg.Color             = BLACK

# Gap constants to use for spacing
GAP_10: int = 10
GAP_20: int = 20
GAP_30: int = 30
GAP_40: int = 40
GAP_50: int = 50

# You MUST call font.init() before loading any fonts
pg.font.init()
FONT_20: pg.font.Font = pg.font.Font('fonts/Lato-Regular.ttf', 20)
FONT_16: pg.font.Font = pg.font.Font('fonts/Lato-Regular.ttf', 16)

# Utility functions
def get_color() -> pg.Color:
    global PLAYER_COLORS
    return PLAYER_COLORS.pop()
