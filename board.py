import pygame as pg

from __init__ import *
from __init__ import is_even
from __init__ import is_odd

from cell import Cell
from config import Config
from dot import Dot
from edge import Edge
from entity import Entity


class Board:
    def __init__(self):
        super().__init__()
        self._cfg = Config()

        # A 2D array holding all of the entities that comprise the board
        # Size is 2*ROWS+1 x 2*COLS+1
        self._board = []

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

        x_shift = (self._cfg.SCREEN_WIDTH - self._cfg.BOARD_WIDTH) // 2

        entity = None
        for r in range(0, (2 * self._cfg.CELL_ROWS + 1)):
            row = []
            for c in range(0, (2 * self._cfg.CELL_COLS + 1)):
                if is_even(r) and is_even(c):
                    # dot
                    size = (self._cfg.DOT_DIA, self._cfg.DOT_DIA)
                    pos = (
                        x_shift 
                        + c // 2 * self._cfg.DOT_DIA
                        + c // 2 * self._cfg.CELL_WIDTH,

                        r // 2 * self._cfg.DOT_DIA
                        + r // 2 * self._cfg.CELL_HEIGHT
                        + self._cfg.GUTTER_WIDTH * 2
                        + self._cfg.SCOREBOARD_HEIGHT
                    )
                    entity = Dot(pos, size, r, c, DOT_COLOR)

                elif is_odd(r) and is_odd(c):
                    # cell
                    size = self._cfg.CELL_SIZE
                    pos = (
                        x_shift 
                        + (c + 1) // 2 * self._cfg.EDGE_THICKNESS
                        + (c - 1) // 2 * self._cfg.CELL_WIDTH,

                        (r + 1) // 2 * self._cfg.EDGE_THICKNESS
                        + (r - 1) // 2 * self._cfg.CELL_HEIGHT
                        + self._cfg.GUTTER_WIDTH * 2
                        + self._cfg.SCOREBOARD_HEIGHT
                    )
                    entity = Cell(pos, size, r, c,
                        CELL_COLOR_DEFAULT)

                else:
                    # edge
                    if is_even(r):
                        size = (self._cfg.CELL_WIDTH, self._cfg.EDGE_THICKNESS)
                        pos = (
                            x_shift 
                            + (c + 1) // 2 * self._cfg.DOT_DIA
                            + (c - 1) // 2 * self._cfg.CELL_WIDTH,

                            r // 2 * self._cfg.DOT_DIA
                            + r // 2 * self._cfg.CELL_HEIGHT
                            + self._cfg.GUTTER_WIDTH * 2
                            + self._cfg.SCOREBOARD_HEIGHT
                        )
                        entity = Edge(pos, size, r, c,
                            EDGE_COLOR_DEFAULT)
                    else:
                        size = (self._cfg.EDGE_THICKNESS, self._cfg.CELL_HEIGHT)
                        pos = (
                            x_shift 
                            + c // 2 * self._cfg.DOT_DIA
                            + c // 2 * self._cfg.CELL_WIDTH,

                            (r + 1) // 2 * self._cfg.DOT_DIA
                            + r // 2 * self._cfg.CELL_HEIGHT
                            + self._cfg.GUTTER_WIDTH * 2
                            + self._cfg.SCOREBOARD_HEIGHT
                        )
                        entity = Edge(pos, size, r, c,
                            EDGE_COLOR_DEFAULT)

                row.append(entity)
                self._entities.append(entity)

                if r == 0:
                    self._col_extents[c] = (entity.left, entity.right)

            self._board.append(row)
            self._row_extents[r] = (entity.top, entity.bottom)

        # Now that all the entities have been created, it's time to establish
        # all of the connection relationships between them.
        self._establish_connections()

        self.draw()

    def get_entity(self, pos: tuple) -> Entity:
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
                return self._board[row][col]

        return None

    def _establish_connections(self) -> None:
        for row in self._board:
            for entity in row:
                r, c = entity.row, entity.col
                if isinstance(entity, Cell):
                    # Every cell will always have four edges
                    entity.edge_top = self._board[r-1][c]
                    entity.edge_bottom = self._board[r+1][c]
                    entity.edge_left = self._board[r][c-1]
                    entity.edge_right = self._board[r][c+1]
                elif isinstance(entity, Edge):
                    # Depending on location in the board,
                    if r == 0: # top row of board
                        entity.cell1 = None
                        entity.cell2 = self._board[r+1][c]
                    elif r == 2 * self._cfg.CELL_ROWS: # bottom row of board
                        entity.cell1 = self._board[r-1][c]
                        entity.cell2 = None
                    elif c == 0: # left column of board
                        entity.cell1 = None
                        entity.cell2 = self._board[r][c+1]
                    elif c == 2 * self._cfg.CELL_COLS: # right column of board
                        entity.cell1 = self._board[r][c-1]
                        entity.cell2 = None
                    elif is_even(r): # horizontal edge
                        entity.cell1 = self._board[r-1][c]
                        entity.cell2 = self._board[r+1][c]
                    else: # vertical edge
                        entity.cell1 = self._board[r][c-1]
                        entity.cell2 = self._board[r][c+1]

    def draw(self) -> None:
        for e in self._entities:
            e.draw()
        pg.display.update(self._entities)

    def __str__(self) -> str:
        return f'{type(self).__name__}: ' \
            f'{len(self._board[0])}x{len(self._board)} entities'

    def __repr__(self) -> str:
        return str(self)
