import pygame as pg

from __init__ import *
from game import Game
from player import Player
from scorebox import Scorebox
import scorebox

GAP = 20


class Scoreboard:
    def __init__(self, pos: tuple, size: tuple, bg_color: pg.Color, game: Game):
        super().__init__()
        self._rect = pg.Rect(pos, size)
        self._pos = pos
        self._size = size
        self._bg_color = bg_color
        self._game = game
        self._screen = pg.display.get_surface()
        self._scoreboxes = []
        x, y = self._pos

        for count, player in enumerate(self._game.players):
            sb = Scorebox((x + GAP + count*scorebox.WIDTH, y + GAP), player)
            self._scoreboxes.append(sb)

    def draw(self) -> None:
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
