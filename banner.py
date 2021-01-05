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

from __init__ import *
from player import Player


class Banner(pg.Rect):
    def __init__(self, rect: pg.Rect, bg_color: pg.Color):
        super().__init__(rect)
        self.bg_color = bg_color
        self.screen = pg.display.get_surface()

        self.center = (self.screen.get_width() // 2,
            self.screen.get_height() // 2)

    def draw(self, winner: list[Player]) -> None:
        # Create the message text
        msg = f'{winner[0].name} Wins!' if len(winner) == 1 else "It's a TIE!"
        text = FONT_20.render(msg, True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = self.center

        # Draw the shapes
        pg.draw.rect(self.screen, self.bg_color, self)
        pg.draw.rect(self.screen, DARK_GRAY, self, width=1)

        # Blit the text to the screen
        self.screen.blit(text, text_rect)

        pg.display.update(self)

    def clear(self) -> None:
        pg.draw.rect(self.screen, BACKGROUND_COLOR, self)

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
