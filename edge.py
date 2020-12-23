import pygame as pg

from __init__ import *
from config import Config
from entity import Entity


class Edge(Entity):
    def __init__(self, origin: tuple, size: tuple, row: int, col: int,
        bg_color: pg.Color):

        super().__init__(origin, size, row, col, bg_color)
        self._cfg = Config()
        self.is_captured = False
        self.cell1 = None
        self.cell2 = None

    def draw(self) -> None:
        pg.draw.rect(self.screen, self.bg_color, self)
        pg.display.update(self)

    def highlight(self) -> None:
        if not self.is_captured:
            pg.draw.rect(self.screen, self._cfg.EDGE_COLOR_ACTIVATED, self,
                width=1)
            pg.display.update(self)

    def clear(self) -> None:
        self.draw()

    def capture(self) -> None:
        if not self.is_captured:
            self.is_captured = True
            self.bg_color = self._cfg.EDGE_COLOR_ACTIVATED
            self.draw()
            return True
        return False

    def __str__(self) -> str:
        if self.cell1 and self.cell2:
            return f'{type(self).__name__}[{self.row},{self.col}]: ' \
                f'origin={self.topleft} size={self.size} ' \
                f'cell_1={self.cell1.row},{self.cell1.col} ' \
                f'cell_2={self.cell2.row},{self.cell2.col}'
        elif self.cell1:
            return f'{type(self).__name__}[{self.row},{self.col}]: ' \
                f'origin={self.topleft} size={self.size} ' \
                f'cell_1={self.cell1.row},{self.cell1.col} cell_2=None'
        elif self.cell2:
            return f'{type(self).__name__}[{self.row},{self.col}]: ' \
                f'origin={self.topleft} size={self.size} ' \
                f'cell_1=None cell_2={self.cell2.row},{self.cell2.col}'
        else:
            return f'{type(self).__name__}[{self.row},{self.col}]: ' \
                f'origin={self.topleft} size={self.size} ' \
                f'cell_1=None cell_2=None'

    def __repr__(self) -> str:
        return repr(self)
