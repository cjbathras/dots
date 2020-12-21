import pygame as pg

from __init__ import *
from entity import Entity
from player import Player


class Cell(Entity):
    def __init__(self, origin: tuple, size: tuple, row: int, col: int,
        bg_color: pg.Color):

        super().__init__(origin, size, row, col, bg_color)
        self.is_captured = False
        self.captured_by = None
        self.edge_top = None
        self.edge_bottom = None
        self.edge_left = None
        self.edge_right = None

    def draw(self) -> None:
        pg.draw.rect(self.screen, self.bg_color, self)
        pg.display.update(self)

    def check_for_capture(self, player: Player) -> bool:
        if self.edge_top.is_captured and self.edge_bottom.is_captured \
            and self.edge_left.is_captured and self.edge_right.is_captured:

            self.is_captured = True
            self.captured_by = player
            self.bg_color = player.color
            self.draw()
            return True

        return False

    def __str__(self) -> str:
        return f'{type(self).__name__}[{self.row},{self.col}]: ' \
            f'origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
