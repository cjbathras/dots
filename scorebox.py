import pygame as pg

from __init__ import *
from game import Game
from player import Player

GAP = 20
WIDTH = 150
HEIGHT = 40


class Scorebox:
    def __init__(self, pos: tuple, player: Player):
        super().__init__()
        self._bg_color = LIGHT_GRAY
        self._pos = pos
        self._player = player
        self._size = (WIDTH, HEIGHT)
        self._screen = pg.display.get_surface()

        self._rect = pg.Rect(pos, self._size)

        self._arrow_surf = pg.image.load('left-arrow-24.png')
        self._arrow_rect = self._arrow_surf.get_rect()
        self._arrow_rect.left = self._rect.right - self._arrow_rect.width
        self._arrow_rect.centery = self._rect.centery

        self._score_rect = pg.Rect(
            self._rect.right - self._arrow_rect.width - 24,
            self._rect.top + 6,
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
        return self._size

    @property
    def pos(self) -> tuple:
        return self._pos

    def draw(self) -> None:
        pg.draw.rect(self._screen, self._player.color, self._score_rect)
        self._screen.blit(self._score_text_surf, self._score_text_rect)
        self._screen.blit(self._name_text_surf, self._name_text_rect)

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
    