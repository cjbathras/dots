from __init__ import *
from singleton import Singleton


class Config(metaclass=Singleton):
    def __init__(self, rows=5, cols=5, cell_size=(100, 100), dot_radius=5,
                gutter_top=20, gutter_bottom=20, gutter_left=20, gutter_right=20,
                scoreboard_height=70, footer_height=70):
        # Anything that should be gettable/settable should be defined here
        # Anything that should only be gettable because it depends on another
        # value, should be defined with a @property decorator

        self.ROWS = rows
        self.COLS = cols

        # Cell attributes
        self.CELL_SIZE = cell_size
        self.CELL_COLOR_DEFAULT = WHITE

        # Dot attributes
        self.DOT_RAD = dot_radius
        self.DOT_COLOR = BLACK

        # Edge attributes
        self.EDGE_COLOR_DEFAULT = LIGHT_GRAY
        self.EDGE_COLOR_ACTIVATED = pygame.Color(125, 125, 255)

        # Gutter attributes
        self.GUTTER_TOP    = gutter_top
        self.GUTTER_BOTTOM = gutter_bottom
        self.GUTTER_LEFT   = gutter_left
        self.GUTTER_RIGHT  = gutter_right

        # Scoreboard attributes
        self.SCOREBOARD_HEIGHT = scoreboard_height

        # Footer attributes
        self.FOOTER_HEIGHT = footer_height

    @property
    def DOT_DIA(self):
        return self.DOT_RAD * 2

    @property
    def CELL_WIDTH(self):
        return self.CELL_SIZE[0]

    @property
    def CELL_HEIGHT(self):
        return self.CELL_SIZE[1]

    @property
    def EDGE_THICKNESS(self):
        return self.DOT_DIA

    @property
    def SCOREBOARD_ORIGIN(self):
        return (self.GUTTER_LEFT, self.GUTTER_TOP)

    @property
    def SCOREBOARD_WIDTH(self):
        return self.COLS * self.CELL_WIDTH + (self.COLS + 1) * self.EDGE_THICKNESS

    @property
    def SCOREBOARD_SIZE(self):
        return (self.SCOREBOARD_WIDTH, self.SCOREBOARD_HEIGHT)

    @property
    def FOOTER_ORIGIN(self):
        return (self.GUTTER_LEFT, self.GUTTER_TOP * 2 + self.SCOREBOARD_HEIGHT + self.ROWS * self.CELL_WIDTH + (self.ROWS + 1) * self.EDGE_THICKNESS + self.GUTTER_BOTTOM)

    @property
    def FOOTER_WIDTH(self):
        return self.SCOREBOARD_WIDTH

    @property
    def FOOTER_SIZE(self):
        return (self.FOOTER_WIDTH, self.FOOTER_HEIGHT)
