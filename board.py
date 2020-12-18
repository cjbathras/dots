import pygame

from __init__ import *
# from entity import Entity
from cell import Cell
from dot import Dot
from edge import Edge


class Board:
    def __init__(self):
        super().__init__()

        # A 2D array holding all of the entities that comprise the board
        # Size is 2*ROWS+1 x 2*COLS+1
        self.board = []

        # extents dictionaries are used for quickly identifying which entity
        # encloses a location
        # dictionary to hold the extents of each row in the board
        # the key is the row number and the value is a tuple of (top, bottom)
        self.row_extents = {}

        # dictionary to hold the extents of each col in the board
        # the key is the column number and the value is a tuple of (left, right)
        self.col_extents = {}

        # A list of all of the dots in left to right and top to bottom order
        # self.dots = []

        # A list of all of the cells in left to right and top to bottom order
        # self.cells = []

        # A list of all of the edges in left to right and top to bottom order
        # self.edges = []

        for r in range(0, (2 * ROWS + 1)):
            row = []
            for c in range(0, (2 * COLS + 1)):
                if is_even(r) and is_even(c):
                    # dot
                    size = (DOT_DIA, DOT_DIA)
                    origin = (c // 2 * DOT_DIA + c // 2 * CELL_WIDTH + GUTTER_LEFT,
                              r // 2 * DOT_DIA + r // 2 * CELL_HEIGHT + GUTTER_TOP * 2 + SCOREBOARD_HEIGHT)
                    entity = Dot(origin, size, r, c, DOT_COLOR)
                    #self.dots.append(entity)

                elif is_odd(r) and is_odd(c):
                    # cell
                    size = CELL_SIZE
                    origin = ((c + 1) // 2 * EDGE_THICKNESS + (c - 1) // 2 * CELL_WIDTH + GUTTER_LEFT,
                              (r + 1) // 2 * EDGE_THICKNESS + (r - 1) // 2 * CELL_HEIGHT + GUTTER_TOP * 2 + SCOREBOARD_HEIGHT)
                    entity = Cell(origin, size, r, c, CELL_COLOR_DEFAULT)
                    #self.cells.append(entity)

                else:
                    # edge
                    if is_even(r):
                        size = (CELL_WIDTH, EDGE_THICKNESS)
                        origin = ((c + 1) // 2 * DOT_DIA + (c - 1) // 2 * CELL_WIDTH + GUTTER_LEFT,
                                  r // 2 * DOT_DIA + r // 2 * CELL_HEIGHT + GUTTER_TOP * 2 + SCOREBOARD_HEIGHT)
                        entity = Edge(origin, size, r, c, EDGE_COLOR_DEFAULT)
                    else:
                        size = (EDGE_THICKNESS, CELL_HEIGHT)
                        origin = (c // 2 * DOT_DIA + c // 2 * CELL_WIDTH + GUTTER_LEFT,
                                  (r + 1) // 2 * DOT_DIA + r // 2 * CELL_HEIGHT + GUTTER_TOP * 2 + SCOREBOARD_HEIGHT)
                        entity = Edge(origin, size, r, c, EDGE_COLOR_DEFAULT)
                    #self.edges.append(entity)

                row.append(entity)

                if r == 0:
                    self.col_extents[c] = (entity.left, entity.right)

            self.board.append(row)
            self.row_extents[r] = (entity.top, entity.bottom)

        # Now that all the entities have been created, it's time to establish all
        # of the connection relationships between them.
        self._establish_connections()

    def __getitem__(self, coord):
        if coord is None:
            return None

        if isinstance(coord, tuple):
            return self.board[coord[0]][coord[1]]
        else:
            return self.board[coord]

    def get_row_col(self, pos):
        x, y = pos
        row, col = None, None
        for c, extents in self.col_extents.items():
            left, right = extents
            if left <= x < right:
                col = c
                break

        if col is not None:
            for r, extents in self.row_extents.items():
                top, bottom = extents
                if top <= y < bottom:
                    row = r
                    break
            if row is not None:
                return row, col

        return None

    def _establish_connections(self):
        for row in self.board:
            for entity in row:
                r, c = entity.row, entity.col
                if isinstance(entity, Cell):
                    entity.edge_top = self.board[r-1][c]
                    entity.edge_bottom = self.board[r+1][c]
                    entity.edge_left = self.board[r][c-1]
                    entity.edge_right = self.board[r][c+1]
                elif isinstance(entity, Edge):
                    if r == 0:
                        entity.cell1 = None
                        entity.cell2 = self.board[r+1][c]
                    elif r == 2*ROWS:
                        entity.cell1 = self.board[r-1][c]
                        entity.cell2 = None
                    elif c == 0:
                        entity.cell1 = None
                        entity.cell2 = self.board[r][c+1]
                    elif c == 2*COLS:
                        entity.cell1 = self.board[r][c-1]
                        entity.cell2 = None
                    elif is_even(r):
                        entity.cell1 = self.board[r-1][c]
                        entity.cell2 = self.board[r+1][c]
                    else:
                        entity.cell1 = self.board[r][c-1]
                        entity.cell2 = self.board[r][c+1]

    def draw(self):
        for r in range(0, len(self.board)):
            for c in range(0, len(self.board[0])):
                self.board[r][c].draw()
        pygame.display.update()

    def __repr__(self):
        return f'{self.__class__.__name__} {len(self.board[0])}x{len(self.board)}'
