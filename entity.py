from abc import ABCMeta, abstractmethod

import pygame as pg

from __init__ import *


class Entity(pg.Rect, metaclass=ABCMeta):
    def __init__(self, origin: tuple, size: tuple, row: int, col: int,
        bg_color: pg.Color):

        super().__init__(origin, size)
        self.row = row
        self.col = col
        self.bg_color = bg_color
        self.screen = pg.display.get_surface()

    @abstractmethod
    def draw(self): pass
