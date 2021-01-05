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
from singleton import Singleton


class Config(metaclass=Singleton):
    def __init__(self, cell_rows: int=5, cell_cols: int=5,
        cell_size: tuple=(100, 100), num_players: int=2, dot_radius: int=6,
        gutter_width: int=20):

        self._cell_rows: int = cell_rows
        self._cell_cols: int = cell_cols
        self._cell_size: tuple = cell_size
        self._num_players: int = num_players
        self._dot_rad: int = dot_radius
        # Gutter is the empty spacing surrounding the drawn components to offset
        # them from the display window.
        self._gutter_width: int = gutter_width

    @property
    def BANNER_SIZE(self) -> tuple:
        return (self.BANNER_WIDTH, self.BANNER_HEIGHT)

    @property
    def BANNER_WIDTH(self) -> int:
        return self.MIN_ALLOWABLE_SCREEN_WIDTH - 100

    @property
    def BANNER_HEIGHT(self) -> int:
        return 70

    @property
    def BOARD_SIZE(self) -> tuple:
        return (self.BOARD_WIDTH, self.BOARD_HEIGHT)

    @property
    def BOARD_WIDTH(self) -> int:
        return self.CELL_COLS * self.CELL_WIDTH \
            + (self.CELL_COLS + 1) * self.EDGE_THICKNESS

    @property
    def BOARD_HEIGHT(self) -> int:
        return self.CELL_ROWS * self.CELL_HEIGHT \
            + (self.CELL_ROWS + 1) * self.EDGE_THICKNESS

    @property
    def CELL_ROWS(self) -> int:
        return self._cell_rows

    @property
    def CELL_COLS(self) -> int:
        return self._cell_cols

    @property
    def CELL_SIZE(self) -> tuple:
        return self._cell_size

    @property
    def CELL_WIDTH(self) -> int:
        return self._cell_size[0]

    @property
    def CELL_HEIGHT(self) -> int:
        return self._cell_size[1]

    @property
    def DOT_RAD(self) -> int:
        return self._dot_rad

    @property
    def DOT_DIA(self) -> int:
        return self.DOT_RAD * 2

    @property
    def EDGE_THICKNESS(self) -> int:
        return self.DOT_DIA

    @property
    def GUTTER_WIDTH(self) -> int:
        return self._gutter_width

    @property
    def MIN_ALLOWABLE_SCREEN_WIDTH(self) -> int:
        multiplier = 3 if self.NUM_PLAYERS == 3 else 2
        return self.SCOREBOX_WIDTH * multiplier \
            + GAP_30 * (multiplier - 1) + GAP_20 * 2 + self.GUTTER_WIDTH * 2

    @property
    def NUM_PLAYERS(self) -> int:
        return self._num_players

    @property
    def SCOREBOARD_ORIGIN(self) -> tuple:
        return (self.GUTTER_WIDTH, self.GUTTER_WIDTH)

    @property
    def SCOREBOARD_SIZE(self) -> tuple:
        return (self.SCOREBOARD_WIDTH, self.SCOREBOARD_HEIGHT)

    @property
    def SCOREBOARD_WIDTH(self) -> int:
        return self.SCREEN_WIDTH - self.GUTTER_WIDTH*2

    @property
    def SCOREBOARD_HEIGHT(self) -> int:
        return self.SCOREBOARD_ROWS * self.SCOREBOX_HEIGHT + \
            (self.SCOREBOARD_ROWS + 1) * GAP_20

    @property
    def SCOREBOARD_ROWS(self) -> int:
        one_line_width = self.SCOREBOX_WIDTH * self.NUM_PLAYERS \
            + GAP_20 * 2 + GAP_30 * (self.NUM_PLAYERS - 1)

        if self.NUM_PLAYERS == 2:
            return 1
        else:
            if self.SCREEN_WIDTH < one_line_width:
                return 2
            else:
                return 1

    @property
    def SCOREBOX_SIZE(self) -> tuple:
        return (self.SCOREBOX_WIDTH, self.SCOREBOX_HEIGHT)

    @property
    def SCOREBOX_WIDTH(self) -> int:
        return 174

    @property
    def SCOREBOX_HEIGHT(self) -> int:
        return 40

    @property
    def SCREEN_SIZE(self) -> tuple:
        return (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    @property
    def SCREEN_WIDTH(self) -> int:
        potential_width = self.BOARD_WIDTH + self.GUTTER_WIDTH * 2
        return max(potential_width, self.MIN_ALLOWABLE_SCREEN_WIDTH)

    @property
    def SCREEN_HEIGHT(self) -> int:
        return self.CELL_ROWS * self.CELL_HEIGHT \
            + (self.CELL_ROWS + 1) * self.EDGE_THICKNESS \
            + self.GUTTER_WIDTH * 2 \
            + self.SCOREBOARD_HEIGHT + GAP_20

    @property
    def SCREEN_CENTER(self) -> tuple:
        return (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)

    def __str__(self) -> str:
        return \
            f'{type(self).__name__}:\n' \
            f'  BANNER_SIZE={self.BANNER_SIZE}\n' \
            f'  BOARD_SIZE={self.BOARD_SIZE}\n' \
            f'  CELL_ROWS={self.CELL_ROWS}\n' \
            f'  CELL_COLS={self.CELL_COLS}\n' \
            f'  CELL_SIZE={self.CELL_SIZE}\n' \
            f'  DOT_DIA={self.DOT_DIA}\n' \
            f'  EDGE_THICKNESS={self.EDGE_THICKNESS}\n' \
            f'  GUTTER_WIDTH={self.GUTTER_WIDTH}\n' \
            f'  MIN_ALLOWABLE_SCREEN_WIDTH={self.MIN_ALLOWABLE_SCREEN_WIDTH}\n' \
            f'  NUM_PLAYERS={self.NUM_PLAYERS}\n' \
            f'  SCOREBOARD_ORIGIN={self.SCOREBOARD_ORIGIN}\n' \
            f'  SCOREBOARD_SIZE={self.SCOREBOARD_SIZE}\n' \
            f'  SCOREBOARD_ROWS={self.SCOREBOARD_ROWS}\n' \
            f'  SCOREBOX_SIZE={self.SCOREBOX_SIZE}\n' \
            f'  SCREEN_SIZE={self.SCREEN_SIZE}\n' \
            f'  SCREEN_CENTER={self.SCREEN_CENTER}\n'

    def __repr__(self) -> str:
        return f'{type(self).__name__}'
