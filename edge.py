# Copyright 2021 Curt Bathras
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pygame as pg

from __init__ import *
from config import Config
from entity import Entity


class Edge(Entity):
    def __init__(self, pos: tuple, size: tuple, bg_color: pg.Color):

        super().__init__(pos, size, bg_color)
        self._cfg = Config()
        self._captured = False
        self._highlighted = False
        self._cell1 = None
        self._cell2 = None

    @property
    def captured(self) -> bool:
        return self._captured

    @property
    def highlighted(self) -> bool:
        return self._highlighted

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
        if not self._captured:
            if self._highlighted:
                pg.draw.rect(self._screen, EDGE_COLOR_CAPTURED, self, width=1)

    def clear(self) -> None:
        self._highlighted = False
        self.draw()

    def handle_event(self, event: pg.event) -> None:
        if event.type == pg.MOUSEMOTION:
            self._highlighted = True

        elif event.type == pg.MOUSEBUTTONUP:
            if not self._captured:
                self._captured = True
                self._highlighted = False
                self._bg_color = EDGE_COLOR_CAPTURED

        self.draw()

    def __str__(self) -> str:
        return f'{type(self).__name__}: origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return repr(self)
