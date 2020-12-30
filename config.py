import pygame as pg

from __init__ import *
from singleton import Singleton


class Config(metaclass=Singleton):
    def __init__(self, cell_rows: int=5, cell_cols: int=5,
        cell_size: tuple=(100, 100), num_players: int=2, dot_radius: int=6,
        gutter_width: int=0):

        self._cell_rows: int = cell_rows
        self._cell_cols: int = cell_cols
        self._cell_size: tuple = cell_size
        self._num_players: int = num_players
        self._dot_rad: int = dot_radius
        # Gutter is the empty spacing surrounding the drawn components to offset
        # them from the display window.
        self._gutter_width: int = gutter_width

    @property
    def BANNER_WIDTH(self) -> int:
        return self.MIN_ALLOWABLE_SCREEN_WIDTH - 100

    @property
    def BANNER_HEIGHT(self) -> int:
        return 70

    @property
    def BANNER_SIZE(self) -> tuple:
        return (self.BANNER_WIDTH, self.BANNER_HEIGHT)

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
    def SCOREBOARD_WIDTH(self) -> int:
        return self.SCREEN_WIDTH - self.GUTTER_WIDTH*2

    @property
    def SCOREBOARD_HEIGHT(self) -> int:
        return self.SCOREBOARD_ROWS * self.SCOREBOX_HEIGHT + \
            (self.SCOREBOARD_ROWS + 1) * GAP_20

    @property
    def SCOREBOARD_SIZE(self) -> tuple:
        return (self.SCOREBOARD_WIDTH, self.SCOREBOARD_HEIGHT)

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
    def SCOREBOX_WIDTH(self) -> int:
        return 174

    @property
    def SCOREBOX_HEIGHT(self) -> int:
        return 40

    @property
    def SCOREBOX_SIZE(self) -> tuple:
        return (self.SCOREBOX_WIDTH, self.SCOREBOX_HEIGHT)

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
            f'{type(self).__name__}:\n'
            # f'  min_screen_width={self.MIN_ALLOWABLE_SCREEN_WIDTH}\n' \
            # f'  rows={self.CELL_ROWS}\n' \
            # f'  cols={self.CELL_COLS}\n' \
            # f'  cell_size={self.CELL_SIZE}\n' \
            # f'  cell_width={self.CELL_WIDTH}\n' \
            # f'  cell_height={self.CELL_HEIGHT}\n' \
            # f'  cell_color_default={self.CELL_COLOR_DEFAULT}\n' \
            # f'  dot_rad={self.DOT_RAD}\n' \
            # f'  dot_dia={self.DOT_DIA}\n' \
            # f'  dot_color={self.DOT_COLOR}\n' \
            # f'  edge_thickness={self.EDGE_THICKNESS}\n' \
            # f'  edge_color_default={self.EDGE_COLOR_DEFAULT}\n' \
            # f'  edge_color_captured={self.EDGE_COLOR_ACTIVATED}\n' \
            # f'  gutter_width={self.GUTTER_WIDTH}\n' \
            # f'  scoreboard_origin={self.SCOREBOARD_ORIGIN}\n' \
            # f'  scoreboard_size={self.SCOREBOARD_SIZE}\n' \
            # f'  scoreboard_width={self.SCOREBOARD_WIDTH}\n' \
            # f'  scoreboard_height={self.SCOREBOARD_HEIGHT}\n' \
            # f'  scorebox_width={self.SCOREBOX_WIDTH}\n' \
            # f'  scorebox_height={self.SCOREBOX_HEIGHT}\n' \
            # f'  banner_origin={self.BANNER_ORIGIN}\n' \
            # f'  banner_size={self.BANNER_SIZE}\n' \
            # f'  banner_width={self.BANNER_WIDTH}\n' \
            # f'  banner_height={self.BANNER_HEIGHT}'

    def __repr__(self) -> str:
        return f'{type(self).__name__}'
