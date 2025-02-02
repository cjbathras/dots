"""An abstract base class representing entities in the game board in the game of
Dots."""

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

from abc import ABCMeta, abstractmethod

import pygame as pg


class Entity(pg.Rect, metaclass=ABCMeta):
    """The Entity class derives from the Pygame Rect class so it has all of the
    functionality of a Rect. This base class is used by the Dot, Edge, and Cell
    child classes.
    """
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
        """Get the background color of the entity."""
        return self._bg_color

