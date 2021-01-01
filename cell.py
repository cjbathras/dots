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
        self._edge_top: Edge = None
        self._edge_bottom: Edge = None
        self._edge_left: Edge = None
        self._edge_right: Edge = None

    @property
    def captured(self) -> bool:
        return self._captured

    @property
    def captured_by(self) -> Player:
        return self._captured_by

    @property
    def edge_top(self) -> Edge:
        return self._edge_top

    @edge_top.setter
    def edge_top(self, val) -> None:
        self._edge_top = val

    @property
    def edge_bottom(self) -> Edge:
        return self._edge_bottom

    @edge_bottom.setter
    def edge_bottom(self, val) -> None:
        self._edge_bottom = val

    @property
    def edge_right(self) -> Edge:
        return self._edge_right

    @edge_right.setter
    def edge_right(self, val) -> None:
        self._edge_right = val

    @property
    def edge_left(self) -> Edge:
        return self._edge_left

    @edge_left.setter
    def edge_left(self, val) -> None:
        self._edge_left = val

    def handle_event(self, event: pg.event) -> None:
        return

    def draw(self) -> None:
        pg.draw.rect(self._screen, self._bg_color, self)

    def check_for_capture(self, player: Player) -> bool:
        if self._edge_top.captured and self._edge_bottom.captured \
            and self._edge_left.captured and self._edge_right.captured:

            self._captured = True
            self._captured_by = player
            self._bg_color = player.color
            self.draw()
            return True

        return False

    def __str__(self) -> str:
        return f'{type(self).__name__}: origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
