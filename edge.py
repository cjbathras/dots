import pygame as pg

from __init__ import *
from config import Config
from entity import Entity


class Edge(Entity):
    def __init__(self, pos: tuple, size: tuple, row: int, col: int,
        bg_color: pg.Color):

        super().__init__(pos, size, row, col, bg_color)
        self._cfg = Config()
        self._is_captured = False
        self._is_highlighted = False
        self._cell1 = None
        self._cell2 = None

    @property
    def is_captured(self) -> bool:
        return self._is_captured

    @property
    def is_highlighted(self) -> bool:
        return self._is_highlighted

    @property
    def cell1(self):
        return self._cell1

    @cell1.setter
    def cell1(self, val) -> None:
        self._cell1 = val

    @property
    def cell2(self):
        return self._cell2

    @cell2.setter
    def cell2(self, val) -> None:
        self._cell2 = val

    def draw(self) -> None:
        pg.draw.rect(self._screen, self._bg_color, self)
        if not self._is_captured:
            if self._is_highlighted:
                pg.draw.rect(self._screen, EDGE_COLOR_CAPTURED, self, width=1)
        pg.display.update(self)

    def capture(self) -> None:
        self._is_captured = True
        self._is_highlighted = False
        self._bg_color = EDGE_COLOR_CAPTURED

    def highlight(self) -> None:
        self._is_highlighted = True

    def clear(self) -> None:
        self._is_highlighted = False

    def handle_event(self, event: pg.event) -> None:
        if event.type == pg.MOUSEMOTION:
            self.highlight()
        
        elif event.type == pg.MOUSEBUTTONUP:
            self.capture()
            if self.cell1:
                self.cell1.check_for_capture(self._current_player)
            if self.cell2:
                self.cell2.check_for_capture(self._current_player)

        self.draw()

    def __str__(self) -> str:
        if self._cell1 and self._cell2:
            return f'{type(self).__name__}[{self.row},{self.col}]: ' \
                f'origin={self.topleft} size={self.size} ' \
                f'cell_1={self._cell1.row},{self._cell1.col} ' \
                f'cell_2={self._cell2.row},{self._cell2.col}'
        elif self._cell1:
            return f'{type(self).__name__}[{self.row},{self.col}]: ' \
                f'origin={self.topleft} size={self.size} ' \
                f'cell_1={self._cell1.row},{self._cell1.col} cell_2=None'
        elif self._cell2:
            return f'{type(self).__name__}[{self.row},{self.col}]: ' \
                f'origin={self.topleft} size={self.size} ' \
                f'cell_1=None cell_2={self._cell2.row},{self._cell2.col}'
        else:
            return f'{type(self).__name__}[{self.row},{self.col}]: ' \
                f'origin={self.topleft} size={self.size} ' \
                f'cell_1=None cell_2=None'

    def __repr__(self) -> str:
        return repr(self)
