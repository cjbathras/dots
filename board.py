import pygame as pg

from __init__ import *
from __init__ import is_even
from __init__ import is_odd
from __init__ import TupleOrInt

# from entity import Entity
from cell import Cell
from config import Config
from dot import Dot
from edge import Edge
from entity import Entity


class Board:
    def __init__(self):
        super().__init__()
        self.cfg = Config()

        # A 2D array holding all of the entities that comprise the board
        # Size is 2*ROWS+1 x 2*COLS+1
        self.board = []

        # extents dictionaries are used for quickly identifying which entity
        # encloses a location
        # dictionary to hold the extents of each row in the board
        # the key is the row number and the value is a tuple of (top, bottom)
        self._row_extents = {}

        # dictionary to hold the extents of each col in the board
        # the key is the column number and the value is a tuple of (left, right)
        self._col_extents = {}

        # A list containing all entities for redrawing the entire board
        self._entities = []

        entity = None
        for r in range(0, (2 * self.cfg.ROWS + 1)):
            row = []
            for c in range(0, (2 * self.cfg.COLS + 1)):
                if is_even(r) and is_even(c):
                    # dot
                    size = (self.cfg.DOT_DIA, self.cfg.DOT_DIA)
                    origin = (
                        c // 2 * self.cfg.DOT_DIA
                        + c // 2 * self.cfg.CELL_WIDTH
                        + self.cfg.GUTTER_LEFT,

                        r // 2 * self.cfg.DOT_DIA
                        + r // 2 * self.cfg.CELL_HEIGHT
                        + self.cfg.GUTTER_TOP * 2
                        + self.cfg.SCOREBOARD_HEIGHT
                    )
                    entity = Dot(origin, size, r, c, self.cfg.DOT_COLOR)

                elif is_odd(r) and is_odd(c):
                    # cell
                    size = self.cfg.CELL_SIZE
                    origin = (
                        (c + 1) // 2 * self.cfg.EDGE_THICKNESS
                        + (c - 1) // 2 * self.cfg.CELL_WIDTH
                        + self.cfg.GUTTER_LEFT,

                        (r + 1) // 2 * self.cfg.EDGE_THICKNESS
                        + (r - 1) // 2 * self.cfg.CELL_HEIGHT
                        + self.cfg.GUTTER_TOP * 2
                        + self.cfg.SCOREBOARD_HEIGHT
                    )
                    entity = Cell(origin, size, r, c,
                        self.cfg.CELL_COLOR_DEFAULT)

                else:
                    # edge
                    if is_even(r):
                        size = (self.cfg.CELL_WIDTH, self.cfg.EDGE_THICKNESS)
                        origin = (
                            (c + 1) // 2 * self.cfg.DOT_DIA
                            + (c - 1) // 2 * self.cfg.CELL_WIDTH
                            + self.cfg.GUTTER_LEFT,

                            r // 2 * self.cfg.DOT_DIA
                            + r // 2 * self.cfg.CELL_HEIGHT
                            + self.cfg.GUTTER_TOP * 2
                            + self.cfg.SCOREBOARD_HEIGHT
                        )
                        entity = Edge(origin, size, r, c,
                            self.cfg.EDGE_COLOR_DEFAULT)
                    else:
                        size = (self.cfg.EDGE_THICKNESS, self.cfg.CELL_HEIGHT)
                        origin = (
                            c // 2 * self.cfg.DOT_DIA
                            + c // 2 * self.cfg.CELL_WIDTH
                            + self.cfg.GUTTER_LEFT,

                            (r + 1) // 2 * self.cfg.DOT_DIA
                            + r // 2 * self.cfg.CELL_HEIGHT
                            + self.cfg.GUTTER_TOP * 2
                            + self.cfg.SCOREBOARD_HEIGHT
                        )
                        entity = Edge(origin, size, r, c,
                            self.cfg.EDGE_COLOR_DEFAULT)

                row.append(entity)
                self._entities.append(entity)

                if r == 0:
                    self._col_extents[c] = (entity.left, entity.right)

            self.board.append(row)
            self._row_extents[r] = (entity.top, entity.bottom)

        # Now that all the entities have been created, it's time to establish
        # all of the connection relationships between them.
        self._establish_connections()

    def __getitem__(self, coord: TupleOrInt) -> Entity:
        if coord is None:
            return None

        if isinstance(coord, tuple):
            return self.board[coord[0]][coord[1]]
        else:
            return self.board[coord]

    def get_row_col(self, pos: tuple) -> tuple:
        x, y = pos
        row, col = None, None
        for c, extents in self._col_extents.items():
            left, right = extents
            if left <= x < right:
                col = c
                break

        if col is not None:
            for r, extents in self._row_extents.items():
                top, bottom = extents
                if top <= y < bottom:
                    row = r
                    break
            if row is not None:
                return row, col

        return None

    def _establish_connections(self) -> None:
        for row in self.board:
            for entity in row:
                r, c = entity.row, entity.col
                if isinstance(entity, Cell):
                    # Every cell will always have four edges
                    entity.edge_top = self.board[r-1][c]
                    entity.edge_bottom = self.board[r+1][c]
                    entity.edge_left = self.board[r][c-1]
                    entity.edge_right = self.board[r][c+1]
                elif isinstance(entity, Edge):
                    # Depending on location in the board,
                    if r == 0: # top row of board
                        entity.cell1 = None
                        entity.cell2 = self.board[r+1][c]
                    elif r == 2 * self.cfg.ROWS: # bottom row of board
                        entity.cell1 = self.board[r-1][c]
                        entity.cell2 = None
                    elif c == 0: # left column of board
                        entity.cell1 = None
                        entity.cell2 = self.board[r][c+1]
                    elif c == 2 * self.cfg.COLS: # right column of board
                        entity.cell1 = self.board[r][c-1]
                        entity.cell2 = None
                    elif is_even(r): # horizontal edge
                        entity.cell1 = self.board[r-1][c]
                        entity.cell2 = self.board[r+1][c]
                    else: # vertical edge
                        entity.cell1 = self.board[r][c-1]
                        entity.cell2 = self.board[r][c+1]

    def draw(self) -> None:
        for e in self._entities:
            e.draw()
        pg.display.update(self._entities)

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'{len(self.board[0])}x{len(self.board)} entities'

    def __repr__(self) -> str:
        return str(self)
