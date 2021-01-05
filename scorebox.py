"""A scorebox represents a player's displayed score in the game of Dots."""

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
from config import Config
from player import Player


class Scorebox:
    """The Scorebox object encompasses the name of the player, a colored box to
    display the player's score, the player's score, and the active arrow if the
    player is the current player in the game.
    """
    def __init__(self, pos: tuple, player: Player):
        super().__init__()
        self._cfg = Config()
        self._bg_color = LIGHT_GRAY
        self._pos = pos
        self._player = player
        self._size = (self._cfg.SCOREBOX_WIDTH, self._cfg.SCOREBOX_HEIGHT)
        self._screen = pg.display.get_surface()

        self._rect = pg.Rect(pos, self._size)

        self._arrow_surf = pg.image.load('left-arrow-24.png')
        self._arrow_rect = self._arrow_surf.get_rect()
        self._arrow_rect.left = self._rect.right - self._arrow_rect.width
        self._arrow_rect.centery = self._rect.centery

        self._score_rect = pg.Rect(
            self._rect.right - self._arrow_rect.width - 48,
            self._rect.top + (self._cfg.SCOREBOX_HEIGHT - 28) // 2,
            48, 28)

        self._score_text_surf = FONT_20.render('0', True, BLACK)
        self._score_text_rect = self._score_text_surf.get_rect()
        self._score_text_rect.center = self._score_rect.center

        self._name_text_surf = FONT_20.render(self._player.name, True, BLACK)
        self._name_text_rect = self._name_text_surf.get_rect()
        self._name_text_rect.left = self._rect.left
        self._name_text_rect.centery = self._rect.centery

    @property
    def size(self) -> tuple:
        """Get the size, in pixels, of the scorebox."""
        return self._size

    @property
    def pos(self) -> tuple:
        """Get the position, in pixels, of the scorebox."""
        return self._pos

    def draw(self) -> None:
        """Draw the scorebox to the screen."""
        if SHOW_OUTLINE:
            pg.draw.rect(self._screen, RED, self._rect, width=1)
        pg.draw.rect(self._screen, self._player.color, self._score_rect)
        self._screen.blit(self._score_text_surf, self._score_text_rect)
        self._screen.blit(self._name_text_surf, self._name_text_rect)

    def update_score(self, score: int) -> None:
        """Update the displayed score text."""
        self._score_text_surf = FONT_20.render(f'{score}', True, BLACK)
        self._score_text_rect = self._score_text_surf.get_rect()
        self._score_text_rect.center = self._score_rect.center
        pg.draw.rect(self._screen, self._player.color, self._score_rect)
        self._screen.blit(self._score_text_surf, self._score_text_rect)

    def set_active(self) -> None:
        """Display the active arrow."""
        self._screen.blit(self._arrow_surf, self._arrow_rect)

    def set_inactive(self) -> None:
        """Deactivate the active arrow."""
        pg.draw.rect(self._screen, self._bg_color, self._arrow_rect)

    def reset(self) -> None:
        """Reset the score to zero."""
        self.update_score(0)

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
