from abc import ABCMeta, abstractmethod

import pygame as pg

from __init__ import *


class Entity(pg.Rect, metaclass=ABCMeta):
    def __init__(self, pos: tuple, size: tuple, bg_color: pg.Color):

        super().__init__(pos, size)
        self._bg_color: pg.Color = bg_color
        self._screen: pg.Surface = pg.display.get_surface()

    @abstractmethod
    def draw(self) -> None: pass

    @abstractmethod
    def handle_event(self, event: pg.event) -> None: pass

    @property
    def bg_color(self) -> pg.Color:
        return self._bg_color
        
