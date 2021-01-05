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

from edge import Edge
from entity import Entity
from player import Player


class Cell(Entity):
    def __init__(self, pos: tuple, size: tuple, bg_color: pg.Color):

        super().__init__(pos, size, bg_color)
        self._captured: bool = False
        self._edge_top: Edge = None
        self._edge_bottom: Edge = None
        self._edge_left: Edge = None
        self._edge_right: Edge = None

    @property
    def captured(self) -> bool:
        return self._captured

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
            self._bg_color = player.color
            self.draw()
            return True

        return False

    def __str__(self) -> str:
        return f'{type(self).__name__}: origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
