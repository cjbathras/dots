import pygame as pg

from __init__ import *
from edge import Edge
from entity import Entity
from player import Player


class Cell(Entity):
    def __init__(self, pos: tuple, size: tuple, bg_color: pg.Color):

        super().__init__(pos, size, bg_color)
        self._captured: bool = False
        self._captured_by: Player = None
        self._top: Edge = None
        self._bottom: Edge = None
        self._left: Edge = None
        self._right: Edge = None

    @property
    def captured(self) -> bool:
        return self._captured

    @property
    def captured_by(self) -> Player:
        return self._captured_by

    @property
    def top(self) -> Edge:
        return self._top

    @top.setter
    def top(self, val) -> None:
        self._top = val

    @property
    def bottom(self) -> Edge:
        return self._bottom

    @bottom.setter
    def bottom(self, val) -> None:
        self._bottom = val

    @property
    def right(self) -> Edge:
        return self._right

    @right.setter
    def right(self, val) -> None:
        self._right = val

    @property
    def left(self) -> Edge:
        return self._left

    @left.setter
    def left(self, val) -> None:
        self._left = val

    def handle_event(self, event: pg.event) -> None:
        return

    def draw(self) -> None:
        pg.draw.rect(self._screen, self._bg_color, self)
        # pg.display.update(self)

    def check_for_capture(self, player: Player) -> None:
        if self._top.is_captured and self._bottom.is_captured \
            and self._left.is_captured and self._right.is_captured:

            self._captured = True
            self._captured_by = player
            self._bg_color = player.color
            self.draw()

    def __str__(self) -> str:
        return f'{type(self).__name__}[{self.row},{self.col}]: ' \
            f'origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
