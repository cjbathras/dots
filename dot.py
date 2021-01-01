import pygame as pg

from __init__ import *
from entity import Entity


class Dot(Entity):
    def __init__(self, pos: tuple, size: tuple, bg_color: pg.Color):

        super().__init__(pos, size, bg_color)

    def draw(self) -> None:
        pg.draw.rect(self._screen, self._bg_color, self)

    def handle_event(self, event: pg.event) -> None:
        return

    def __str__(self) -> str:
        return f'{type(self).__name__}: origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
