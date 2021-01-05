"""A location in 2D space in the game of Dots."""

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

from entity import Entity


class Dot(Entity):
    """Players try to connect Dot objects to each to try and capture cells. It
    represents a location in 2D space. The Dot class derives from the Entity
    abstract base class which in turns derives from the Pygame Rect class so
    every Dot is also a Rect.
    """
    def __init__(self, pos: tuple, size: tuple, bg_color: pg.Color):

        super().__init__(pos, size, bg_color)

    def draw(self) -> None:
        """Draw the dot to the screen."""
        pg.draw.rect(self._screen, self._bg_color, self)

    def handle_event(self, event: pg.event) -> None:
        """No-op implemenation because a dot handles no events."""
        return

    def __str__(self) -> str:
        return f'{type(self).__name__}: origin={self.topleft} size={self.size}'

    def __repr__(self) -> str:
        return str(self)
