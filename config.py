import pygame

from __init__ import *
from singleton import Singleton


class Config(metaclass=Singleton):
    def __init__(self, rows: int=5, cols: int=5, cell_size: tuple=(100, 100), 
        dot_radius: int=5, gutter_top: int=20, gutter_bottom: int=20, 
        gutter_left: int=20, gutter_right: int=20, scoreboard_height: int=70, 
        banner_height: int=70):
        # Anything that should be gettable/settable should be defined here
        # Anything that should only be gettable because it depends on another
        # value, should be defined with the @property decorator

        """Number of rows of cells"""
        self.ROWS: int = rows
        """Number of columns of cells"""
        self.COLS: int = cols

        """2D size of a cell in pixels"""
        self.CELL_SIZE: tuple = cell_size
        """Default background color of a cell"""
        self.CELL_COLOR_DEFAULT: pygame.Color = WHITE

        """Radius of a dot"""
        self.DOT_RAD: int = dot_radius
        """Color of a dot"""
        self.DOT_COLOR: pygame.Color = BLACK

        """Default background color of an edge"""
        self.EDGE_COLOR_DEFAULT: pygame.Color = LIGHT_GRAY
        """Color of an edge when it has been captured (i.e. clicked on by a 
        player)"""
        self.EDGE_COLOR_ACTIVATED: pygame.Color = pygame.Color(125, 125, 255)

        # Gutter is the empty spacing surrounding the drawn components to offset
        # them from the display window.
        """Width of top gutter, in pixels"""
        self.GUTTER_TOP: int    = gutter_top
        """Width of bottom gutter, in pixels"""
        self.GUTTER_BOTTOM: int = gutter_bottom
        """Width of left gutter, in pixels"""
        self.GUTTER_LEFT: int   = gutter_left
        """Width of right gutter, in pixels"""
        self.GUTTER_RIGHT: int  = gutter_right

        """Height of the scoreboard, in pixels"""
        self.SCOREBOARD_HEIGHT: int = scoreboard_height

        """Height of the banner, in pixels"""
        self.BANNER_HEIGHT: int = banner_height

    @property
    def DOT_DIA(self) -> int:
        return self.DOT_RAD * 2

    @property
    def CELL_WIDTH(self) -> int:
        return self.CELL_SIZE[0]

    @property
    def CELL_HEIGHT(self) -> int:
        return self.CELL_SIZE[1]

    @property
    def EDGE_THICKNESS(self) -> int:
        return self.DOT_DIA

    @property
    def SCOREBOARD_ORIGIN(self) -> tuple:
        return (self.GUTTER_LEFT, self.GUTTER_TOP)

    @property
    def SCOREBOARD_WIDTH(self) -> int:
        return self.COLS * self.CELL_WIDTH \
            + (self.COLS + 1) * self.EDGE_THICKNESS

    @property
    def SCOREBOARD_SIZE(self) -> tuple:
        return (self.SCOREBOARD_WIDTH, self.SCOREBOARD_HEIGHT)

    @property
    def BANNER_ORIGIN(self) -> tuple:
        return (
            self.GUTTER_LEFT, 
            
            self.GUTTER_TOP * 2 
            + self.SCOREBOARD_HEIGHT 
            + self.ROWS * self.CELL_WIDTH 
            + (self.ROWS + 1) * self.EDGE_THICKNESS 
            + self.GUTTER_BOTTOM
        )

    @property
    def BANNER_WIDTH(self) -> int:
        return self.SCOREBOARD_WIDTH - 60

    @property
    def BANNER_SIZE(self) -> tuple:
        return (self.BANNER_WIDTH, self.BANNER_HEIGHT)

    def __str__(self) -> str:
        return \
            f'{type(self).__name__}:\n' \
            f'  rows={self.ROWS}\n  cols={self.COLS}\n' \
            f'  cell_size={self.CELL_SIZE}\n  cell_width={self.CELL_WIDTH}\n' \
            f'  cell_height={self.CELL_HEIGHT}\n' \
            f'  cell_color_default={self.CELL_COLOR_DEFAULT}\n' \
            f'  dot_rad={self.DOT_RAD}\n  dot_dia={self.DOT_DIA}\n' \
            f'  dot_color={self.DOT_COLOR}\n' \
            f'  edge_thickness={self.EDGE_THICKNESS}\n' \
            f'  edge_color_default={self.EDGE_COLOR_DEFAULT}\n' \
            f'  edge_color_captured={self.EDGE_COLOR_ACTIVATED}\n' \
            f'  gutter_top={self.GUTTER_TOP}\n' \
            f'  gutter_bottom={self.GUTTER_BOTTOM}\n'\
            f'  gutter_left={self.GUTTER_LEFT}\n' \
            f'  gutter_right={self.GUTTER_RIGHT}\n' \
            f'  scoreboard_origin={self.SCOREBOARD_ORIGIN}\n' \
            f'  scoreboard_size={self.SCOREBOARD_SIZE}\n' \
            f'  scoreboard_width={self.SCOREBOARD_WIDTH}\n' \
            f'  scoreboard_height={self.SCOREBOARD_HEIGHT}\n' \
            f'  banner_origin={self.BANNER_ORIGIN}\n' \
            f'  banner_size={self.BANNER_SIZE}\n' \
            f'  banner_width={self.BANNER_WIDTH}\n' \
            f'  banner_height={self.BANNER_HEIGHT}'

    def __repr__(self) -> str:
        return f'{type(self).__name__}'
