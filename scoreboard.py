import pygame as pg

from __init__ import *
from config import Config
from game import Game
from player import Player
from scorebox import Scorebox
import scorebox


class Scoreboard:
    def __init__(self, pos: tuple, size: tuple, bg_color: pg.Color, game: Game):
        super().__init__()
        self._cfg = Config()
        self._rect = pg.Rect(pos, size)
        self._pos = pos
        self._size = size
        self._bg_color = bg_color
        self._game = game
        self._screen = pg.display.get_surface()
        self._scoreboxes = {}
        x, y = self._pos

        num_rows = self._cfg.SCOREBOARD_ROWS
        o_gap = GAP_20 * 2

        if self._cfg.SCOREBOARD_ROWS == 1:
            scorebox_widths = self._cfg.SCOREBOX_WIDTH * self._cfg.NUM_PLAYERS
            i_gap = (self._cfg.SCOREBOARD_WIDTH - o_gap - scorebox_widths) \
                // (self._cfg.NUM_PLAYERS - 1)
            iter = self._cfg.NUM_PLAYERS
        else:
            scorebox_widths = self._cfg.SCOREBOX_WIDTH * 2
            i_gap = self._cfg.SCOREBOARD_WIDTH - o_gap - scorebox_widths
            iter = 2

        count = 0
        for row in range(0, self._cfg.SCOREBOARD_ROWS):
            for col in range(0, iter):
                sb = Scorebox(
                    (x + GAP_20 + self._cfg.SCOREBOX_WIDTH*(count-row*2) + i_gap*(count-row*2),
                    y + GAP_20 + self._cfg.SCOREBOX_HEIGHT*row + row*GAP_20),
                    self._game.players[count])
                self._scoreboxes[self._game.players[count]] = sb
                count += 1

        self.draw()

    def draw(self) -> None:
        if SHOW_OUTLINE:
            pg.draw.rect(self._screen, RED, self._rect, width=1)
        pg.draw.rect(self._screen, self._bg_color, self._rect)
        pg.draw.rect(self._screen, GRAY, self._rect, width=1)
        for _, sb in self._scoreboxes.items():
            sb.draw()

        pg.display.update(self._rect)

    def set_active(self, player: Player) -> None:
        raise NotImplementedError()

    def update_score(self, player: Player, score: int) -> None:
        self._scoreboxes[player].update_score(score)

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
