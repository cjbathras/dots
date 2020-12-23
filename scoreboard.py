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
        self._scoreboxes = []
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
                count += 1
                self._scoreboxes.append(sb)

    def draw(self) -> None:
        if SHOW_OUTLINE:
            pg.draw.rect(self._screen, RED, self._rect, width=1)
        pg.draw.rect(self._screen, self._bg_color, self._rect)
        pg.draw.rect(self._screen, GRAY, self._rect, width=1)
        for sb in self._scoreboxes:
            sb.draw()

        pg.display.update(self._rect)

    def set_active_box(self, player: Player) -> None:
        self._screen.blit(self._arrow, self._active_boxes[player])
        pg.draw.rect(self._screen, self._bg_color, self.prev_active_box)
        pg.display.update(self._active_boxes[player])
        pg.display.update(self.prev_active_box)
        self.prev_active_box = self._active_boxes[player]

    def update_score(self, player: Player) -> None:
        if player == self._game._players[0]:
            pg.draw.rect(self._screen,
                self._game._players[0].color, self.p1_scorebox)
            self.p1_score_text = FONT_20.render( \
                f'{self._game.get_score(player)}', True, BLACK)
            self.p1_score_rect = self.p1_score_text.get_rect()
            self.p1_score_rect.center = self.p1_scorebox.center
            self._screen.blit(self.p1_score_text, self.p1_score_rect)
            pg.display.update(self.p1_score_rect)

        else:
            pg.draw.rect(self._screen,
                self._game._players[1].color, self.p2_scorebox)
            self.p2_score_text = FONT_20.render( \
                f'{self._game.get_score(player)}', True, BLACK)
            self.p2_score_rect = self.p2_score_text.get_rect()
            self.p2_score_rect.center = self.p2_scorebox.center
            self._screen.blit(self.p2_score_text, self.p2_score_rect)
            pg.display.update(self.p2_score_rect)

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
